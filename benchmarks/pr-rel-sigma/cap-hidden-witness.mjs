/** Experimental CAP-010 hidden-scalar witness feasibility, not a CAP proof.
 * Reuses the pinned Ristretto255 primitive from EXP-PR-REL-SIGMA-01.
 * All commitments in this experiment are *assumed* authenticated.
 */
import { ristretto255, ristretto255_hasher } from '@noble/curves/ed25519.js';
import { randomBytes } from 'node:crypto';

const encoder = new TextEncoder();
const Point = ristretto255.Point;
const ORDER = Point.Fn.ORDER;
const G = Point.BASE;
const H = ristretto255_hasher.hashToCurve(encoder.encode('DTG-PR-REL-SIGMA-H-v1'));
const DOMAIN = 'DTG-CAP-010-HIDDEN-WITNESS-SPIKE-V1';
const DST = 'DTG_CAP_010_HIDDEN_WITNESS_CHALLENGE_V1';
const SCALAR_DST = 'DTG_CAP_010_TEST_SCALAR_V1';

function hashScalar(value, dst = SCALAR_DST) {
  const scalar = ristretto255_hasher.hashToScalar(encoder.encode(value), { DST: dst });
  return scalar === 0n ? 1n : scalar;
}

function randomScalar() {
  const n = BigInt('0x' + randomBytes(64).toString('hex')) % ORDER;
  return n || 1n;
}

function mul(p, n) {
  const scalar = (n % ORDER + ORDER) % ORDER;
  return scalar === 0n ? Point.ZERO : p.multiply(scalar);
}

function combination(m, r) {
  return mul(G, m).add(mul(H, r));
}

function boundBytes(commitments, announcements, context) {
  if (typeof context !== 'string' || context.length === 0 || [...context].some(ch => ch.charCodeAt(0) < 32 || ch.charCodeAt(0) > 126)) {
    throw new Error('context must be a nonempty ASCII string');
  }
  const chunks = [encoder.encode(DOMAIN), Uint8Array.from([0]), encoder.encode(context)];
  for (const p of [...commitments, ...announcements]) chunks.push(p.toBytes());
  return Buffer.concat(chunks);
}

export function commitHidden(message, blind) {
  return combination(message, blind);
}

/** Prove knowledge of one m and three independently blinded committed values. */
export function proveSharedWitness({ message, blindings, commitments, context }) {
  if (blindings.length !== 3 || commitments.length !== 3) throw new Error('three inputs required');
  const tm = randomScalar();
  const tr = [randomScalar(), randomScalar(), randomScalar()];
  const announcements = tr.map((r) => combination(tm, r));
  const c = ristretto255_hasher.hashToScalar(boundBytes(commitments, announcements, context), { DST });
  return {
    announcements,
    zm: (tm + c * message) % ORDER,
    zr: tr.map((r, i) => (r + c * blindings[i]) % ORDER),
  };
}

export function verifySharedWitness({ commitments, proof, context }) {
  try {
    if (commitments.length !== 3 || proof.announcements.length !== 3 || proof.zr.length !== 3) return false;
    const c = ristretto255_hasher.hashToScalar(
      boundBytes(commitments, proof.announcements, context), { DST }
    );
    return commitments.every((commitment, i) =>
      combination(proof.zm, proof.zr[i]).equals(proof.announcements[i].add(mul(commitment, c)))
    );
  } catch {
    return false;
  }
}

export function fixture() {
  const message = hashScalar('voucher-relationship-witness-demo');
  const blindings = ['membership', 'relationship', 'linkage'].map((v) => hashScalar('blind-' + v));
  const commitments = blindings.map((r) => combination(message, r));
  const context = 'root-A|community-1|transcript-1|verifier-A';
  return { message, blindings, commitments, context };
}
