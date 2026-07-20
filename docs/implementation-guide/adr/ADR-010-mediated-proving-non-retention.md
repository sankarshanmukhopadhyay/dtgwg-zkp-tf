---
layout: default
title: "Mediated proving non-retention"
parent: "Architecture Decision Records"
grand_parent: "Implementation Guide"
nav_order: 10
has_toc: true
---
# Mediated proving non-retention

## Context

The implementation guide requires a system-level decision that can be tested across independent deployments.

## Decision

Treat remote proving as a separate profile with isolation, non-retention and accountability controls.

## Consequences

Silent fallback is prohibited and deployments publish the assurance and disclosure difference.

## Status

Accepted for the implementation-guide maturity refinement. This ADR does not ratify a cryptographic construction.
