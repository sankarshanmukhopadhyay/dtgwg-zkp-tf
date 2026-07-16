---
title: Attestation schema and correlation profile
status: incubating
normative_status: non-normative
owner: DTG ZKP Task Force
last_reviewed: 2026-07-16
---


# Attestation schema and correlation profile

A profile identifies each attestation field as one of: disclosed, selectively disclosed, committed, derived in proof, verifier-resolved, or prohibited. The schema must not include issuer-local tracking values merely because they are convenient for operations.

## Minimum semantic fields

| Field | Purpose | Preferred treatment |
|---|---|---|
| schema/profile version | Interpretation and negotiation | disclosed at profile granularity |
| policy identifier and version | Reliance semantics | prove accepted value or disclose a coarse accepted class |
| assurance class | Risk decision | minimize cardinality; avoid issuer-specific values |
| issuance and expiry bounds | freshness and validity | prove interval membership where feasible |
| holder binding commitment | subject continuity | hidden witness or committed value |
| status reference | revocation and suspension | privacy-preserving status mechanism or bounded cache |
| issuer accreditation reference | issuer qualification | set-membership proof or explicit disclosure per profile |
| enrolment-root reference | scoped uniqueness | committed and context-governed; never a global public identifier |

## Schema controls

1. Every field has a documented assurance purpose and disclosure consequence.
2. Stable identifiers, fine-grained timestamps and unique status indices require explicit justification.
3. Schema versions cannot encode issuer identity through rare variants or extension ordering.
4. Status mechanisms are analysed together with network and registry observations.
5. Migration specifies how old attestations remain interpretable without enabling downgrade or indefinite correlation.
