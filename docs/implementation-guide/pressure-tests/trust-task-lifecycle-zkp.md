---
layout: default
title: "Pressure Test — Trust Task Lifecycle ZKP"
parent: "Cross-Specification Pressure Tests"
nav_order: 7
---
# Pressure test — Trust Task lifecycle ZKP

## Review record

| Field | Value |
|---|---|
| Review ID | ZPT-006 |
| Target | Trust Task task-control/effect-time lifecycle + ZKP + external authority/status |
| Trust Tasks revision | `7e0d755f5b815498c861cacecee5cae49b3f14eb` |
| Reviewed | 2026-08-18 |
| Trigger | cancel/suspend/resume and pre-effect re-evaluation semantics |

## Lifecycle scenario

```text
T0  task accepted
    |
T1  human proof verified
    |
T2  delegation valid
    |
T3  task suspended
    |
T4  delegation or credential status changes
    |
T5  task resume requested
    |
T6  irreversible effect checkpoint
```

A proof generated or verified at `T1` cannot, by itself, establish that the action remains authorized at `T6`.

## Evidence clocks

The composition can involve several independent clocks:

| Evidence | Clock / boundary | Refresh question |
|---|---|---|
| ZKP proof | challenge/session/proof validity | Is this proof still bound to the active request? |
| capture/liveness attestation | capture and attestation freshness | Does policy still accept the underlying human evidence? |
| credential | status/expiry/suspension | Is the credential acceptable now or at the required as-of time? |
| delegation/mandate | scope/expiry/revocation | Does the agent still have authority for this effect? |
| Trust Task | acceptance/control/effect checkpoint | Was the task cancelled or suspended? May it resume? |
| policy | version/effective time | Is the requested action still permitted under current policy? |

These clocks must not be collapsed into one `proof_valid` flag.

## Findings

| Finding | Threat | Primary disposition | Evidence of closure |
|---|---|---|---|
| F-025: cached proof validity is treated as current action authority after suspension | [`THR-051`](../reference/identifier-register.md#thr-051) | `runtime-control` | resume/effect path re-evaluates current authority evidence |
| F-026: task cancellation is ignored because a proof was already verified | [`THR-052`](../reference/identifier-register.md#thr-052) | `runtime-control` | task-control state is load-bearing at the next effect checkpoint |
| F-027: credential or issuer status changes between acceptance and effect | [`THR-052`](../reference/identifier-register.md#thr-052) | `runtime-control` | current/as-of status rule and deterministic degraded-mode behaviour |
| F-028: verifier refreshes proof freshness but not delegation or policy state | [`THR-051`](../reference/identifier-register.md#thr-051) | `implementation-guidance` | evidence refresh matrix names every authority input |
| F-029: partial effects are reported as simple success/failure, hiding what already happened | [`THR-052`](../reference/identifier-register.md#thr-052) | `operational-policy` | evidence distinguishes never-started, partial, suspended, cancelled and completed |

## Required assurance evidence

A deployment using delayed or resumable consequential tasks should produce:

- a documented effect checkpoint;
- the evidence set re-evaluated at that checkpoint;
- source/evaluation time for each status result;
- deterministic behaviour for unavailable status sources;
- task-control state and control-operation evidence;
- delegation scope and current status;
- policy version/effective time;
- proof/session freshness state; and
- a disposition that distinguishes partial application from non-execution.

## Recommendation

Define an **effect-time evidence refresh contract** for every consequential ZKP-enabled Trust Task profile. The contract should name each authority input, its freshness rule and the state transition that invalidates cached evidence.

## Retest trigger

Re-run when task-control semantics, effect-time authorization rules, credential/status lifecycle, delegation lifecycle or ZKP proof-freshness rules change.
