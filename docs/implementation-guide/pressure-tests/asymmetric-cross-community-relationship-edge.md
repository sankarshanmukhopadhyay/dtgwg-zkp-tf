---
layout: default
title: "Pressure Test — Asymmetric Cross-Community Relationship Edge"
parent: "Cross-Specification Pressure Tests"
nav_order: 8
---
# Asymmetric cross-community relationship edge

Status: experimental pressure test  
Tracks: [#13](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/13)

## Purpose

This pressure test asks what privacy claim a verifier may legitimately infer when the two reciprocal halves of a DTG relationship intentionally have different correlation postures.

It does **not** define a new Credential-spec identifier taxonomy, a VTN policy model, or a new proof construction. Those remain owned by their respective specifications and deployment profiles.

## Scenario

- `half-a` is deliberately public or correlatable.
- `half-b` uses a pairwise/private identifier.
- both relationship artifacts are authentic;
- a verifier needs evidence of the required relationship predicate;
- the proof must not expose more about `half-b` than the predicate requires.

The test distinguishes five privacy subjects:

1. identifier-level privacy;
2. credential-half privacy;
3. relationship-level privacy;
4. presentation-level privacy; and
5. contextual/graph privacy.

A proof can protect `half-b` while the relationship remains correlatable because `half-a` or surrounding graph information is public. Accordingly, `unlinkable` is never treated as an unscoped Boolean property in this pressure test.

## Required claims and boundaries

A conforming experimental implementation of this pressure test:

- MUST identify the subject and scope of every privacy claim;
- MUST NOT infer relationship-level or contextual unlinkability from proof-level hiding alone;
- MUST NOT introduce a reusable cross-context binder for the private half when a less correlatable relation can establish the required predicate;
- MUST distinguish declared, observable, and effective correlation scope;
- MUST record residual graph/context correlation separately from cryptographic proof properties; and
- MUST NOT treat proof verification as evidence of common VTN anchoring, cross-VTN policy acceptance, or DTG-edge conformance without separate evidence.

## Verification-context variants

| Variant | Context | Expected treatment |
| --- | --- | --- |
| `AE-V1` | both halves anchored in the same VTN | common anchoring requires separate evidence |
| `AE-V2` | halves anchored in different VTNs | proof validity does not imply cross-VTN policy acceptance |
| `AE-V3` | one half anchored, one intentionally unanchored | higher-level edge/trust claim remains indeterminate without owning-layer evidence |

## Executable cases

The machine-readable cases are in `conformance-harness/examples/asymmetric-edge-privacy.json` and are exercised by `test_asymmetric_edge_privacy.py`.

The cases deliberately separate cryptographic validity from the privacy claim asserted:

- private half hidden + public half exposed: private-half non-disclosure can pass while relationship unlinkability fails;
- a reusable binder defeats cross-context unlinkability even if the underlying proof verifies;
- public graph composition constrains presentation/contextual unlinkability;
- proof validity cannot establish a VTN or policy fact that was never proved;
- both halves privately proven without a reusable correlator is only a candidate for a stronger composed claim and still depends on deployment evidence.

## Construction implications

`PR-REL` is the natural existing predicate family to exercise for relationship binding. `PR-HID` may be used where a hiding binder is required, and `PR-RES` applies where resolution/currentness participates in the presentation. None of those profile names changes the semantic boundary above.

The construction must state exactly what relation is proved: hidden-value equality, reciprocal credential binding, common relationship context, common task/exchange context, or another predicate. A missing Credential-spec semantic is recorded as a dependency rather than invented here.

## DPIP hand-off

The composed privacy result is intentionally consumable by DPIP. DPIP's existing `C3` asymmetric cross-community relationship scenario evaluates the interaction-level and contextual consequences that remain outside proof validity.

The ZKP conformance evidence therefore reports scoped proof properties; it does not claim end-to-end relationship privacy.
