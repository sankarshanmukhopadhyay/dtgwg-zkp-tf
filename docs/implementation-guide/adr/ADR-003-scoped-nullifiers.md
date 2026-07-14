# ADR-003 — Nullifiers provide scoped reuse detection

- **Status:** proposed
- **Date:** 2026-07-14

## Context

A stable architectural interpretation is required before selecting or composing proof constructions.

## Decision

A nullifier may detect repeated use within a scope and epoch. It does not independently establish one natural person globally.

## Consequences

- verifier outputs must not overclaim;
- profiles must preserve the distinction;
- conformance tests require negative cases;
- governance dependencies remain explicit.

## Validation

Map this ADR to at least one scenario and one negative conformance test.

## Traceability

- **Scenarios (constrains):** UC-001, UC-002, UC-007, UC-008 — see
  `matrices/adr-scenario-map.csv`.
- **Scenarios (validated-by):** UC-023, UC-024, which specifically pressure-test
  whether scoped-nullifier unlinkability survives a malicious or colluding
  verifier.
- **Negative conformance tests:** `CT-UC001-NEG-01` (two legitimate contexts
  must stay unlinkable under issuer-verifier collusion), `CT-UC023-NEG-01`
  (one verifier cannot force context reuse across services), `CT-UC024-NEG-01`
  (an unfalsifiable "collusion resistant" claim with no named adversary or
  horizon fails) — see `../conformance/test-matrix.csv`.
