---
layout: default
title: "Conformance and Assurance Evidence Pipeline"
parent: "Diagrams"
grand_parent: "Implementation Guide"
nav_order: 38
has_toc: true
---
# Conformance and Assurance Evidence Pipeline

```mermaid
flowchart LR
    S[Specification + governed decisions] --> I[Internal consistency validation]
    I --> F[Fixtures + schemas + deterministic harness]
    F --> P[Protocol conformance cases CL-1..CL-4]
    S --> G[Security guardrails + threat model]
    G --> A[Security-assurance tests]
    P --> E[Implementation/profile evidence bundle]
    A --> E
    E --> X[Cross-implementation / plugfest execution]
    X --> C{Evidence sufficient for claim?}
    C -->|No| R[Record disposition, blocker or residual-risk decision]
    R --> F
    C -->|Yes| M[Publish bounded conformance / assurance claim]
```

## Interpretation

Repository validation, protocol conformance, security assurance and cross-vendor interoperability are different evidence layers. Passing Markdown/schema validators proves internal consistency, not cryptographic correctness or production interoperability. The deterministic harness supplies executable evidence for the cases it actually implements; security-assurance tests evaluate guardrails and threat controls; plugfest evidence is required for claims that depend on independent implementations.

Any published claim must state its level, profile, source revision, environment, evidence set, exceptions and residual-risk decisions. Missing executable or interoperability evidence is a governed limitation, not a result that can be filled by narrative assertion.
