---
title: Implementation and Interoperability Guide workspace
status: incubating
normative_status: non-normative
owner: DTG ZKP Task Force
last_reviewed: 2026-07-16
---

# Implementation and Interoperability Guide

This workspace turns proof, credential, policy, delegation and registry assumptions into reviewable implementation guidance and conformance evidence.

## Start here

- [Main implementation guide](guide/implementation-interoperability-guide.md)
- [Architecture core](architecture/README.md)
- [Scenario corpus](scenarios/README.md)
- [Conformance programme](conformance/README.md)
- [Boundary model](boundaries/README.md)
- [Threat, harm and control model](security/README.md)
- [Attestation information model](information-model/README.md)
- [Style profile](editorial/STYLE-GUIDE.md)
- [Glossary](appendices/GLOSSARY.md)

## Repository map

| Directory | Purpose |
|---|---|
| `guide/` | Coherent implementation lifecycle and implementer checklists |
| `architecture/` | Context, layers, trust boundaries, ownership and architectural viewpoints |
| `adr/` | Explicit decisions, alternatives and consequences |
| `taxonomy/` | Stable predicate, adversary and supporting classification identifiers |
| `scenarios/` | Structured pressure-test scenarios |
| `matrices/` | Traceability and maturity data |
| `conformance/` | Conformance levels, machine-checkable tests, fixtures, schemas and evidence templates |
| `boundaries/` | Paired assurance and disclosure boundaries, together with context decisions |
| `security/` | Canonical threat matrix, harm taxonomy, control catalogue and residual-risk process |
| `information-model/` | Attestation schema and field-level correlation analysis |
| `privacy/` | Composition, reconstruction, observable-event and mediated-proving analysis |
| `lifecycle/` | Cryptoperiod, assurance-horizon and migration guidance |
| `editorial/` | Style profile, terminology and contribution controls |
| `appendices/` | Glossary, errors, references and guidance index |
| `diagrams/` | Mermaid sources with accompanying textual interpretations |

## Validation

Run the following commands from the repository root:

```sh
python3 scripts/validate_docs.py
python3 scripts/validate_conformance.py
python3 scripts/validate_style.py
python3 scripts/validate_links.py
python3 scripts/validate_fixtures.py
python3 scripts/validate_threat_model.py
python3 scripts/build_traceability.py
