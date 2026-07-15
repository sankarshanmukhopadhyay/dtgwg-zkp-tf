# Agent delegation and step-up flow

```mermaid
sequenceDiagram
 participant P as Principal
 participant A as Agent
 participant V as Verifier
 P->>A: Delegation: scope, duration, constraints
 A->>V: Request action with delegation evidence
 V->>V: Check action against scope and policy
 alt material change or high-risk action
 V->>P: Require fresh step-up
 P-->>V: Fresh authorization proof
 end
 V-->>A: Decision receipt
```

## Interpretation

Agent key control is insufficient. The verifier evaluates delegation scope and can require the principal to provide fresh authorization when risk, environment or requested permissions change.
