---
layout: default
title: "Verifier compromise runbook"
parent: "Operations"
grand_parent: "Implementation Guide"
nav_order: 4
has_toc: true
---
# Verifier compromise runbook

## Trigger and detection

A suspected compromise of verifier service credentials, decision-policy configuration, administrative control, request-generation logic, logs/telemetry or deployment pipeline.

## Decision authority and scope

The verifier security authority classifies and contains the component incident. The relying-party decision authority determines whether prior or ongoing decisions remain usable and whether the verifier profile must be suspended.

## Immediate containment

Isolate the affected verifier and administrative identities, stop new high-impact reliance, disable compromised credentials, preserve policy/configuration state, and route traffic only to an independently validated deployment if policy explicitly permits it.

## Evidence to preserve

Preserve decision IDs, reason codes, policy and software digests, request/profile versions, administrative actions, service credential events and relevant telemetry. Minimise or redact proof/presentation content and holder-linked identifiers.

## Recovery procedure

Rotate service/admin credentials, rebuild from trusted source, restore approved policy and registry dependencies, validate request entropy/context binding, and reassess exposure of stored presentations or logs.

## Recovery test and closure

Run positive and negative verifier tests including replay, stale status, revoked credential, invalid delegation and policy-denial cases. Compare decision receipts against the pre-incident baseline. Closure requires approval from the relying-party authority that suspended decision reliance.

## Communications and redress

Identify potentially incorrect accepts/denials and invoke the redress/correction process where consequences may have flowed from compromised decisions. Preserve evidence linking corrective action to affected decision IDs.

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
