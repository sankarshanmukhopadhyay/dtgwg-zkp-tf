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
| Reviewed revision | `b89f389abbdae77ba60b673c0836c781c2b54169` |
| Reviewed | 2026-08-18 |
| Trigger | VWC edge-binding change plus still-open Credential Spec issue #9 |
| RAHP method | specification pressure testing and governance-boundary disposition |
| ZKP profile | credential linkage assurance profile |

## What changed since the previous review

Credential Spec now requires the VWC `digest` needed to bind witnessed evidence to a specific VRC/relationship edge. This materially improves **edge binding** and addresses the earlier condition where a VWC could identify a subject and task context without identifying the exact relationship being witnessed.

That change does **not** resolve the separate subject/controller correspondence problem tracked by Credential Spec issue #9:

- P-DID to R-DID;
- R-DID to M-DID; and
- how those relationships are proven without creating an unintended correlation mechanism.

The review therefore splits the previous broad linkage concern into two different questions.

## Affected parties

Credential subjects, relationship participants, wallet holders, delegated agents, verifiers, credential issuers, relying parties, witnesses and people incorrectly linked by implementation inference.

## Findings

| Finding | Threat | Status / disposition | Evidence of closure |
|---|---|---|---|
| F-001: VWC-to-edge binding was previously under-specified | [`THR-046`](../reference/identifier-register.md#thr-046) | `resolved-by-pr` for the VWC digest requirement | VWC digest required and verifier has the referenced VRC |
| F-002: P-DID/R-DID or R-DID/M-DID equivalence can still be assumed without authoritative evidence | [`THR-046`](../reference/identifier-register.md#thr-046) | `specification` | authoritative linkage semantics plus positive/negative vectors |
| F-003: a stable linkage mechanism can defeat cross-context privacy | [`THR-047`](../reference/identifier-register.md#thr-047) | `companion-specification` | correlation assessment demonstrating compliance with the declared privacy class |
| F-004: implementations can silently treat co-possession as subject/controller evidence | [`THR-046`](../reference/identifier-register.md#thr-046) | `implementation-guidance` | negative conformance fixture rejects implicit linkage |

## Key invariant

```text
VWC digest -> exact relationship edge
             !=
P-DID == R-DID == M-DID subject/controller equivalence
```

Both can be required by a profile, but they require different evidence.

## Recommendation

Treat edge binding as substantially improved and stop reporting it as an unresolved Credential Spec defect. Keep the cross-identifier linkage question open until the Credential TF defines the evidence model or explicitly constrains the construction.

Until then, stronger statements requiring unresolved P-DID/R-DID/M-DID correspondence fail closed under [`ZKP-LINK-04`](../reference/identifier-register.md#zkp-link-04).

## Retest trigger

Re-run when Credential Spec issue #9 is resolved, VRC/VWC digest semantics change, a relationship-linkage artifact is adopted, or a proof construction proposes a concrete witness encoding for identifier correspondence.
