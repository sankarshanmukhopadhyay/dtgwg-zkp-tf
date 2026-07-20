---
layout: default
title: "Operational viewpoint"
parent: "Architecture"
grand_parent: "Implementation Guide"
nav_order: 11
has_toc: true
---
# Operational viewpoint

Operations preserve the meaning of a verification decision across policy, registry, issuer, algorithm and infrastructure change.

Monitoring distinguishes cryptographic failure, semantic mismatch, policy rejection, stale or conflicting state, revocation, delegation failure, privacy-control failure and infrastructure fault. Each class maps to a stable error, authority and runbook.

Incident response identifies the affected authority boundary, suspends unsafe behavior, preserves minimized evidence, publishes status where authorized and supports correction or redress. Recovery shall not silently reset scoped uniqueness, delegation restrictions, prior revocations or assurance horizons.

Executable procedures are maintained in the [operational playbooks](../operations/README.md).
