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
- [Harm taxonomy](harm-taxonomy.md)
- [Control catalogue](control-catalog.md)
- [Residual-risk register](residual-risk-register.md)
- [Deployment assessment template](deployment-threat-assessment-template.md)
- [Profile views](profiles/)

A threat is not considered addressed until it has at least one control, an accountable owner, a verification method and an explicit residual-risk disposition.
