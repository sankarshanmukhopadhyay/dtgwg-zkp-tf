---
layout: default
title: "Delegated-Agent Authority Transaction"
parent: "Diagrams"
grand_parent: "Implementation Guide"
nav_order: 33
has_toc: true
---
# Delegated-Agent Authority Transaction

```mermaid
sequenceDiagram
    participant P as Principal
    participant W as Wallet / Prover
    participant A as Delegated Agent
    participant V as Verifier / Relying Party
    participant R as Authority / Status Source

    P->>R: Establish scoped, time-bounded, revocable mandate
    R-->>P: Mandate evidence + status reference
    P->>W: Configure proving / consent policy
    P->>A: Delegate permitted action + constraints
    V->>A: Action request + proof requirements + context
    A->>R: Resolve mandate status and scope
    R-->>A: Current authority state + effective time
    A->>W: Request bounded proof for transaction context
    alt Holder confirmation or step-up required
        W->>P: Request confirmation / stronger authentication
        P-->>W: Approve or deny
    end
    W-->>A: Proof result bound to request context
    A->>V: Proof + delegation evidence + action request
    V->>R: Resolve authority/status as policy requires
    R-->>V: Current governed state
    V->>V: Verify proof, mandate, scope and relying-party policy separately
    V-->>A: Accept / deny / defer + reason code
    A-->>P: Receipt / evidence according to mandate policy
```

## Interpretation

The principal is the source of delegated intent, but the relying party decides whether the requested action is acceptable under its policy. The wallet controls proof capability, the agent exercises only the delegated scope, and the authority/status source makes mandate state independently verifiable. Possession of proof material, successful proof generation and valid agent identity do not independently establish permission to act.

A step-up returns authority-sensitive control to the principal rather than allowing the agent to expand its mandate. Revocation at the authority/status source must prevent future reliance within the profile's approved propagation horizon and leave evidence of the effective transition.
