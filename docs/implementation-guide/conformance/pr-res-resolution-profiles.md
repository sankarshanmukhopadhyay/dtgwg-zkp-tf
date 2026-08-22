---
layout: default
title: "PR-RES Resolution Profiles"
parent: "Conformance"
nav_order: 16
---
# PR-RES resolution profiles

**Status:** Experimental / non-normative

`PR-RES` is intentionally modeled as a profile/architecture property rather than one universal cryptographic construction. Different deployments have different freshness, availability and privacy requirements, and forcing one status or registry mechanism would collapse those distinctions.

This document defines three explicit experimental profiles.

## `RES-BSL-CACHE-01` — shared cached Bitstring Status List

For VC credential-status semantics where W3C Bitstring Status List v1.0 is applicable, this profile uses a shared status list rather than a credential-specific status endpoint.

The W3C Recommendation was published on 15 May 2025 and is explicitly designed to reduce the privacy problems associated with one-credential/one-URL status checking. It also makes clear that group size, request origin and access patterns can still create correlation risk. The profile therefore claims **reduced correlation**, not perfect anonymity.

Requirements:

- retrieve or distribute the whole shared list rather than query the authority by subject or credential identifier;
- validate the status-list credential and applicable status purpose;
- enforce a governed cache/freshness horizon;
- fail closed when the cached evidence is outside that horizon unless a separate degraded-mode profile is explicitly selected;
- do not treat status semantics as equivalent to registry membership, accreditation or authorization merely because a similar set representation could encode them.

## `RES-CARRIED-SNAPSHOT-01` — holder-carried authenticated snapshot

This profile permits an authenticated state snapshot to be carried with the presentation or obtained through a privacy-preserving cache/distribution layer before verification.

The verifier performs no authoritative network interaction during the verification event. The snapshot must identify its semantic type, policy/version and freshness information, and the verifier must validate authenticity and evidence binding.

This is a profile pattern, not a claim that one snapshot serialization is standardized for every DTG predicate.

## `RES-LIVE-DECLARED-01` — explicitly declared live lookup

Some deployments may require current authoritative state that cannot be supplied through a sufficiently fresh cache or carried snapshot.

This profile permits live authoritative lookup only when governance explicitly allows it. Because the authority can observe the verification event, the privacy profile must declare that degradation. A verifier using this profile cannot simultaneously claim that verification is unobservable to the authoritative service.

The existence of this profile is deliberate: `PR-RES` does **not** impose an absolute prohibition on live lookup. It makes the privacy consequence explicit and testable.

## Freshness and fallback

Freshness is part of the trust decision, not merely a transport optimization.

For cached/carried profiles, evidence outside the governed freshness horizon fails closed unless a separately declared fallback profile applies. A silent transition from cached/carried evidence to live authoritative lookup is a conformance failure because it changes the privacy boundary without changing the declared profile.

## Semantic separation

Status, registry membership, accreditation, anchoring and authorization can sometimes reuse a list, tree, accumulator or membership-proof primitive. They remain different predicates with different authorities, lifecycle rules, freshness needs and failure semantics.

**Same proof primitive does not mean same semantic primitive.**

## Executable evidence

`conformance-harness/examples/pr-res-profiles.json` and `conformance-harness/tests/test_pr_res_profiles.py` exercise:

- fresh cached shared-list evidence;
- stale cached evidence;
- subject-specific authoritative lookup under a cache profile;
- fresh carried snapshot evidence;
- stale carried snapshot evidence;
- undeclared live fallback;
- governed/declaration-complete live lookup; and
- semantic collapse across otherwise similar set representations.

These tests establish profile behavior. They do not claim cryptographic soundness for a future accumulator, Merkle proof or snapshot signature format.

## Promotion gate

Promotion of any `PR-RES` profile requires deployment/governance agreement on freshness horizons, authoritative provenance, failure behavior, privacy claims and interoperability evidence for the exact mechanism being claimed.
