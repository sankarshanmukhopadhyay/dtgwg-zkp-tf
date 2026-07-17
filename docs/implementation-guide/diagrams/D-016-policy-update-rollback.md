---
layout: default
title: Policy update and rollback
nav_order: 16
parent: Diagrams
has_toc: true
---
# Policy update and rollback

```mermaid
flowchart LR
 A[Approved change] --> T[Test]
 T --> S[Staged deployment]
 S --> M[Monitor decisions]
 M -->|accepted| P[Promote]
 M -->|defect| R[Rollback]
 R --> E[Evidence and review]
```

## Interpretation

Policy deployment is versioned, tested and reversible. Rollback authority is preassigned.

## Assurance use

Use this diagram with the applicable deployment profile, scenario, threat-control mapping and evidence record. The diagram is explanatory; the linked records remain authoritative.
