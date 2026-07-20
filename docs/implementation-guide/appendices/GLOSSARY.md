---
layout: default
title: "Glossary"
parent: "Appendices"
grand_parent: "Implementation Guide"
nav_order: 2
has_toc: true
---
# Glossary

| Term | Definition |
|---|---|
| Accreditation | Governed determination that an actor satisfies a named framework or assurance policy. |
| Agent | Software or service acting under explicitly delegated authority from a principal. |
| Assurance class | Named set of evidence, process and governance expectations accepted by a relying party. |
| Canonical transcript | Deterministic representation of the request and transaction data bound into a proof. |
| Conformance evidence | Reproducible records supporting a claim that an implementation passed named tests. |
| Context | Governed scope within which correlation or reuse detection is permitted. |
| Decision receipt | Evidence of the policy, inputs, governed state, outcome and reason used by a verifier. |
| Delegation | Authority granted by a principal to an agent with scope, duration, constraints and revocation. |
| Epoch | Governed time interval used by a profile for freshness, correlation or reuse semantics. |
| Holder binding | Evidence that the presenter controls the configured credential key or secret. |
| Liveness attestation | Attestation that a named liveness policy was satisfied; not proof that the upstream determination was correct. |
| Nullifier | Derived value used to detect reuse within an authorized scope and epoch. |
| Personhood | Satisfaction of a named personhood policy; not civil identity or global uniqueness. |
| Predicate | Precisely defined statement evaluated or proven by a profile. |
| Principal | Actor whose authority is delegated to an agent. |
| Recognition | Governed acceptance of another authority or framework; distinct from discovery or reliance. |
| Relying-party policy | Versioned rules a verifier applies to proofs, issuers, registries, status and transactions. |
| Scoped uniqueness | Reuse-detection property limited to a declared context and epoch. |
| Status | Governed lifecycle state such as active, suspended, revoked or expired. |
| Verifier | Component or relying party that validates a presentation and applies policy. |
| Zero-knowledge proof | Cryptographic proof that establishes a statement without revealing specified witness information under stated assumptions. |

## Assurance boundary
The exact proposition a verifier may rely on, its exclusions, dependencies, accountable party and evidence.

## Disclosure boundary
The information a participant can observe or reconstruct, the recipients, persistence, collusion assumptions and accompanying artefacts.

## Assurance horizon
The period over which a profile asserts that an assurance or privacy claim remains defensible under its stated assumptions.

## Cryptoperiod
The authorized lifetime of a cryptographic or enrolment artefact before rotation, retirement or reassessment.

## Observable event
The externally visible fact, timing or pattern of a request, proof generation, mediation, retry, rejection or step-up, separate from proof-transcript disclosure.

