---
layout: default
title: "CAP Hidden-Witness Feasibility"
parent: "Conformance"
nav_order: 52
---

# CAP record 010: hidden-witness equality feasibility

**Status:** experimental construction component only. **Full record-010 CAP proof:** not established. **Selection:** not frozen.

This experiment reuses the pinned Ristretto255 group/Fiat–Shamir construction already exercised by [PR-REL](experimental-pr-rel-sigma-profile.md). It proves knowledge of a **single hidden scalar** `m` shared across three independently blinded commitments:

```text
C_member = m*G + r_member*H
C_relation = m*G + r_relation*H
C_link = m*G + r_link*H
```

A Sigma-style proof gives the verifier three announcements, one response for `m`, and independent blinding responses. A Fiat–Shamir challenge binds all three commitments, announcements and the named verifier/application context. The witness `m` and blinds are not transmitted. Repeated proof generation uses fresh random nonces.

The tests deliberately demonstrate rejection after substituting a commitment, changing a hidden value, changing the root/verifier context, or supplying an incomplete proof. Verification does not involve a voucher online. The test uses synthetic scalar values and example context only.

## Reproduce

```sh
cd benchmarks/pr-rel-sigma
npm ci --ignore-scripts --no-audit --no-fund
npm test
```

The existing PR-REL CI workflow runs these tests together with the original relationship proof. The chosen curve library version is already pinned by the benchmark's dependency lock.

## Scope and non-implication

**Cryptographic fact established:** the prover knows an equal hidden scalar opening all three commitments, assuming the discrete-log relation is secure, independent generator derivation and the Fiat–Shamir assumptions. Context and commitment substitution invalidate the proof.

**Not established:** the commitments represent actual VMC/VRC/membership objects, are authenticated by a trusted source, encode a governed record-007 linkage, share a canonical membership-root construction, or express the complete record-010 statement. A hidden scalar equality relation is **not** a membership proof, signature verification, holder binding, status-root validation, non-revocation proof, consent proof, evidence of distinct humans, or full end-to-end CAP proof. The experiment makes no proof-of-knowledge security claim beyond the specified mathematical relation.

No record-010 construction evidence label changes. The experiment is a falsifiable input to the [CAP construction-selection gate](cap-construction-selection.md) and [#54](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/54). The [proof-claim boundary contract](proof-claim-boundaries.md) remains authoritative for prohibited stronger inferences.

## Remaining decisive construction test

Authenticate the actual commitments from issuer/registry-controlled artifacts and prove membership, relationship, voucher-offline linkage and transcript binding as one complete record-010 statement. In particular, the **Credential-owned encoding and authenticated mapping from record-007 identifier/linkage fields to a common hidden scalar** is not supplied here. Without that, a forged set of internally consistent Pedersen commitments can pass this experiment while satisfying no legitimate CAP entitlement. That is a blocking distinction for construction selection, not an implementation detail to suppress.
