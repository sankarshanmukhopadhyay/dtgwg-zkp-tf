---
layout: default
title: "Lifecycle flow"
parent: "Diagrams"
grand_parent: "Implementation Guide"
nav_order: 6
has_toc: true
---
# Lifecycle flow

```mermaid
stateDiagram-v2
 [*] --> Issued
 Issued --> Active
 Active --> Suspended
 Suspended --> Active
 Active --> Revoked
 Active --> Expired
 Expired --> Replaced
 Revoked --> ReenrolmentReview
 ReenrolmentReview --> Replaced
```

## Interpretation

Lifecycle transitions are authority-controlled and time-bound. Recovery or replacement does not erase prior revocation, duplicate-use or audit evidence.
