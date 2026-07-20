---
layout: default
title: "Hybrid proving deployment"
parent: "Diagrams"
grand_parent: "Implementation Guide"
nav_order: 11
has_toc: true
---
# Hybrid proving deployment

```mermaid
flowchart TD
 Q[Request] --> S{Policy and capability selection}
 S --> L[Local proving]
 S --> R[Remote proving]
 L --> V[Verifier]
 R --> V
 S --> E[Mode evidence]
```

## Interpretation

Selection and fallback are policy decisions. Silent downgrade to a more observable mode is prohibited.

## Assurance use

Use this diagram with the applicable deployment profile, scenario, threat-control mapping and evidence record. The diagram is explanatory; the linked records remain authoritative.
