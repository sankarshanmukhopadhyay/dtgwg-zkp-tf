---
layout: default
title: "ADR-013 — Task Context Is Not Authority"
parent: "Architecture Decision Records"
grand_parent: "Implementation Guide"
nav_order: 13
---
# ADR-013 — Task context is not authority

## Status

Implemented as a non-normative working baseline for v0.4.0.

## Decision

Trust Task and Trust Ceremony context may be used to bind a proof to the exact exchange, audience, challenge, policy and action. Task participation, ceremony membership and ceremony completion are not authority evidence. Agent delegation remains separate structured evidence.

## Consequences

Task-bound proofs gain replay and confused-deputy resistance without collapsing protocol orchestration into the delegation or governance control plane.
