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
| Target | Trust Ceremonies design work in `dtgwg-trust-tasks-tf` |
| Reviewed | 2026-08-11 |
| ZKP profile | Trust Ceremony ZKP profile |

## Findings

| Finding | Threat | Primary disposition | Evidence of closure |
|---|---|---|---|
| F-007: ceremony membership or completion may be treated as authority | [`THR-048`](../reference/identifier-register.md#thr-048) | `governance` | evidence domains remain separate; authority independently verified |
| F-008: a stable ceremony/enactment identifier can become a cross-context correlation handle | [`THR-049`](../reference/identifier-register.md#thr-049) | `companion-specification` | minimised/scoped ceremony reference and privacy assessment |
| F-009: historical ceremony evidence can be reinterpreted under changed policy or status | [`THR-052`](../reference/identifier-register.md#thr-052) | `runtime-control` | versioned policy/status evidence and explicit assurance horizon |

## Composition invariant

`ceremony completion != proof validity != delegated authority`. Each conclusion must be independently evidenced by its owning authority.

## Retest trigger

Re-run when ceremony envelope metadata, enactment identifiers, evidence receipts or completion semantics change.
