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
it is expected to satisfy. Levels are cumulative: a CL-2 claim presumes CL-1
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
| Predicates | `PR-LIV`, `PR-HLD`, `PR-FRE` |
| Scenarios | UC-004, UC-006, UC-017, UC-020, UC-021 |
| Primary gates | Gate A (predicate clarity), Gate F (operational viability) |
| Test count | 20 (10 positive / 10 negative) |

CL-1 does **not** require personhood, uniqueness, delegation, or federated
issuer accreditation. An implementation may be CL-1 conformant while making
no claim at all about duplicate-account resistance.

## CL-2 — Extended Personhood Profile

**Claim:** the implementation additionally supports scoped, policy-defined
personhood with reuse detection (nullifiers) inside a stated scope and
epoch, including recovery without duplicate enrolment.

| | |
|---|---|
| Predicates | adds `PR-PER`, `PR-UNQ` to CL-1 |
| Scenarios | UC-001, UC-002, UC-005 |
| Primary gates | Gate A, Gate B (privacy clarity), Gate D (lifecycle completeness) |
| Test count | 12 (6 positive / 6 negative) |

CL-2 does not establish civil identity or global uniqueness (see ADR-002,
ADR-003) and does not itself specify agent delegation or cross-registry
recognition.

## CL-3 — Delegated Agent Profile

**Claim:** the implementation can bind an AI agent to a live human
principal under a scoped, time-bound delegation, and can require a fresh
human step-up when the agent's requested action, permission, or environment
changes materially.

| | |
|---|---|
| Predicates | reuses CL-1's `PR-LIV`, `PR-HLD`, `PR-FRE` |
| Scenarios | UC-009, UC-010 |
| Primary gates | Gate A, Gate D |
| Test count | 8 (4 positive / 4 negative) |

**Open gap:** `taxonomy/predicates.md` has no predicate ID for "delegation
evidence" or "agent key binding," both of which UC-009, UC-010 and UC-011
require. CL-3 test cases reference these informally pending a taxonomy
update (tracked in `matrices/maturity-map.csv`). Implementers should not
read the absence of a `PR-DEL` identifier as meaning delegation is
unconstrained — see ADR-001.

## CL-4 — Federated & Adversarial Assurance Profile

**Claim:** the implementation behaves correctly under issuer accreditation
change, registry disagreement, algorithm migration, and named adversaries
including a malicious verifier and issuer-verifier collusion; it produces
actionable, non-opaque decision receipts; and it has been exercised against
at least one other independent implementation.

| | |
|---|---|
| Predicates | adds `PR-ISS`; reuses `PR-LIV`, `PR-HLD`, `PR-FRE`, `PR-UNQ`, `PR-PER` from lower levels where the scenario requires them |
| Scenarios | UC-012, UC-013, UC-022, UC-023, UC-024, UC-025, UC-026, UC-027, UC-030 |
| Primary gates | Gate C (assurance clarity), Gate E (interoperability), Gate G (governance and redress) |
| Test count | 36 (18 positive / 18 negative) |

CL-4 is the level at which "collusion resistant" is only a valid claim if
it states, per DRAFTING-RULES.md, the adversary and horizon it was tested
against (CT-UC024-NEG-01 exists specifically to fail unfalsifiable claims).
CL-4's UC-030 tests require **two independent implementations**; a single
implementation cannot claim CL-4 by testing against itself.

## What a level does not certify

Passing every test in a level's row of `test-matrix.csv` demonstrates that
an implementation's **behaviour matches this specification's stated
expectations**. It does not certify:

- that the underlying cryptographic construction is sound (no construction
  has been selected yet — see `proof-of-liveness-requirements.md`);
- that the biometric determination behind any `PR-LIV` predicate was
  correct (see ADR-004, AP-02); or
- production readiness, which additionally requires the operational,
  accessibility and governance evidence described in
  `scenarios/pressure-test-use-case-corpus.md#10-readiness-gates`.

## Status of this level scheme

This four-level scheme is a proposal to make the corpus's Phase 3
("Convert P0 conformance statements into positive and negative test
cases") executable. It covers the 19 P0 scenarios; the 11 P1/P2 scenarios
(UC-003, UC-007, UC-008, UC-011, UC-014, UC-015, UC-016, UC-018, UC-019,
UC-028, UC-029) are not yet assigned to a level and remain open work,
tracked in `matrices/maturity-map.csv`.
