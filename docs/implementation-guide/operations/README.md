---
layout: default
title: "Operations"
parent: "Implementation Guide"
nav_order: 11
has_children: true
has_toc: true
---
# Operational playbooks

Operational governance preserves the meaning of accepted and rejected presentations when dependencies fail, keys rotate, policies change, components are compromised or affected people seek correction. A runbook is therefore not merely an engineering checklist: it is an executable statement of **who may change trust state, under what trigger, with what evidence, and how that authority ends**.

## Common incident lifecycle

Use [D-035 — Operational Incident Lifecycle](../diagrams/D-035-operational-incident-lifecycle.md) as the shared state model across these runbooks. The [incident authority escalation diagram](../diagrams/D-015-incident-authority-escalation.md) complements it by showing escalation boundaries.

Every runbook should identify:

1. trigger and detecting actor;
2. classification criteria and affected scope;
3. decision authority;
4. immediate containment;
5. enforcement, suspension or revocation action;
6. evidence to preserve and privacy limits;
7. communications and affected-party obligations;
8. recovery procedure;
9. recovery test and independent verification where required;
10. redress/correction route; and
11. closure authority and post-incident review.

## Runbook index

| Runbook | Primary governance question | Related visual model |
|---|---|---|
| [Policy update](policy-update-runbook.md) | Who may change decision semantics and roll them back? | [D-016](../diagrams/D-016-policy-update-rollback.md) |
| [Registry and status](registry-status-runbook.md) | What happens when authority state is stale, conflicting or unavailable? | [D-031](../diagrams/D-031-registry-authority-status-state-model.md) |
| [Revocation propagation](revocation-propagation-runbook.md) | How quickly must withdrawal of trust become effective everywhere? | [D-017](../diagrams/D-017-revocation-propagation.md) |
| [Issuer compromise](issuer-compromise-runbook.md) | How is affected issuing authority bounded and restored? | [D-034](../diagrams/D-034-credential-issuer-lifecycle-states.md) |
| [Verifier compromise](verifier-compromise-runbook.md) | How is decision reliance suspended and safely restored? | [D-032](../diagrams/D-032-verifier-decision-failure-pipeline.md) |
| [Wallet compromise and recovery](wallet-compromise-and-recovery-runbook.md) | How is holder control restored without erasing prior restrictions? | [D-036](../diagrams/D-036-wallet-compromise-recovery.md) |
| [Key rotation](key-rotation-runbook.md) | How are key changes authorised, propagated and evidenced? | [D-014](../diagrams/D-014-key-lifecycle.md) |
| [Proof-system migration](proof-system-migration-runbook.md) | How are version changes made without downgrade or historical ambiguity? | [D-020](../diagrams/D-020-proof-system-migration.md) |
| [Degraded mode](degraded-mode-runbook.md) | What bounded decisions remain permissible during dependency failure? | [D-035](../diagrams/D-035-operational-incident-lifecycle.md) |
| [Redress and correction](redress-and-correction-runbook.md) | Who can correct an erroneous decision/state and prove propagation? | [D-024](../diagrams/D-024-redress-correction-flow.md) |
| [Incident evidence](incident-evidence-guide.md) | What evidence supports investigation without creating unnecessary privacy risk? | [D-027](../diagrams/D-027-control-assurance-evidence-chain.md) |

Use the [operational readiness checklist](operational-readiness-checklist.md) before production entry.

## Evidence principle

Operational evidence should prove the state transition without indiscriminately retaining the subject data that caused the transaction. Prefer signed state, version identifiers, reason codes, policy/configuration digests, administrative approvals, timestamps and recovery-test results over copied credentials, witnesses or complete presentations.

## Closure principle

Restoration is not the same as closure. A service may technically recover while residual risk, propagation, redress or evidence obligations remain open. Every incident therefore ends only when the named closure authority accepts the recovery evidence and confirms any remaining obligations.
