---
layout: default
title: Federated registry topology
nav_order: 13
parent: Diagrams
has_toc: true
---
# Federated registry topology

```mermaid
flowchart LR
 P1[Publisher A] --> F[Distribution layer]
 P2[Publisher B] --> F
 G[Recognition authority] --> F
 F --> C[Bounded cache]
 C --> V[Verifier]
 X[Conflict policy] --> V
```

## Interpretation

Distribution does not rewrite authority. Conflict and freshness behavior are explicit.

## Assurance use

Use this diagram with the applicable deployment profile, scenario, threat-control mapping and evidence record. The diagram is explanatory; the linked records remain authoritative.
