---
layout: default
title: "RAHP v1.1 lifecycle and assurance refresh"
parent: "Cross-specification Pressure Tests"
grand_parent: "Implementation Guide"
nav_order: 5
has_toc: true
---
# RAHP v1.1 lifecycle and assurance refresh

This review refreshes the fork's embedded RAHP work against **RAHP Toolkit v1.1.0**, pinned to `sankarshanmukhopadhyay/rahp-toolkit@6a95a9a2a948ece93a75e9583554b448714ef4c4`, while reviewing ZKP repository state at `9a1ae81465e1da9f5c06ccd500a70708eb2511a6`.

The canonical machine-readable record is `.rahp/reviews/dtg-zkp-v1-1-refresh/pressure-test.yaml`. The review does not transfer normative authority from the ZKP Task Force to RAHP. It tests whether the fork's requirements and assurance machinery expose enough authority, lifecycle, evidence and affected-party state to make implementation claims testable.

## Why this refresh matters

The earlier ZKP security layer adopted RAHP's risks/harms, control, guardrail, assurance-test and metric distinctions. RAHP v1.1 adds a more explicit portable assurance catalogue, scenario-driven testing, lifecycle and evidence-retention discipline, semantic governance and durable review records. The refresh therefore tests the ZKP repository as an **executable governance system**, not just a collection of security documents.

## Focused pressure tests

| Test | Pressure | Required evidence | Passing condition |
|---|---|---|---|
| `RPT-01` | **Long-retention evidence** | retained artefact classes, purpose, access, retention/deletion or archival rule, original evaluation time, later audit semantics, applicable assurance horizon | later audit can distinguish historical validity from current validity and does not silently extend expired privacy/security claims |
| `RPT-02` | **Revocation cadence and stale state** | status cadence, maximum cache age, effective-time rules, partition/unavailable behaviour, independent-verifier vectors | independent conformant verifiers reach the same result at boundary times or invoke the same governed degraded mode |
| `RPT-03` | **Post-quantum / suite migration** | supported-suite record, migration trigger, overlap window, downgrade vectors, rollback authority, pre/post security horizons | migration preserves semantic claims without representing lineage as restored confidentiality, unlinkability or unforgeability |
| `RPT-04` | **Enrolment-dedup failure** | uniqueness scope, dedup method, error evidence, re-enrolment/recovery controls, false-match/false-non-match handling, redress | `f-distinct` or scoped-uniqueness claims remain bounded to demonstrated evidence and do not collapse into global personhood claims |
| `RPT-05` | **Correlated multi-issuer biometric dependency** | issuer/provider dependency graph, common processors/models/template stores, breach domains, governance and change authority | nominally independent issuers do not inherit an unacknowledged common correlation, coercion, compromise or exclusion dependency |

## Findings and disposition

All five tests remain **open assurance obligations**, not evidence that the requirements text is defective. The fork has already introduced substantial normative and implementation guardrails for each area. The remaining question is whether deployments and candidate constructions can produce the required evidence.

This distinction matters: a pressure test should not manufacture specification changes when the narrowest effective control plane is deployment, assurance, architecture or governance.

## Requirement traceability

The corresponding `LIV-*` coverage is recorded in [`requirements-assurance-map.csv`](../matrices/requirements-assurance-map.csv). In particular:

- `LIV-LCM-01..06` map lifecycle, retention, revocation cadence and historical evidence to scenarios, controls, guardrails and assurance tests;
- `LIV-ALG-01..08` map proof-system independence, suite identification, negotiation, migration, dependencies and post-quantum readiness;
- `LIV-UNIQ-06` maps distinct-human semantics to scoped uniqueness and deduplication assurance.

## Retest triggers

Re-run the focused tests when any of the following occurs:

1. a concrete proof construction or suite is selected;
2. retention obligations or historical-verification requirements change;
3. status, registry or offline/degraded-mode behaviour changes;
4. a cryptographic suite is deprecated or post-quantum migration begins;
5. a biometric/deduplication method or provider changes;
6. a new issuer enters the ecosystem or common infrastructure changes provider independence;
7. B1 or B2 is amended through decision governance.

## Assurance boundary

A passing RAHP refresh means the repository exposes a testable control and evidence path. It does **not** prove that a biometric determination is correct, that a particular construction is production-ready, or that upstream DTG has adopted the fork's working positions.
