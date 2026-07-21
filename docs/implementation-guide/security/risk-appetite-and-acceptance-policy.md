---
layout: default
title: "Risk appetite and acceptance"
parent: "Threats, Harms and Controls"
grand_parent: "Implementation Guide"
nav_order: 5
has_toc: true
---
# Risk appetite and acceptance policy

Risk acceptance is an exercise of delegated authority. It must be scoped, evidenced, time-bounded and revocable. This policy closes the formal risk-acceptance gap identified in the RAHP upstream toolkit while adapting the decision model to ZKP deployments.

## Appetite classes

| Class | Meaning | Acceptance rule |
|---|---|---|
| prohibited | unacceptable loss of proof integrity, covert correlation, unbounded authority, unavailable redress, or unsafe witness handling | cannot be accepted |
| exceptional | critical risk that may be tolerated only to contain a larger incident | maximum 72 hours; independent approval required |
| tolerable | bounded high or medium risk with compensating controls | maximum 90 days |
| operational | low residual risk within an approved profile | review at normal assurance cadence |

## Authority floor

| Risk | Minimum authority | Independent review |
|---|---|---|
| critical | governance authority plus security authority | mandatory |
| high | accountable deployment owner | mandatory for privacy, redress or affected-party harm |
| medium | control owner and deployment owner | risk-based |
| low | control owner | optional |

## Required record

Every approval must identify affected parties, scope, compensating controls, activation restrictions, evidence, expiry, review date and revocation triggers. Approval expires automatically and does not renew by silence.

## Mandatory revocation triggers

- evidence is shown to be false, incomplete or stale;
- severity or affected population materially increases;
- a guardrail becomes non-exceptionable;
- compensating controls fail;
- the deployment changes profile, topology, issuer set, mediator, context or authority;
- the approval reaches its expiry;
- incident evidence shows active exploitation or harm.

{: .warning }
Repeated temporary approvals must not be used to normalize an unsafe operating state. Three consecutive exceptions for the same root cause require governance review and a block-or-remediate decision.
