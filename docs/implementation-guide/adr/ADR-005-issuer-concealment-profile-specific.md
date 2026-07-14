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
