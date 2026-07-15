# Conformance and plugfest

**Status:** Incubating
**Normative status:** Non-normative unless explicitly promoted into the Working Draft

## What's in this directory

| File | Purpose |
|---|---|
| [`levels.md`](./levels.md) | Formal definition of conformance levels CL-1 through CL-4: which predicates and scenarios each requires, and which readiness gate it targets |
| [`test-matrix.csv`](./test-matrix.csv) | Machine-readable conformance test matrix: 76 test cases across the 19 P0 scenarios, each with a level, scenario, predicate set, named adversary, test type (positive/negative), description and expected result |
| [`test-matrix.md`](./test-matrix.md) | Human-readable view of the same matrix, grouped by level and scenario |
| [`fixtures/`](./fixtures/) | Illustrative, non-normative JSON fixtures (canonical transcript, issuer set, nullifier scope/epoch, delegation, registry snapshot) referenced by test cases |

Validate all of the above with:

```sh
python3 scripts/validate_conformance.py
```

run from the repository root. It checks that every `predicate_id`,
`adversary_id` and `scenario_id` referenced in the test matrix and the
`matrices/` CSVs actually exists in the taxonomy and scenario corpus, and
that every conformance level has at least one passing (positive) and one
failing (negative) test case.

## What conformance validates

Predicate semantics, canonical transcript and encodings, lifecycle and
status, cross-vendor interoperability, privacy against named adversaries,
constrained devices, fallback and downgrade, and error consistency — see
`levels.md` for how each of these maps onto CL-1 through CL-4.

## Minimum plugfest topology

- two issuer implementations;
- two wallet/prover implementations;
- two verifiers;
- registry and policy fixtures (see `fixtures/issuer-set.json`, `fixtures/registry-snapshot.json`);
- positive, negative, malformed, lifecycle, and privacy tests (see `test-matrix.csv`).

This matches UC-030 (Partial Deployment Across Independent Implementations)
in the pressure-test corpus, which is itself the exit criterion for Phase 4
of the corpus's implementation programme.

## What this suite is, and is not

This suite defines **expected behaviour** for a conformant implementation.
It is not, itself, a working conformance harness: no cryptographic
construction has been selected for any predicate (see
`../../../proof-of-liveness-requirements.md`), so no test case here can yet
be executed against real proofs. `scripts/validate_conformance.py`
validates the *specification's internal consistency* — that every claim is
traceable to a real predicate, adversary and scenario, and that no
conformance level is defined by assertion alone (rule 1 and rule 2 of
`../../../DRAFTING-RULES.md`) — not cryptographic correctness.

## Known gaps

- 11 of the 30 scenarios (all P1/P2) are not yet assigned to a conformance
  level: UC-003, UC-007, UC-008, UC-011, UC-014, UC-015, UC-016, UC-018,
  UC-019, UC-028, UC-029. See `matrices/maturity-map.csv`.
- CL-3 (delegated agent) test cases reference "delegation evidence" and
  "agent key binding," neither of which has a predicate ID in
  `taxonomy/predicates.md` yet.
- No cross-vendor plugfest (UC-030) has run. CL-4's positive test cases
  assume two independent implementations exist; today there are zero.

## Evidence packaging

Use the implementation and profile statement templates and the JSON schemas in `schemas/` to produce portable evidence. A conformance claim identifies a level, profile, source revision, environment, fixture digests, results and exceptions.
