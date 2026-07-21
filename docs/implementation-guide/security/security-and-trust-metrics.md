---
layout: default
title: "Security and trust metrics"
parent: "Threats, Harms and Controls"
grand_parent: "Implementation Guide"
nav_order: 6
has_toc: true
---
# Security and trust metrics

These indicators adapt the RAHP trust-metric discipline to ZKP operational assurance. They measure control effectiveness without creating a new identity, correlation or surveillance surface.

| ID | Indicator | Evidence | Escalation signal |
|---|---|---|---|
| ZM-01 | proof validation failure rate | aggregate verifier counters by profile version | material deviation from tested baseline |
| ZM-02 | replay and transcript rejection rate | aggregate negative-decision reason codes | sudden increase or cross-domain pattern |
| ZM-03 | stale governance-state decision rate | signed snapshot age and rejection counters | freshness SLO breached |
| ZM-04 | downgrade attempt rate | negotiation and policy logs | any accepted downgrade or sustained attempts |
| ZM-05 | fallback invocation rate | aggregate path-selection events | fallback becomes default or disclosure rises |
| ZM-06 | mediated retention exception count | mediator audit evidence | any unexplained retention event |
| ZM-07 | correlation assessment failure rate | scheduled composition tests | any new deterministic linkage |
| ZM-08 | delegated-agent scope violation rate | aggregate authorization failures | accepted out-of-scope action or rising attempts |
| ZM-09 | contest and correction completion time | redress case timestamps | SLO breach or unresolved high-impact case |
| ZM-10 | incident acknowledgement and containment time | incident evidence records | authority or containment SLO breach |
| ZM-11 | accessibility disparity | privacy and completion comparison across supported paths | material disclosure or completion disparity |
| ZM-12 | expiring residual-risk exceptions | approval registry | exception enters escalation window |
| ZM-13 | critical-provider concentration | approved component and authority inventory | threshold breached without exit plan |
| ZM-14 | unavailable-status decision rate | aggregate status resolution outcomes | degraded mode exceeds approved window |

## Privacy constraints

Metrics must be collected at the coarsest useful aggregation. They must not include witnesses, predicates, credential identifiers, nullifiers, stable device identifiers, raw presentation transcripts or person-level histories unless an independently approved incident process requires narrowly scoped evidence. Retention, access and deletion rules are part of the metric definition.

## Evidence contract

Each metric record identifies the calculation boundary, collection purpose, accountable owner, threshold, privacy controls, retention period, linked threats, linked guardrails and escalation action. See `conformance/schemas/security-metric-evidence.schema.json`.
