---
layout: default
title: "Experimental PR-HID Hiding-Binder Profile"
parent: "Conformance"
nav_order: 15
---
# Experimental PR-HID hiding-binder profile

**Status:** Experimental / non-normative

`EXP-PR-HID-PEDERSEN-01` pressure-tests a concrete confidential binder for low-entropy or feasibly enumerable values. It is downstream of the construction-neutral requirement in `PR-HID`; it does not alter that predicate's semantics.

## Construction

The profile uses a Ristretto255 Pedersen-style commitment:

```text
m = hash_to_scalar(domain || context || value)
C = m*G + r*H
```

where `r` is sampled independently from a cryptographically secure random source for every commitment and `H` is a profile-specific independently derived group point.

The value-to-scalar encoding is domain-separated. The encoding does **not** supply confidentiality by itself; confidentiality against dictionary enumeration comes from the fresh blinding scalar.

## Why deterministic hashing is insufficient

A digest of a low-entropy vocabulary value can be compared against every candidate in the vocabulary. The executable evidence includes a deliberately enumerable scope vocabulary and verifies that a deterministic SHA-256 binder can be recovered by dictionary enumeration.

The same test then verifies that two independently blinded commitments to the same enumerable value are distinct at the commitment layer.

This establishes the intended requirements distinction:

> integrity binding is not the same property as confidential binding.

## Required properties

A profile-conformant commitment:

- MUST use fresh cryptographically random blinding for each independently exposed commitment;
- MUST domain-separate value encoding by predicate/application context;
- MUST reject an opening with the wrong value;
- MUST reject an opening with the wrong blinding scalar;
- MUST NOT treat a deterministic digest of an enumerable value as a confidential commitment;
- MUST NOT reuse the commitment as a durable cross-context identifier; and
- MUST authenticate the commitment through the source artifact or an independently authenticated proof input before relying on it.

## Relationship to `PR-REL`

`PR-HID` answers **how a value can be committed without exposing an enumerable plaintext**. `PR-REL` answers **how a relationship between independently authenticated hidden values can be proven**.

The two predicates may use compatible commitment representations, but one does not imply the other. A verifier MUST NOT infer equality merely because it receives two commitments, and a successful equality proof MUST NOT substitute for authentication of either commitment.

## Executable evidence

`benchmarks/pr-hid-pedersen/hiding-binder.mjs` provides:

- valid-opening verification;
- wrong-value rejection;
- wrong-blinding rejection;
- two fresh commitments to the same value that are distinct;
- a deterministic-digest dictionary-enumeration regression; and
- commitment/opening performance measurements.

The CI workflow uploads the deterministic vector and benchmark JSON as construction evidence.

## Limits

This experiment does not define a canonical encoding for every possible DTG data type. Profiles using structured or externally defined values still need canonical value semantics before hashing to a scalar.

Pedersen-style commitments are not authenticated objects. Authentication remains an artifact/interface responsibility.

This profile also does not establish `PR-RES`, registry semantics, status freshness, delegation validity or arbitrary range/set predicates.

## Promotion gate

Promotion requires governed agreement on value canonicalization, domain separation, randomness requirements, supported implementation environments, negative vectors, and independent interoperability for the exact serialization claimed by the profile.
