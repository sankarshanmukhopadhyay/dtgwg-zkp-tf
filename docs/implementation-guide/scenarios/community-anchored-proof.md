# Community-Anchored Proof (ADR-001)

Status: experimental implementation target  
Tracks: [#14](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/14)  
Source: https://docs.fpp.storm.ws/dtg-community-anchored-proof-adr.html

## Target statement

A presenter proves, in one composed presentation, that:

1. the presenter possesses a valid relationship credential;
2. the presenter possesses a valid membership credential from community `C`; and
3. the issuer/counterparty of the relationship credential also holds a valid membership credential from the same community `C`.

The verifier should learn the outcome and deliberately disclosed attributes, but not the relationship identifier, counterparty identifier, holder identifier, or a reusable value that enables later correlation.

## Predicate decomposition

This repository models the target as a composed predicate set rather than inventing new Credential semantics:

| Clause | Experimental predicate responsibility | Required evidence |
| --- | --- | --- |
| 1 | credential possession/validity + holder binding | relationship credential, validity evidence, holder-binding evidence |
| 2 | membership/set predicate + holder binding | holder membership credential for community `C`, validity evidence |
| 3 | relationship-issuer binding + third-party membership/set predicate | sound evidence binding the relationship issuer to current membership in the same `C` |
| composed result | `PR-CMP` | verifier challenge, public inputs, deliberately disclosed attributes, registry/currentness state |

Existing experimental families such as `PR-REL`, `PR-HID`, and `PR-RES` may contribute to a construction. Their presence does not imply that Clause 3 is already solved.

## Clause 3 dependency boundary

Clause 3 is the critical unresolved seam. A conforming implementation needs a sound, independently checkable way for the presenter to prove a fact about the counterparty's membership while the counterparty is offline.

This repository MUST NOT simulate that property with an ordinary holder assertion or a stable registry lookup identifier. Until the credential/registry layers expose sufficient proof input — for example a suitable commitment, witness, accumulator input, or another construction-neutral equivalent — the Clause 3 construction is reported as **INDETERMINATE / external dependency**, not as a cryptographic PASS.

Any required issuance-time material is an explicit X3 dependency and must be surfaced before a construction is promoted.

## ADR requirement mapping

### Privacy P1–P5

The proof path must expose no relationship identifier, counterparty identifier, or holder identifier beyond deliberate disclosure. Repeated proofs must not contain a reusable binder. Cross-verifier comparison is part of the test surface.

### Soundness S1–S5

Credential absence, wrong-community membership, missing third-party membership, missing holder binding, and missing/reused verifier challenge are negative cases. S3 requires the counterparty to be offline at presentation time.

### Currency C1–C4

A construction must bind to independently checkable status/registry state and must not turn currentness checking into an identity/correlation oracle. Revocation propagation bounds are evidence, not assumptions.

### Registry T1–T4

The ZKP layer consumes a construction-neutral registry interface. It does not define one registry implementation. Registry state used by the proof must be independently checkable and sufficiently deterministic for equivalent verification.

### Deployment D1–D3

Concrete construction profiles must publish prover time/memory, verifier cost, and proof/transport size once a real Clause 3 construction exists. The semantic fixture in this repository is not a substitute for those measurements.

### Conformance X1–X3

Machine-readable semantic vectors cover ACCEPTS, REJECTS, UNLINKABLE, CURRENT and dependency-negative cases. Cross-implementation proof interoperability remains pending until a concrete Clause 3 construction and encoding are selected. Any issuance-time requirement is recorded explicitly.

## Executable semantic vectors

`conformance-harness/examples/community-anchored-proof.json` contains the current executable requirement-level vectors and `test_community_anchored_proof.py` evaluates them.

These vectors intentionally distinguish:

- a semantically complete candidate flow;
- failure when the counterparty is not a member of `C`;
- failure when a reusable proof binder appears;
- failure after revocation exceeds the published freshness bound;
- failure when verifier challenge binding is absent; and
- `indeterminate` when Clause 3 is asserted without independently checkable third-party membership evidence.

They are **semantic conformance evidence**, not a claim that a production zero-knowledge construction has been implemented.

## Relationship to asymmetric-edge pressure test

[#13](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/13) supplies adversarial cases that constrain privacy claims even when the Community-Anchored Proof verifies. In particular, proof-level hiding cannot justify relationship/contextual unlinkability when a reciprocal half or surrounding graph context is intentionally public.

## DPIP hand-off

The proof-validity and scoped privacy evidence produced here is intended to be bound into DPIP issue [#58](https://github.com/sankarshanmukhopadhyay/dtg-privacy-implementation-profile/issues/58). DPIP owns the resulting composed-interaction privacy conclusion; this repository owns proof predicates, construction evidence, and proof-level conformance.