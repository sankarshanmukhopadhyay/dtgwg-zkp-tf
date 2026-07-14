# Implementation & Interoperability Guide

**Status:** Incubating  
**Normative status:** Non-normative unless explicitly marked

## Purpose

This workspace pressure-tests whether DTG ZKP profiles are implementable across
biometric providers, issuers, wallets, verifiable trust agents, agents, verifiers,
trust registries, and governance frameworks.

It focuses on semantic interoperability, privacy boundaries, assurance dependencies,
lifecycle behaviour, operational resilience, accessibility, and conformance.

## Structure

| Directory | Purpose |
|---|---|
| `architecture/` | principles, layers, trust boundaries, ownership, quality attributes |
| `adr/` | decisions and rationale |
| `taxonomy/` | predicates, adversaries, lifecycle and validation classifications |
| `scenarios/` | structured pressure-test use cases |
| `matrices/` | traceability and coverage tables (populated: 30 scenarios, 72 predicate mappings, 46 threat mappings) |
| `conformance/` | conformance levels, 76-case test matrix, fixtures, and plugfest planning |
| `editorial/` | templates and contribution conventions |
| `appendices/` | glossary and references |
| `diagrams/` | Mermaid sources and diagram register |

## Inherited drafting rules

Every privacy claim names its adversary and horizon. Every predicate states what it
does not establish. Conjecture is labelled as conjecture.

## Validation

Two scripts validate this workspace, both run from the repository root:

```sh
python3 scripts/validate_docs.py          # doc hygiene: required files, tabs, final newlines
python3 scripts/validate_conformance.py   # referential integrity of matrices/ and conformance/
```

`validate_conformance.py` fails the build if any matrix is a placeholder
(header row only), if any predicate/adversary/scenario/ADR reference is
dangling, or if any conformance level (see `conformance/levels.md`) is
missing a positive or a negative test case.
