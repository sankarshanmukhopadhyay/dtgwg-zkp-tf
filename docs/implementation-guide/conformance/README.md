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
| [`test-matrix.csv`](./test-matrix.csv) | Machine-readable protocol conformance matrix for the established profile corpus |
| [`composed-presentation-test-matrix.csv`](./composed-presentation-test-matrix.csv) | First-class machine-readable semantic conformance matrix for evidence-closure privacy, delegation relationships, confidential binders and external resolution |
| [`test-matrix.md`](./test-matrix.md) | Human-readable view of the established protocol matrix, grouped by level and scenario |
| [`execution-dispositions.csv`](./execution-dispositions.csv) | Governed execution status for every protocol case |
| [`executable-harness.md`](./executable-harness.md) | Harness architecture, adapter boundary and CI isolation |
| [`conformance-decision-backlog.csv`](./conformance-decision-backlog.csv) | Machine-readable blockers for non-executable cases |
| [`fixtures/`](./fixtures/) | Illustrative, non-normative JSON fixtures referenced by established test cases |
| [`composed-presentation-privacy-tests.md`](./composed-presentation-privacy-tests.md) | Human-readable construction-neutral negative semantics for composed-presentation privacy |
| `../../../conformance-harness/examples/composed-presentation-privacy.json` | Executable semantic fixtures corresponding one-to-one with the composed-presentation matrix |
| [`experimental-bbs-2023-construction-profile.md`](./experimental-bbs-2023-construction-profile.md) | Experimental concrete credential-side construction profile using W3C `bbs-2023` |
| [`experimental-bbs-2023-construction-profile.yaml`](./experimental-bbs-2023-construction-profile.yaml) | Machine-readable BBS construction selection, upstream pins and promotion gates |
| [`experimental-pr-rel-sigma-profile.md`](./experimental-pr-rel-sigma-profile.md) | Experimental `PR-REL` equality/relationship proof over authenticated commitments |
| [`experimental-pr-rel-sigma-profile.yaml`](./experimental-pr-rel-sigma-profile.yaml) | Machine-readable Sigma/Fiat-Shamir construction selection and boundaries |
| [`construction-evidence-bbs-2023.json`](./construction-evidence-bbs-2023.json) | Pinned external BBS vector and independent-interoperability evidence record |
| [`construction-coverage-matrix.csv`](./construction-coverage-matrix.csv) | Predicate-by-predicate construction coverage and remaining gates |

Validate the aggregate semantic corpus with:

```sh
python3 scripts/validate_conformance.py
```

and execute the semantic harness with:

```sh
pytest conformance-harness/tests/test_composed_presentation_privacy.py
```

The validator treats `test-matrix.csv` and `composed-presentation-test-matrix.csv` as one conformance corpus. It checks predicate, adversary and scenario traceability, uniqueness of test IDs, level coverage, and one-to-one linkage between the composed matrix and executable fixtures.

## Evidence pipeline

[D-038 — Conformance and Assurance Evidence Pipeline](../diagrams/D-038-conformance-assurance-evidence-pipeline.md) distinguishes internal repository validation, executable semantic/protocol cases, construction evidence, security assurance and cross-implementation evidence. A claim should never imply a stronger evidence layer than was actually executed.

## What conformance validates

Predicate semantics, canonical transcript and encodings, lifecycle and status, cross-vendor interoperability, privacy against named adversaries, constrained devices, fallback and downgrade, and error consistency — see `levels.md` for how these map onto [`CL-1`](../reference/identifier-register.md#cl-1) through [`CL-4`](../reference/identifier-register.md#cl-4).

Privacy conformance applies across the **complete evidence closure** of a verification predicate. A credential or proof that passes standalone selective-disclosure or unlinkability tests does not establish end-to-end privacy when required delegation, status, registry/accreditation, Trust Task or network-resolution evidence introduces an additional correlation surface.

The composed-presentation corpus makes that rule executable before a cryptographic construction is selected. It can deterministically reject undeclared status correlation, unnecessary delegation ancestry, enumerable deterministic binders, unnecessary exact-issuer disclosure, composition-only correlation, undeclared live authoritative lookup and semantic collapse caused by primitive reuse.

## Construction evidence

The repository carries separate deliberately **experimental** construction profiles rather than selecting one proof system for every predicate.

`EXP-BBS-2023-01` selects W3C `bbs-2023` with BLS12-381/SHA-256 for credential-side selective disclosure, unlinkable derived proofs and anonymous holder binding. It pins the W3C 7 April 2026 Candidate Recommendation Draft and an immutable upstream test-vector revision, records external W3C interoperability evidence, and runs a local correctness smoke test plus performance benchmark in CI.

`EXP-PR-REL-SIGMA-01` addresses the separate cross-artifact relationship predicate. It uses a Ristretto255 linear-relation Sigma proof, transformed non-interactively with a context-bound Fiat-Shamir challenge, to prove that two independently authenticated Pedersen-style commitments contain the same hidden scalar. Its CI evidence includes a deterministic positive vector, wrong-value and wrong-context negatives, fresh-proof checks, and proof/verification benchmarks.

Neither profile is treated as a universal construction choice. `construction-coverage-matrix.csv` distinguishes predicates fully or partially covered by each experiment and keeps unsupported construction slots explicit. Cryptographic success MUST NOT silently upgrade an unsupported evidence-closure predicate.

Local benchmark timings are evidence-producing but non-normative: GitHub-hosted runner performance is too variable for hard performance thresholds. Promotion requires representative constrained-device and server-class measurements.

## Minimum plugfest topology

- two issuer implementations;
- two wallet/prover implementations;
- two verifiers;
- registry and policy fixtures;
- positive, negative, malformed, lifecycle and privacy tests from the aggregate conformance corpus.

This matches [`UC-030`](../reference/identifier-register.md#uc-030), whose independent-implementation evidence remains the exit criterion for the strongest interoperability claim.

For `EXP-BBS-2023-01`, external independent implementation evidence is sourced from the W3C BBS interoperability report rather than synthesized from two local adapters. This can support claims about the BBS features actually covered by that report.

For `EXP-PR-REL-SIGMA-01`, the exact DTG relationship statement, transcript binding and serialization still require independent implementation interoperability before the profile can move beyond experimental status. Local independent code paths are not counted as independent implementations.

## What this suite is, and is not

This suite defines **expected behaviour** for a conformant implementation. The semantic layer is executable now, and concrete construction experiments are executable for credential-side BBS capabilities and the `PR-REL` equality-of-committed-value predicate.

The evidence layers are intentionally separate:

1. **semantic conformance** — deterministic fixtures and policy/evidence-closure logic;
2. **construction conformance** — construction-specific vectors, smoke tests, benchmarks and soundness-relevant behaviour;
3. **interoperability evidence** — agreement across independently maintained implementations and plugfest evidence.

Passing semantic tests does not establish cryptographic soundness. Conversely, a mathematically valid proof cannot rescue a profile that fails the semantic privacy boundary.

## Known gaps

- 11 P1/P2 scenarios remain outside the four-level profile assignment and are tracked in `matrices/maturity-map.csv`.
- No DTG-specific cross-vendor plugfest ([`UC-030`](../reference/identifier-register.md#uc-030)) has run; the strongest end-to-end DTG interoperability claim therefore remains unavailable.
- `EXP-BBS-2023-01` closes a concrete credential-side selective-disclosure/unlinkability track.
- `EXP-PR-REL-SIGMA-01` closes the first executable construction slot for [`PR-REL`](../reference/identifier-register.md#pr-rel), subject to independent implementation evidence and governed value-encoding profiles.
- [`PR-HID`](../reference/identifier-register.md#pr-hid) remains the next explicit construction slot for low-entropy/confidential binders.
- [`PR-RES`](../reference/identifier-register.md#pr-res) remains a profile/architecture selection problem: stronger privacy profiles still need a carried, cached or privacy-preserving state mechanism rather than an undeclared verifier-originated lookup.
- [`PR-DEL`](../reference/identifier-register.md#pr-del) is only partially covered: relationship proof over committed authority inputs does not itself establish delegation scope, lifecycle, ancestry semantics or governance authorization.

The previous taxonomy gap for delegation evidence is closed: `PR-DEL` expresses current delegated authority and `PR-REL` expresses the separately testable cross-artifact relationship.

## Evidence packaging

Use the implementation and profile statement templates and the JSON schemas in `schemas/` to produce portable evidence. A conformance claim identifies a level, profile, source revision, environment, fixture digests, results and exceptions.

For composed predicates, the evidence bundle also identifies the minimum evidence closure, cross-artifact relationship inputs, verifier-originated external observations, declared adversary and privacy horizon, and the executed composed-presentation fixture cases.

For construction-specific claims, include the construction profile identifier, upstream specification/vector revision where applicable, local test/benchmark artifact, and provenance of independent interoperability evidence.

## Security assurance

- [Security assurance tests](security-assurance-tests.md)
- `security-assurance-test-matrix.csv`
- `schemas/security-assurance-result.schema.json`
- `schemas/security-metric-evidence.schema.json`

These artefacts adapt the RAHP assurance-test discipline while remaining separate from protocol conformance claims.

## Decision conformance

The [decision conformance tests](decision-conformance-tests.md) operationalise the governed-context and privacy-class baseline for B1 and B2.
