---
layout: default
title: "Remote proving deployment"
parent: "Diagrams"
grand_parent: "Implementation Guide"
nav_order: 10
has_toc: true
---
# Remote proving deployment

```mermaid
flowchart LR
 W[Wallet] -->|encrypted job| P[Remote prover]
 P -->|presentation| V[Verifier]
 K[Isolated key service] --> P
 A[Assurance evidence] -.-> P
```

## Interpretation

The remote prover is an additional observation and administrative boundary requiring non-retention evidence.

## Assurance use

Use this diagram with the applicable deployment profile, scenario, threat-control mapping and evidence record. The diagram is explanatory; the linked records remain authoritative.
