# ADR-002 — Personhood is distinct from civil identity

- **Status:** proposed
- **Date:** 2026-07-14

## Context

A stable architectural interpretation is required before selecting or composing proof constructions. This distinction follows the personhood credential (PHC) model in the normative reference — see [`appendices/REFERENCES.md`](../appendices/REFERENCES.md).

## Decision

Personhood predicates must not imply civil identity unless a separate identity predicate is explicitly requested.

## Consequences

- verifier outputs must not overclaim;
- profiles must preserve the distinction;
- conformance tests require negative cases;
- governance dependencies remain explicit.

## Validation

Map this ADR to at least one scenario and one negative conformance test.

## Traceability

- **Scenarios (constrains):** UC-001, UC-002, UC-003, UC-007, UC-008 — see
  `matrices/adr-scenario-map.csv`.
- **Negative conformance tests:** `CT-UC001-NEG-02` (verifier cannot
  substitute an audience to infer identity from a personhood proof),
  `CT-UC002-NEG-02` (issuer cannot embed a covert per-holder tag) — see
  `../conformance/test-matrix.csv`. UC-003 and UC-007/UC-008 are P1 and
  not yet assigned a conformance level (see `../conformance/levels.md`);
  their corpus-native "Minimum conformance tests" fields remain the
  interim validation until they are.
