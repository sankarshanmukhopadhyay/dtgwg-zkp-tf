---
layout: default
title: "Incident evidence guide"
parent: "Operations"
grand_parent: "Implementation Guide"
nav_order: 9
has_toc: true
---
# Incident evidence guide

## Trigger and detection

Use this guide whenever an operational event requires evidence preservation for investigation, restoration, audit, conformance, redress or governance review.

## Decision authority and scope

The incident authority defines the evidence scope; privacy/security governance constrains collection and access; evidence custodians maintain chain of custody. Investigators do not gain open-ended authority to copy holder data merely because an incident exists.

## Immediate containment

Prefer state/version evidence before collecting transaction content. Isolate logs and snapshots from mutation, protect export credentials, document collection purpose and prohibit secondary analytics unless separately authorised.

## Evidence to preserve

Preserve signed state, policy/software/configuration versions, administrative actions, decision IDs/outcome codes, timestamps, integrity digests, key/status events, approvals and recovery-test results. Copy credentials, witnesses or full presentations only when demonstrably necessary, authorised and protected.

## Recovery procedure

Store incident evidence in a controlled case boundary with provenance, integrity checks, access logging, retention/deletion dates and explicit references to the source runbook. Link evidence rather than duplicating high-risk artefacts where possible.

## Recovery test and closure

Validate integrity and provenance, confirm that another authorised reviewer can reconstruct the incident timeline and trust-state transitions, and verify scheduled deletion or archival obligations. The closure authority accepts evidence sufficiency; it does not waive privacy obligations.

## Communications and redress

Evidence packages should support redress without forcing affected parties to disclose more data. Record disclosure to regulators, auditors or counterparties under the applicable authority and retain a disclosure trail.

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
