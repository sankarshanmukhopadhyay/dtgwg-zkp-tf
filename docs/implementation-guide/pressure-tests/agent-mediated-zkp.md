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
| Reviewed revision | `trustoverip/dtgwg-trust-tasks-tf@7e0d755f5b815498c861cacecee5cae49b3f14eb` |
| Reviewed | 2026-08-18 |
| Related ADR | [`ADR-001`](../reference/identifier-register.md#adr-001) and [`ADR-013`](../reference/identifier-register.md#adr-013) |

## Refresh result

Trust Tasks now explicitly separates authorization from identity/proof validation and requires current required conditions before consequential effects. This strengthens the fork's existing rule that holder binding, human proof and agent authority are different statements.

The remaining pressure point is lifecycle: an agent can hold a technically valid human proof while its mandate is suspended, revoked, expired or outside the current task scope.

## Findings

| Finding | Threat | Primary disposition | Evidence of closure |
|---|---|---|---|
| F-015: an agent can present a valid human proof outside delegated scope | [`THR-051`](../reference/identifier-register.md#thr-051) | `governance` | principal/agent/scope/constraint/expiry/revocation evidence verified separately |
| F-016: verifier can confuse proof holder control with authority to bind a principal | [`THR-051`](../reference/identifier-register.md#thr-051) | `implementation-guidance` | explicit negative test rejects proof-only delegation |
| F-017: task-bound proof may be valid while the delegated mandate is already revoked | [`THR-051`](../reference/identifier-register.md#thr-051) | `runtime-control` | fresh delegation status at the applicable decision/effect time |
| F-018: a suspended task can resume after delegation or principal policy changed | [`THR-051`](../reference/identifier-register.md#thr-051) | `runtime-control` | resume path re-evaluates task-control, mandate, policy and credential status |
| F-019: a resolved agent name or transport identity may be treated as delegated authority | [`THR-051`](../reference/identifier-register.md#thr-051) | `implementation-guidance` | authorization decision names the mandate evidence rather than identity evidence |

## Recommendation

Keep the architectural rule:

```text
human proof
    + holder binding
    + agent identity
    + task participation
    != delegated authority
```

An agent-mediated consequential action succeeds only when the requested ZKP statement and the independently governed mandate/authorization checks succeed at the time they are required.

## Retest trigger

Re-run when delegation/mandate semantics, Trust Task authorization rules, task-control semantics or agent identity/naming inputs materially change.
