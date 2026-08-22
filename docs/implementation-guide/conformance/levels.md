---
layout: default
title: "Conformance levels"
parent: "Conformance"
grand_parent: "Implementation Guide"
nav_order: 3
has_toc: true
---
# Conformance levels

**Status:** Incubating
**Normative status:** Non-normative unless promoted into the Working Draft

## Purpose

A profile or implementation claims a conformance level, not "conformance" in
general. Each level names the predicates it requires, the scenarios it must
pass, and the readiness gates (see
[`../scenarios/pressure-test-use-case-corpus.md`](../scenarios/pressure-test-use-case-corpus.md#10-readiness-gates))
it is expected to satisfy. Levels are cumulative: a [`CL-2`](../reference/identifier-register.md#cl-2) claim presumes [`CL-1`](../reference/identifier-register.md#cl-1)
passes.

Every test case referenced below lives in
[`test-matrix.csv`](./test-matrix.csv) and is summarised in
[`test-matrix.md`](./test-matrix.md).

## CL-1 — Minimum Liveness Profile

**Claim:** the implementation can produce and verify a fresh, holder-bound
liveness proof, and degrade or fall back on constrained devices without
silently weakening the adversary model.

| | |
|---|---|
| Predicates | [`PR-LIV`](../reference/identifier-register.md#pr-liv), [`PR-HLD`](../reference/identifier-register.md#pr-hld), [`PR-FRE`](../reference/identifier-register.md#pr-fre) |
| Scenarios | [`UC-004`](../reference/identifier-register.md#uc-004), [`UC-006`](../reference/identifier-register.md#uc-006), [`UC-017`](../reference/identifier-register.md#uc-017), [`UC-020`](../reference/identifier-register.md#uc-020), [`UC-021`](../reference/identifier-register.md#uc-021) |
| Primary gates | Gate A (predicate clarity), Gate F (operational viability) |
| Test count | 20 (10 positive / 10 negative) |

[`CL-1`](../reference/identifier-register.md#cl-1) does **not** require personhood, uniqueness, delegation, or federated
issuer accreditation. An implementation may be [`CL-1`](../reference/identifier-register.md#cl-1) conformant while making
no claim at all about duplicate-account resistance.

## CL-2 — Extended Personhood Profile

**Claim:** the implementation additionally supports scoped, policy-defined
personhood with reuse detection (nullifiers) inside a stated scope and
epoch, including recovery without duplicate enrolment.

| | |
|---|---|
| Predicates | adds [`PR-PER`](../reference/identifier-register.md#pr-per), [`PR-UNQ`](../reference/identifier-register.md#pr-unq) to [`CL-1`](../reference/identifier-register.md#cl-1) |
| Scenarios | [`UC-001`](../reference/identifier-register.md#uc-001), [`UC-002`](../reference/identifier-register.md#uc-002), [`UC-005`](../reference/identifier-register.md#uc-005) |
| Primary gates | Gate A, Gate B (privacy clarity), Gate D (lifecycle completeness) |
| Test count | 12 (6 positive / 6 negative) |

[`CL-2`](../reference/identifier-register.md#cl-2) does not establish civil identity or global uniqueness (see [`ADR-002`](../reference/identifier-register.md#adr-002),
[`ADR-003`](../reference/identifier-register.md#adr-003)) and does not itself specify agent delegation or cross-registry
recognition.

## CL-3 — Delegated Agent Profile

**Claim:** the implementation can bind an AI agent to a live human
principal under a scoped, time-bound delegation, and can require a fresh
human step-up when the agent's requested action, permission, or environment
changes materially.

| | |
|---|---|
| Predicates | adds [`PR-DEL`](../reference/identifier-register.md#pr-del) and [`PR-REL`](../reference/identifier-register.md#pr-rel); reuses [`CL-1`](../reference/identifier-register.md#cl-1)'s [`PR-LIV`](../reference/identifier-register.md#pr-liv), [`PR-HLD`](../reference/identifier-register.md#pr-hld), [`PR-FRE`](../reference/identifier-register.md#pr-fre) |
| Scenarios | [`UC-009`](../reference/identifier-register.md#uc-009), [`UC-010`](../reference/identifier-register.md#uc-010) |
| Primary gates | Gate A, Gate B, Gate D |
| Test count | 8 (4 positive / 4 negative), plus composed-privacy semantic cases where delegation evidence participates in the evidence closure |

`PR-DEL` establishes only the current delegated-authority predicate defined by the selected profile. It does not require disclosure of complete delegation ancestry. `PR-REL` covers the separately testable relationship between the authority evidence and the action/task/credential context. Governed sub-delegation remains possible where authority to delegate is explicit, bounded and provable.

## CL-4 — Federated & Adversarial Assurance Profile

**Claim:** the implementation behaves correctly under issuer accreditation
change, registry disagreement, algorithm migration, and named adversaries
including a malicious verifier and issuer-verifier collusion; it produces
actionable, non-opaque decision receipts; and it has been exercised against
at least one other independent implementation.

| | |
|---|---|
| Predicates | adds [`PR-ISS`](../reference/identifier-register.md#pr-iss), [`PR-CMP`](../reference/identifier-register.md#pr-cmp), [`PR-HID`](../reference/identifier-register.md#pr-hid), [`PR-RES`](../reference/identifier-register.md#pr-res); reuses [`PR-REL`](../reference/identifier-register.md#pr-rel), [`PR-DEL`](../reference/identifier-register.md#pr-del), [`PR-LIV`](../reference/identifier-register.md#pr-liv), [`PR-HLD`](../reference/identifier-register.md#pr-hld), [`PR-FRE`](../reference/identifier-register.md#pr-fre), [`PR-UNQ`](../reference/identifier-register.md#pr-unq), [`PR-PER`](../reference/identifier-register.md#pr-per) where the scenario requires them |
| Scenarios | [`UC-012`](../reference/identifier-register.md#uc-012), [`UC-013`](../reference/identifier-register.md#uc-013), [`UC-022`](../reference/identifier-register.md#uc-022), [`UC-023`](../reference/identifier-register.md#uc-023), [`UC-024`](../reference/identifier-register.md#uc-024), [`UC-025`](../reference/identifier-register.md#uc-025), [`UC-026`](../reference/identifier-register.md#uc-026), [`UC-027`](../reference/identifier-register.md#uc-027), [`UC-030`](../reference/identifier-register.md#uc-030) |
| Primary gates | Gate B (privacy clarity), Gate C (assurance clarity), Gate E (interoperability), Gate G (governance and redress) |
| Test count | 36 (18 positive / 18 negative), plus machine-readable composed-presentation semantic cases |

[`CL-4`](../reference/identifier-register.md#cl-4) is the level at which "collusion resistant" is only a valid claim if
it states, per DRAFTING-RULES.md, the adversary and horizon it was tested
against (CT-UC024-NEG-01 exists specifically to fail unfalsifiable claims).
[`CL-4`](../reference/identifier-register.md#cl-4)'s [`UC-030`](../reference/identifier-register.md#uc-030) tests require **two independent implementations**; a single
implementation cannot claim [`CL-4`](../reference/identifier-register.md#cl-4) by testing against itself.

The composed-presentation predicates distinguish semantic execution from construction execution. A harness can deterministically fail undeclared correlation, enumerable binders, unnecessary exact-identifier disclosure, missing relationship evidence, or semantic collapse before a cryptographic construction is selected. Construction-specific soundness and proof-vector execution remain a later gate.

## What a level does not certify

Passing every test in a level's row of `test-matrix.csv` demonstrates that
an implementation's **behaviour matches this specification's stated
expectations**. It does not certify:

- that the underlying cryptographic construction is sound (no construction
  has been selected yet — see `proof-of-liveness-requirements.md`);
- that the biometric determination behind any [`PR-LIV`](../reference/identifier-register.md#pr-liv) predicate was
  correct (see [`ADR-004`](../reference/identifier-register.md#adr-004), [`AP-02`](../reference/identifier-register.md#ap-02)); or
- production readiness, which additionally requires the operational,
  accessibility and governance evidence described in
  `scenarios/pressure-test-use-case-corpus.md#10-readiness-gates`.

## Status of this level scheme

This four-level scheme is a proposal to make the corpus's Phase 3
("Convert P0 conformance statements into positive and negative test
cases") executable. It covers the 19 P0 scenarios; the 11 P1/P2 scenarios
([`UC-003`](../reference/identifier-register.md#uc-003), [`UC-007`](../reference/identifier-register.md#uc-007), [`UC-008`](../reference/identifier-register.md#uc-008), [`UC-011`](../reference/identifier-register.md#uc-011), [`UC-014`](../reference/identifier-register.md#uc-014), [`UC-015`](../reference/identifier-register.md#uc-015), [`UC-016`](../reference/identifier-register.md#uc-016), [`UC-018`](../reference/identifier-register.md#uc-018), [`UC-019`](../reference/identifier-register.md#uc-019),
[`UC-028`](../reference/identifier-register.md#uc-028), [`UC-029`](../reference/identifier-register.md#uc-029)) are not yet assigned to a level and remain open work,
tracked in `matrices/maturity-map.csv`.
