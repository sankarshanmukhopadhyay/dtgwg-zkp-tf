---
title: Assurance and disclosure boundaries
status: incubating
normative_status: non-normative
owner: DTG ZKP Task Force
last_reviewed: 2026-07-16
---


# Assurance and disclosure boundaries

A conformant profile analyses every predicate through two linked views.

- The **assurance boundary** records what a verifier may rely on, what remains outside the proof, and who is accountable when the upstream determination is wrong.
- The **disclosure boundary** records what each participant can observe or reconstruct, to whom the information is exposed, how long it persists, and which other artefacts can make it correlatable.

The issuer attestation schema is the shared input to both views. A field that is necessary to establish policy version or assurance class may simultaneously create a correlation surface. Boundary analysis therefore occurs before construction selection and before schema stabilization.

## Required claim form

Every material claim is complete only when it states:

1. **against whom** the claim is asserted, including collusion assumptions;
2. **for how long** the claim is asserted, including epoch, retention and cryptoperiod;
3. **alongside what** credentials, metadata, protocols, logs, registry state and observable events the claim remains valid.

## Artefacts

- [Assurance-boundary template](assurance-boundary-template.md)
- [Disclosure-boundary template](disclosure-boundary-template.md)
- [Context decision record](context-decision-record.md)
- [Predicate boundary register](predicate-boundary-register.md)
