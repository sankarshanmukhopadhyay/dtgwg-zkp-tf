---
layout: default
title: "Trust Task ZKP Profile"
parent: "DTG Interoperability"
nav_order: 6
---
# Trust Task ZKP profile

This profile describes how a proof request and presentation can be bound to a DTG Trust Task exchange without turning Trust Task participation into proof of delegated authority.

## Binding inputs

Where present and applicable, a ZKP request transcript SHOULD bind the following governed task inputs:

- task or exchange identifier;
- requester/verifier audience;
- challenge or nonce;
- governed context identifier;
- requested predicates and permitted disclosure;
- policy/profile identifier and version;
- status/freshness requirements;
- proof expiry or acceptable verification horizon;
- evidence references needed by the verifier; and
- optional ceremony/enactment reference when the proof is one step in a larger ceremony.

The canonical transcript must define field ordering/normalisation so two conformant implementations derive the same binding digest.

## Requirements

### ZKP-TASK-01 — Exact task binding

A task-bound proof MUST be bound to the exact requester/audience, challenge, requested statement and governed context. A proof created for one task MUST NOT be reusable as success evidence for another task unless the profile explicitly defines equivalent semantics.

### ZKP-TASK-02 — Authority separation

Task participation, task completion, possession of a valid proof, or possession of a ceremony reference MUST NOT be treated as delegated authority. If an agent acts for a principal, authority evidence is verified separately under the applicable delegation mechanism.

### ZKP-TASK-03 — Policy/version binding

Where relying-party policy determines acceptable issuer, status, privacy class, assurance class or proof profile, the relevant policy/profile version MUST be included in or unambiguously referenced by the verification evidence.

### ZKP-TASK-04 — Replay and confused-deputy resistance

The verifier MUST reject a cryptographically valid proof whose task identifier, audience, challenge, context or requested action does not match the current task. Failure handling must not silently reinterpret the proof under a weaker task.

## Evidence produced

A task-bound verification receipt should contain a minimal task reference, proof/profile version, transcript digest, verification time, policy version and result. It should not duplicate private task content merely to make the receipt self-contained.
