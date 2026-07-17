---
layout: default
title: Deployment evidence flow
nav_order: 19
parent: Diagrams
has_toc: true
---
# Deployment evidence flow

```mermaid
flowchart LR
 T[Topology] --> B[Evidence bundle]
 S[Software provenance] --> B
 C[Control tests] --> B
 O[Operational exercises] --> B
 R[Residual risks] --> B
 B --> A[Accountable approval]
```

## Interpretation

Production readiness is supported by versioned design, implementation and operational evidence.

## Assurance use

Use this diagram with the applicable deployment profile, scenario, threat-control mapping and evidence record. The diagram is explanatory; the linked records remain authoritative.
