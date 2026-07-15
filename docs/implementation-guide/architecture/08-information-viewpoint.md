# Information viewpoint

The architecture distinguishes evidence, policy and transaction objects so that proof verification cannot silently stand in for governance authorization.

| Object | Required properties |
|---|---|
| Credential or attestation | issuer, subject-binding method, policy, assurance class, status and validity |
| Predicate | stable identifier, inputs, positive and negative meaning, disclosure and dependencies |
| Proof request | requester, context, epoch, nonce, predicates, policy and acceptable profiles |
| Presentation | proof, transcript binding, disclosed claims, profile and status references |
| Delegation evidence | principal, agent, scope, constraints, validity and revocation reference |
| Registry record | object identifier, authority, version, effective time, status and signature |
| Relying-party policy | authority, version, accepted assurance and failure behavior |
| Decision receipt | request digest, policy version, evidence references, outcome and reason code |
| Conformance evidence | implementation, environment, fixture digests, results and exceptions |

Data minimization applies to the full observable transaction, not only the cryptographic statement. Implementers should account for network metadata, lookup patterns, retries, timing and error differences.
