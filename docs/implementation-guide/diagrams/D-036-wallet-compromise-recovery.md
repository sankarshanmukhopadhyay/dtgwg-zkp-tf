---
layout: default
title: "Wallet Compromise and Recovery"
parent: "Diagrams"
grand_parent: "Implementation Guide"
nav_order: 36
has_toc: true
---
# Wallet Compromise and Recovery

```mermaid
sequenceDiagram
    participant H as Holder / Principal
    participant W as Wallet
    participant I as Issuer
    participant R as Registry / Status / Delegation Authority
    participant V as Verifier

    H->>W: Report suspected loss or compromise
    W->>W: Freeze proving/signing capability and preserve local evidence
    W->>R: Revoke compromised wallet/delegation keys where applicable
    R-->>W: Effective revocation state + evidence
    W->>I: Request governed recovery / re-binding
    I->>I: Re-establish entitlement under recovery policy
    I-->>W: Reissued or rebound credential evidence
    W->>R: Register replacement authority/status relationships if required
    R-->>W: Replacement state + effective time
    W->>W: Validate restored policy, keys and credential state
    W-->>H: Recovery result + redress/exception information
    V->>R: Resolve current state on subsequent presentation
    R-->>V: Compromised state no longer accepted; replacement state visible
```

## Interpretation

Recovery restores holder control; it does not erase the security history of the compromised wallet. Revoked keys, scoped uniqueness state, credential revocation and agent-delegation restrictions remain governed independently. The issuer re-establishes entitlement according to its recovery policy, while registry/status/delegation authorities publish the transitions needed by relying parties.

Evidence should show when compromise was reported, what was frozen or revoked, which authority approved recovery, which previous bindings remain invalid and which recovery tests established that the replacement state is safe to use.
