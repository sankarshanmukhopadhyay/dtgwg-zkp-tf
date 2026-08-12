---
layout: default
title: "Wallet and holder implementation guide"
parent: "Implementation"
grand_parent: "Implementation Guide"
nav_order: 2
has_toc: true
---
# Wallet and holder implementation guide

The wallet protects holder-controlled secrets, interprets requests, constructs presentations and enforces the holder's local disclosure and delegation policy. It is the principal control point for preventing a privacy-preserving credential from becoming a background tracking or automation primitive.

## Responsibilities

The wallet should:

- protect credential and proving secrets against extraction and cross-user use;
- authenticate or otherwise bind the relying-party request origin as required by the profile;
- display the requested predicate, context, purpose, verifier and material consequences intelligibly;
- bind the proof to freshness/challenge and the canonical request transcript;
- enforce context, epoch and linkability rules locally where possible;
- minimise disclosure before proving;
- keep holder control distinct from delegated-agent authority;
- support secure backup/recovery without silently duplicating uniqueness or revocation state; and
- provide accessible alternatives, cancellation and redress routes.

## Request processing pipeline

`receive request → validate origin/context → parse predicate → evaluate local policy → obtain holder/agent authority → construct transcript → prove → return presentation → retain minimal evidence`

The wallet should reject or step up a request before proof generation when the request is outside the supported profile, expands context unexpectedly, asks for prohibited disclosure or cannot establish the required authority.

## Consent and intelligibility

Consent is not established by a generic “continue” control. A wallet should present enough information for the holder to distinguish:

- what is being proven;
- who is asking;
- which context or linkability domain applies;
- whether reuse can be detected in the context;
- whether a mediated/remote prover can observe the request; and
- what happens if the holder declines.

For high-frequency or agent-mediated use, implement policy delegation with explicit limits rather than repeated meaningless consent prompts.

## Secret and device protection

Use platform-appropriate protected storage, anti-rollback measures, key-use authorisation and secure recovery. Shared-device deployments must partition secrets and history by user and must not use device identifiers as a hidden substitute for scoped uniqueness.

## Delegated-agent boundary

A wallet may allow an agent to request a proof, but it must not infer authority from agent access to wallet APIs. The agent must present or reference separate [delegation evidence](delegated-agent-implementation-guide.md), and the wallet/verifier must enforce scope, validity and revocation.

## Privacy and observability

Assess local logs, crash reporting, analytics, push infrastructure, cloud backup and remote proving as part of the disclosure boundary. Do not retain complete proof transcripts, credential contents or stable correlation values unless a documented evidence requirement justifies them.

## Recovery and compromise

Define how the system responds to lost devices, cloned backups, suspected secret extraction, account recovery and transfer to a new device. Recovery must preserve status and revocation semantics and must not create two concurrently valid control states where the profile assumes one.

## Failure cases to test

- replayed or stale verifier challenge;
- mismatched context/predicate;
- verifier origin cannot be authenticated;
- unsupported proof profile;
- shared-device user confusion;
- agent request without valid delegation;
- remote prover unavailable;
- device clock skew;
- credential revoked after local caching; and
- recovery after compromise.

## Evidence to produce

- supported profile/predicate manifest;
- key-storage and recovery design;
- request rendering examples;
- transcript-binding tests;
- local policy/delegation tests;
- privacy and retention assessment;
- shared-device tests where applicable;
- recovery/compromise exercise evidence; and
- conformance results.

## Recovery and compromise model

The [wallet compromise and recovery swimlane](../diagrams/D-036-wallet-compromise-recovery.md) shows how holder control, issuer recovery, registry/status state and verifier reliance remain separate during restoration. Recovery must not silently erase revoked keys, delegations or prior credential state.

## Related guidance

Read [privacy engineering](../privacy/README.md), [observable-event analysis](../privacy/observable-event-analysis.md), [delegated agents](delegated-agent-implementation-guide.md), [wallet compromise runbook](../operations/wallet-compromise-and-recovery-runbook.md) and [conformance](../conformance/README.md).

[Back to component implementation guides →](README.md)
