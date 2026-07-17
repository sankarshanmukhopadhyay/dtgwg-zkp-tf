---
layout: default
title: Proof-system migration
nav_order: 20
parent: Diagrams
has_toc: true
---
# Proof-system migration

```mermaid
flowchart LR
 P1[Proof system v1] --> V[Dual-version verifier]
 P2[Proof system v2] --> V
 N[Negotiation policy] --> V
 V --> E[Versioned decision evidence]
 V --> X[v1 retirement gate]
```

## Interpretation

Overlap supports migration while negotiation policy prevents downgrade and ambiguous acceptance.

## Assurance use

Use this diagram with the applicable deployment profile, scenario, threat-control mapping and evidence record. The diagram is explanatory; the linked records remain authoritative.
