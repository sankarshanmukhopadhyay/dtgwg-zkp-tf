# v0.4.0 — DTG Interoperability and Cross-Specification Assurance

v0.4.0 connects the ZKP implementation and assurance workspace to evolving DTG credential, Trust Task/Trust Ceremony and RAHP work without transferring authority across specifications.

## Highlights

- governed, machine-readable DTG dependency and portfolio alignment model;
- explicit credential-linkage assurance profile for relationship-dependent ZKP constructions;
- Trust Task and Trust Ceremony binding profiles with hard separation between protocol context and authority;
- RAHP-aligned, reproducible cross-specification pressure tests;
- four new interoperability scenarios and eight conformance tests;
- ten executable interoperability fixtures;
- seven new cross-specification threats, expanding the canonical threat model from 45 to 52 threats;
- updated decision governance and requirement traceability for the new profiles.

## Assurance stance

This release deliberately fails closed when a proof statement depends on unresolved credential relationship semantics. It also prevents task or ceremony participation from being interpreted as delegated authority, and requires stable linkage/ceremony references to be assessed as correlation surfaces.

## Upstream authority boundaries

- Credential TF remains authoritative for credential and identifier relationship semantics.
- Trust Tasks TF remains authoritative for Trust Task and Trust Ceremony protocol semantics.
- RAHP remains authoritative for its reusable pressure-testing method.
- ZKP TF remains authoritative only for the ZKP profile requirements and assurance conclusions proposed here.

## Validation

The release is accepted only if repository documentation, navigation, conformance, fixtures, threat model, security assurance, decision governance, interoperability and traceability checks pass.

## Requirements alignment from Discussion #13

This working release also reconciles the root proof-of-liveness requirements with the Task Force's v0.4 progression discussion:

- treats privacy-not-assurance, context-dependent unlinkability, the profile split, paired boundaries and named adversary/horizon as adopted foundations;
- moves B1 and B2 from open questions to adopted working positions;
- defines the requirements → boundary decision method → predicate register authority chain;
- adds the construction-selection gate and explicitly classifies unreproduced circuit/lab benchmarks as experimental evidence;
- strengthens post-quantum migration and assurance-horizon requirements;
- adds lifecycle requirements for epochs, cryptoperiods, retention and revocation cadence;
- tightens delegation separation, biometric enrolment-dedup assumptions and multi-issuer independence; and
- aligns terminology with `F_PoP` and `f-distinct` where those terms sharpen the normative-reference mapping.
