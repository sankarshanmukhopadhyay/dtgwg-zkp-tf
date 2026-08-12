---
layout: default
title: "Revocation propagation runbook"
parent: "Operations"
grand_parent: "Implementation Guide"
nav_order: 3
has_toc: true
---
# Revocation propagation runbook

## Trigger and detection

An authorised credential, issuer, registry, key or delegation revocation/withdrawal event that dependent verifiers must observe within a bounded assurance horizon.

## Decision authority and scope

Only the authority defined for the revoked object may originate the semantic revocation. Operators publish and propagate it; they do not independently create the revocation meaning. Escalation authority is invoked when propagation exceeds the approved bound.

## Immediate containment

Publish the event with effective time, invalidate relevant caches, disable fallback sources that would return pre-revocation state, and identify verifiers or offline zones that may not have observed the transition.

## Evidence to preserve

Record revocation authority, source event, effective/publication times, cache invalidations, resolver/verifier observations, exceptions and escalation decisions. Preserve the pre/post signed state needed for audit.

## Recovery procedure

Follow [D-017](../diagrams/D-017-revocation-propagation.md) until all required dependants observe the event or are explicitly quarantined. Correct publication defects without changing the original effective-time semantics.

## Recovery test and closure

Measure propagation latency against the approved horizon, test that revoked objects are rejected, verify historical decisions still resolve against historical state, and obtain closure from the propagation/incident authority.

## Communications and redress

Where late propagation permitted an action that should have been blocked, identify affected decision IDs and invoke correction/redress. Communicate unresolved offline or federated exceptions rather than declaring complete propagation prematurely.

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
