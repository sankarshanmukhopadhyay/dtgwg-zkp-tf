---
layout: default
title: "ADR-004 — Assurance is governance-backed"
parent: "Architecture Decision Records"
grand_parent: "Implementation Guide"
nav_order: 4
has_toc: true
---
# ADR-004 — Assurance is governance-backed

- **Status:** proposed
- **Date:** 2026-07-14

## Context

A stable architectural interpretation is required before selecting or composing proof constructions.

## Decision

The proof carries privacy and integrity. Accreditation, policy, audit, and accountability support assurance in the underlying claim.

## Consequences

- verifier outputs must not overclaim;
- profiles must preserve the distinction;
- conformance tests require negative cases;
- governance dependencies remain explicit.
- a profile may aggregate confidence across multiple independent issuers rather than treating accreditation as single-issuer pass/fail; see `boundaries/predicate-assurance-boundary-decision.md` §12.5 (non-normative, decision input).

## Validation

Map this ADR to at least one scenario and one negative conformance test.

## Traceability

- **Scenarios (constrains):** UC-012, UC-013, UC-027 — see
  `matrices/adr-scenario-map.csv`.
- **Scenario (validated-by):** UC-022, where a validly signed but
  substantively false liveness attestation is the exact case this ADR is
  written to govern.
- **Negative conformance tests:** `CT-UC022-NEG-01` (any verifier output or
  documentation implying the ZKP proves correctness of the underlying
  determination is non-conformant), `CT-UC013-NEG-01` (a proof omitting
  its policy version is rejected rather than assumed current) — see
  `../conformance/test-matrix.csv`.
