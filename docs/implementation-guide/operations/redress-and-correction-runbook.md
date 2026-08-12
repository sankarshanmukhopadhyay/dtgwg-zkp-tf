---
layout: default
title: "Redress and correction runbook"
parent: "Operations"
grand_parent: "Implementation Guide"
nav_order: 10
has_toc: true
---
# Redress and correction runbook

## Trigger and detection

A holder/principal contest, operator-detected erroneous decision, incorrect credential/status state, delayed revocation, policy defect or governance review requiring correction.

## Decision authority and scope

The receiving service authenticates and triages the request without unnecessary disclosure. The authority that owns the disputed state or decision controls correction; an independent reviewer should be available where the governance model requires appeal.

## Immediate containment

Preserve the disputed decision/state, pause harmful continued reliance where justified, prevent automated propagation of known-bad data, and separate evidence preservation from assumptions about fault.

## Evidence to preserve

Preserve decision ID, reason code, relevant policy/status/schema versions, authority records, correction requests, review decisions and propagation evidence. Avoid requiring the affected person to resubmit unnecessary credential data merely to make the system investigate its own records.

## Recovery procedure

Follow [D-024](../diagrams/D-024-redress-correction-flow.md): identify the authoritative source, correct issuer/registry/policy state, propagate the correction, rerun the affected decision where appropriate and issue a reviewable outcome.

## Recovery test and closure

Verify corrected state at independent consumers, confirm stale erroneous state is no longer relied upon, and test that historical evidence still explains both the original and corrective decisions. Closure requires the correction/review authority to confirm the remedy and any residual obligations.

## Communications and redress

Give the affected party a comprehensible result, scope of correction, remaining consequences and escalation path. Record whether downstream decisions require remediation rather than assuming state correction automatically reverses all consequences.

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
