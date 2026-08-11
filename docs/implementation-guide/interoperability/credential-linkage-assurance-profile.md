---
layout: default
title: "Credential Linkage Assurance Profile"
parent: "DTG Interoperability"
nav_order: 4
---
# Credential linkage assurance profile

This profile defines how a ZKP construction handles a DTG credential relationship when the proof statement depends on correspondence between identifiers or credential subjects. It does **not** define the missing credential relationship itself. That authority remains with the Credential Specification and its governance process.

## Linkage classes

### L1 — P-DID to R-DID

A construction may need to establish that the persona represented through a P-DID corresponds to the participant represented through an R-DID. The proof MUST consume explicit relationship evidence defined by the responsible credential/governance layer. Wallet co-possession is insufficient.

### L2 — R-DID to M-DID

A construction may need to establish that the relationship participant represented through an R-DID corresponds to the controller or subject represented by the membership credential's M-DID. The required semantic relationship and its evidence MUST be defined outside the ZKP layer before the ZKP profile can claim it.

## Requirements

### ZKP-LINK-01 — Explicit relationship witness

A proof construction that depends on correspondence between two DTG identifiers MUST identify verifiable evidence establishing the required relationship. It MUST NOT treat co-possession, common wallet storage, common device control, common presentation timing, or implementation convention as sufficient relationship evidence.

### ZKP-LINK-02 — Linkage provenance and authority

Relationship evidence MUST identify the issuing or governing authority, relationship type, scope, lifecycle/status semantics and verification method. The verifier MUST be able to determine whether that authority is acceptable under the applicable relying-party policy.

### ZKP-LINK-03 — Correlation impact

A linkage mechanism MUST be evaluated against the privacy class and context boundaries claimed by the applicable profile. Stable linkage handles MUST NOT be exposed outside the governed context merely to simplify verification.

### ZKP-LINK-04 — Fail closed on unresolved linkage

If a proof statement requires a relationship that the authoritative credential/governance layer has not defined or the presenter cannot evidence, the implementation MUST fail the stronger proof request explicitly. It MUST NOT return a success result whose semantics imply the missing relationship.

## Verification result

A linkage-aware verification result should distinguish:

- `relationship-established` — required evidence was verified under an accepted authority;
- `relationship-not-established` — evidence was absent, invalid, stale or unacceptable;
- `relationship-semantics-unresolved` — the external specification has not defined the relationship required by the requested proof statement.

The result must not expose unnecessary identifiers or stable correlation handles.

## Upstream pressure-test question

The profile leaves a concrete question for the Credential TF: **what verifiable artifact or governed relationship allows an implementation to establish the P-DID/R-DID and R-DID/M-DID correspondence required by a proof without defeating the privacy properties the ZKP profile is intended to preserve?**
