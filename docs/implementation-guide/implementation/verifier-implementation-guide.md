---
layout: default
title: "Verifier implementation guide"
parent: "Implementation"
grand_parent: "Implementation Guide"
nav_order: 3
has_toc: true
---
# Verifier implementation guide

The verifier converts a proof presentation into a relying-party decision. Its most important design obligation is to keep cryptographic validity, credential semantics, registry/status state, delegated authority and business/policy authorisation **separate and auditable**.

## Decision pipeline

Use [D-032 — Verifier Decision and Failure Pipeline](../diagrams/D-032-verifier-decision-failure-pipeline.md) as the reference separation of cryptographic, semantic, authority/status, delegation and relying-party policy gates.


Use an explicit staged pipeline:

`parse → request validation → transcript binding → cryptographic verification → predicate evaluation → registry/status resolution → delegation validation → relying-party policy → outcome → evidence`

Do not expose only a single `verified` boolean to application code. A relying party must be able to distinguish why a transaction was accepted, denied, deferred or sent for review.

## Decision record

For each material decision retain a privacy-minimised record containing, as applicable:

- decision identifier and time;
- request/purpose/context identifier;
- proof profile and algorithm version;
- predicate result;
- issuer/registry/status evidence references and effective times;
- delegation result and authority reference;
- relying-party policy version;
- final outcome and stable reason code; and
- evidence integrity reference.

Avoid retaining raw credentials, witnesses, complete proof transcripts or linkable identifiers unless justified by the disclosure boundary.

## Registry and status resolution

Treat registry discovery, issuer recognition and credential status as different questions. Define cache lifetimes, stale-state policy and effective-time semantics. `unavailable`, `unknown`, `not recognised`, `suspended`, `revoked` and `expired` should not collapse into the same error.

When historical/as-of decisions matter, retain enough versioned state or evidence references to reconstruct which authoritative state was consulted at the decision time.

## Delegated actions

Validate delegation after establishing the proof/predicate inputs but before authorising the requested action. Check principal, agent, action, resource/context, limits, validity period, revocation source and any required step-up. A proof made by or through an agent does not itself establish permission to act.

## Policy and non-claims

Relying-party policy should declare both positive requirements and prohibited inferences. For example, a liveness predicate must not be converted into a civil-identity or global-uniqueness claim unless separately supported.

## Availability and degraded modes

Define fail-open/fail-closed/review behaviour for registry outage, status outage, policy service failure, proof service degradation and time-source uncertainty. High-impact actions should not silently downgrade to weaker assurance.

## Privacy controls

Minimise request uniqueness, avoid unnecessary verifier identifiers, constrain telemetry, and assess whether error messages or timing create correlation channels. Where issuer concealment is a profile goal, verifier implementation must not reintroduce issuer discovery through auxiliary APIs or logs.

## Failure cases to test

Test malformed proof, transcript mismatch, replay, unsupported profile, invalid predicate, stale registry data, status unavailability, revoked credential, expired policy, invalid delegation, scope overreach, step-up failure and redress after an incorrect denial.

## Evidence to produce

- verifier policy and reason-code catalogue;
- dependency/cache configuration;
- positive/negative decision traces;
- degraded-mode tests;
- delegation tests;
- privacy/retention statement;
- compromise response evidence; and
- conformance statement.

## Related guidance

Read [registry implementation](registry-implementation-guide.md), [delegated agents](delegated-agent-implementation-guide.md), [deployment profiles](../deployment/README.md), [registry/status runbook](../operations/registry-status-runbook.md), [error catalogue](../appendices/ERROR-CATALOGUE.md) and [conformance](../conformance/README.md).

[Back to component implementation guides →](README.md)
