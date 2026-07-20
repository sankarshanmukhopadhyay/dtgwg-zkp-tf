---
layout: default
title: "Three-part claim parameterization"
parent: "Architecture Decision Records"
grand_parent: "Implementation Guide"
nav_order: 8
has_toc: true
---
# Three-part claim parameterization

## Context

The implementation guide requires a system-level decision that can be tested across independent deployments. The three-part form mirrors the adversary, oracle-error and issuer-composition parameters made explicit in the normative reference's security model — see [`appendices/REFERENCES.md`](../appendices/REFERENCES.md).

## Decision

Require every material claim to state against whom, for how long and alongside what it applies.

## Consequences

The rule applies to assurance, privacy, security and interoperability claims and is validated in profile evidence.

## Status

Accepted for the implementation-guide maturity refinement. This ADR does not ratify a cryptographic construction.
