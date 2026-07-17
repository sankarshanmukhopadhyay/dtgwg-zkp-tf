---
layout: default
title: Registry resolution flow
nav_order: 5
parent: Diagrams
has_toc: true
---
# Registry resolution flow

```mermaid
flowchart LR
 V[Verifier] --> C{Cache valid?}
 C -- yes --> P[Apply relying-party policy]
 C -- no --> R[Resolve authoritative registry]
 R --> S{State fresh and consistent?}
 S -- yes --> P
 S -- no --> E[Fail closed or explicit degraded path]
 P --> D[Decision receipt]
```

## Interpretation

Registry discovery, state publication, recognition and reliance remain separate decisions. Cached or unavailable state follows an explicit policy and is recorded in the decision receipt.
