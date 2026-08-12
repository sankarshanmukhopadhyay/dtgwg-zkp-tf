---
layout: default
title: "Registry and status runbook"
parent: "Operations"
grand_parent: "Implementation Guide"
nav_order: 2
has_toc: true
---
# Registry and status runbook

## Trigger and detection

Signature failure, stale response, rollback, conflicting federation sources, delayed status propagation, missing/unknown record, resolver error or total authority-source unavailability.

## Decision authority and scope

The registry/status operator classifies publication and infrastructure faults. The governance authority for the affected record class determines authoritative state and conflict precedence. The relying party decides operational consequences under its approved policy.

## Immediate containment

Do not infer good status from absence. Quarantine invalid signatures/rollback, narrow accepted sources during federation conflict, invalidate unsafe caches and move high-impact decisions to deny/defer/review when current authority cannot be established.

## Evidence to preserve

Preserve signed snapshots/responses, source identifiers, effective/publication times, resolver versions, cache age, conflict observations and administrative changes. Evidence should permit reconstruction of what each verifier could have observed.

## Recovery procedure

Restore authoritative publication, reconcile federation conflicts under the documented precedence rule, republish corrected state, invalidate stale caches and measure propagation. Use [D-031](../diagrams/D-031-registry-authority-status-state-model.md) to distinguish recognised, authorised, active, suspended and terminal states.

## Recovery test and closure

Verify signature, freshness, effective-time semantics, conflict resolution, cache invalidation and historical/as-of reconstruction from an independent resolver. Closure requires the record authority to confirm state correctness and operations to confirm propagation within the assurance horizon.

## Communications and redress

Notify relying parties when stale or conflicting state could have changed decisions. Identify affected decision windows and route erroneous reliance or denial through the redress/correction process.

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
