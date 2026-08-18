---
layout: default
title: "RAHP adoption and adaptation"
parent: "Threats, Harms and Controls"
grand_parent: "Implementation Guide"
nav_order: 2
has_toc: true
---
# RAHP adoption and adaptation statement

This security-assurance layer was originally developed by examining and adapting the **Trust over IP DTG Risk Assessment and Harms Prevention Task Force (RAHP TF)** work. It is now maintained against the independently evolved **RAHP Toolkit** method used by this fork for reproducible specification pressure testing.

## Provenance baselines

### Historical methodological source

- Repository: [trustoverip/dtgwg-rahp-tf](https://github.com/trustoverip/dtgwg-rahp-tf)
- Reviewed historical commit: `94d17a6f5e8b448aae4698ff183e77a4a2f7a083`
- Role: provenance for the original risks/harms, controls, guardrails, assurance-test and metric separation adopted by the ZKP implementation guide.

### Current operational refresh source

- Repository: [sankarshanmukhopadhyay/rahp-toolkit](https://github.com/sankarshanmukhopadhyay/rahp-toolkit)
- Toolkit version: `v1.1.0`
- Reviewed commit: `6a95a9a2a948ece93a75e9583554b448714ef4c4`
- Engine contract: `rahp-engine-contract-v1`
- Refresh date: `2026-08-18`
- ZKP target revision: `9a1ae81465e1da9f5c06ccd500a70708eb2511a6`
- Canonical review record: `.rahp/reviews/dtg-zkp-v1-1-refresh/pressure-test.yaml`
- Human view: [RAHP v1.1 lifecycle and assurance refresh](../pressure-tests/rahp-v1.1-refresh.md)

{: .evidence }
Both identifiers are intentionally preserved. The first answers **where the ZKP adaptation originated**. The second answers **which current RAHP method and engine contract were used for the latest refresh**. Neither source automatically changes ZKP normative requirements.

## What is adopted

The ZKP guide adopts the following RAHP distinctions:

1. **Harms are first-class design inputs.** Security analysis identifies human and institutional consequences, not only technical failure.
2. **Controls, guardrails and assurance tests are separate artefacts.** Controls continuously reduce risk; guardrails block activation; assurance tests produce evidence that a guardrail is satisfied.
3. **Risk evidence connects to lifecycle decisions.** Treatment links to deployment gates, accountable authority, monitoring, review and revocation.
4. **Metrics connect design-time analysis to runtime assurance.** Measures detect whether controls and governance remain effective without creating a new surveillance surface.
5. **Stable identifiers enable traceability.** Threats, controls, guardrails, tests, metrics, requirements and evidence are connected through machine-readable matrices.
6. **Scenario-driven pressure testing complements clause review.** A requirement is tested under degraded operation, collusion, lifecycle transition, accessibility, delegation and cross-implementation conditions.
7. **Durable evidence is different from transient output.** A review should preserve target revision, method/version, findings, disposition, evidence, resolution state and retest triggers.
8. **The narrowest effective control plane wins.** A real risk does not automatically justify adding another normative field to the core protocol.

## How it is adapted for ZKP implementation

| RAHP concept | ZKP adaptation | Resulting artefact |
|---|---|---|
| `RK-*` deployment risks and portable risk patterns | Existing `THR-xxx` cryptographic, implementation, governance and harm threats remain canonical in this repo | `security/threat-matrix.yaml` |
| `CT-*` controls | Existing `CTL-xxx` ZKP control families retained and expanded operationally | `security/control-catalog.md` |
| `GR-*` guardrails | ZKP activation guardrails for profiles, mediated proving, agents, offline verification, migration and production entry | `security/security-guardrails.md` |
| `AT-*` assurance tests | ZKP security assurance tests separated from protocol conformance tests | `conformance/security-assurance-tests.md` |
| scenario corpora and patterns | ZKP use-case corpus is exercised as a pressure-test corpus without transferring scenario ownership to RAHP | `scenarios/pressure-test-use-case-corpus.md` and RAHP `CORPUS-DTG-ZKP` adapter |
| lifecycle/evidence-retention discipline | `LIV-LCM-*` and historical/as-of evidence are mapped to controls and assurance | `matrices/requirements-assurance-map.csv` |
| durable review records | pinned review state and retest triggers are stored alongside the repo | `.rahp/reviews/` plus rendered pressure-test pages |
| portable assurance | reusable RAHP patterns inform cross-repo comparison while ZKP-local IDs remain authoritative here | pressure-test records and adaptation map |

## Intentional differences

This repository does **not** copy the RAHP catalogue wholesale or claim RAHP identifiers as normative ZKP requirements. It intentionally:

- preserves the ZKP guide's existing `THR-*`, `CTL-*`, `ZGR-*`, `ZAT-*` and `LIV-*` namespaces;
- uses ZKP-specific cryptographic, interoperability and deployment evidence;
- allows time-bounded exceptions for explicitly classified risks while treating selected guardrails as non-exceptionable;
- avoids importing lifecycle language whose authority belongs to another deployment or community;
- adds machine-readable evidence schemas and repository validators;
- treats operational telemetry as privacy-sensitive and prohibits metrics that create a new correlation surface; and
- keeps normative adoption authority with the applicable ZKP/DTG decision process rather than with the assurance method.

## Ongoing provenance rule

A future RAHP-derived change should update, when material:

1. the current RAHP Toolkit version and reviewed commit;
2. the canonical `.rahp/reviews/` record or its successor;
3. `matrices/rahp-adaptation-map.csv` and `requirements-assurance-map.csv` where coverage changes;
4. the relevant document provenance note; and
5. release notes describing adopted concepts, changed evidence obligations and any remaining open findings.
