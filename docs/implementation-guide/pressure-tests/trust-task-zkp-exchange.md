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
| Reviewed revision | `7e0d755f5b815498c861cacecee5cae49b3f14eb` |
| Reviewed | 2026-08-18 |
| ZKP profile | Trust Task ZKP profile |
| Trigger | Trust Tasks authorization, task-control, duplicate-execution, digest and payload-validation changes |

## Material upstream changes re-examined

The current Trust Tasks framework now makes several boundaries explicit that were previously only assumptions in this fork:

- identity and proof validation are not authorization;
- consequential specifications declare the class of authorization evidence they rely on;
- authority/required conditions are re-evaluated before irreversible effects;
- task control defines cancel, suspend and resume;
- duplicate execution protection is normative;
- external citations can carry a task digest rather than relying on an id alone;
- transport bindings must state the security properties relied upon; and
- runtime payload validation must be explicit rather than inferred from a TypeScript type.

These changes strengthen the architectural alignment with the ZKP fork. They also create new lifecycle assertions that a ZKP composition must not bypass.

## Findings

| Finding | Threat | Primary disposition | Evidence of closure |
|---|---|---|---|
| F-005: a valid proof can be replayed into a different task, audience or requested action | [`THR-050`](../reference/identifier-register.md#thr-050) | `companion-specification` | exact task/audience/challenge/task-digest transcript-binding tests |
| F-006: a valid proof or recognized task participant can be misread as authorization | [`THR-048`](../reference/identifier-register.md#thr-048) | `governance` | separate authorization evidence and explicit negative non-inference tests |
| F-007: acceptance-time authority can become stale before a consequential effect | [`THR-052`](../reference/identifier-register.md#thr-052) | `runtime-control` | effect-time status/delegation/policy/task-control re-evaluation |
| F-008: a cancelled or suspended task can be resumed using a cached valid proof while current authority is no longer valid | [`THR-051`](../reference/identifier-register.md#thr-051) | `runtime-control` | resume path refreshes all evidence required at the next effect checkpoint |
| F-009: task id equality without content binding can pair proof evidence with the wrong task document | [`THR-050`](../reference/identifier-register.md#thr-050) | `companion-specification` | task digest or equivalent content-bound citation validated before reliance |
| F-010: transport or generated type acceptance can be mistaken for payload semantic validation | [`THR-052`](../reference/identifier-register.md#thr-052) | `implementation-guidance` | explicit payload validation policy and negative malformed-payload tests |

## Composition invariant

```text
proof_valid
    != task_accepted
    != task_authorized
    != authority_still_valid_at_effect_time
    != effect_completed
```

A deployment may require all of these outcomes, but the evidence and authority for each remain separate.

## Recommendation

Bind proof transcripts to exact task content where the task is relied upon, not merely to a task id. Preserve Trust Tasks' explicit authorization boundary. For delayed or resumable consequential work, define the effect checkpoint at which credential status, delegation, policy and task-control state are refreshed.

Verification receipts should retain the minimum versioned evidence needed to explain the decision without copying sensitive task payloads.

## Retest trigger

Re-run when the Trust Tasks framework version changes materially, task-control semantics change, authorization-evidence requirements change, task-digest semantics change, or payload validation/security-binding requirements change.
