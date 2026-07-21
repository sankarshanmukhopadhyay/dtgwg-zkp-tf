---
layout: default
title: Documentation Architecture
nav_order: 2
parent: Implementation Guide
has_toc: true
---
# Documentation Architecture

The documentation is organised as an executable assurance lifecycle rather than a reference library. Each layer answers a different governance question and produces evidence consumed by the next layer.

| Layer | Primary question | Authoritative content | Expected output |
|---|---|---|---|
| Orientation | Why and for whom? | [Guided learning paths](guided-learning.md) | Selected route and completion outcome |
| Adoption | What should be attempted now? | [Adoption pathway](adoption/README.md) | Stage, scope, ownership and gate |
| Architecture | Where are boundaries and dependencies? | [Architecture](architecture/README.md) | Component and trust-boundary model |
| Implementation | What must each role build? | [Implementation guides](implementation/README.md) | Role-specific implementation decisions |
| Deployment | Which controls are mandatory? | [Secure deployment](deployment/README.md) | Approved deployment profile |
| Operations | How is assurance sustained? | [Operational playbooks](operations/README.md) | Monitoring, response and recovery evidence |
| Evaluation | Does behaviour match the claim? | [Scenarios](scenarios/README.md), [conformance](conformance/README.md) | Test and assessment evidence |
| Risk | What remains unmitigated and who accepts it? | [Security](security/README.md) | Traceable residual-risk decision |

The machine-readable `_data/learning_paths.json` manifest defines the maintained routes. `scripts/validate_learning_paths.py` fails when a route target disappears or a step lacks a declared outcome.

[Choose a guided learning path →](guided-learning.md)
