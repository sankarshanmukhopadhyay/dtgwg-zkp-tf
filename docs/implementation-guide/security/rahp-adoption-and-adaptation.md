---
layout: default
title: "RAHP adoption and adaptation"
parent: "Threats, Harms and Controls"
grand_parent: "Implementation Guide"
nav_order: 2
has_toc: true
---
# RAHP adoption and adaptation statement

This security-assurance layer was developed by examining and adapting the work of the **Trust over IP Decentralized Trust Graph Working Group Risk Assessment and Harms Prevention Task Force (RAHP TF)**.

## Upstream source

- Repository: [trustoverip/dtgwg-rahp-tf](https://github.com/trustoverip/dtgwg-rahp-tf)
- Reviewed branch: `main`
- Reviewed upstream commit: [`94d17a6f5e8b448aae4698ff183e77a4a2f7a083`](https://github.com/trustoverip/dtgwg-rahp-tf/commit/94d17a6f5e8b448aae4698ff183e77a4a2f7a083)
- Upstream artefacts examined: RAHP Risk Register v4, User Stories Framework v3, HTML risk and matrix views, workflow reference, and AI-assisted process guidance
- Upstream licence stated by the RAHP repository: CC BY 4.0

{: .evidence }
The commit identifier fixes the source baseline used for this adaptation. Future RAHP changes are not automatically incorporated and require a new review and recorded provenance update.

## What was adopted

The ZKP guide adopts the following RAHP methodological distinctions:

1. **Harms are first-class design inputs.** Security analysis must identify human and institutional consequences, not only technical failure.
2. **Controls, guardrails and assurance tests are different artefacts.** Controls continuously reduce risk; guardrails block activation; assurance tests provide evidence that guardrails are satisfied.
3. **Risk evidence must connect to lifecycle decisions.** Risk treatment is linked to deployment gates, accountable authority, monitoring and review.
4. **Metrics connect design-time analysis to runtime assurance.** Measures are defined to detect whether controls and governance remain effective in operation.
5. **Stable identifiers enable cross-artefact traceability.** Threats, controls, guardrails, tests, metrics and evidence are connected through machine-readable matrices.

## How it was adapted for ZKP implementation

The RAHP toolkit is oriented toward decentralised trust systems and VTC lifecycle governance. This repository applies its method specifically to zero-knowledge proof profiles, implementations and deployments.

| RAHP concept | ZKP adaptation | Resulting artefact |
|---|---|---|
| `RK-xx` risks | Existing `THR-xxx` cryptographic, implementation, governance and harm threats retained as canonical | `threat-matrix.yaml` |
| `CT-xx` controls | Existing `CTL-xxx` ZKP control families retained and expanded in operational meaning | `control-catalog.md` |
| `GR-xx` guardrails | ZKP activation guardrails for profiles, mediated proving, agents, offline verification, migration and production entry | `security-guardrails.md` |
| `AT-xx` assurance tests | ZKP security assurance tests separated from protocol conformance tests | `security-assurance-tests.md` |
| `M-xx` trust metrics | Privacy-bounded security and trust indicators tied to ZKP attack surfaces | `security-and-trust-metrics.md` |
| Phase gates | Deployment and capability activation gates rather than VTC bootstrapping phases | `production-entry-criteria.md` and guardrail matrices |
| Persona and use-case linkage | Threat, scenario, affected-party and deployment-profile linkage | matrices under `docs/implementation-guide/matrices/` |

## Intentional differences

This repository does **not** copy the RAHP register or claim that RAHP identifiers are normative ZKP requirements. It intentionally:

- preserves the ZKP guide's existing threat IDs and control vocabulary;
- uses ZKP-specific cryptographic and protocol evidence;
- allows time-bounded exceptions for explicitly classified risks, while treating selected guardrails as non-exceptionable;
- avoids importing VTC phase language where the relevant decision is implementation or deployment activation;
- adds machine-readable JSON evidence schemas and repository validators;
- treats operational telemetry as privacy-sensitive and prohibits metrics that create a new correlation surface.

## Attribution boundary

The RAHP TF is credited as the methodological source for the adopted risk, guardrail, assurance-test and metric discipline. All ZKP-specific threat statements, mappings, schemas, thresholds and deployment decisions in this repository are adaptations made for this implementation guide. Their inclusion does not imply RAHP TF approval, Trust over IP endorsement, or normative status.

## Ongoing provenance rule

Any future change materially derived from RAHP should update:

1. the reviewed upstream commit above;
2. `matrices/rahp-adaptation-map.csv`;
3. the relevant document's provenance note;
4. release notes describing the adopted and adapted concepts.
