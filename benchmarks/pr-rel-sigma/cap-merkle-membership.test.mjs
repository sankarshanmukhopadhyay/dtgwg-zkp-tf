import assert from 'node:assert/strict';
import { test } from 'node:test';
import { generateKeyPairSync } from 'node:crypto';
import { fixture, proveSharedWitness } from './cap-hidden-witness.mjs';
import { assessBoundProof, issuedEnvelope, spikeKeyPair } from './cap-authenticated-commitments.mjs';
import { signExperimentalRoot, treeForCommitments, verifyMembership } from './cap-merkle-membership.mjs';

const hex = p => Buffer.from(p.toBytes()).toString('hex');
function setup() {
  const witness = fixture();
  const other = '1'.repeat(64);
  const commitment = hex(witness.commitments[0]);
  const tree = treeForCommitments([other, commitment]);
  const rootSigner = generateKeyPairSync('ed25519');
  const rootAssertion = signExperimentalRoot(rootSigner.privateKey, {
    root: tree.root, community: 'community-1', scope: 'community-1', epoch: 7,
  });
  const members = {
    commitment, path: tree.path(1), rootAssertion, trustedRootKey: rootSigner.publicKey,
    expectedCommunity: 'community-1', expectedScope: 'community-1',
    expectedRoot: tree.root, expectedEpoch: 7,
  };
  const roles = ['membership', 'relationship', 'linkage'];
  const keys = roles.map(() => spikeKeyPair());
  const receipts = roles.map((role, i) => issuedEnvelope(keys[i].privateKey, {
    issuer: 'test-issuer-' + i, role, scope: 'community-1', communityRoot: tree.root,
    commitment: witness.commitments[i],
  }));
  const bound = { ...witness, proof: proveSharedWitness(witness), receipts,
    trustedKeys: Object.fromEntries(keys.map((k, i) => ['test-issuer-' + i, k.publicKey])),
    root: tree.root, scope: 'community-1' };
  return { tree, members, bound };
}
test('signed membership root and linked commitment proof validate separately', () => {
  const v = setup();
  assert.equal(verifyMembership(v.members), true);
  assert.equal(assessBoundProof(v.bound), 'AUTHENTICATED_COMMITMENTS_AND_EQUALITY_ONLY');
});
test('attacker-supplied untrusted root is rejected', () => {
  const v = setup();
  const outsider = generateKeyPairSync('ed25519');
  v.members.rootAssertion = signExperimentalRoot(outsider.privateKey, {
    root: v.tree.root, community: 'community-1', scope: 'community-1', epoch: 7,
  });
  assert.equal(verifyMembership(v.members), false);
});
test('wrong membership root fails', () => {
  const v = setup(); v.members.expectedRoot = '0'.repeat(64);
  assert.equal(verifyMembership(v.members), false);
});
test('wrong epoch fails despite authentic signature', () => {
  const v = setup(); v.members.expectedEpoch = 8;
  assert.equal(verifyMembership(v.members), false);
});
test('substituted leaf fails membership', () => {
  const v = setup(); v.members.commitment = 'f'.repeat(64);
  assert.equal(verifyMembership(v.members), false);
});
test('tampered Merkle direction fails', () => {
  const v = setup(); v.members.path[0].side = 'right';
  assert.equal(verifyMembership(v.members), false);
});
test('changed root scope fails signature', () => {
  const v = setup(); v.members.rootAssertion.scope = 'other-community';
  assert.equal(verifyMembership(v.members), false);
});
test('invalid path digest rejected', () => {
  const v = setup(); v.members.path[0].digest = 'bad';
  assert.equal(verifyMembership(v.members), false);
});
test('membership proof for another commitment cannot replace issued envelope', () => {
  const v = setup();
  v.bound.commitments[0] = v.bound.commitments[1];
  assert.equal(assessBoundProof(v.bound), 'REJECTED_BINDING');
});

test('two verifier presentations reveal a stable leaf and membership path', () => {
  // Falsification: a fresh hidden-equality transcript is insufficient to hide
  // the Merkle leaf/path transmitted by the membership component.
  const v = setup();
  const presentationA = {
    leaf: v.members.commitment,
    path: v.members.path.map(step => ({ ...step })),
    proof: proveSharedWitness({ ...v.bound, context: 'verifier-A|challenge-1' }),
  };
  const presentationB = {
    leaf: v.members.commitment,
    path: v.members.path.map(step => ({ ...step })),
    proof: proveSharedWitness({ ...v.bound, context: 'verifier-B|challenge-2' }),
  };
  assert.equal(presentationA.leaf, presentationB.leaf);
  assert.deepEqual(presentationA.path, presentationB.path);
  assert.notDeepEqual(
    presentationA.proof.announcements.map(p => Buffer.from(p.toBytes()).toString('hex')),
    presentationB.proof.announcements.map(p => Buffer.from(p.toBytes()).toString('hex')),
  );
  assert.equal(verifyMembership(v.members), true);
});
