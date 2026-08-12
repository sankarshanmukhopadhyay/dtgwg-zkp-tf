---
layout: default
title: "Lifecycle and Migration"
parent: "Implementation Guide"
nav_order: 13
has_children: true
has_toc: true
---
# Lifecycle and Migration

Lifecycle governance answers a question that cryptographic validity alone cannot answer: **for how long may a proof, credential, key, policy or proof system remain a trustworthy basis for a decision, and what evidence survives when that basis changes?**

This section connects day-to-day status transitions to cryptoperiods, assurance horizons, proof-system migration and historical verification. Use it after the component implementation guidance and before relying on a deployment as production-ready.

## Lifecycle layers

| Layer | Governing question | Typical authority | Evidence required |
|---|---|---|---|
| Credential/status | Is this credential currently usable, suspended, revoked, expired or superseded? | issuer/status authority | effective-time status event, replacement relationship |
| Issuer/registry authority | Was the issuer or registry recognised and authorised for this scope at the relevant time? | governance/recognition authority | versioned recognition and scope records |
| Keys and cryptoperiods | Was the signing/verifying key acceptable at the decision time? | key-management authority under approved policy | key activation, rotation, retirement and compromise evidence |
| Delegation | Was the agent mandate current and in scope when the action occurred? | principal/delegation authority | mandate, revocation state, effective time |
| Policy | Which relying-party and profile rules governed the outcome? | policy authority | immutable/versioned policy reference |
| Proof system | Was the proof construction/profile still accepted and downgrade-safe? | profile/specification governance | supported-version policy, migration evidence, retirement decision |

## State and migration models

The [credential and issuer lifecycle state model](../diagrams/D-034-credential-issuer-lifecycle-states.md) shows governed credential transitions. The existing [key lifecycle](../diagrams/D-014-key-lifecycle.md), [revocation propagation](../diagrams/D-017-revocation-propagation.md) and [proof-system migration](../diagrams/D-020-proof-system-migration.md) diagrams cover the other major transition classes.

A lifecycle design should always identify **who can cause a transition, when it becomes effective, how dependent components learn about it, and what evidence permits later reconstruction**.

## Cryptoperiod and assurance horizon

Read [Cryptoperiod and assurance horizon](cryptoperiod-and-assurance-horizon.md) when setting key lifetimes, cache/staleness tolerances, revocation propagation targets and evidence-retention periods. These bounds should be derived from the assurance claim and threat model rather than copied from generic operational defaults.

## Proof-system migration

Read the [proof-system migration profile](proof-system-migration-profile.md) before introducing a new proof construction or deprecating an existing one. Migration must prevent silent downgrade, preserve version-specific decision evidence and define how archived decisions remain verifiable after retirement.

Operational execution is covered by the [proof-system migration runbook](../operations/proof-system-migration-runbook.md).

## Historical-state requirement

For any decision that may be audited or contested later, the system should be able to reconstruct the authoritative state at time **T** without asking the current registry or policy to reinterpret history. Preserve version identifiers, effective times, signed snapshots or equivalent evidence needed to answer:

> What authority, status, policy, key and proof-system state was relied upon when this decision was made?

## Lifecycle readiness evidence

A production profile should be able to produce:

- state-transition definitions and authorities;
- revocation/suspension propagation measurements;
- key rotation and compromise exercise evidence;
- cache/freshness policy;
- proof-system migration and downgrade tests;
- historical-state reconstruction evidence;
- replacement/re-issuance semantics; and
- explicit closure criteria for obsolete state.

## Where to go next

- For implementation responsibilities, return to [Component implementation guides](../implementation/README.md).
- For operational incidents and recovery, continue to [Operational playbooks](../operations/README.md).
- For deployment controls, see [Deployment](../deployment/README.md).
- For evidence claims, continue to [Conformance](../conformance/README.md).
