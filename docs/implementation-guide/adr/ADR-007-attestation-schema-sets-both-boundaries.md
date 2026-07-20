---
layout: default
title: "Attestation schema sets both boundaries"
parent: "Architecture Decision Records"
grand_parent: "Implementation Guide"
nav_order: 7
has_toc: true
---
# Attestation schema sets both boundaries

## Context

The implementation guide requires a system-level decision that can be tested across independent deployments. The attestation fields modelled here correspond to the revealed-attribute mechanism of verifiable relationship credentials (VRCs) in the normative reference — see [`appendices/REFERENCES.md`](../appendices/REFERENCES.md).

## Decision

Treat the issuer attestation schema as a controlled interoperability and privacy artefact.

## Consequences

Every field has an assurance purpose, disclosure mode, correlation analysis, lifecycle and migration rule.

## Status

Accepted for the implementation-guide maturity refinement. This ADR does not ratify a cryptographic construction.
