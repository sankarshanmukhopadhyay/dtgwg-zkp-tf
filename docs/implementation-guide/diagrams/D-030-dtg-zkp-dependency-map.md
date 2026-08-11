---
layout: default
title: "D-030 — DTG ZKP Dependency Map"
parent: "Diagrams"
nav_order: 30
---
# D-030 — DTG ZKP dependency map

```mermaid
flowchart LR
  C[Credential Spec] -->|claims, status, relationships| Z[ZKP profile]
  T[Trust Tasks] -->|request, challenge, audience, constraints| Z
  TC[Trust Ceremonies] -->|optional enactment context| Z
  R[RAHP] -->|pressure-test method| A[ZKP assurance]
  Z -->|bounded proof result| V[Verifier policy]
  RG[Registry / governance state] --> V
  D[Delegation / mandate evidence] --> V
  A --> V
  Z -. cannot create .-> C
  Z -. cannot create .-> D
  Z -. cannot create .-> RG
```

The diagram is intentionally directional: adjacent DTG specifications provide governed semantics or evidence to the ZKP profile, while ZKP returns only a bounded proof result. It does not acquire authority over the source specification.

## Interpretation

Credential, Trust Task, ceremony, registry and governance work feed bounded semantics or evidence into the ZKP profile. The ZKP profile can return a proof result to verifier policy, but it cannot create or supersede the source authority. RAHP contributes an assurance method rather than runtime authority.
