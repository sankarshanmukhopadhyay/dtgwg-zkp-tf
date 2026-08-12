---
layout: default
title: "Degraded mode runbook"
parent: "Operations"
grand_parent: "Implementation Guide"
nav_order: 8
has_toc: true
---
# Degraded mode runbook

## Trigger and detection

Loss or uncertainty of a dependency such as registry/status, policy service, time source, proof service or network path where immediate total shutdown may itself cause disproportionate harm.

## Decision authority and scope

Degraded operation must be pre-authorised by profile/risk governance. The incident authority may enter only the already-approved mode and scope; it cannot invent weaker acceptance criteria during an outage. High-impact prohibited actions remain prohibited.

## Immediate containment

Identify the failed dependency, bound the affected profiles/actions, enforce the degraded-policy version, start the maximum-duration timer and increase monitoring. Prefer deny/defer/review when authoritative state cannot be safely reconstructed.

## Evidence to preserve

Record entry trigger, authority, dependency state, degraded-policy version, affected decisions, expiry time, monitoring observations and exit/extension decisions. Tag every degraded decision for later review without retaining unnecessary presentation data.

## Recovery procedure

Restore the authoritative dependency, invalidate emergency caches, reconcile any state accumulated during partition and return through the `Recovering`/`Restored` states in [D-035](../diagrams/D-035-operational-incident-lifecycle.md).

## Recovery test and closure

Re-run normal dependency and negative tests, sample all degraded decisions for policy compliance, and verify that temporary allowances can no longer be invoked. Closure requires review of consequences and explicit acceptance by the authority that approved degraded operation.

## Communications and redress

Communicate scope and expiry to operators and affected relying parties. If degraded decisions caused denial or weaker reliance, provide review/redress where policy requires it. Any extension beyond the pre-authorised duration requires a new attributable risk decision.

## Minimum evidence produced

- incident or change identifier and classification;
- named decision/closure authorities;
- affected scope and effective times;
- relevant signed state, policy/configuration and software/key versions;
- containment and enforcement actions;
- recovery-test results;
- exceptions and residual-risk approvals; and
- closure record plus redress/correction references where applicable.

[Back to Operational playbooks →](README.md)
