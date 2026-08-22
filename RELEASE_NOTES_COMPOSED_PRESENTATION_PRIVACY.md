# Composed-presentation privacy refinement

This change set carries the composition/privacy boundary identified in DTG Credential Task Force discussions into the fork's v0.4 ZKP requirements and implementation guidance.

## What changes

- defines **evidence closure** as the complete set of artefacts, relationships, external state and protocol observations required to establish a verification predicate;
- strengthens `LIV-PRIV-06` so end-to-end privacy is evaluated across that closure rather than credential-by-credential;
- adds proof-input composability, predicate-oriented modelling, confidential-binder semantics for low-entropy inputs and semantic separation when cryptographic primitives are reused;
- generalises status privacy into an external-resolution privacy requirement without making offline verification universally mandatory;
- clarifies that delegation evidence need not imply disclosure of durable delegation ancestry and preserves governed sub-delegation as a profile choice;
- adds a four-layer responsibility model spanning governance, semantic predicates, evidence interfaces and private proof construction; and
- adds construction-neutral negative conformance cases for composition failures.

## Deliberate non-decisions

The change does not select a ZK system, commitment scheme, accumulator, Merkle construction, selective-disclosure suite, revocation architecture or delegation-chain format. It preserves the v0.4 principle that semantic/privacy requirements are resolved before construction selection.

## Tracking

Addresses the implementation scope tracked in issue #4. The issue body is intentionally left unchanged; commits and the pull request provide implementation traceability.