/** Experimental signed-root Merkle membership component for CAP record 010.
 *
 * This verifies inclusion of a commitment in a binary SHA-256 Merkle tree and
 * integrity of the root under an explicitly configured test key.
 *
 * NOT a zero-knowledge membership proof: leaf and path are disclosed.
 * NOT a source of Registry authority, status, freshness or non-revocation.
 */
import { createHash, sign, verify } from 'node:crypto';

const PREFIX = Buffer.from('DTG-CAP-010-MERKLE-SPIKE-V1\0', 'utf8');
const ROOT_DOMAIN = Buffer.from('DTG-CAP-010-ROOT-SPIKE-V1\0', 'utf8');
const sha = (...chunks) => createHash('sha256').update(Buffer.concat(chunks)).digest();

function hex32(value) {
  if (typeof value !== 'string' || !/^[0-9a-f]{64}$/.test(value)) {
    throw new TypeError('expected canonical lowercase 32-byte hex');
  }
  return Buffer.from(value, 'hex');
}
function label(value) {
  if (typeof value !== 'string' || !/^[a-zA-Z0-9_.:-]{1,128}$/.test(value)) {
    throw new TypeError('invalid experimental context label');
  }
  return value;
}
const leaf = bytes => sha(PREFIX, Buffer.from([0]), bytes);
const parent = (left, right) => sha(PREFIX, Buffer.from([1]), left, right);

/** Deterministic binary tree fixture; supports power-of-two leaves only. */
export function treeForCommitments(commitmentHexes) {
  if (!Array.isArray(commitmentHexes) || commitmentHexes.length < 2 ||
      (commitmentHexes.length & (commitmentHexes.length - 1)) !== 0) {
    throw new TypeError('requires a power-of-two array of at least two commitments');
  }
  const layers = [commitmentHexes.map(value => leaf(hex32(value)))];
  while (layers.at(-1).length > 1) {
    const nodes = layers.at(-1);
    const next = [];
    for (let i = 0; i < nodes.length; i += 2) next.push(parent(nodes[i], nodes[i + 1]));
    layers.push(next);
  }
  function path(index) {
    if (!Number.isSafeInteger(index) || index < 0 || index >= commitmentHexes.length) {
      throw new TypeError('invalid leaf index');
    }
    return layers.slice(0, -1).map(nodes => {
      const sibling = index ^ 1;
      const entry = { side: sibling < index ? 'left' : 'right', digest: nodes[sibling].toString('hex') };
      index = Math.floor(index / 2);
      return entry;
    });
  }
  return { root: layers.at(-1)[0].toString('hex'), path };
}
function rootPayload({ root, community, scope, epoch }) {
  if (!Number.isSafeInteger(epoch) || epoch < 0) throw new TypeError('invalid epoch');
  return Buffer.concat([ROOT_DOMAIN, Buffer.from(JSON.stringify({
    community: label(community), epoch, root: hex32(root).toString('hex'), scope: label(scope),
  }), 'utf8')]);
}
export function signExperimentalRoot(privateKey, assertion) {
  return { ...assertion, signature: sign(null, rootPayload(assertion), privateKey).toString('base64') };
}
export function verifyExperimentalRoot(publicKey, assertion) {
  try {
    if (!assertion || Object.keys(assertion).sort().join(',') !==
        'community,epoch,root,scope,signature') return false;
    if (typeof assertion.signature !== 'string' ||
        !/^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$/.test(assertion.signature)) return false;
    const signature = Buffer.from(assertion.signature, 'base64');
    return signature.length === 64 &&
      verify(null, rootPayload(assertion), publicKey, signature);
  } catch { return false; }
}
/** Membership is accepted only relative to a verified root *and* caller's root context. */
export function verifyMembership({ commitment, path, rootAssertion, trustedRootKey,
                                    expectedCommunity, expectedScope, expectedRoot, expectedEpoch }) {
  try {
    if (!Array.isArray(path) || path.length < 1 || path.length > 32 ||
        !verifyExperimentalRoot(trustedRootKey, rootAssertion)) return false;
    if (rootAssertion.community !== expectedCommunity ||
        rootAssertion.scope !== expectedScope || rootAssertion.root !== expectedRoot ||
        rootAssertion.epoch !== expectedEpoch) return false;
    let current = leaf(hex32(commitment));
    for (const step of path) {
      if (!step || Object.keys(step).sort().join(',') !== 'digest,side' ||
          !['left', 'right'].includes(step.side)) return false;
      const sibling = hex32(step.digest);
      current = step.side === 'left' ? parent(sibling, current) : parent(current, sibling);
    }
    return current.equals(hex32(rootAssertion.root));
  } catch { return false; }
}
