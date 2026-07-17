---
layout: default
title: Presentation and verification flow
nav_order: 3
parent: Diagrams
has_toc: true
---
# Presentation and verification flow

```mermaid
sequenceDiagram
 participant V as Verifier
 participant H as Holder wallet
 participant R as Registry
 V->>H: Canonical request: context, epoch, nonce, predicates, policy
 H->>H: Authorize and generate proof
 H->>V: Presentation bound to transcript
 V->>R: Resolve status and accreditation
 R-->>V: Versioned state
 V->>V: Verify proof and apply policy
 V-->>H: Result and disclosure-safe reason
```

## Interpretation

Verification combines proof validity with policy, status and accreditation. The resulting decision receipt records which versions and evidence supported the outcome.
