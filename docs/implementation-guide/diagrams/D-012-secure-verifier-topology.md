---
layout: default
title: "Secure verifier topology"
parent: "Diagrams"
grand_parent: "Implementation Guide"
nav_order: 12
has_toc: true
---
# Secure verifier topology

```mermaid
flowchart LR
 E[Request edge] --> C[Cryptographic verifier]
 C --> P[Policy engine]
 P --> R[Registry resolver]
 R --> D[Decision service]
 D --> A[Minimized evidence store]
 O[Admin control plane] -. authenticated .-> P
```

## Interpretation

Cryptographic, policy, registry and administrative authority are separated into authenticated zones.

## Assurance use

Use this diagram with the applicable deployment profile, scenario, threat-control mapping and evidence record. The diagram is explanatory; the linked records remain authoritative.
