---
layout: default
title: "Canonical threat, harm and control model"
parent: "Architecture Decision Records"
grand_parent: "Implementation Guide"
nav_order: 11
has_toc: true
---
# Canonical threat, harm and control model

## Context

The implementation guide requires a system-level decision that can be tested across independent deployments.

## Decision

Adopt a machine-readable canonical threat matrix connected to controls, tests and residual-risk decisions.

## Consequences

The YAML source generates human-readable views and validation detects orphan threats and controls.

## Status

Accepted for the implementation-guide maturity refinement. This ADR does not ratify a cryptographic construction.
