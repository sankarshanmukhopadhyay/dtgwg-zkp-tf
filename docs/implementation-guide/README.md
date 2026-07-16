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
- [Boundary model](boundaries/README.md)
- [Threat, harm and control model](security/README.md)
- [Attestation information model](information-model/README.md)
- [Style profile](editorial/STYLE-GUIDE.md)
- [Glossary](appendices/GLOSSARY.md)

## Repository map

| Directory | Purpose |
|---|---|
| `guide/` | coherent implementation lifecycle and implementer checklists |
| `architecture/` | context, layers, trust boundaries and viewpoints |
| `adr/` | explicit decisions, alternatives and consequences |
| `taxonomy/` | stable predicate and adversary identifiers |
| `scenarios/` | 30 structured pressure-test scenarios |
| `matrices/` | traceability and maturity data |
| `conformance/` | four levels, machine-checkable tests, fixtures, schemas and evidence templates |
| `boundaries/` | paired assurance and disclosure boundaries plus context decisions |
| `security/` | canonical threat matrix, harms, controls and residual-risk process |
| `information-model/` | attestation schema and correlation analysis |
| `privacy/` | composition, observable-event and mediated-proving analysis |
| `lifecycle/` | cryptoperiod, assurance-horizon and migration guidance |
| `editorial/` | style profile, terminology and contribution controls |
| `appendices/` | glossary, errors, references and guidance index |
| `diagrams/` | Mermaid sources with textual interpretations |

## Validation

Run from the repository root:

```sh
python3 scripts/validate_docs.py
python3 scripts/validate_conformance.py
python3 scripts/validate_style.py
python3 scripts/validate_links.py
python3 scripts/validate_fixtures.py
python3 scripts/validate_threat_model.py
python3 scripts/validate_threat_model.py
python3 scripts/build_traceability.py
```

The implementation guide is non-normative by default. Open cryptographic or governance choices remain explicit decision dependencies.
