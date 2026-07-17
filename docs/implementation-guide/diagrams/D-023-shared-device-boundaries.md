---
layout: default
title: Shared-device threat boundaries
nav_order: 23
parent: Diagrams
has_toc: true
---
# Shared-device threat boundaries

```mermaid
flowchart LR
 U1[User A] --> S[Shared device]
 U2[User B] --> S
 S --> K1[Isolated key profile A]
 S --> K2[Isolated key profile B]
 R[Recovery authority] --> S
 S --> V[Verifier]
```

## Interpretation

User, key, consent, history and recovery state require separation on a shared device.

## Assurance use

Use this diagram with the applicable deployment profile, scenario, threat-control mapping and evidence record. The diagram is explanatory; the linked records remain authoritative.
