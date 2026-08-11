---
layout: default
title: "Pressure Test — Agent-Mediated ZKP"
parent: "Cross-Specification Pressure Tests"
nav_order: 4
---
# Pressure test — agent-mediated ZKP

## Review record

| Field | Value |
|---|---|
| Review ID | ZPT-004 |
| Target | ZKP + Trust Task delegated-agent composition |
| Reviewed | 2026-08-11 |
| Related ADR | ADR-001 and ADR-013 |

## Findings

| Finding | Threat | Primary disposition | Evidence of closure |
|---|---|---|---|
| F-010: an agent can present a valid human proof outside delegated scope | THR-051 | `governance` | principal/agent/scope/constraint/expiry/revocation evidence verified separately |
| F-011: verifier can confuse proof holder control with authority to bind a principal | THR-051 | `implementation-guidance` | explicit negative test rejects proof-only delegation |
| F-012: task-bound proof may be valid but delegated mandate may already be revoked | THR-051 | `runtime-control` | fresh delegation status evidence at relying-party decision time |

## Recommendation

Keep the existing architectural rule: holder binding and delegated authority are different statements. An agent-mediated proof succeeds only when both the requested ZKP statement and the independently governed mandate/authority checks succeed.

## Retest trigger

Re-run when DTG delegation/mandate semantics or Trust Task agent authority handling materially changes.
