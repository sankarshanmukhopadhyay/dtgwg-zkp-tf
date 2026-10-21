import assert from 'node:assert/strict';
import { test } from 'node:test';
import { ristretto255_hasher } from '@noble/curves/ed25519.js';
import { commitHidden, fixture, proveSharedWitness, verifySharedWitness } from './cap-hidden-witness.mjs';

function setup() {
  const args = fixture();
  const proof = proveSharedWitness(args);
  return { ...args, proof };
}
test('shared hidden scalar proof verifies with voucher offline', () => {
  assert.equal(verifySharedWitness(setup()), true);
});
test('different relation witness is rejected', () => {
  const v = setup();
  const different = ristretto255_hasher.hashToScalar(new TextEncoder().encode('other-voucher'), { DST: 'DTG_CAP_010_TEST_SCALAR_V1' });
  const altered = [...v.commitments];
  altered[1] = commitHidden(different, v.blindings[1]);
  assert.equal(verifySharedWitness({ ...v, commitments: altered }), false);
});
test('substituted membership commitment is rejected', () => {
  const v = setup();
  const other = fixture();
  other.commitments[0] = commitHidden(v.message, v.blindings[0] + 1n);
  assert.equal(verifySharedWitness({ ...v, commitments: [other.commitments[0], ...v.commitments.slice(1)] }), false);
});
test('replayed proof in another verifier context fails', () => {
  const v = setup();
  assert.equal(verifySharedWitness({ ...v, context: v.context + '|verifier-B' }), false);
});
test('replayed proof under another root fails', () => {
  const v = setup();
  assert.equal(verifySharedWitness({ ...v, context: 'root-B|community-1|transcript-1|verifier-A' }), false);
});
test('wrong number of commitments fails', () => {
  const v = setup();
  assert.equal(verifySharedWitness({ ...v, commitments: v.commitments.slice(0, 2) }), false);
});
test('proofs use fresh random nonces', () => {
  const v = fixture();
  const first = proveSharedWitness(v);
  const second = proveSharedWitness(v);
  assert.notDeepEqual(first.announcements.map(p=>Buffer.from(p.toBytes()).toString('hex')),
    second.announcements.map(p=>Buffer.from(p.toBytes()).toString('hex')));
  assert.equal(verifySharedWitness({ ...v, proof: first }), true);
  assert.equal(verifySharedWitness({ ...v, proof: second }), true);
});
