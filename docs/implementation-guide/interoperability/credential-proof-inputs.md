---
layout: default
title: "Credential Proof Inputs"
parent: "DTG Interoperability"
nav_order: 2
---
# Credential proof inputs

A proof construction operates over governed credential evidence. It must not repair missing credential semantics by treating wallet co-location, shared device control, common presentation timing, or implementation convention as proof of a relationship.

## Input classes

| Input class | Required provenance | ZKP treatment |
|---|---|---|
| Claim value or predicate input | credential and issuer semantics | prove only the declared predicate |
| Holder-binding material | credential/profile binding rule | establish possession/control within the declared model |
| Credential status | authoritative status mechanism | bind the relevant status/freshness decision to verification |
| Identifier relationship | explicit evidence defined by the responsible credential/governance layer | treat as an independent witness requirement when the proof depends on it |
| Recognition/accreditation state | registry or governance authority | evaluate separately from mathematical proof validity |
| Delegation/mandate | authoritative delegation mechanism | verify separately; never derive from holder binding |

## P-DID, R-DID and M-DID dependency

The Credential Specification discussion tracked in `trustoverip/dtgwg-cred-spec#9` identifies relationships that may be required by ZKP constructions but are not safe to assume implicitly. Until the owning specification resolves the semantics, this workspace treats such linkage as an **open external dependency**.

A ZKP profile that depends on correspondence between two DTG identifiers MUST declare:

- which identifiers are being related;
- what semantic relationship is required;
- what verifiable evidence establishes that relationship;
- who is authoritative for that evidence;
- whether the relationship is current, historical, scoped or revocable; and
- what correlation surface is introduced by establishing it.

{: .warning }
Co-possession is not relationship evidence. A wallet that can access two identifiers or credentials does not, by that fact alone, prove that they identify the same person, role, relationship participant or controller.

## Failure handling

If required relationship evidence is absent, stale, unverifiable or outside the accepted governance scope, the implementation must return a distinct semantic failure. It must not silently downgrade the proof to a weaker statement while retaining the stronger relying-party claim.
