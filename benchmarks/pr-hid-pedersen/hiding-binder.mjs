import { ristretto255, ristretto255_hasher } from '@noble/curves/ed25519.js';
import { createHash, randomBytes } from 'node:crypto';
import { writeFileSync } from 'node:fs';
import { performance } from 'node:perf_hooks';

const enc = new TextEncoder();
const Point = ristretto255.Point;
const ORDER = Point.Fn.ORDER;
const G = Point.BASE;
const H = ristretto255_hasher.hashToCurve(enc.encode('DTG-PR-HID-PEDERSEN-H-v1'));
const VALUE_DST = 'DTG_PR_HID_VALUE_TO_SCALAR_V1';
const ENUMERABLE_VALUES = ['read', 'write', 'approve', 'admin'];

function scalarFromBytes(bytes) {
  const value = BigInt(`0x${Buffer.from(bytes).toString('hex')}`) % ORDER;
  return value === 0n ? 1n : value;
}

function randomScalar() {
  return scalarFromBytes(randomBytes(64));
}

function scalarFromLabel(label) {
  return ristretto255_hasher.hashToScalar(enc.encode(label), { DST: 'DTG_PR_HID_TEST_SCALAR_V1' });
}

function encodeValue(value, context = 'scope-v1') {
  return ristretto255_hasher.hashToScalar(enc.encode(`${context}\u0000${value}`), { DST: VALUE_DST });
}

function commitValue(value, blinding, context = 'scope-v1') {
  const m = encodeValue(value, context);
  return G.multiply(m).add(H.multiply(blinding));
}

function verifyOpening(commitment, value, blinding, context = 'scope-v1') {
  return commitment.equals(commitValue(value, blinding, context));
}

function deterministicDigest(value) {
  return createHash('sha256').update(`DTG-ENUM-v1\u0000${value}`).digest('hex');
}

function dictionaryRecover(digest, candidates = ENUMERABLE_VALUES) {
  return candidates.find((candidate) => deterministicDigest(candidate) === digest) ?? null;
}

function hexPoint(point) {
  return Buffer.from(point.toBytes()).toString('hex');
}

function runTests() {
  const value = 'approve';
  const context = 'delegation-scope-v1';
  const r1 = randomScalar();
  const r2 = randomScalar();
  const C1 = commitValue(value, r1, context);
  const C2 = commitValue(value, r2, context);

  if (!verifyOpening(C1, value, r1, context)) throw new Error('valid opening failed');
  if (verifyOpening(C1, 'admin', r1, context)) throw new Error('wrong value opened commitment');
  if (verifyOpening(C1, value, r2, context)) throw new Error('wrong blinding opened commitment');
  if (C1.equals(C2)) throw new Error('fresh randomized commitments to same value were linkable');

  const digest = deterministicDigest(value);
  const recovered = dictionaryRecover(digest);
  if (recovered !== value) throw new Error('dictionary regression did not recover enumerable deterministic digest');

  const dr = scalarFromLabel('deterministic-pr-hid-vector-blinding');
  const DC = commitValue(value, dr, context);
  const vector = {
    profile_id: 'EXP-PR-HID-PEDERSEN-01',
    predicate: 'PR-HID',
    construction: 'Ristretto255 Pedersen-style commitment',
    relation: 'C = encode(value,context)*G + r*H',
    context,
    enumerable_domain: ENUMERABLE_VALUES,
    value,
    G: hexPoint(G),
    H: hexPoint(H),
    commitment: hexPoint(DC),
    blinding_scalar_hex: dr.toString(16).padStart(64, '0'),
    deterministic_digest_baseline: digest,
    dictionary_recovered_value: recovered,
    expected: {
      valid_opening: true,
      wrong_value_opening: false,
      wrong_blinding_opening: false,
      same_value_fresh_commitments_distinct: true,
      deterministic_digest_enumerable: true
    }
  };
  writeFileSync('pr-hid-pedersen-vector.json', `${JSON.stringify(vector, null, 2)}\n`);
  console.log('PR-HID Pedersen hiding-binder tests passed.');
}

function stats(values) {
  const sorted = [...values].sort((a, b) => a - b);
  const mean = values.reduce((a, b) => a + b, 0) / values.length;
  return {
    mean_ms: mean,
    p50_ms: sorted[Math.floor(sorted.length * 0.50)],
    p95_ms: sorted[Math.min(sorted.length - 1, Math.floor(sorted.length * 0.95))]
  };
}

function time(fn) {
  const start = performance.now();
  fn();
  return performance.now() - start;
}

function runBenchmark() {
  runTests();
  const warmup = Number(process.env.PR_HID_BENCH_WARMUP ?? 10);
  const iterations = Number(process.env.PR_HID_BENCH_ITERATIONS ?? 100);
  const value = 'approve';
  const context = 'delegation-scope-v1';

  for (let i = 0; i < warmup; i += 1) {
    const r = randomScalar();
    const C = commitValue(value, r, context);
    if (!verifyOpening(C, value, r, context)) throw new Error('warmup opening failed');
  }

  const commitTimes = [];
  const openTimes = [];
  for (let i = 0; i < iterations; i += 1) {
    const r = randomScalar();
    let C;
    commitTimes.push(time(() => { C = commitValue(value, r, context); }));
    openTimes.push(time(() => {
      if (!verifyOpening(C, value, r, context)) throw new Error('benchmark opening failed');
    }));
  }

  const result = {
    profile_id: 'EXP-PR-HID-PEDERSEN-01',
    predicate: 'PR-HID',
    implementation: '@noble/curves@2.3.0',
    group: 'ristretto255',
    warmup,
    iterations,
    commit: stats(commitTimes),
    verify_opening: stats(openTimes),
    timing_class: 'informational-non-normative'
  };
  writeFileSync('pr-hid-pedersen-benchmark.json', `${JSON.stringify(result, null, 2)}\n`);
  console.log(JSON.stringify(result, null, 2));
}

const mode = process.argv[2] ?? '--test';
if (mode === '--benchmark') runBenchmark();
else runTests();
