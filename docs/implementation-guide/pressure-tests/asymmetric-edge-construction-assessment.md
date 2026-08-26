---
layout: default
title: "Pressure Test — Asymmetric Edge Construction Assessment"
parent: "Cross-Specification Pressure Tests"
nav_order: 9
---
# Asymmetric edge construction assessment

**Status:** Experimental evidence note  
**Tracks:** [#13](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/13)

## Purpose

This note exercises the existing experimental construction families against the asymmetric cross-community relationship edge without promoting any experimental profile to normative status.

The pressure test asks a narrower question than “does the proof verify?”: which privacy property can each construction help support when one reciprocal relationship half is deliberately public/correlatable and the other is pairwise/private?

## Construction-family assessment

| Construction/profile family | Relevant contribution | Visible/reusable values to inspect | What it can support | What it cannot establish by itself |
| --- | --- | --- | --- | --- |
| BBS experimental profile | selective disclosure / proof of credential statements | issuer/public parameters, disclosed messages, proof transcript | hiding credential fields while proving supported statements | reciprocal-edge semantics, relationship-level unlinkability, VTN policy, contextual privacy |
| `PR-REL` experimental relation profile | prove a specified relation between hidden values or credential statements | relation public inputs, transcript, any relation tag/binder | private-half binding if the exact semantic relation is defined | a missing Credential-spec definition of the relationship or common trust context |
| `PR-HID` experimental hiding profile | hide a binder/value with a commitment-style construction | commitment parameters, commitment/transcript values | prevent direct disclosure of a private identifier when entropy/randomisation assumptions hold | privacy if the committed value is low-entropy/enumerable or the same commitment/binder is reused across contexts |
| `PR-RES` resolution/currentness profiles | bind proof verification to resolution/status/freshness evidence | registry state, status inputs, resolution observations | currentness evidence with an explicitly bounded correlation surface | policy recognition, common VTN anchoring, or privacy of a live lookup unless the deployment supplies it |
| `PR-CMP` composition | combine predicates into one presentation result | transcript/public inputs across all composed predicates | enforce a scoped composed-presentation contract | erase correlation already introduced by a public half, registry lookup, transport metadata, or graph context |

## Required construction evidence

For an asymmetric-edge implementation, evidence must state:

- the exact semantic relation proven by `PR-REL` or equivalent;
- whether a hiding binder/commitment is deterministic or randomised;
- whether any binder, commitment, issuer handle, registry reference, or transcript field repeats across verifier contexts;
- which reciprocal half is intentionally public/correlatable;
- what the verifier learns from proof material alone;
- what a verifier can infer after joining public/community graph information;
- which registry/VTN facts are separately evidenced; and
- the strongest privacy claim supported at each subject level: identifier, credential half, relationship, presentation, contextual graph.

## Findings

### BBS/selective disclosure

Selective disclosure can prevent direct disclosure of the private half's fields, but that is only credential-half protection. It does not make a public reciprocal half disappear and therefore cannot justify a global relationship-unlinkability claim.

### PR-REL

`PR-REL` is a suitable candidate responsibility for binding reciprocal statements **only if** the relationship semantic is already defined by the owning Credential layer. The proof must not solve semantic ambiguity by introducing a common durable identifier purely for implementation convenience.

### PR-HID

`PR-HID` can hide the private-side binder, but hiding is insufficient if the binder or its commitment is stable and reusable across unrelated presentations. A low-entropy deterministic digest is also not treated as confidential proof input.

### PR-RES

`PR-RES` highlights the registry seam: a cryptographically correct relationship proof can still acquire a broader effective correlation scope through live status/resolution observations. Common VTN anchoring or cross-VTN policy acceptance remains a separate trust-policy claim.

### PR-CMP

Composition is the point where privacy claims must be scoped. A composed proof may PASS private-half non-disclosure while FAILING or constraining relationship-/context-level unlinkability because of the deliberately public half or external graph data.

## Executable evidence

The pressure test is represented in two layers:

- `conformance-harness/examples/asymmetric-edge-privacy.json` provides dedicated semantic cases; and
- `conformance-harness/examples/composed-presentation-privacy.json` plus `docs/implementation-guide/conformance/composed-presentation-test-matrix.csv` integrate the cases into the aggregate composed-presentation conformance suite.

The integrated cases include positive evidence for scoped private-half protection and negative/indeterminate evidence preventing unsupported relationship, contextual, cross-context, and common-VTN claims.

## Cross-specification boundary record

The pressure test intentionally leaves these questions to their owning layers:

- identifier/correlation vocabulary in the Credential specification;
- normative reciprocal-edge semantics;
- which VTN or governance framework governs an asymmetric relationship;
- policy discovery between communities;
- Trust Task semantics not already defined; and
- deployment-specific graph visibility.

The ZKP result reports what was proved and the scoped privacy properties of the construction. DPIP remains the appropriate layer for evaluating the effective composed-interaction privacy claim.