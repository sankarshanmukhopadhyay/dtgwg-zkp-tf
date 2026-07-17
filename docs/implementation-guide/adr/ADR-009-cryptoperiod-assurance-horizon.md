---
title: Cryptoperiod and assurance horizon
status: accepted
normative_status: non-normative
owner: DTG ZKP Task Force
last_reviewed: 2026-07-17
---

# Cryptoperiod and assurance horizon

## Context

The implementation guide requires a system-level decision that can be tested across independent deployments. Enrolment-root and epoch treatment follow the bounded-epoch nullifier and cryptoperiod framing discussed against the normative reference — see [`appendices/REFERENCES.md`](../appendices/REFERENCES.md).

## Decision

Model long-lived artefacts and privacy claims with explicit temporal bounds.

## Consequences

Profiles declare enrolment-root cryptoperiods, nullifier epochs, retention and assurance horizons.

## Status

Accepted for the implementation-guide maturity refinement. This ADR does not ratify a cryptographic construction.
