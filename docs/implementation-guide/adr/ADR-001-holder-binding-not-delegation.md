# ADR-001 — Holder binding is not agent delegation

- **Status:** proposed
- **Date:** 2026-07-14

## Context

A stable architectural interpretation is required before selecting or composing proof constructions.

## Decision

Holder-key control does not establish that an agent is authorised, that an action is in scope, or that delegation remains valid.

## Consequences

- verifier outputs must not overclaim;
- profiles must preserve the distinction;
- conformance tests require negative cases;
- governance dependencies remain explicit.

## Validation

Map this ADR to at least one scenario and one negative conformance test.

## Traceability

- **Scenarios (constrains):** UC-004, UC-006, UC-009, UC-010, UC-011 — see `matrices/adr-scenario-map.csv`.
- **Scenario (validated-by):** UC-021, where key control diverging from human
  continuity is the entire premise of the scenario.
- **Negative conformance tests:** `CT-UC009-NEG-01` (agent key swap does not
  extend delegation), `CT-UC009-NEG-02` (liveness proof alone is not
  authorisation), `CT-UC021-NEG-01` (key-only attacker fails) — see
  `../conformance/test-matrix.csv`.
