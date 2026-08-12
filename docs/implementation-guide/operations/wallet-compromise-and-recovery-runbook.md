---
layout: default
title: "Wallet compromise and recovery runbook"
parent: "Operations"
grand_parent: "Implementation Guide"
nav_order: 5
has_toc: true
---
# Wallet compromise and recovery runbook

## Trigger and detection

Loss, theft, malware, suspected key extraction, unauthorised proof generation, compromised recovery factor, or evidence that an agent obtained proof capability beyond its mandate.

## Decision authority and scope

The wallet/recovery service classifies the technical event; issuer and delegation authorities retain control over credential and mandate state. Recovery must not implicitly reinstate credentials, nullifiers, delegations or permissions that another authority has suspended or revoked.

## Immediate containment

Freeze affected proving/signing capability, invalidate active sessions, revoke compromised wallet or delegation keys where applicable, and prevent unattended agent use. Preserve a bounded local evidence record before destructive reset where feasible.

## Evidence to preserve

Preserve device/wallet key IDs, recovery-policy version, security events, delegation references, revocation transactions and recovery approvals. Do not export credential contents or witnesses merely for incident convenience.

## Recovery procedure

Use the governed recovery route to re-establish holder control, rebind or reissue credentials only through issuer-approved processes, restore policy configuration, and register replacement key/mandate relationships where required. See [D-036](../diagrams/D-036-wallet-compromise-recovery.md).

## Recovery test and closure

Prove that compromised keys and delegations are rejected, restored proofs are bound to the new valid state, scoped uniqueness/revocation restrictions remain intact and affected credentials resolve correctly. Closure requires the recovery authority to accept the test evidence and any issuer/delegation dependencies to be reconciled.

## Communications and redress

Provide a holder-visible explanation of what was recovered, what remains revoked or replaced and how to contest an incorrect suspension/revocation. Where an unauthorised agent acted, link resulting action receipts to the redress process.

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
