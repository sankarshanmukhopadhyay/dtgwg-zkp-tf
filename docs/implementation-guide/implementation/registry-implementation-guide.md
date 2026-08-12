---
layout: default
title: "Registry implementation guide"
parent: "Implementation"
grand_parent: "Implementation Guide"
nav_order: 4
has_toc: true
---
# Registry implementation guide

A registry publishes governed recognition, status or other authority state. It is an evidence source for a verifier; it does **not** create legitimacy merely by returning a record.

## Responsibilities

A registry implementation should provide:

- explicit authority for each record class;
- signed or otherwise integrity-protected state;
- provenance and version identifiers;
- effective, publication and expiry times where relevant;
- deterministic correction, suspension, revocation and replacement semantics;
- bounded cache guidance;
- authenticated administrative changes;
- historical/as-of evidence where the governance model requires it; and
- a federation/conflict policy if multiple registries can speak about overlapping state.

## State model

See [D-031 — Registry Authority and Status State Model](../diagrams/D-031-registry-authority-status-state-model.md) for the governed transition model. Each transition should identify the authority that can cause it, its effective time and the evidence emitted.


Separate at least these concepts when applicable: **discovered**, **recognised**, **authorised for scope**, **currently valid**, **suspended**, **revoked/withdrawn**, **expired**, **superseded** and **unknown/unavailable**.

Consumers should not have to infer the meaning of absence. Define whether a missing record means never recognised, removed, unavailable, outside scope or unknown.

## Time semantics and historical truth

Registry responses should distinguish the state that is effective for a target time from the time at which the response was generated. If past decisions must be auditable, preserve append-only history, signed snapshots, transparency evidence or another mechanism sufficient to answer: **what state was authoritative at time T?**

## Federation

A federated registry must define:

- authority partitioning;
- conflict precedence;
- trust-anchor distribution;
- stale/partitioned operation;
- cross-registry identifiers and correlation risks;
- revocation propagation expectations; and
- evidence retained when state is reconciled.

## Security controls

Protect publication keys, administration interfaces, build/deployment pipelines and state stores. Require dual control or equivalent safeguards for high-impact recognition/revocation changes. Monitor for unauthorised additions, delayed revocations and rollback to older signed state.

## Privacy controls

A registry used during every verification can become a high-value observation point. Evaluate whether requests reveal holder, verifier, predicate, issuer or transaction context. Prefer privacy-preserving distribution/caching patterns where they preserve freshness and governance requirements.

## Failure cases to test

- stale cache;
- signed rollback;
- conflicting federation sources;
- delayed revocation propagation;
- unavailable authority source;
- operator key compromise;
- correction of an erroneous revocation; and
- reconstruction of historical state.

## Evidence to produce

- registry governance/authority statement;
- state schema and lifecycle model;
- signed example state/snapshot;
- change audit trail;
- cache/freshness policy;
- federation/conflict policy where applicable;
- compromise/recovery exercise evidence; and
- historical-state reconstruction test where required.

## Related guidance

Read [DTG interoperability](../interoperability/README.md), [registry resolution flow](../diagrams/D-005-registry-resolution-flow.md), [federated registry deployment](../deployment/deployment-profile-federated-registry.md), [registry/status runbook](../operations/registry-status-runbook.md) and [revocation propagation](../operations/revocation-propagation-runbook.md).

[Back to component implementation guides →](README.md)
