---
layout: default
title: Conformance evidence flow
nav_order: 7
parent: Diagrams
has_toc: true
---
# Conformance evidence flow

```mermaid
flowchart LR
 I[Implementation statement] --> T[Test manifest]
 F[Canonical fixtures] --> T
 T --> R[Test runner]
 R --> O[Structured results]
 O --> E[Evidence bundle]
 E --> A[Independent review or plugfest]
```

## Interpretation

A conformance claim is supported by a reproducible evidence bundle that identifies the implementation, profile, environment, fixtures, results and exceptions.
