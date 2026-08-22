import fs from 'node:fs/promises';
import os from 'node:os';
import process from 'node:process';
import {performance} from 'node:perf_hooks';
import * as Bls12381Multikey from '@digitalbazaar/bls12-381-multikey';

const WARMUP = Number(process.env.BBS_BENCH_WARMUP ?? 3);
const ITERATIONS = Number(process.env.BBS_BENCH_ITERATIONS ?? 20);
const encoder = new TextEncoder();
const header = encoder.encode('dtgwg-zkp-tf:EXP-BBS-2023-01');
const presentationHeader = encoder.encode('dtgwg-zkp-tf:benchmark:presentation');
const messages = Array.from({length: 8}, (_, i) =>
  encoder.encode(`message-${i}:value-${i * 17}`));
const disclosedMessageIndexes = [0, 3, 7];

function disclosedMessages() {
  return messages.map((message, index) =>
    disclosedMessageIndexes.includes(index) ? message : undefined);
}

function summarize(values) {
  const sorted = [...values].sort((a, b) => a - b);
  const mean = values.reduce((a, b) => a + b, 0) / values.length;
  const percentile = p => sorted[Math.min(
    sorted.length - 1,
    Math.max(0, Math.ceil((p / 100) * sorted.length) - 1)
  )];
  return {
    iterations: values.length,
    mean_ms: Number(mean.toFixed(3)),
    median_ms: Number(percentile(50).toFixed(3)),
    p95_ms: Number(percentile(95).toFixed(3)),
    min_ms: Number(sorted[0].toFixed(3)),
    max_ms: Number(sorted.at(-1).toFixed(3))
  };
}

async function measure(operation) {
  for(let i = 0; i < WARMUP; ++i) {
    await operation();
  }
  const values = [];
  for(let i = 0; i < ITERATIONS; ++i) {
    const start = performance.now();
    await operation();
    values.push(performance.now() - start);
  }
  return summarize(values);
}

const keyPair = await Bls12381Multikey.generateBbsKeyPair({
  algorithm: Bls12381Multikey.ALGORITHMS.BBS_BLS12381_SHA256
});
const signer = keyPair.signer();
const verifier = keyPair.verifier();
let signature = await signer.multisign({header, messages});
let proof = await keyPair.deriveProof({
  signature,
  header,
  messages,
  presentationHeader,
  disclosedMessageIndexes
});

const initialVerified = await verifier.multiverify({
  proof,
  header,
  presentationHeader,
  messages: disclosedMessages()
});
if(!initialVerified) {
  throw new Error('Initial BBS derived proof did not verify.');
}

const results = {};
results.key_generation = await measure(async () => {
  await Bls12381Multikey.generateBbsKeyPair({
    algorithm: Bls12381Multikey.ALGORITHMS.BBS_BLS12381_SHA256
  });
});
results.sign_8_messages = await measure(async () => {
  signature = await signer.multisign({header, messages});
});
results.derive_proof_reveal_3_of_8 = await measure(async () => {
  proof = await keyPair.deriveProof({
    signature,
    header,
    messages,
    presentationHeader,
    disclosedMessageIndexes
  });
});
results.verify_derived_proof = await measure(async () => {
  const verified = await verifier.multiverify({
    proof,
    header,
    presentationHeader,
    messages: disclosedMessages()
  });
  if(!verified) {
    throw new Error('BBS derived proof verification failed during benchmark.');
  }
});

const output = {
  profile_id: 'EXP-BBS-2023-01',
  normative_thresholds: false,
  correctness_checked: true,
  warmup_iterations: WARMUP,
  measured_iterations: ITERATIONS,
  message_count: messages.length,
  disclosed_message_count: disclosedMessageIndexes.length,
  environment: {
    node: process.version,
    platform: process.platform,
    arch: process.arch,
    cpu_model: os.cpus()[0]?.model ?? 'unknown',
    cpu_count: os.cpus().length,
    total_memory_bytes: os.totalmem()
  },
  results
};

const json = `${JSON.stringify(output, null, 2)}\n`;
await fs.writeFile('bbs-2023-benchmark.json', json, 'utf8');
process.stdout.write(json);
