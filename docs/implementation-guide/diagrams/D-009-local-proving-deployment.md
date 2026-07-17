---
layout: default
title: Local proving deployment
nav_order: 9
parent: Diagrams
has_toc: true
---
# Local proving deployment

```mermaid
flowchart LR
 I[Issuer] -->|credential| W[Holder wallet]
 V[Verifier request] --> W
 W -->|presentation only| V
 R[Registry] --> V
```

## Interpretation

Credentials and witnesses remain in the holder zone. The verifier receives a bounded presentation.

## Assurance use

Use this diagram with the applicable deployment profile, scenario, threat-control mapping and evidence record. The diagram is explanatory; the linked records remain authoritative.
