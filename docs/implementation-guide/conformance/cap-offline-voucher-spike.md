---
layout: default
title: "CAP Offline Voucher Feasibility Spike"
parent: "Conformance"
nav_order: 51
---

# Record 010 feasibility: signed, bound issuance receipts

**Disposition: partial feasibility evidence; full CAP construction not established.**

This deliberately small experiment tests **one** necessary property for [record 010](record-010-community-anchored-proof.md): a holder can present issuance-time voucher linkage and membership receipts without involving the voucher during verification. It evaluates the hybrid-bound-receipt option in the [construction selection register](cap-construction-selection.md), but **does not select or freeze** that option.

## Execute

```sh
python3 -m pip install cryptography pytest
python3 -m pytest -q scripts/tests/test_cap_offline_spike.py
```

The experiment signs two separate domain-separated, canonically serialized ASCII statements using Ed25519: a membership receipt and an issuance-time linkage receipt. Verification requires both signatures, identical community root, voucher, holder and transcript fields, an expected request context, and different holder/voucher identifiers. Signing and verifying keys are generated locally in tests. No voucher process or private voucher key is needed at verification.

The positive outcome is **`RECEIPTS_CONSISTENT_ONLY`**, not `PASS` or `CAP_VERIFIED`. Negative tests cover swapped voucher, mismatched root, replayed context, signature tampering, wrong verification key, self-vouching, unsupported encoding and swapped receipt roles.

## Security and assurance boundary

This experiment uses genuine cryptographic signatures, but **the signed statements disclose identifiers and therefore do not satisfy CAP privacy requirements or constitute a zero-knowledge proof**. The two receipt signers are local test roles, not externally authoritative issuers. The verifier assumes trusted public keys; it does not authenticate community recognition, key lifecycle, credential issuance, registry status, freshness or revocation. Signature validity alone does not prove a membership path, hidden co-control, or jointly constrained private witnesses. Matching cleartext fields is **not** cryptographic proof of hidden-witness equality.

Consequently, the following gates remain **open**: P1–P5 privacy/non-correlation, S1/S2 cryptographic proof correspondence (including true witness equality), C1–C4 status/currentness, T1–T4 authority and governance, D1–D3 CAP proof measurements, X1–X3 actual CAP vectors and independent interoperability.

A successful execution supports only the narrower proposition that issuance-time, signed cleartext linkage receipts can be validated with the voucher offline and that this particular verifier can detect certain substitutions and context mismatches. It is insufficient to choose a construction or change any record-010 evidence-promotion label.

## Next experiment / rejection condition

Demonstrate a **privacy-preserving** joint proof of voucher membership and the required relationship against authenticated credential and registry evidence, including an explicit route for the Credential-owned record-007 linkage representation. Prove shared witness consistency without transmitting voucher or holder identifiers in cleartext; subject the resulting transcript to negative substitution and replay vectors. If no candidate can meet those obligations under pinned upstream semantics, record the blocker rather than treating bound signed receipts as a functional substitute.

Related: [#54](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/54), [#67](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/67).
