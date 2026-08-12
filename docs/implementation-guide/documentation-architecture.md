---
layout: default
title: Documentation Architecture
nav_order: 2
parent: Implementation Guide
has_toc: true
---
# Documentation Architecture

The documentation is organised as an **executable assurance lifecycle**, not as a flat reference library. The sidebar now follows the sequence in which a programme should normally make decisions: orient, adopt, design boundaries, implement, integrate, deploy, operate, test, govern and reference.

## Primary reading spine

| Stage | Primary question | Start here | Expected output |
|---|---|---|---|
| Orientation | What problem is being solved and which route applies? | [Guided learning paths](guided-learning.md) | Selected role/route and completion outcome |
| Adoption | What profile and maturity stage should be attempted? | [Adoption](adoption/README.md) | Stage, profile, owners and entry/exit gates |
| Architecture | Where are system and trust boundaries? | [Architecture](architecture/README.md) | Component/trust-boundary model |
| Assurance boundaries | What may be relied on and what may be observed? | [Boundaries](boundaries/README.md) | Paired assurance/disclosure records |
| Information + privacy | What data is necessary and what can be correlated? | [Information model](information-model/README.md), [privacy](privacy/README.md) | Minimal schema, adversary/privacy class |
| Implementation | What must each role build and evidence? | [Implementation](implementation/README.md) | Role-specific contracts and tests |
| Interoperability | Which external DTG semantics/authority are consumed? | [DTG interoperability](interoperability/README.md) | Explicit dependency/evidence register |
| Deployment | Which topology and controls are mandatory? | [Secure deployment](deployment/README.md) | Approved deployment profile/evidence |
| Operations | How is assurance preserved after launch? | [Operations](operations/README.md) | Monitoring, incident, recovery and redress evidence |
| Security + lifecycle | What can fail, age, migrate or be compromised? | [Threats/harms/controls](security/README.md), [lifecycle](lifecycle/README.md) | Control coverage and migration/cryptoperiod rules |
| Evaluation | Does behaviour match the bounded claim? | [Pressure tests](pressure-tests/README.md), [scenarios](scenarios/README.md), [conformance](conformance/README.md) | Test results and dispositions |
| Governance | Which decisions are ratified, local or unresolved? | [Decision governance](decisions/README.md), [ADRs](adr/README.md) | Decision evidence and change history |
| Reference | Where are taxonomies, diagrams, matrices and citations? | [Taxonomy](taxonomy/README.md), [appendices](appendices/README.md) | Reviewable supporting evidence |

## Navigation contract

Every major section has one of three purposes:

- **Path page** — tells a reader what to read and in what order (`Guided Learning Paths`).
- **Landing page** — explains why a section exists, what decisions it supports and where to go next (`Implementation`, `Deployment`, `Conformance`, etc.).
- **Evidence/reference page** — records a specific decision, model, test, runbook, matrix or source.

Readers should be able to enter through a path or landing page without understanding the repository tree in advance.

## Source-of-truth hierarchy

This fork distinguishes sources by authority:

1. [`proof-of-liveness-requirements.md`](../../proof-of-liveness-requirements.md) is the fork's semantic requirements baseline.
2. Ratified upstream decisions and authoritative external specifications govern the subjects within their scope.
3. [Decision records](decisions/README.md) and [ADRs](adr/README.md) state how this fork interprets or implements those requirements.
4. Implementation/deployment/operations guidance operationalises the above without silently strengthening upstream requirements.
5. Scenarios, tests, matrices and generated artifacts are evidence and traceability views; they do not create authority by themselves.

## Machine-verifiable navigation

`_data/learning_paths.json` defines maintained reader routes. `scripts/validate_learning_paths.py` fails when a route target disappears or a step lacks a declared outcome. `scripts/validate_navigation.py` validates front matter and also rejects duplicate top-level `nav_order` values, preserving deterministic sidebar flow.

[Choose a guided learning path →](guided-learning.md)
