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
