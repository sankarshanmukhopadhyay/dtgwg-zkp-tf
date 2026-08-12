---
layout: default
title: "Decision Ratification and Impact Propagation"
parent: "Diagrams"
grand_parent: "Implementation Guide"
nav_order: 37
has_toc: true
---
# Decision Ratification and Impact Propagation

```mermaid
flowchart TD
    U[Attributable upstream decision] --> R[Create ratification record
Authority + date + exact outcome]
    R --> D[Update governed decision register]
    D --> V[Run decision-impact validation]
    V --> Q{Contradictions or affected artefacts?}
    Q -->|Yes| A[Amend / supersede / block ADRs, requirements, schemas, fixtures, tests and guidance]
    A --> T[Run full validation and conformance suite]
    Q -->|No| T
    T --> P{All checks pass and authority boundary preserved?}
    P -->|No| B[Block publication and record unresolved impact]
    B --> A
    P -->|Yes| E[Regenerate readiness / release evidence]
    E --> C[Publish governed state]
```

## Interpretation

Upstream authority changes become repository state only through an attributable ratification record and deterministic impact review. Editorial consensus or implementation progress cannot substitute for the upstream decision authority. Publication is blocked while contradictions remain or affected machine-verifiable artefacts have not been regenerated and tested.

The output of the flow is evidence: the ratification record, updated decision register, impact results, amended artefacts, validation results and publication/release evidence form an auditable chain from authority source to implemented repository state.
