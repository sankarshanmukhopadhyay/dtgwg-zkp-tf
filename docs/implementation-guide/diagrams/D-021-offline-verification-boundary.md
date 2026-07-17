---
layout: default
title: Offline verification boundary
nav_order: 21
parent: Diagrams
has_toc: true
---
# Offline verification boundary

```mermaid
flowchart LR
 R[Registry snapshot] --> O[Offline verifier]
 P[Presentation] --> O
 F[Freshness policy] --> O
 O --> D[Bounded decision]
 O --> S[Resynchronization evidence]
```

## Interpretation

Offline acceptance is bounded by snapshot provenance, expiry and the approved assurance horizon.

## Assurance use

Use this diagram with the applicable deployment profile, scenario, threat-control mapping and evidence record. The diagram is explanatory; the linked records remain authoritative.
