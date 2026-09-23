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

1. [`trustoverip/dtgwg-zkp-spec`](https://github.com/trustoverip/dtgwg-zkp-spec) is canonical for ZKP specification semantics, construction records, conformance semantics and integration boundaries wherever it speaks.
2. [`trustoverip/dtgwg-zkp-tf`](https://github.com/trustoverip/dtgwg-zkp-tf) owns task-force requirements, discussions and decisions; `proof-of-liveness-requirements.md` is a requirements source for the personhood/liveness use-case family rather than a universal ZKP semantic baseline.
3. Other authoritative DTG specifications and ratified upstream decisions govern the subjects within their scope.
4. [Decision records](decisions/README.md) and [ADRs](adr/README.md) state how this downstream repository interprets or implements those authoritative inputs and identify any fork-local extension.
5. Implementation/deployment/operations guidance operationalises the above without silently strengthening or redefining upstream requirements.
6. Scenarios, tests, matrices and generated artifacts are evidence and traceability views; they do not create authority by themselves.

## Machine-verifiable navigation

`_data/learning_paths.json` defines maintained reader routes. `scripts/validate_learning_paths.py` fails when a route target disappears or a step lacks a declared outcome. `scripts/validate_navigation.py` validates front matter and also rejects duplicate top-level `nav_order` values, preserving deterministic sidebar flow.

[Choose a guided learning path →](guided-learning.md)
