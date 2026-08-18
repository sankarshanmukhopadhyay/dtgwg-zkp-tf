---
layout: default
title: "Pressure Test — Trust Ceremony ZKP Composition"
parent: "Cross-Specification Pressure Tests"
nav_order: 3
---
# Pressure test — Trust Ceremony ZKP composition

## Review record

| Field | Value |
|---|---|
| Review ID | ZPT-003 |
| Target | Trust Ceremonies / enactment composition in `dtgwg-trust-tasks-tf` |
| Reviewed revision | `7e0d755f5b815498c861cacecee5cae49b3f14eb` |
| Reviewed | 2026-08-18 |
| ZKP profile | Trust Ceremony ZKP profile |

## Refresh result

The original composition invariant remains correct. The newer Trust Tasks authorization and effect-time lifecycle rules make it more important, not less: a ceremony can order or evidence several tasks, while authorization and current authority remain properties that must be established at the applicable decision/effect points.

## Findings

| Finding | Threat | Primary disposition | Evidence of closure |
|---|---|---|---|
| F-011: ceremony membership or completion may be treated as authority | [`THR-048`](../reference/identifier-register.md#thr-048) | `governance` | evidence domains remain separate; authorization independently verified |
| F-012: a stable ceremony/enactment identifier can become a cross-context correlation handle | [`THR-049`](../reference/identifier-register.md#thr-049) | `companion-specification` | minimised/scoped ceremony reference and privacy assessment |
| F-013: historical ceremony evidence can be reinterpreted under changed policy, task state or credential status | [`THR-052`](../reference/identifier-register.md#thr-052) | `runtime-control` | versioned policy/status/task-control evidence and explicit assurance horizon |
| F-014: ceremony completion can hide partial or cancelled consequential effects | [`THR-052`](../reference/identifier-register.md#thr-052) | `runtime-control` | step-level disposition distinguishes accepted, applied, partial, cancelled and suspended states |

## Composition invariant

```text
ceremony completion
    != proof validity
    != task authorization
    != delegated authority
    != effect completion
```

Each conclusion must be independently evidenced by its owning authority.

## Recommendation

Keep ceremony identifiers purpose-scoped and bind only the ceremony/step context needed by the ZKP transcript. Where a ceremony contains consequential or resumable tasks, preserve their individual task-control and effect-time authority checks rather than collapsing them into a ceremony-level success flag.

## Retest trigger

Re-run when ceremony/enactment metadata, evidence receipts, step disposition or completion semantics materially change.
