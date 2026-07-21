---
layout: default
title: "Threats, Harms and Controls"
parent: "Implementation Guide"
nav_order: 11
has_children: true
has_toc: true
---
# Threat, harm and control model

The security model connects system claims to adversaries, attack paths, harms, controls and evidence. It complements cryptographic security definitions by covering persistent artefacts, governance state, implementation behaviour and information observed outside the proof transcript.

## Canonical sources

- `threat-matrix.yaml` is authoritative.
- `threat-matrix.csv` and `threat-matrix.md` are generated views.
- [Methodology](threat-model-methodology.md)
- [RAHP adoption and adaptation](rahp-adoption-and-adaptation.md)
- [Security guardrails](security-guardrails.md)
- [Risk appetite and acceptance](risk-appetite-and-acceptance-policy.md)
- [Security and trust metrics](security-and-trust-metrics.md)
- [Harm taxonomy](harm-taxonomy.md)
- [Control catalogue](control-catalog.md)
- [Residual-risk register](residual-risk-register.md)
- [Deployment assessment template](deployment-threat-assessment-template.md)
- [Profile views](profiles/)

A threat is not considered addressed until it has at least one control, an accountable owner, a verification method and an explicit residual-risk disposition.

## Method provenance

The controls–guardrails–assurance-tests–metrics structure adapts the methodology of the [Trust over IP RAHP TF](https://github.com/trustoverip/dtgwg-rahp-tf). The [adoption and adaptation statement](rahp-adoption-and-adaptation.md) records the reviewed upstream commit and the ZKP-specific transformation.
