---
layout: default
title: Implementation Guide
nav_order: 2
has_children: true
has_toc: true
---
# Implementation and Interoperability Guide

This workspace provides an implementation path from controlled exploration to independently assessable production deployment.

## Start here

1. Select an [adoption stage](adoption/README.md).
2. Identify the applicable [component implementation guides](implementation/README.md).
3. choose a [secure deployment profile](deployment/README.md).
4. Establish [operational playbooks](operations/README.md).
5. Test the implementation through the [scenario corpus](scenarios/README.md) and [conformance programme](conformance/README.md).

## Repository map

| Directory | Purpose |
|---|---|
| `adoption/` | Staged adoption, pilot design and production-entry gates |
| `implementation/` | Role-specific issuer, wallet, verifier, registry, agent and assessor guidance |
| `deployment/` | Secure topologies, production controls and deployment evidence |
| `operations/` | Executable runbooks for change, compromise, recovery and redress |
| `architecture/` | Context, layers, trust boundaries, ownership and viewpoints |
| `scenarios/` | Functional, governance, deployment and operational pressure tests |
| `conformance/` | Levels, tests, schemas, fixtures and evidence templates |
| `security/` | Threat, harm, control and residual-risk model |
| `boundaries/` | Assurance and disclosure boundaries |
| `diagrams/` | Registered Mermaid sources and textual interpretations |
| `matrices/` | Machine-readable traceability maps |

## Validation

```sh
python3 scripts/validate_docs.py
python3 scripts/validate_conformance.py
python3 scripts/validate_style.py
python3 scripts/validate_links.py
python3 scripts/validate_fixtures.py
python3 scripts/validate_threat_model.py
python3 scripts/validate_deployment_profiles.py
python3 scripts/validate_operations.py
python3 scripts/validate_navigation.py
python3 scripts/validate_diagrams.py
python3 scripts/validate_generated_counts.py
python3 scripts/build_traceability.py
```
