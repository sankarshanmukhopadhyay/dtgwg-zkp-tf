---
layout: default
title: Revocation propagation
nav_order: 17
parent: Diagrams
has_toc: true
---
# Revocation propagation

```mermaid
sequenceDiagram
 participant I as Issuer authority
 participant R as Registry
 participant C as Cache
 participant V as Verifier
 I->>R: Publish signed revocation
 R->>C: Distribute state
 C->>V: Refresh or invalidate
 V-->>I: Propagation evidence
```

## Interpretation

Propagation is measured from authoritative effective time to verifier observation.

## Assurance use

Use this diagram with the applicable deployment profile, scenario, threat-control mapping and evidence record. The diagram is explanatory; the linked records remain authoritative.
