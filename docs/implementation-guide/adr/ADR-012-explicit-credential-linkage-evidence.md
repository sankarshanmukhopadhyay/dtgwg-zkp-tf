---
layout: default
title: "ADR-012 — Explicit Credential Linkage Evidence"
parent: "Architecture Decision Records"
grand_parent: "Implementation Guide"
nav_order: 12
---
# ADR-012 — Explicit credential linkage evidence

## Status

Implemented as a non-normative working baseline for v0.4.0; upstream credential semantics remain unresolved.

## Decision

A ZKP construction must not infer a relationship between identifiers from co-possession or shared wallet control. If the proof statement depends on identifier correspondence, explicit evidence defined by the responsible credential or governance authority is required.

## Consequences

This prevents the ZKP layer from becoming an accidental source of identity semantics and creates a testable fail-closed behaviour while Credential TF issue #9 remains unresolved. The linkage method must also be assessed for correlation impact.
