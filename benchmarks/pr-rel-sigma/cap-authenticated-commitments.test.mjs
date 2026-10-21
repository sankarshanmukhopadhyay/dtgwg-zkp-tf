import assert from 'node:assert/strict';
import { test } from 'node:test';
import { fixture, proveSharedWitness, commitHidden } from './cap-hidden-witness.mjs';
import { assessBoundProof, issuedEnvelope, spikeKeyPair, verifyEnvelope } from './cap-authenticated-commitments.mjs';

const roles = ['membership', 'relationship', 'linkage'];
function setup() {
  const fixtureData = fixture();
  const keys = roles.map(() => spikeKeyPair());
  const receipts = roles.map((role, i) => issuedEnvelope(keys[i].privateKey, {
    issuer: 'test-issuer-' + i, role, scope: 'community-1', communityRoot: 'root-A',
    commitment: fixtureData.commitments[i],
  }));
  return {
    ...fixtureData, proof: proveSharedWitness(fixtureData), receipts,
    trustedKeys: Object.fromEntries(keys.map((key, i) => ['test-issuer-' + i, key.publicKey])),
    root: 'root-A', scope: 'community-1',
  };
}
const check = a => assessBoundProof(a);
test('authenticated commitments and hidden equality with offline voucher', () => {
  assert.equal(check(setup()), 'AUTHENTICATED_COMMITMENTS_AND_EQUALITY_ONLY');
});
test('attacker-created commitments without issuer signatures rejected', () => {
  const v = setup();
  const hostileKey = spikeKeyPair();
  v.receipts[2] = issuedEnvelope(hostileKey.privateKey, {
    issuer: 'test-issuer-2', role: 'linkage', scope: 'community-1', communityRoot: 'root-A',
    commitment: v.commitments[2],
  });
  assert.equal(check(v), 'REJECTED_AUTHENTICATION');
});
test('attacker replaces accepted issuer trust anchor rejected', () => {
  const v = setup();
  v.trustedKeys['test-issuer-1'] = spikeKeyPair().publicKey;
  assert.equal(check(v), 'REJECTED_AUTHENTICATION');
});
test('swapped authenticated commitment is rejected', () => {
  const v = setup();
  v.commitments[0] = commitHidden(v.message, v.blindings[0] + 1n);
  assert.equal(check(v), 'REJECTED_BINDING');
});
test('signed receipt metadata tampering is rejected', () => {
  const v = setup();
  v.receipts[1].statement.scope = 'other-community';
  assert.equal(check(v), 'REJECTED_AUTHENTICATION');
});
test('signed wrong community root rejected, even with valid signatures', () => {
  const v = setup();
  const kp = spikeKeyPair();
  v.trustedKeys['test-issuer-0'] = kp.publicKey;
  v.receipts[0] = issuedEnvelope(kp.privateKey, {
    issuer: 'test-issuer-0', role: 'membership', scope: 'community-1',
    communityRoot: 'root-B', commitment: v.commitments[0],
  });
  assert.equal(check(v), 'REJECTED_BINDING');
});
test('another verifier transcript is rejected', () => {
  const v = setup();
  v.context += '|other-verifier';
  assert.equal(check(v), 'REJECTED_WITNESS_PROOF');
});
test('reordered source roles rejected', () => {
  const v = setup();
  [v.receipts[0], v.receipts[1]] = [v.receipts[1], v.receipts[0]];
  assert.equal(check(v), 'REJECTED_ROLE');
});
test('malformed signature rejected', () => {
  const v = setup();
  v.receipts[0].signature = 'not-base64!';
  assert.equal(check(v), 'REJECTED_AUTHENTICATION');
});
test('unsigned extra fields fail verification', () => {
  const v = setup();
  v.receipts[0].statement.claims = 'admin';
  assert.equal(verifyEnvelope(v.trustedKeys['test-issuer-0'], v.receipts[0]), false);
});
