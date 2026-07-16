---
title: Context decision record
status: incubating
normative_status: non-normative
owner: DTG ZKP Task Force
last_reviewed: 2026-07-16
---


# Context decision record

A context is a governed linkability domain, not only a string supplied to a nullifier function. Each profile or deployment records the following decision before selecting a nullifier or pseudonym construction.

| Decision field | Required content |
|---|---|
| Context ID and version | Stable identifier and canonical derivation |
| Context authority | Entity authorized to define and change the boundary |
| Permitted linkability | Actions and observations intentionally linkable inside the context |
| Prohibited linkability | Cross-context linkage the design claims to resist |
| Collusion target | Whether the boundary must survive issuer-verifier, verifier-verifier or registry collusion |
| Epoch authority | Who defines rollover and exceptional extension |
| User-facing name | Human-readable description of the context |
| User test | How a person can determine whether two verifiers share a context |
| Change process | Notice, migration, appeal and effective-time rules |
| Retention | Nullifier and decision-state retention limits |
| Threat references | Applicable correlation and governance threats |
| Evidence | Test vectors, configuration digests and governance records |

A context definition fails review when it is cryptographically precise but cannot be communicated to the affected person or when an organizational merger can silently expand the boundary.
