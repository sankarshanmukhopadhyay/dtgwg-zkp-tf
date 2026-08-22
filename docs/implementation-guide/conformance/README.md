---
layout: default
title: "Conformance"
parent: "Implementation Guide"
nav_order: 16
has_children: true
has_toc: true
---
# Conformance and plugfest

**Status:** Incubating
**Normative status:** Non-normative unless explicitly promoted into the Working Draft

## What's in this directory

| File | Purpose |
|---|---|
| [`levels.md`](./levels.md) | Formal definition of conformance levels [`CL-1`](../reference/identifier-register.md#cl-1) through [`CL-4`](../reference/identifier-register.md#cl-4): which predicates and scenarios each requires, and which readiness gate it targets |
| [`test-matrix.csv`](./test-matrix.csv) | Machine-readable protocol conformance matrix: 96 positive and negative cases across four levels, with scenario, predicate, adversary and expected-result traceability |
| [`test-matrix.md`](./test-matrix.md) | Human-readable view of the same matrix, grouped by level and scenario |
| [`execution-dispositions.csv`](./execution-dispositions.csv) | Governed execution status for every protocol case |
| [`executable-harness.md`](./executable-harness.md) | Harness architecture, adapter boundary and CI isolation |
| [`conformance-decision-backlog.csv`](./conformance-decision-backlog.csv) | Machine-readable blockers for non-executable cases |
| [`fixtures/`](./fixtures/) | Illustrative, non-normative JSON fixtures (canonical transcript, issuer set, nullifier scope/epoch, delegation, registry snapshot) referenced by test cases |
| [`composed-presentation-privacy-tests.md`](./composed-presentation-privacy-tests.md) | Construction-neutral negative tests for privacy failures introduced by status, delegation, registry/accreditation, enumerable binders, network resolution and cross-artifact composition |

Validate all of the above with:

```sh
python3 scripts/validate_conformance.py
```

run from the repository root. It checks that every `predicate_id`,
`adversary_id` and `scenario_id` referenced in the test matrix and the
`matrices/` CSVs actually exists in the taxonomy and scenario corpus, and
that every conformance level has at least one passing (positive) and one
failing (negative) test case.

## Evidence pipeline

[D-038 — Conformance and Assurance Evidence Pipeline](../diagrams/D-038-conformance-assurance-evidence-pipeline.md) distinguishes internal repository validation, executable protocol cases, security assurance and cross-implementation evidence. A claim should never imply a stronger evidence layer than was actually executed.

## What conformance validates

Predicate semantics, canonical transcript and encodings, lifecycle and
status, cross-vendor interoperability, privacy against named adversaries,
constrained devices, fallback and downgrade, and error consistency — see
`levels.md` for how each of these maps onto [`CL-1`](../reference/identifier-register.md#cl-1) through [`CL-4`](../reference/identifier-register.md#cl-4).

Privacy conformance also applies across the **complete evidence closure** of a verification predicate. A credential or proof that passes standalone selective-disclosure or unlinkability tests does not establish end-to-end privacy when required delegation, status, registry/accreditation, Trust Task or network-resolution evidence introduces an additional correlation surface. See [`composed-presentation-privacy-tests.md`](./composed-presentation-privacy-tests.md).

## Minimum plugfest topology

- two issuer implementations;
- two wallet/prover implementations;
- two verifiers;
- registry and policy fixtures (see `fixtures/issuer-set.json`, `fixtures/registry-snapshot.json`);
- positive, negative, malformed, lifecycle, and privacy tests (see `test-matrix.csv`).

This matches [`UC-030`](../reference/identifier-register.md#uc-030) (Partial Deployment Across Independent Implementations)
in the pressure-test corpus, which is itself the exit criterion for Phase 4
of the corpus's implementation programme.

## What this suite is, and is not

This suite defines **expected behaviour** for a conformant implementation.
It includes a working construction-neutral harness for 27 deterministic cases:
16 mock-based harness/interoperability checks and 11 repository-owned semantic
fixtures. No cryptographic construction has been selected for the predicates
(see `../../../proof-of-liveness-requirements.md`), so the harness does not
execute real proofs. The 96 protocol cases remain authoritative and 69 retain
explicit construction-selection blockers. `scripts/validate_conformance.py`
validates the *specification's internal consistency* — that every claim is
traceable to a real predicate, adversary and scenario, and that no
conformance level is defined by assertion alone (rule 1 and rule 2 of
`../../../DRAFTING-RULES.md`) — not cryptographic correctness.

The composed-presentation cases are currently construction-neutral semantic tests. They define failure conditions that must eventually be represented in the machine-readable matrix or equivalent executable/assurance evidence as affected predicates and constructions mature.

## Known gaps

- 11 of the 30 scenarios (all P1/P2) are not yet assigned to a conformance
  level: [`UC-003`](../reference/identifier-register.md#uc-003), [`UC-007`](../reference/identifier-register.md#uc-007), [`UC-008`](../reference/identifier-register.md#uc-008), [`UC-011`](../reference/identifier-register.md#uc-011), [`UC-014`](../reference/identifier-register.md#uc-014), [`UC-015`](../reference/identifier-register.md#uc-015), [`UC-016`](../reference/identifier-register.md#uc-016), [`UC-018`](../reference/identifier-register.md#uc-018),
  [`UC-019`](../reference/identifier-register.md#uc-019), [`UC-028`](../reference/identifier-register.md#uc-028), [`UC-029`](../reference/identifier-register.md#uc-029). See `matrices/maturity-map.csv`.
- [`CL-3`](../reference/identifier-register.md#cl-3) (delegated agent) test cases reference "delegation evidence" and
  "agent key binding," neither of which has a predicate ID in
  `taxonomy/predicates.md` yet.
- No cross-vendor plugfest ([`UC-030`](../reference/identifier-register.md#uc-030)) has run. [`CL-4`](../reference/identifier-register.md#cl-4)'s positive test cases
  assume two independent implementations exist; today there are zero.
- The composed-presentation privacy cases have not yet been promoted into `test-matrix.csv`; construction-independent semantics are defined here first to avoid inventing predicate identifiers or executable claims prematurely.

## Evidence packaging

Use the implementation and profile statement templates and the JSON schemas in `schemas/` to produce portable evidence. A conformance claim identifies a level, profile, source revision, environment, fixture digests, results and exceptions.

## Boundary and threat evidence

A profile evidence bundle includes linked assurance and disclosure records, a field-level attestation schema assessment, applicable canonical threat IDs, control evidence, lifecycle bounds, migration behaviour and residual-risk decisions. The boundary-record schema and fixtures provide portable examples. Run `python3 scripts/validate_threat_model.py` with the existing validation suite.

For composed predicates, the bundle should also identify the minimum evidence closure, cross-artifact relationship inputs and verifier-originated external observations that materially affect the privacy class.

## Security assurance

- [Security assurance tests](security-assurance-tests.md)
- `security-assurance-test-matrix.csv`
- `schemas/security-assurance-result.schema.json`
- `schemas/security-metric-evidence.schema.json`

These artefacts adapt the RAHP assurance-test discipline while remaining separate from protocol conformance claims.

## Decision conformance

The [decision conformance tests](decision-conformance-tests.md) operationalise the governed-context and privacy-class baseline for B1 and B2.
