# ADR-002 — Personhood is distinct from civil identity

- **Status:** proposed
- **Date:** 2026-07-14

## Context

A stable architectural interpretation is required before selecting or composing proof constructions.

## Decision

Personhood predicates must not imply civil identity unless a separate identity predicate is explicitly requested.

## Consequences

- verifier outputs must not overclaim;
- profiles must preserve the distinction;
- conformance tests require negative cases;
- governance dependencies remain explicit.

## Validation

Map this ADR to at least one scenario and one negative conformance test.
