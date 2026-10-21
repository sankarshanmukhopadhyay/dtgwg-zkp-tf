/** Experimental issuer-authenticated commitment envelope for CAP-010 feasibility.
 * Authentication proves integrity under a configured Ed25519 public key, not
 * Credential/Registry authorization or normative representation compatibility.
 */
import { createPublicKey, generateKeyPairSync, sign, verify } from 'node:crypto';
import { proveSharedWitness, verifySharedWitness } from './cap-hidden-witness.mjs';

const encoder = new TextEncoder();
const DOMAIN = 'DTG-CAP-010-EXPERIMENTAL-COMMITMENT-ENVELOPE-V1';
const ROLES = ['membership', 'relationship', 'linkage'];

function ascii(label, value) {
  if (typeof value !== 'string' || value.length < 1 || value.length > 256 ||
      [...value].some(ch => ch.charCodeAt(0) < 33 || ch.charCodeAt(0) > 126)) {
    throw new TypeError(`invalid ${label}`);
  }
  return value;
}

function canonical(envelope) {
  if (Object.keys(envelope).sort().join(',') !==
      'commitment,community_root,issuer,profile,role,scope') throw new TypeError('unexpected envelope fields');
  if (envelope.profile !== 'cap-010-auth-binding-spike-v1' || !ROLES.includes(envelope.role)) {
    throw new TypeError('unsupported envelope role/profile');
  }
  const fields = ['issuer', 'scope', 'community_root', 'commitment'];
  for (const key of fields) ascii(key, envelope[key]);
  if (!/^[0-9a-f]{64}$/.test(envelope.commitment)) throw new TypeError('invalid commitment encoding');
  const json = JSON.stringify(Object.fromEntries(Object.keys(envelope).sort().map(k => [k, envelope[k]])));
  return encoder.encode(DOMAIN + '\\u0000' + json);
}

export function issuedEnvelope(privateKey, { issuer, role, scope, communityRoot, commitment }) {
  const statement = {
    profile: 'cap-010-auth-binding-spike-v1', issuer, role, scope,
    community_root: communityRoot, commitment: Buffer.from(commitment.toBytes()).toString('hex'),
  };
  return { statement, signature: sign(null, canonical(statement), privateKey).toString('base64') };
}

export function verifyEnvelope(publicKey, receipt) {
  try {
    if (Object.keys(receipt).sort().join(',') !== 'signature,statement') return false;
    if (typeof receipt.signature !== 'string' ||
        !/^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$/.test(receipt.signature)) return false;
    const signature = Buffer.from(receipt.signature, 'base64');
    if (signature.length !== 64) return false;
    return verify(null, canonical(receipt.statement), publicKey, signature);
  } catch {
    return false;
  }
}

/** Verify all issuer-authenticated commitments *before* trusting the equality proof.
 * A passing result is only a bounded feasibility outcome.
 */
export function assessBoundProof({ receipts, trustedKeys, commitments, proof, context, root, scope }) {
  if (!Array.isArray(receipts) || receipts.length !== 3 ||
      !Array.isArray(commitments) || commitments.length !== 3) return 'REJECTED_INPUT';
  for (let i = 0; i < 3; i++) {
    const receipt = receipts[i];
    const statement = receipt?.statement;
    if (!statement || statement.role !== ROLES[i]) return 'REJECTED_ROLE';
    const key = trustedKeys?.[statement.issuer];
    if (!key || !verifyEnvelope(key, receipt)) return 'REJECTED_AUTHENTICATION';
    if (statement.community_root !== root || statement.scope !== scope ||
        statement.commitment !== Buffer.from(commitments[i].toBytes()).toString('hex')) {
      return 'REJECTED_BINDING';
    }
  }
  return verifySharedWitness({ commitments, proof, context })
    ? 'AUTHENTICATED_COMMITMENTS_AND_EQUALITY_ONLY' : 'REJECTED_WITNESS_PROOF';
}

export function spikeKeyPair() {
  return generateKeyPairSync('ed25519');
}
