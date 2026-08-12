---
layout: default
title: "Policy update runbook"
parent: "Operations"
grand_parent: "Implementation Guide"
nav_order: 1
has_toc: true
---
# Policy update runbook

## Trigger and detection

An approved semantic, assurance, privacy, eligibility or relying-party policy change; an upstream decision ratification; or an emergency control change that modifies decision behaviour.

## Decision authority and scope

The named policy authority approves meaning. Deployment operators may stage and activate an approved version but cannot alter the policy semantics. Emergency controls require incident authority plus the governance path defined for retrospective ratification.

## Immediate containment

Version the policy immutably, prevent mixed or unknown versions, stage against representative fixtures, and ensure rollback remains available. If a change unexpectedly broadens acceptance, halt rollout before expanding scope.

## Evidence to preserve

Preserve the approval/ratification reference, old/new policy digests, affected requirements, regression results, rollout state, decision-receipt samples and rollback events.

## Recovery procedure

Use [D-016](../diagrams/D-016-policy-update-rollback.md). Deploy progressively, monitor outcome/rejection changes, and roll back to the last governed version if acceptance semantics diverge from the approved intent.

## Recovery test and closure

Run positive, negative, privacy and delegation regression cases; confirm active verifiers report the intended version; and verify rollback with deterministic evidence. Closure requires policy-authority acceptance of the deployed semantics.

## Communications and redress

Communicate changes that affect holder obligations, relying-party decisions or redress rights. If an erroneous policy produced consequential decisions, preserve affected decision IDs and apply the correction/redress runbook.

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
