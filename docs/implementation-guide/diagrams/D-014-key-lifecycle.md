---
layout: default
title: Key and trust-anchor lifecycle
nav_order: 14
parent: Diagrams
has_toc: true
---
# Key and trust-anchor lifecycle

```mermaid
stateDiagram-v2
 [*] --> Generated
 Generated --> Active: authorized activation
 Active --> Rotating: scheduled or emergency
 Rotating --> Retired: propagation complete
 Active --> Suspended: compromise
 Suspended --> Revoked
 Retired --> Destroyed
```

## Interpretation

Every transition has an authority, effective time and evidence record.

## Assurance use

Use this diagram with the applicable deployment profile, scenario, threat-control mapping and evidence record. The diagram is explanatory; the linked records remain authoritative.
