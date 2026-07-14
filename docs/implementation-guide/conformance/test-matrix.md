# Conformance test matrix

**Status:** Incubating
**Normative status:** Non-normative unless promoted into the Working Draft

## Purpose

This is the human-readable view of [`test-matrix.csv`](./test-matrix.csv), the machine-readable source of truth. Level definitions, predicate and scenario scope are in [`levels.md`](./levels.md). Run `python3 scripts/validate_conformance.py` from the repo root to check referential integrity and level coverage.

## Summary

| Level | Scenarios | Predicates | Tests | Positive | Negative |
|---|---|---|---|---|---|
| CL-1 | UC-004, UC-006, UC-017, UC-020, UC-021 | PR-LIV, PR-HLD, PR-FRE | 20 | 10 | 10 |
| CL-2 | UC-001, UC-002, UC-005 | PR-LIV, PR-PER, PR-UNQ, PR-HLD, PR-FRE | 12 | 6 | 6 |
| CL-3 | UC-009, UC-010 | PR-LIV, PR-HLD, PR-FRE (+ delegation, untyped) | 8 | 4 | 4 |
| CL-4 | UC-012, UC-013, UC-022, UC-023, UC-024, UC-025, UC-026, UC-027, UC-030 | PR-ISS (+ lower-level predicates as needed) | 36 | 18 | 18 |
| **Total** | 19 P0 scenarios | 7 predicates | 76 | 38 | 38 |

## CL-1 — Minimum Liveness Profile

### UC-004

| Test ID | Type | Predicates | Adversary | Description | Expected result |
|---|---|---|---|---|---|
| `CT-UC004-POS-01` | positive | PR-LIV;PR-HLD;PR-FRE | ADV-U | Holder presents a fresh liveness+holder-binding proof transcript-bound to the exact amount, destination and currency. | verifier returns step-up-satisfied=true with matching transaction binding digest |
| `CT-UC004-NEG-01` | negative | PR-LIV;PR-HLD;PR-FRE | ADV-U | Same valid proof is replayed against a transaction with a different amount. | verifier rejects: transcript binding mismatch, reason code distinct from expiry |
| `CT-UC004-NEG-02` | negative | PR-LIV;PR-HLD;PR-FRE | ADV-W | Proof is presented after its stated expiry window has elapsed. | verifier rejects: expired, and fallback does not silently lower assurance class |
| `CT-UC004-POS-02` | positive | PR-ISS | ADV-I | Issuer is suspended mid-transaction between challenge issuance and verification. | revocation timing is deterministic and identical across two independent verifier implementations |

### UC-006

| Test ID | Type | Predicates | Adversary | Description | Expected result |
|---|---|---|---|---|---|
| `CT-UC006-POS-01` | positive | PR-LIV;PR-FRE;PR-HLD | ADV-U | Returning user presents a fresh proof continuous with the original enrolment commitment. | verifier returns same-enrolled-subject=true without a reusable global identifier in the artefact |
| `CT-UC006-NEG-01` | negative | PR-LIV;PR-FRE;PR-HLD | ADV-U | Attacker holds a copied wallet key but cannot satisfy same-human-as-enrolment continuity. | verifier rejects; failure reason does not distinguish 'key ok / continuity failed' in a way that helps the attacker |
| `CT-UC006-POS-02` | positive | PR-LIV;PR-FRE;PR-HLD | ADV-IV | Same principal logs in to two unrelated services under the minimum liveness profile. | the two proof artefacts are unlinkable to each other under the service-issuer collusion adversary stated in the profile |
| `CT-UC006-NEG-02` | negative | PR-LIV;PR-FRE;PR-HLD | ADV-U | Principal migrates device without following the recovery policy. | login fails deterministically rather than silently degrading to key-only assurance |

### UC-017

| Test ID | Type | Predicates | Adversary | Description | Expected result |
|---|---|---|---|---|---|
| `CT-UC017-POS-01` | positive | — | ADV-W | Reference low-end device generates a proof within the profile's documented resource ceiling. | proof verifies and resource usage (memory, time, battery) is within the published benchmark bounds |
| `CT-UC017-NEG-01` | negative | — | ADV-W | Device capability is below the minimum ceiling and no fallback policy signal is present. | wallet returns a standardised failure code rather than silently invoking a mediated prover |
| `CT-UC017-POS-02` | positive | — | ADV-W | Wallet invokes an explicitly authorised mediated-proving fallback. | verifier output carries an explicit fallback indicator and the mediator cannot reconstruct protected inputs from the exchanged data |
| `CT-UC017-NEG-02` | negative | — | ADV-W | Fallback is triggered without an explicit policy signal. | verifier treats the proof as non-conformant rather than accepting a silently downgraded adversary model |

### UC-020

| Test ID | Type | Predicates | Adversary | Description | Expected result |
|---|---|---|---|---|---|
| `CT-UC020-POS-01` | positive | PR-LIV;PR-HLD;PR-FRE | ADV-IV | Principal completes an accredited alternative liveness process and presents the resulting proof. | verifier returns an explicit assurance class for the alternative policy, equal to or clearly distinguished from the default |
| `CT-UC020-NEG-01` | negative | PR-LIV;PR-HLD;PR-FRE | ADV-V | Verifier demands the default facial-liveness method despite the alternative profile being accepted by policy. | conformant verifier implementation must not reject a policy-accepted alternative profile |
| `CT-UC020-NEG-02` | negative | PR-LIV;PR-HLD;PR-FRE | ADV-IV | Verifier attempts to infer disability status from the choice of alternative profile alone. | profile disclosure fields do not include an unnecessary disability attribute; test fails if one is present |
| `CT-UC020-POS-02` | positive | PR-LIV;PR-HLD;PR-FRE | ADV-IV | Alternative-profile proof is submitted alongside a default-profile proof from a different principal for the same transaction type. | both proofs are accepted under their respective declared assurance classes without discrimination in verifier decision logic |

### UC-021

| Test ID | Type | Predicates | Adversary | Description | Expected result |
|---|---|---|---|---|---|
| `CT-UC021-POS-01` | positive | PR-HLD;PR-LIV;PR-FRE | ADV-U | Legitimate principal completes recovery after key compromise, satisfying liveness and same-human continuity. | old key is invalidated and the new key is bound; nullifier continuity follows the documented recovery policy |
| `CT-UC021-NEG-01` | negative | PR-HLD;PR-LIV;PR-FRE | ADV-U | Key thief presents a proof using the copied key alone, without a live human satisfying continuity. | composite policy rejects; rejection reason does not reveal enrolment membership to the attacker |
| `CT-UC021-POS-02` | positive | PR-HLD;PR-LIV;PR-FRE | ADV-U | Two independent verifier implementations apply the same composite (key-control AND continuity) policy to identical inputs. | both implementations return the same composite result |
| `CT-UC021-NEG-02` | negative | PR-HLD;PR-LIV;PR-FRE | ADV-U | Attacker races a fraudulent transaction against the legitimate user's in-progress recovery. | race is resolved deterministically by profile-defined ordering, not implementation-specific timing |

## CL-2 — Extended Personhood Profile

### UC-001

| Test ID | Type | Predicates | Adversary | Description | Expected result |
|---|---|---|---|---|---|
| `CT-UC001-POS-01` | positive | PR-LIV;PR-PER;PR-UNQ;PR-HLD;PR-FRE | ADV-U | Same person attempts account creation twice in the same scope and epoch. | second attempt produces the same nullifier and is rejected as a duplicate |
| `CT-UC001-NEG-01` | negative | PR-LIV;PR-PER;PR-UNQ;PR-HLD;PR-FRE | ADV-IV | Same person creates accounts in two legitimately separate contexts under issuer-verifier collusion. | the two nullifiers must not be linkable to each other under the adversary model the profile declares |
| `CT-UC001-POS-02` | positive | PR-LIV;PR-PER;PR-UNQ;PR-HLD;PR-FRE | ADV-V | Verifier presents a stale enrolment root at presentation time. | verification fails deterministically rather than accepting a stale root |
| `CT-UC001-NEG-02` | negative | PR-LIV;PR-PER;PR-UNQ;PR-HLD;PR-FRE | ADV-V | Verifier attempts to substitute a different audience value in the transcript after challenge issuance. | proof verification fails; substitution is detectable by the wallet before presentation |

### UC-002

| Test ID | Type | Predicates | Adversary | Description | Expected result |
|---|---|---|---|---|---|
| `CT-UC002-POS-01` | positive | PR-PER;PR-UNQ;PR-FRE | ADV-IV | Principal participates in two unrelated communities under the same accreditation framework. | proofs across the two communities are unlinkable under the declared platform-issuer collusion adversary |
| `CT-UC002-NEG-01` | negative | PR-PER;PR-UNQ;PR-FRE | ADV-U | Principal presents a proof from a recovered wallet whose nullifier changed inconsistently with policy. | platform rejects or requires an explicit continuity re-proof per the documented recovery rule |
| `CT-UC002-POS-02` | positive | PR-PER;PR-UNQ;PR-FRE | ADV-U | Same community accessed from two different clients (mobile and web) by the same principal. | both clients derive the same context-scoped nullifier |
| `CT-UC002-NEG-02` | negative | PR-PER;PR-UNQ;PR-FRE | ADV-I | Issuer embeds a covert per-holder tag in the underlying attestation. | conformant proof construction does not surface issuer-chosen covert values in the presented artefact |

### UC-005

| Test ID | Type | Predicates | Adversary | Description | Expected result |
|---|---|---|---|---|---|
| `CT-UC005-POS-01` | positive | PR-LIV;PR-PER;PR-UNQ;PR-FRE | ADV-U | Principal completes recovery with fresh liveness and enrolment continuity. | old key is invalidated, continuity state is updated, and no second enrolment is created |
| `CT-UC005-NEG-01` | negative | PR-LIV;PR-PER;PR-UNQ;PR-FRE | ADV-U | Malicious help-desk operator attempts recovery on behalf of a principal without a satisfying liveness proof. | recovery is rejected; audit event contains no correlating biometric data |
| `CT-UC005-POS-02` | positive | PR-LIV;PR-PER;PR-UNQ;PR-FRE | ADV-IV | Recovery completes and the old key is subsequently presented in an unrelated transaction. | old key is uniformly rejected across all verifiers that consult the revocation state |
| `CT-UC005-NEG-02` | negative | PR-LIV;PR-PER;PR-UNQ;PR-FRE | ADV-U | Recovery attempt fails due to non-matching liveness. | failure response does not leak whether the presenting party has an enrolment on file |

## CL-3 — Delegated Agent Profile

### UC-009

| Test ID | Type | Predicates | Adversary | Description | Expected result |
|---|---|---|---|---|---|
| `CT-UC009-POS-01` | positive | PR-LIV;PR-HLD;PR-FRE | ADV-A | Principal proves fresh liveness and signs delegation evidence bound to agent key, scope and duration. | service accepts authorisation only for the exact agent key, scope and relying-party context in the transcript |
| `CT-UC009-NEG-01` | negative | PR-LIV;PR-HLD;PR-FRE | ADV-A | Agent swaps its key after authorisation and presents the original delegation evidence. | service rejects: delegation is bound to the original agent key, not renewable by substitution |
| `CT-UC009-POS-02` | positive | PR-LIV;PR-HLD;PR-FRE | ADV-W | Delegation evidence expires at the end of its stated validity period. | service rejects presentation after expiry using a standard, non-ambiguous reason code |
| `CT-UC009-NEG-02` | negative | PR-LIV;PR-HLD;PR-FRE | ADV-A | Agent presents only a liveness proof with no delegation evidence. | service must not treat liveness proof alone as sufficient authorisation |

### UC-010

| Test ID | Type | Predicates | Adversary | Description | Expected result |
|---|---|---|---|---|---|
| `CT-UC010-POS-01` | positive | PR-FRE;PR-LIV;PR-HLD | ADV-A | Agent requests a new permission; principal completes a fresh step-up bound to the specific action. | service approves a narrowly scoped delegation update matching the action digest |
| `CT-UC010-NEG-01` | negative | PR-FRE;PR-LIV;PR-HLD | ADV-A | Agent attempts to reuse a step-up approval for a materially different action. | service rejects: action digest mismatch invalidates the approval |
| `CT-UC010-POS-02` | positive | PR-FRE;PR-LIV;PR-HLD | ADV-A | Step-up approval expires at the end of the short permission window. | service enforces expiry consistently and requires a new step-up for further action |
| `CT-UC010-NEG-02` | negative | PR-FRE;PR-LIV;PR-HLD | ADV-W | Compromised service attempts to omit material action details from the challenge. | wallet-side policy refuses to approve an under-specified action digest |

## CL-4 — Federated & Adversarial Assurance Profile

### UC-012

| Test ID | Type | Predicates | Adversary | Description | Expected result |
|---|---|---|---|---|---|
| `CT-UC012-POS-01` | positive | PR-ISS | ADV-R | Issuer is suspended before presentation time; profile applies presentation-time status semantics. | verifier rejects the proof with a deterministic, reason-coded status result |
| `CT-UC012-NEG-01` | negative | PR-ISS | ADV-V | Verifier consults a stale cached issuer set that predates the suspension. | stale-cache acceptance is a documented non-conformance; conformant verifiers enforce cache-age limits |
| `CT-UC012-POS-02` | positive | PR-ISS | ADV-R | Two independent verifier implementations evaluate the same suspension timeline. | both return the same status result and reason code for identical inputs |
| `CT-UC012-NEG-02` | negative | PR-ISS | ADV-V | Status check is implemented as a holder-specific online query. | conformant profile forbids holder-identifying status queries; test fails if the holder is individually queryable |

### UC-013

| Test ID | Type | Predicates | Adversary | Description | Expected result |
|---|---|---|---|---|---|
| `CT-UC013-POS-01` | positive | PR-ISS | ADV-I | Proof discloses policy version P1 and is presented while P1 is still accepted during a P1→P2 transition. | verifier accepts with an explicit policy-version result |
| `CT-UC013-NEG-01` | negative | PR-ISS | ADV-I | Proof omits the policy version field entirely. | verifier rejects: policy version is mandatory for a conformant profile disclosure |
| `CT-UC013-POS-02` | positive | PR-ISS | ADV-I | P1 is formally deprecated with a published effective date; proof is presented after that date. | verifier returns accepted-with-deprecation or rejected per the profile's own migration rule, consistently |
| `CT-UC013-NEG-02` | negative | PR-ISS | ADV-V | Verifier silently treats a deprecated policy version as equivalent to the current one. | conformant verifier must surface the version distinction in its output, not merge them silently |

### UC-022

| Test ID | Type | Predicates | Adversary | Description | Expected result |
|---|---|---|---|---|---|
| `CT-UC022-POS-01` | positive | PR-ISS | ADV-P | Validly signed attestation from an accredited-but-later-compromised provider is verified before the compromise is detected. | cryptographic verification succeeds; verifier output does not claim the biometric determination was correct |
| `CT-UC022-NEG-01` | negative | PR-ISS | ADV-P | After compromise is detected, verifier output continues to represent the ZKP as proof of correct determination. | conformance language check fails: any verifier or documentation text implying the proof establishes correctness is non-conformant |
| `CT-UC022-POS-02` | positive | PR-ISS | ADV-P | Framework operator suspends the provider's accreditation after the incident. | suspension propagates to subsequent status checks without requiring mass disclosure of holder biometrics |
| `CT-UC022-NEG-02` | negative | PR-ISS | ADV-IV | Incident response attempts to identify affected holders by deanonymising presented proofs. | conformant incident process resolves affected policy classes without holder deanonymisation |

### UC-023

| Test ID | Type | Predicates | Adversary | Description | Expected result |
|---|---|---|---|---|---|
| `CT-UC023-POS-01` | positive | PR-UNQ | ADV-V | Wallet is asked for a proof under a context identifier the user's policy engine recognises as authorised. | proof is generated only for that authorised context |
| `CT-UC023-NEG-01` | negative | PR-UNQ | ADV-V | One verifier operating two nominally separate services requests the same context identifier for both. | wallet rejects the unauthorised context reuse or the two resulting artefacts remain unlinkable |
| `CT-UC023-POS-02` | positive | PR-UNQ | ADV-IV | Two genuinely separate, properly authorised contexts are used by the same principal. | the two proof artefacts are unlinkable under the declared adversary model |
| `CT-UC023-NEG-02` | negative | PR-UNQ | ADV-V | Verifier changes its context identifier without a defined migration path. | wallet treats this as a new, distinct context rather than silently continuing the old nullifier scope |

### UC-024

| Test ID | Type | Predicates | Adversary | Description | Expected result |
|---|---|---|---|---|---|
| `CT-UC024-POS-01` | positive | PR-ISS | ADV-IV | Issuer and verifier combine issuance timing, commitments and roots in a documented red-team exercise. | the privacy result explicitly states what remains unlinkable, for how long, and under what assumptions |
| `CT-UC024-NEG-01` | negative | PR-ISS | ADV-IV | A profile claims 'collusion resistance' with no stated adversary, horizon or assumptions. | unfalsifiable claim fails conformance per DRAFTING-RULES.md rule 1 and rule 2 |
| `CT-UC024-POS-02` | positive | PR-ISS | ADV-I | Issuer-issued artefacts are inspected for covert per-holder tags. | no covert tag is present in the presented proof artefact |
| `CT-UC024-NEG-02` | negative | PR-ISS | ADV-IV | Unique combinations of policy fields fingerprint a specific holder across presentations. | conformant profile documents and bounds this residual fingerprinting risk; undocumented fingerprinting fails |

### UC-025

| Test ID | Type | Predicates | Adversary | Description | Expected result |
|---|---|---|---|---|---|
| `CT-UC025-POS-01` | positive | PR-LIV;PR-HLD;PR-FRE | ADV-V | Wallet binds several credential predicates plus liveness to one composite transcript. | verifier returns a single composite result and no component is individually replayable elsewhere |
| `CT-UC025-NEG-01` | negative | PR-LIV;PR-HLD;PR-FRE | ADV-V | One component proof in the bundle uses a different transcript than the others. | bundle fails as a whole; partial acceptance of a mismatched component is non-conformant |
| `CT-UC025-POS-02` | positive | PR-LIV;PR-HLD;PR-FRE | ADV-IV | Same composite bundle type is presented repeatedly across unrelated tasks. | repetition does not expose a stable cross-task identifier beyond the declared adversary model |
| `CT-UC025-NEG-02` | negative | PR-LIV;PR-HLD;PR-FRE | ADV-V | A single component proof from one bundle is replayed inside a second, unrelated bundle. | verifier detects the transcript mismatch and rejects the second bundle |

### UC-026

| Test ID | Type | Predicates | Adversary | Description | Expected result |
|---|---|---|---|---|---|
| `CT-UC026-POS-01` | positive | — | ADV-U | Wallet and verifier negotiate a mutually supported profile from an advertised list. | negotiated profile and algorithm identifier are both present in the verifier output |
| `CT-UC026-NEG-01` | negative | — | ADV-U | Downgrade attacker forces negotiation toward a deprecated, weaker profile. | conformant wallet or verifier refuses the downgrade past the published minimum version |
| `CT-UC026-POS-02` | positive | — | ADV-U | Same predicate is proven under profile version A and profile version B. | both proofs yield semantically identical predicate results |
| `CT-UC026-NEG-02` | negative | — | ADV-V | Verifier receives a profile identifier it does not support. | verifier returns a standard unsupported-profile error rather than an ambiguous generic failure |

### UC-027

| Test ID | Type | Predicates | Adversary | Description | Expected result |
|---|---|---|---|---|---|
| `CT-UC027-POS-01` | positive | — | ADV-V | Verifier rejects a proof and issues a decision receipt with profile, policy, status snapshot and failure class. | receipt is machine-readable and sufficient to distinguish proof failure from policy rejection |
| `CT-UC027-NEG-01` | negative | — | ADV-V | Verifier returns an opaque 'invalid proof' message with no reason class. | conformant profile requires a standard reason code; opaque failure is non-conformant |
| `CT-UC027-POS-02` | positive | — | ADV-V | Holder initiates an appeal using only the decision receipt. | appeal process can verify the decision without requiring raw biometric resubmission |
| `CT-UC027-NEG-02` | negative | — | ADV-IV | The same underlying failure produces different reason classes from two verifier implementations. | conformance test fails: reason-class taxonomy must be applied consistently across implementations |

### UC-030

| Test ID | Type | Predicates | Adversary | Description | Expected result |
|---|---|---|---|---|---|
| `CT-UC030-POS-01` | positive | PR-LIV;PR-PER;PR-UNQ;PR-HLD;PR-FRE | ADV-U | Each of two wallet implementations proves attestations from each of two issuer implementations to each of two verifiers. | the full cross-product produces consistent verifier outcomes for identical inputs |
| `CT-UC030-NEG-01` | negative | PR-LIV;PR-PER;PR-UNQ;PR-HLD;PR-FRE | ADV-U | A maliciously crafted, malformed proof is submitted to all verifier implementations. | all conformant verifiers reject it; any implementation that accepts it fails the plugfest |
| `CT-UC030-POS-02` | positive | PR-LIV;PR-PER;PR-UNQ;PR-HLD;PR-FRE | ADV-V | All implementations independently verify their own generated proofs. | self-verification succeeds for every implementation as a precondition to cross-vendor testing |
| `CT-UC030-NEG-02` | negative | PR-LIV;PR-PER;PR-UNQ;PR-HLD;PR-FRE | ADV-V | Implementations that pass self-verification are cross-tested against each other. | any pair that disagrees on outcome for identical inputs is logged as a defect, even though each passed alone |

