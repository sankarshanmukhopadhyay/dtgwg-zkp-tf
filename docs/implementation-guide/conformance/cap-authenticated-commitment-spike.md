---
layout: default
title: "CAP Authenticated Commitment Boundary"
parent: "Conformance"
nav_order: 53
---

# CAP record 010: authenticated-commitment feasibility

**Status: experimental integration spike; complete CAP implementation not established.**

This increment extends the [hidden-witness experiment](cap-hidden-witness-spike.md) with a deliberately *experimental* Ed25519-signed commitment envelope for each of three roles: membership, relationship and linkage. It validates signature integrity and issuer-key configuration **before** evaluating the existing Ristretto255 proof that those commitments encode the same hidden scalar.

An envelope binds the exact Ristretto255 commitment bytes, a named role, issuer identifier, community-root identifier and scope. Verification must match the signature to an **explicitly supplied** trusted public key, compare signed commitment bytes and expected root/scope, and only then check the context-bound hidden-equality proof. The positive disposition is `AUTHENTICATED_COMMITMENTS_AND_EQUALITY_ONLY`, not `CAP_VERIFIED`.

## Run

```sh
cd benchmarks/pr-rel-sigma
npm ci --ignore-scripts --no-audit --no-fund
npm test
```

Negative tests cover forged envelopes, substituted public keys, commitment swaps, signed/unsigned field mutation, conflicting roots, cross-verifier transcript replay and changed evidence roles. All keys and identities in tests are synthetic and local. The existing PR-REL workflow runs the tests.

## Assurance and authority boundary

The envelope is **not** a Credential specification or canonical record-007 encoding; its schema is intentionally private to this feasibility experiment. Configuring a public key in the test verifier is **not** evidence that the issuer has any authority to issue VMC/VRC or membership evidence. Signatures authenticate bytes under assumed keys, not their real-world origin, source governance, qualification, or lifecycle.

This experiment **does not** prove a Merkle membership path, authenticate a Registry snapshot, validate non-revocation/freshness, establish two distinct persons or model the full CAP relationship statement. The signed metadata itself may be correlatable; there is **no unlinkability claim**. The equality proof also assumes all three input artifacts encode the same governed private value, which the upstream Credential profile does not yet establish.

The verifier-side acceptance of all three signatures and a hidden-scalar equality relation therefore supplies only a **necessary component feasibility observation**, not a sufficient CAP proof.

## Next gate

Replace synthetic issuer/trust inputs and generic hidden-scalar encoding with a pinned, independently interpretable Credential/Registry statement contract. Demonstrate the record-010 membership/relationship witness paths, voucher-offline eligibility, revocation/status, and privacy of the complete evidence closure. Record exact interoperability, non-implication and performance evidence before any construction selection can be frozen.

The [construction selection](cap-construction-selection.md) remains `not_frozen`. [#54](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/54) stays open.
