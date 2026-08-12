---
layout: default
title: "Key rotation runbook"
parent: "Operations"
grand_parent: "Implementation Guide"
nav_order: 6
has_toc: true
---
# Key rotation runbook

## Trigger and detection

Scheduled cryptoperiod expiry, algorithm/profile change, protection-boundary change, personnel/control change, suspected exposure or emergency compromise.

## Decision authority and scope

The key-management authority approves ordinary rotation under published policy. Emergency rotation is initiated by the incident authority but must still produce attributable approval and retrospective governance evidence. No operator may self-authorise a broader trust scope through rotation.

## Immediate containment

For compromise, stop affected signing or verification trust immediately within the approved assurance horizon. For routine rotation, prepare overlap only where the profile explicitly permits it and prevent ambiguous key selection.

## Evidence to preserve

Preserve old/new key identifiers, generation/activation/retirement times, protection-boundary evidence, approval records, trust-anchor/status publications, propagation observations and destruction/retention evidence.

## Recovery procedure

Generate replacement keys in the approved boundary, publish activation metadata, update dependent trust stores, exercise overlap or cutover, retire old keys and invalidate caches that could extend the old cryptoperiod. Follow [D-014](../diagrams/D-014-key-lifecycle.md).

## Recovery test and closure

Verify success with independent consumers, confirm rejection after retirement, test historical verification where required and validate that rollback cannot reactivate the retired key. Closure requires evidence that all required dependants observe the intended state.

## Communications and redress

Communicate emergency rotations and affected validity windows to relying parties and status/registry operators. Where compromise changes the confidence of past decisions, invoke the issuer/verifier incident and redress processes rather than treating rotation as sufficient remediation.

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
