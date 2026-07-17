---
layout: default
title: Multi-implementation plugfest
nav_order: 18
parent: Diagrams
has_toc: true
---
# Multi-implementation plugfest

```mermaid
flowchart LR
 F[Shared fixtures] --> I1[Issuer A]
 F --> I2[Issuer B]
 I1 --> W1[Wallet A]
 I2 --> W2[Wallet B]
 W1 --> V1[Verifier A]
 W2 --> V2[Verifier B]
 V1 --> E[Evidence collector]
 V2 --> E
```

## Interpretation

Independent control and shared fixtures distinguish interoperability from single-stack integration.

## Assurance use

Use this diagram with the applicable deployment profile, scenario, threat-control mapping and evidence record. The diagram is explanatory; the linked records remain authoritative.
