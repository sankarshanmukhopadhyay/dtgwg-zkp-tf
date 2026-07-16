---
title: Dual assurance and disclosure boundaries
status: accepted
normative_status: non-normative
owner: DTG ZKP Task Force
last_reviewed: 2026-07-16
---

# Dual assurance and disclosure boundaries

## Context

The implementation guide requires a system-level decision that can be tested across independent deployments.

## Decision

Adopt paired boundary records for every material predicate and profile.

## Consequences

A proof profile must state both what a verifier may rely on and what participants can learn or reconstruct. The two records share the attestation schema and threat references.

## Status

Accepted for the implementation-guide maturity refinement. This ADR does not ratify a cryptographic construction.
