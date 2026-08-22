import { ristretto255, ristretto255_hasher } from '@noble/curves/ed25519.js';
import { randomBytes } from 'node:crypto';
import { writeFileSync } from 'node:fs';
import { performance } from 'node:perf_hooks';

const enc = new TextEncoder();
const Point = ristretto255.Point;
const ORDER = Point.Fn.ORDER;
const G = Point.BASE;
const H = ristretto255_hasher.hashToCurve(enc.encode('DTG-PR-REL-SIGMA-H-v1'));
const PROFILE_DOMAIN = 'DTG-PR-REL-SIGMA-v1';
const CHALLENGE_DST = 'DTG_PR_REL_SIGMA_CHALLENGE_V1';

function concatBytes(...arrays) {
  const length = arrays.reduce((n, a) => n + a.length, 0);
  const out = new Uint8Array(length);
  let offset = 0;
  for (const a of arrays) {
    out.set(a, offset);
    offset += a.length;
  }
  return out;
}

function scalarFromLabel(label) {
  const value = ristretto255_hasher.hashToScalar(enc.encode(label), { DST: 'DTG_PR_REL_TEST_SCALAR_V1' });
  return value === 0n ? 1n : value;
}

function randomScalar() {
  const bytes = randomBytes(64);
  const value = BigInt(`0x${bytes.toString('hex')}`) % ORDER;
  return value === 0n ? 1n : value;
}

function mul(point, scalar) {
  const n = ((scalar % ORDER) + ORDER) % ORDER;
  return n === 0n ? Point.ZERO : point.multiply(n);
}

function lin2(a, p, b, q) {
  return mul(p, a).add(mul(q, b));
}

function commit(message, blinding) {
  return lin2(message, G, blinding, H);
}

function challenge({ C1, C2, A1, A2, context }) {
  const transcript = concatBytes(
    enc.encode(PROFILE_DOMAIN),
    enc.encode('\u0000'),
    enc.encode(context),
    C1.toBytes(),
    C2.toBytes(),
    A1.toBytes(),
    A2.toBytes(),
  );
  return ristretto255_hasher.hashToScalar(transcript, { DST: CHALLENGE_DST });
}

function proveEquality({ message, r1, r2, C1, C2, context, nonceScalars }) {
  const tm = nonceScalars?.tm ?? randomScalar();
  const tr1 = nonceScalars?.tr1 ?? randomScalar();
  const tr2 = nonceScalars?.tr2 ?? randomScalar();

  const A1 = lin2(tm, G, tr1, H);
  const A2 = lin2(tm, G, tr2, H);
  const c = challenge({ C1, C2, A1, A2, context });

  return {
    A1,
    A2,
    zm: (tm + c * message) % ORDER,
    zr1: (tr1 + c * r1) % ORDER,
    zr2: (tr2 + c * r2) % ORDER,
  };
}

function verifyEquality({ C1, C2, context, proof }) {
  const c = challenge({ C1, C2, A1: proof.A1, A2: proof.A2, context });
  const lhs1 = lin2(proof.zm, G, proof.zr1, H);
  const rhs1 = proof.A1.add(mul(C1, c));
  const lhs2 = lin2(proof.zm, G, proof.zr2, H);
  const rhs2 = proof.A2.add(mul(C2, c));
  return lhs1.equals(rhs1) && lhs2.equals(rhs2);
}

function hexScalar(n) {
  return n.toString(16).padStart(64, '0');
}

function serializeProof(proof) {
  return {
    A1: Buffer.from(proof.A1.toBytes()).toString('hex'),
    A2: Buffer.from(proof.A2.toBytes()).toString('hex'),
    zm: hexScalar(proof.zm),
    zr1: hexScalar(proof.zr1),
    zr2: hexScalar(proof.zr2),
  };
}

function deterministicVector() {
  const message = scalarFromLabel('shared-hidden-value');
  const r1 = scalarFromLabel('artifact-one-blinding');
  const r2 = scalarFromLabel('artifact-two-blinding');
  const C1 = commit(message, r1);
  const C2 = commit(message, r2);
  const context = 'verifier.example|task-123|policy-v0.4';
  const proof = proveEquality({
    message,
    r1,
    r2,
    C1,
    C2,
    context,
    nonceScalars: {
      tm: scalarFromLabel('deterministic-proof-tm'),
      tr1: scalarFromLabel('deterministic-proof-tr1'),
      tr2: scalarFromLabel('deterministic-proof-tr2'),
    },
  });

  return { message, r1, r2, C1, C2, context, proof };
}

function runTests() {
  const v = deterministicVector();
  if (!verifyEquality(v)) throw new Error('positive equality proof did not verify');

  const differentMessage = scalarFromLabel('different-hidden-value');
  const C2Different = commit(differentMessage, v.r2);
  if (verifyEquality({ C1: v.C1, C2: C2Different, context: v.context, proof: v.proof })) {
    throw new Error('proof verified after changing the second committed value');
  }

  if (verifyEquality({ C1: v.C1, C2: v.C2, context: `${v.context}|different`, proof: v.proof })) {
    throw new Error('proof verified under a different context');
  }

  const fresh1 = proveEquality(v);
  const fresh2 = proveEquality(v);
  const s1 = JSON.stringify(serializeProof(fresh1));
  const s2 = JSON.stringify(serializeProof(fresh2));
  if (s1 === s2) throw new Error('fresh proofs unexpectedly reused prover randomness');
  if (!verifyEquality({ ...v, proof: fresh1 }) || !verifyEquality({ ...v, proof: fresh2 })) {
    throw new Error('fresh equality proof failed verification');
  }

  const vector = {
    profile_id: 'EXP-PR-REL-SIGMA-01',
    predicate: 'PR-REL',
    relation: 'C1=m*G+r1*H; C2=m*G+r2*H',
    group: 'ristretto255',
    context: v.context,
    G: Buffer.from(G.toBytes()).toString('hex'),
    H: Buffer.from(H.toBytes()).toString('hex'),
    C1: Buffer.from(v.C1.toBytes()).toString('hex'),
    C2: Buffer.from(v.C2.toBytes()).toString('hex'),
    proof: serializeProof(v.proof),
    expected: {
      matching_commitments: true,
      changed_second_value: false,
      changed_context: false,
      fresh_proofs_distinct: true,
    },
  };
  writeFileSync('pr-rel-sigma-vector.json', `${JSON.stringify(vector, null, 2)}\n`);
  console.log('PR-REL sigma relationship proof tests passed.');
}

function stats(values) {
  const sorted = [...values].sort((a, b) => a - b);
  const mean = values.reduce((a, b) => a + b, 0) / values.length;
  const p50 = sorted[Math.floor(sorted.length * 0.50)];
  const p95 = sorted[Math.min(sorted.length - 1, Math.floor(sorted.length * 0.95))];
  return { mean_ms: mean, p50_ms: p50, p95_ms: p95 };
}

function time(fn) {
  const start = performance.now();
  fn();
  return performance.now() - start;
}

function runBenchmark() {
  runTests();
  const warmup = Number(process.env.PR_REL_BENCH_WARMUP ?? 5);
  const iterations = Number(process.env.PR_REL_BENCH_ITERATIONS ?? 50);
  const v = deterministicVector();

  for (let i = 0; i < warmup; i += 1) {
    const proof = proveEquality(v);
    if (!verifyEquality({ ...v, proof })) throw new Error('warmup proof failed');
  }

  const proveTimes = [];
  const verifyTimes = [];
  for (let i = 0; i < iterations; i += 1) {
    let proof;
    proveTimes.push(time(() => { proof = proveEquality(v); }));
    verifyTimes.push(time(() => {
      if (!verifyEquality({ ...v, proof })) throw new Error('benchmark proof failed');
    }));
  }

  const result = {
    profile_id: 'EXP-PR-REL-SIGMA-01',
    predicate: 'PR-REL',
    implementation: '@noble/curves@2.3.0',
    group: 'ristretto255',
    relation: 'two Pedersen-style commitments to one shared hidden scalar',
    warmup,
    iterations,
    prove: stats(proveTimes),
    verify: stats(verifyTimes),
    timing_class: 'informational-non-normative',
  };
  writeFileSync('pr-rel-sigma-benchmark.json', `${JSON.stringify(result, null, 2)}\n`);
  console.log(JSON.stringify(result, null, 2));
}

const mode = process.argv[2] ?? '--test';
if (mode === '--benchmark') runBenchmark();
else runTests();
