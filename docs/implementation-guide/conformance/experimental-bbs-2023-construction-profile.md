---
layout: default
title: "Experimental BBS 2023 Construction Profile"
parent: "Conformance"
nav_order: 13
---
# Experimental BBS 2023 construction profile

**Status:** Experimental / non-normative

This profile selects a concrete construction for the credential-side selective-disclosure and unlinkability portion of the v0.4 work without making that construction mandatory for DTG.

The selected construction is the W3C Data Integrity BBS Cryptosuites v1.0 `bbs-2023` cryptosuite, using the BLS12-381 SHA-256 ciphersuite. The profile is pinned to the 7 April 2026 Candidate Recommendation Draft and the corresponding W3C test-vector repository revision recorded in `experimental-bbs-2023-construction-profile.yaml`.

## Why this profile exists

The requirements and semantic conformance layers deliberately remain construction-neutral. A construction profile is therefore an implementation experiment: it demonstrates which requirements a real construction can satisfy, records test-vector and interoperability evidence, measures implementation cost, and leaves unsupported predicates visible rather than weakening them silently.

## Selected construction

| Property | Selection |
|---|---|
| Credential proof format | W3C Data Integrity `DataIntegrityProof` |
| Cryptosuite | `bbs-2023` |
| Signature/proof scheme | BBS signatures / derived proofs |
| Curve | BLS12-381 |
| Hash variant | SHA-256 |
| VC canonicalisation | As defined by the pinned W3C BBS cryptosuite |
| Holder binding | W3C anonymous-holder-binding feature where the governing profile requires it |
| Pseudonym feature | Optional and profile-governed; not enabled as a global correlator |

## Predicate coverage

Construction selection does not imply that every predicate is solved by one cryptosuite.

| Predicate | Construction status | Notes |
|---|---|---|
| `PR-CMP` | **partially supported** | BBS derived proofs can avoid cryptographic linkage between repeated selective-disclosure presentations, but evidence-closure privacy still depends on surrounding status, delegation, registry and protocol evidence. |
| `PR-HLD` | **supported for the BBS credential layer** | Uses the anonymous holder-binding feature when required by the profile. |
| `PR-ISS` | **supported with caveat** | Signature validity is supported; proving only membership in an acceptable issuer set without revealing the exact issuer is a separate predicate/construction problem. |
| `PR-DEL` | **partially supported** | A delegation credential can selectively disclose bounded authority fields, but BBS alone does not prove arbitrary delegation ancestry or cross-artifact authority relationships in zero knowledge. |
| `PR-REL` | **not closed by BBS alone** | Cross-artifact relationship proofs need an additional composition construction or a data model that places the required relation inside one authenticated proof domain. |
| `PR-HID` | **not closed by deterministic digesting** | BBS can hide signed messages in a derived proof, but a separate confidential commitment/binder requirement must select an appropriate hiding construction where a binder is independently exposed. |
| `PR-RES` | **architecture/profile property** | BBS does not itself solve private status/registry resolution. The governing profile must use carried/cached/privacy-preserving evidence or explicitly declare live-lookup correlation. |

This table is intentionally conservative. A profile MUST NOT upgrade `partially supported` or `not closed` to `supported` merely because the BBS proof verifies cryptographically.

## Test-vector evidence

The profile consumes the published W3C BBS test vectors by immutable upstream revision rather than copying them and allowing them to drift. The pinned revision is recorded in the machine-readable profile.

The W3C vector set includes baseline proof generation/verification as well as optional holder-binding and pseudonym material. The repository treats those vectors as **construction evidence**, distinct from the local `CP-PRIV-*` semantic fixtures.

## Independent interoperability evidence

Independent implementation evidence is sourced from the W3C Data Integrity BBS interoperability report rather than manufactured inside this repository. The report dated 2 August 2026 records multiple independent issuer and verifier implementations and cross-implementation results.

This repository may cite that report as external construction evidence. It MUST NOT describe two local adapters, two code paths, or two wrappers maintained here as independent implementations.

## Local benchmark evidence

`benchmarks/bbs-2023/benchmark.mjs` measures the foundational BBS operations used by this profile:

1. key generation;
2. multi-message signing;
3. signature verification;
4. unlinkable proof derivation; and
5. proof verification.

The benchmark verifies correctness before recording timings. CI uploads the JSON result as evidence, but timing values are informational because GitHub-hosted runner performance is not stable enough for hard conformance thresholds.

## Conformance rule

A claim using this experimental profile MUST identify three evidence layers separately:

1. **semantic conformance** — the local construction-neutral predicate and `CP-PRIV-*` results;
2. **construction conformance** — the pinned BBS specification/vector evidence and local cryptographic smoke/benchmark run; and
3. **independent interoperability** — external evidence from independently maintained implementations.

Passing the construction layer MUST NOT cause an unsupported evidence-closure predicate to be reported as satisfied.

## Exit criteria for promotion

Promotion from experimental to a recommended profile would require, at minimum:

- the governing group to affirm the construction choice;
- all required predicates to have explicit construction coverage or an explicit profile exclusion;
- current upstream BBS specification status to be reviewed;
- vector compatibility to remain green against the pinned or intentionally updated revision;
- benchmark evidence on representative constrained and server-class environments; and
- independent interoperability evidence covering the features this profile actually claims.

Until those conditions are met, this profile is a pressure-test implementation, not a DTG-wide construction mandate.
