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
