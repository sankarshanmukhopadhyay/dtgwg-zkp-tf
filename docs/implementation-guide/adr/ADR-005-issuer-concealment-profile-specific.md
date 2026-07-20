---
layout: default
title: "ADR-005 — Issuer concealment is profile-specific"
parent: "Architecture Decision Records"
grand_parent: "Implementation Guide"
nav_order: 5
has_toc: true
---
# ADR-005 — Issuer concealment is profile-specific

- **Status:** proposed
- **Date:** 2026-07-14

## Context

A stable architectural interpretation is required before selecting or composing proof constructions.

## Decision

Profiles may conceal the issuer while disclosing a framework or class, or may require issuer visibility for liability, status, or redress.

## Consequences

- verifier outputs must not overclaim;
- profiles must preserve the distinction;
- conformance tests require negative cases;
- governance dependencies remain explicit.

## Validation

Map this ADR to at least one scenario and one negative conformance test.

## Traceability

- **Scenarios (constrains):** UC-008, UC-016 — see `matrices/adr-scenario-map.csv`.
- **Scenario (informs):** UC-020, where whether the issuer of an
  accessibility-alternative attestation must be visible interacts directly
  with non-discrimination requirements.
- **Scenario (validated-by):** UC-024, where issuer concealment is one of
  the properties tested against issuer-verifier collusion.
- **Negative conformance test:** `CT-UC024-POS-02`/`CT-UC024-NEG-02`
  (issuer artefacts must carry no covert tag, and undocumented
  fingerprinting via policy-field combinations is non-conformant even
  when the issuer identity itself is concealed) — see
  `../conformance/test-matrix.csv`. UC-008 and UC-016 are P1 and not yet
  assigned a conformance level; see `../conformance/levels.md`.
