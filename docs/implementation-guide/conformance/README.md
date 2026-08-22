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
| [`levels.md`](./levels.md) | Formal definition of conformance levels [`CL-1`](../reference/identifier-register.md#cl-1) through [`CL-4`](../reference/identifier-register.md#cl-4) |
| [`test-matrix.csv`](./test-matrix.csv) | Machine-readable protocol conformance matrix for the established profile corpus |
| [`composed-presentation-test-matrix.csv`](./composed-presentation-test-matrix.csv) | Machine-readable semantic conformance matrix for evidence-closure privacy |
| [`composed-presentation-privacy-tests.md`](./composed-presentation-privacy-tests.md) | Human-readable construction-neutral negative semantics |
| [`experimental-bbs-2023-construction-profile.md`](./experimental-bbs-2023-construction-profile.md) | Experimental credential-side W3C `bbs-2023` construction profile |
| [`experimental-pr-rel-sigma-profile.md`](./experimental-pr-rel-sigma-profile.md) | Experimental `PR-REL` hidden-equality proof profile |
| [`experimental-pr-hid-pedersen-profile.md`](./experimental-pr-hid-pedersen-profile.md) | Experimental `PR-HID` confidential binder for low-entropy/enumerable values |
| [`pr-res-resolution-profiles.md`](./pr-res-resolution-profiles.md) | Explicit `PR-RES` cached/carried/live resolution profiles and privacy boundaries |
| [`pr-res-resolution-profiles.yaml`](./pr-res-resolution-profiles.yaml) | Machine-readable `PR-RES` profile choices, freshness and privacy properties |
| [`construction-coverage-matrix.csv`](./construction-coverage-matrix.csv) | Predicate-by-predicate construction/profile coverage and remaining gates |

Validate the aggregate semantic corpus with:

```sh
python3 scripts/validate_conformance.py
pytest conformance-harness/tests
```

## Evidence pipeline

[D-038 — Conformance and Assurance Evidence Pipeline](../diagrams/D-038-conformance-assurance-evidence-pipeline.md) distinguishes internal repository validation, executable semantic/protocol cases, construction evidence, security assurance and cross-implementation evidence. A claim should never imply a stronger evidence layer than was actually executed.

## Construction and profile evidence

The repository carries separate deliberately **experimental** choices rather than selecting one proof system or one resolution architecture for every predicate.

- `EXP-BBS-2023-01` covers credential-side selective disclosure, unlinkable derived proofs and anonymous holder binding with W3C `bbs-2023`.
- `EXP-PR-REL-SIGMA-01` proves equality of a hidden scalar across two independently authenticated commitments without disclosing the scalar.
- `EXP-PR-HID-PEDERSEN-01` provides a randomized confidential binder for low-entropy/enumerable values and includes an executable regression demonstrating why deterministic hashing is not confidential binding.
- `PR-RES` is represented by explicit resolution profiles rather than a universal cryptographic primitive: shared cached W3C Bitstring Status List evidence where applicable, authenticated carried/cached snapshots, and a separately governed live-lookup profile that declares privacy degradation.

The profiles are semantically distinct even when their implementations can reuse proof or set-membership machinery. A hiding commitment does not prove a relationship; a relationship proof does not authenticate source artifacts; and a set representation does not make status, registry membership, accreditation and authorization equivalent predicates.

`construction-coverage-matrix.csv` keeps partial support and promotion gates explicit. Cryptographic success MUST NOT silently upgrade an unsupported evidence-closure predicate.

Local benchmark timings are evidence-producing but non-normative: hosted-runner timing is too variable for hard performance thresholds.

## `PR-RES` privacy/freshness rule

A strong privacy profile can verify using sufficiently fresh carried/cached evidence without a verifier-originated subject-specific authoritative lookup. If governance requires a live authoritative lookup, the profile must say so and must declare that the authority can observe the verification event.

A silent fallback from cached/carried evidence to live lookup is a conformance failure because it changes the evidence closure and privacy boundary without changing the declared profile.

## Minimum plugfest topology

- two issuer implementations;
- two wallet/prover implementations;
- two verifiers;
- registry and policy fixtures;
- positive, negative, malformed, lifecycle and privacy tests from the aggregate conformance corpus.

This matches [`UC-030`](../reference/identifier-register.md#uc-030). Local independent code paths are not counted as independent implementations.

## Evidence layers

1. **semantic conformance** — deterministic fixtures and policy/evidence-closure logic;
2. **construction/profile conformance** — construction-specific vectors, profile behavior, freshness/fallback tests, benchmarks and soundness-relevant behaviour;
3. **interoperability evidence** — agreement across independently maintained implementations and plugfest evidence.

Passing semantic tests does not establish cryptographic soundness. Conversely, a mathematically valid proof cannot rescue a profile that fails the semantic privacy boundary.

## Known gaps

- No DTG-specific cross-vendor plugfest has run; the strongest end-to-end DTG interoperability claim therefore remains unavailable.
- `EXP-PR-HID-PEDERSEN-01` supplies an executable `PR-HID` construction experiment, subject to governed canonical value encoding and independent interoperability evidence.
- `PR-RES` now has explicit executable profile choices; individual profile promotion still requires governed freshness horizons, exact mechanism/serialization choices and interoperability evidence.
- [`PR-DEL`](../reference/identifier-register.md#pr-del) remains semantically separate: commitment and relationship proofs do not establish delegation scope, lifecycle, ancestry semantics or governance authorization.

## Evidence packaging

A construction/profile claim should include the profile identifier, source/specification revision where applicable, local test/benchmark evidence, fixture digests, environment, freshness horizon, privacy degradation flags and provenance of independent interoperability evidence.

For composed predicates, evidence also identifies the minimum evidence closure, relationship inputs, external observations, adversary and privacy horizon.

## Security assurance

- [Security assurance tests](security-assurance-tests.md)
- `security-assurance-test-matrix.csv`
- `schemas/security-assurance-result.schema.json`
- `schemas/security-metric-evidence.schema.json`

## Decision conformance

The [decision conformance tests](decision-conformance-tests.md) operationalise the governed-context and privacy-class baseline for B1 and B2.
