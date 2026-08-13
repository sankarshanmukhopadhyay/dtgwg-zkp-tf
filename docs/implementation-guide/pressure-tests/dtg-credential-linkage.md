---
layout: default
title: "Pressure Test — DTG Credential Linkage"
parent: "Cross-Specification Pressure Tests"
nav_order: 1
---
# Pressure test — DTG credential linkage

## Review record

| Field | Value |
|---|---|
| Review ID | ZPT-001 |
| Target | `trustoverip/dtgwg-cred-spec`, identifier/credential relationship semantics |
| Trigger | Credential Spec issue #9 and ZKP dependence on relationship evidence |
| Reviewed | 2026-08-11 |
| RAHP method | specification pressure testing and governance-boundary disposition |
| ZKP profile | credential linkage assurance profile |

## Affected parties

Credential subjects, relationship participants, wallet holders, delegated agents, verifiers, credential issuers, relying parties and people incorrectly linked by implementation inference.

## Findings

| Finding | Threat | Primary disposition | Evidence of closure |
|---|---|---|---|
| F-001: a ZKP can be mathematically valid while relying on an unproven P-DID/R-DID or R-DID/M-DID equivalence | [`THR-046`](../reference/identifier-register.md#thr-046) | `specification` | authoritative relationship semantics plus positive/negative vectors |
| F-002: a stable linkage mechanism can defeat the profile's cross-context privacy claim | [`THR-047`](../reference/identifier-register.md#thr-047) | `companion-specification` | correlation assessment demonstrating compliance with declared privacy class |
| F-003: implementations may silently treat co-possession as identity/relationship evidence | [`THR-046`](../reference/identifier-register.md#thr-046) | `implementation-guidance` | negative conformance fixture rejects implicit linkage |

## Recommendation

The Credential TF should define the relationship artifact or semantics needed to establish the relevant correspondence. The ZKP profile should consume that artifact without exposing a stable cross-context linkage handle. Until then, stronger statements requiring the unresolved relationship fail closed under [`ZKP-LINK-04`](../reference/identifier-register.md#zkp-link-04).

## Retest trigger

Re-run this review when Credential issue #9 is resolved, a relationship credential/model is adopted, or a proof construction proposes a concrete witness encoding for these relationships.
