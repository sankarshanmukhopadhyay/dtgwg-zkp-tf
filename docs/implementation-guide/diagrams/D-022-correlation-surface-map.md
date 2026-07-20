---
layout: default
title: "Correlation surface map"
parent: "Diagrams"
grand_parent: "Implementation Guide"
nav_order: 22
has_toc: true
---
# Correlation surface map

```mermaid
flowchart TD
 H[Holder] -->|network and timing| P[Prover]
 H -->|presentation metadata| V[Verifier]
 V -->|status lookup| R[Registry]
 P -->|service telemetry| A[Operator]
 V -->|decision logs| E[Evidence store]
```

## Interpretation

The map identifies observable events so minimization and retention controls can be tested.

## Assurance use

Use this diagram with the applicable deployment profile, scenario, threat-control mapping and evidence record. The diagram is explanatory; the linked records remain authoritative.
