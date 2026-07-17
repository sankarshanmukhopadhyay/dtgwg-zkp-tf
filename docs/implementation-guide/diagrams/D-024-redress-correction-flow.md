---
layout: default
title: Redress and correction flow
nav_order: 24
parent: Diagrams
has_toc: true
---
# Redress and correction flow

```mermaid
flowchart LR
 C[Contest] --> A[Authenticate and scope]
 A --> E[Preserve evidence]
 E --> R[Authority review]
 R --> X[Correct or uphold]
 X --> P[Propagate outcome]
 P --> N[Notify and close]
```

## Interpretation

Redress connects affected persons to the authority capable of correcting source state and downstream reliance.

## Assurance use

Use this diagram with the applicable deployment profile, scenario, threat-control mapping and evidence record. The diagram is explanatory; the linked records remain authoritative.
