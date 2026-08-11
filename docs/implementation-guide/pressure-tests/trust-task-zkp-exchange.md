---
layout: default
title: "Pressure Test — Trust Task ZKP Exchange"
parent: "Cross-Specification Pressure Tests"
nav_order: 2
---
# Pressure test — Trust Task ZKP exchange

## Review record

| Field | Value |
|---|---|
| Review ID | ZPT-002 |
| Target | `trustoverip/dtgwg-trust-tasks-tf`, task/exchange semantics |
| Reviewed | 2026-08-11 |
| ZKP profile | Trust Task ZKP profile |

## Findings

| Finding | Threat | Primary disposition | Evidence of closure |
|---|---|---|---|
| F-004: a valid proof can be replayed into a different task, audience or requested action | THR-050 | `companion-specification` | exact task/audience/challenge transcript-binding tests |
| F-005: task participation can be misread as delegated authority | THR-048 | `governance` | separate authority evidence and explicit non-inference tests |
| F-006: policy changes can make a previously acceptable proof semantically unacceptable | THR-052 | `runtime-control` | policy/version evidence and deterministic reevaluation behavior |

## Recommendation

Bind the proof to exact task context while keeping authority evidence outside the proof-presence inference. Verification receipts should retain enough versioned evidence to explain the relying-party decision without replicating private task content.

## Retest trigger

Re-run when Trust Task envelope fields, evidence semantics, delegation semantics or task identifiers materially change.
