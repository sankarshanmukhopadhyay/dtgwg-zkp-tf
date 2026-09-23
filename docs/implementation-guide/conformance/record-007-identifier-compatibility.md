---
layout: default
title: "Record 007 Identifier and Key-Profile Compatibility"
parent: "Conformance"
nav_order: 44
---
# Record 007 identifier and key-profile compatibility

This downstream compatibility assessment is pinned to canonical upstream construction record 007 at `cfd94063e5cfee7ba6df4dcfd28c10399a0ffd0a`.

Credential-spec examples and identifier guidance were observed at `trustoverip/dtgwg-cred-spec@1152a523c85febfb6b9b0b597a0783b6cdab884a`.

The purpose is not to choose a new identifier profile. It is to determine whether the identifier/key shapes currently appearing in DTG material can actually supply the witness relation record 007 requires.

## Compatibility findings

| Case | Downstream result | Meaning |
|---|---|---|
| same identifier in both credentials | record 007 not required | there is no cross-identifier common-control proposition |
| `did:key` with current Ed25519-style example | incompatible as shown | the derived document has no independent extension point carrying the required ZK-openable commitment |
| `did:peer` numalgo-0 | incompatible as shown | same derived-document limitation |
| `did:webvh` without an explicit ZK-openable commitment | evidence required | an extensible document does not establish that the needed commitment is actually present or correctly bound |
| extensible identifier profile with explicit ZK-openable commitment to the controller secret | compatible in principle | record 007 can consume the commitment if the selected profile defines its derivation/custody semantics |
| equality of a hidden child/parent credential field | use record 009 | hidden equality is not common control |
| counterparty identifier pair with no counterparty witness/linkage artifact | incompatible for presenter-only proof | the presenter cannot prove a secret it does not possess |
| counterparty-produced linkage artifact | possible issuance-time route | the artifact must be authenticated and profile-defined; downstream does not invent its credential representation |

## Important boundary

Record 007 proves a same-controller relation only under the selected commitment/key profile. It does not establish:

- one natural person;
- non-transfer of a controller secret;
- a chain predicate such as child `issuer == parent credentialSubject.id`;
- a counterparty's common control when the presenter has neither the counterparty witness nor an authenticated linkage artifact.

The chain predicate belongs to canonical record 009.

## Current Credential Spec implications

The current Credential Spec already uses or discusses `did:key`, `did:peer`, and `did:webvh` shapes. The examples themselves do not establish a canonical record-007 commitment profile.

Therefore:

- do **not** mark current examples record-007-compatible merely because their DID method can authenticate ordinary signatures;
- do **not** adopt the proposed wording from open upstream ZKP PR #11 until it merges;
- treat extensibility as only a precondition, not proof that the required commitment exists;
- retain the counterparty-linkage question under #26 where the presenter lacks the witness.

## Reuse

The machine-readable matrix in `fixtures/record-007-identifier-compatibility.json` is exercised by the repository test suite and should be consumed by record 010 / Community-Anchored Proof work before a concrete Clause 3 path is selected.
