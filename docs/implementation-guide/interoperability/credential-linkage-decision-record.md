---
layout: default
title: "Credential Linkage Decision Record"
parent: "DTG Interoperability"
nav_order: 5
---
# Credential linkage decision record

| Field | Position |
|---|---|
| Decision ID | C2 |
| Decision authority | DTG ZKP Task Force for ZKP consumption rules; Credential TF for credential semantics |
| Upstream status | unresolved external dependency |
| Fork status | implemented as non-normative working baseline |
| Source | `trustoverip/dtgwg-cred-spec#9` |
| Revisit trigger | upstream relationship model adopted or materially changed |

## Decision

The ZKP implementation workspace will not infer identifier equivalence from credential co-possession or shared wallet control. Where a proof statement depends on P-DID/R-DID, R-DID/M-DID, or another cross-credential relationship, the construction must consume explicit relationship evidence with a named authority and must account for the privacy impact of that linkage.

## Why

A proof can be cryptographically sound while making an invalid semantic assumption. Treating a wallet's access to multiple identifiers as evidence that they refer to the same person, controller or relationship participant would move an unresolved credential-model question into implementation convention. It would also risk creating stable linkage that contradicts the privacy profile.

## Consequences

- stronger proof statements fail closed until required relationship evidence exists;
- conformance tests can detect implementations that silently infer identity/relationship linkage;
- Credential TF remains responsible for defining the relationship semantics;
- future upstream resolution can replace the placeholder dependency without changing the authority boundary.
