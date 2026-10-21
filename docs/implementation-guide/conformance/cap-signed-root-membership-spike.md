---
layout: default
title: "CAP Signed-Root Membership Spike"
parent: "Conformance"
nav_order: 54
---

# CAP record 010: experimental membership-root integrity

**Status:** bounded cryptographic feasibility, not a complete CAP construction. **Construction selection:** `not_frozen`.

This experiment tests whether a blinded membership commitment can be checked against an externally supplied and signed community Merkle root, and whether the *same commitment bytes* are constrained by the [experimental authenticated-commitment verifier](cap-authenticated-commitment-spike.md). The separate [hidden-witness Sigma proof](cap-hidden-witness-spike.md) continues to demonstrate equality across authenticated experimental membership, relationship and linkage commitments.

The demonstration uses a domain-separated SHA-256 binary Merkle tree, a signed root assertion with explicit community, scope and epoch, and an explicitly configured Ed25519 verification key. It is intentionally small, with only test fixtures and no real issuers, registry or credential subjects.

## Run

```sh
cd benchmarks/pr-rel-sigma
npm ci --ignore-scripts --no-audit --no-fund
npm test
```

The existing PR-REL cryptographic workflow runs the membership negative cases. These reject an untrusted root signer, root/epoch mismatch, substituted leaf, tampered path direction, altered signed scope and malformed path. A separate regression shows that membership evidence cannot replace the distinct authenticated-commitment binding.

## Assurance boundaries

The experiment verifies **membership inclusion of a published commitment relative to a signed test root**. It does not prove that the test root is authoritative. The key is locally configured, and epoch equality is not proof of real-world freshness, propagation or non-revocation.

Critically, the Merkle path and leaf commitment are disclosed to the verifier. This is **not zero-knowledge membership**, privacy-preserving CAP, or unconditional unlinkability. A single commitment present in a verifier-visible leaf can be a correlator. A Merkle inclusion path also does not prove voucher membership under the *canonical* registry profile, distinct human persons, issuer qualification, personhood or authentic relationship consent. Both issuer credential and registry semantics remain external. These experimental statements are not Credential or Registry serialization proposals.

The test demonstrates only an additional component feasibility condition. It must not advance record 010 to downstream `implemented`, assert X2 interoperability, freeze a construction, or close issue #54.

## Decisive remaining work

The next implementation gate is replacing the disclosed Merkle membership witness with a *privacy-preserving proof* of inclusion against a policy-authorized root, while binding issuer-authenticated relationship evidence, voucher-offline issuance linkage, subject distinctions and complete transcript/status assertions. A key assigned by this test suite cannot stand in for a verifiably authorized Registry operator.

See [construction-selection criteria](cap-construction-selection.md) and [proof-claim non-implication boundaries](proof-claim-boundaries.md).
