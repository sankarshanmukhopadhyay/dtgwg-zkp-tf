---
layout: default
title: "Decision: Composed-Presentation Privacy"
parent: "Decisions"
nav_order: 4
---
# Decision: composed-presentation privacy

**Status:** Adopted in fork working draft

**Issue:** #4

## Decision

Privacy and unlinkability claims are evaluated across the complete evidence closure required to establish a verification predicate, not credential-by-credential.

The requirements remain construction-neutral. Credential and domain specifications define the semantic predicate and authenticated inputs; evidence-producing interfaces expose proof-capable relationship material; the proof layer selects constructions; governance selects acceptable profiles and intentional disclosure.

## Consequences

- A selectively disclosed or ZK credential does not by itself establish end-to-end unlinkability.
- Delegation, Trust Task, status, registry/accreditation and external-resolution evidence are part of the disclosure boundary when required by the relying decision.
- Interfaces must not make a durable cross-context correlator the only way to establish a relationship where a stronger privacy profile requires otherwise.
- Deterministic digests over feasibly enumerable inputs are not treated as confidential commitments.
- Live verifier-originated resolution is not universally prohibited, but its observation and correlation effects must be explicit in the privacy profile.
- Common proof primitives may be reused without collapsing distinct governance, freshness, lifecycle or failure semantics.

## Non-decisions

This decision does not select a proof system, commitment scheme, accumulator, Merkle structure, selective-disclosure signature, status mechanism or delegation-chain representation. It does not make offline verification mandatory and does not prohibit governed sub-delegation.

## Evidence

- `proof-of-liveness-requirements.md`: `LIV-STAT-06`, `LIV-PRIV-06`, `LIV-PRIV-08..11`
- `docs/implementation-guide/boundaries/composed-presentation-privacy.md`
- `docs/implementation-guide/architecture/12-composed-proof-responsibility-model.md`
- `docs/implementation-guide/conformance/composed-presentation-privacy-tests.md`
