---
layout: default
title: "Verifier Decision and Failure Pipeline"
parent: "Diagrams"
grand_parent: "Implementation Guide"
nav_order: 32
has_toc: true
---
# Verifier Decision and Failure Pipeline

```mermaid
flowchart TD
    A[Presentation received] --> B{Request and context valid?}
    B -->|No| X1[Deny: request_context_invalid]
    B -->|Yes| C{Transcript bound and fresh?}
    C -->|No| X2[Deny: transcript_or_replay_failure]
    C -->|Yes| D{Cryptographic verification succeeds?}
    D -->|No| X3[Deny: cryptographic_failure]
    D -->|Yes| E{Requested predicate satisfied?}
    E -->|No| X4[Deny: predicate_unsatisfied]
    E -->|Yes| F{Authority and status evidence usable?}
    F -->|No - known invalid| X5[Deny: authority_or_status_invalid]
    F -->|Unavailable or uncertain| R[Defer or review under approved degraded-mode policy]
    F -->|Yes| G{Delegation required?}
    G -->|No| H{Relying-party policy permits action?}
    G -->|Yes| I{Mandate valid, in scope, current and not revoked?}
    I -->|No| X6[Deny: delegation_invalid]
    I -->|Yes| H
    H -->|No| X7[Deny: policy_denied]
    H -->|Yes| J[Accept action]
    X1 --> EVID[Emit privacy-minimised decision evidence + reason code]
    X2 --> EVID
    X3 --> EVID
    X4 --> EVID
    X5 --> EVID
    X6 --> EVID
    X7 --> EVID
    R --> EVID
    J --> EVID
```

## Interpretation

Cryptographic verification is one gate in a larger relying-party decision. The diagram deliberately prevents a single `verified=true` result from collapsing transcript integrity, predicate semantics, issuer or registry authority, status, delegation and policy into one outcome. Each gate produces a distinct stable reason code and evidence sufficient to explain the decision without retaining unnecessary credential or proof content.

The `Defer or review` branch is governed behaviour, not an implicit fail-open. It is permitted only where an approved degraded-mode policy defines the affected scope, maximum duration, prohibited actions and review obligation.
