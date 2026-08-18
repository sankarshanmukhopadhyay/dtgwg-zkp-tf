---
layout: default
title: "D-030 — DTG ZKP Dependency Map"
parent: "Diagrams"
nav_order: 30
---
# D-030 — DTG ZKP dependency map

```mermaid
flowchart LR
  C[Credential Spec] -->|claims, status, edge evidence| Z[ZKP profile]
  T[Trust Tasks] -->|task content, challenge, audience, control state| Z
  TC[Trust Ceremonies] -->|conditional enactment context| Z
  VDS[VDS] -. conditional evidence .-> Z
  AN[Agent Names] -. conditional resolution evidence .-> Z
  HTX[HTX] -. conditional human-experience evidence .-> Z

  RH[DTG RAHP provenance] --> RM[RAHP Toolkit v1.1 method]
  RM --> A[ZKP assurance]

  Z -->|bounded proof result| RP[Relying-party policy]
  TS[Task effect-time state] --> RP
  RG[Registry / credential status] --> RP
  D[Delegation / mandate evidence] --> RP
  A --> RP

  O[OpenVTC implementations] -. conformance evidence .-> A

  PM[DTG Portfolio Monitor] -. review trigger .-> A

  Z -. cannot create .-> C
  Z -. cannot create .-> D
  Z -. cannot create .-> RG
  Z -. cannot override .-> TS
```

The diagram is intentionally directional. Adjacent DTG work supplies governed semantics, runtime state, optional composition inputs or assurance evidence. ZKP returns only a bounded cryptographic result.

## Dependency classes

- **Solid semantic/runtime edges** are load-bearing when the relevant profile is used.
- **Dotted conditional edges** are examined but do not become dependencies until a ZKP profile selects the composition.
- **Implementation evidence** can demonstrate conformance or expose defects but cannot redefine normative semantics.
- **The Portfolio Monitor** can trigger review but has no authority to change ZKP assumptions.
- **RAHP Toolkit v1.1** is the fork's operational pressure-test method; DTG RAHP remains upstream/historical method provenance and neither becomes ZKP normative authority.

## Interpretation

The consuming decision remains a composition of bounded proof validity, current external authority/state and relying-party policy:

```text
proof result
  + current task/control state
  + credential/registry status
  + delegation/mandate evidence
  + applicable policy
  -> relying-party decision
```

A change in any load-bearing external state can require re-evaluation even when the cryptographic proof itself remains mathematically valid.
