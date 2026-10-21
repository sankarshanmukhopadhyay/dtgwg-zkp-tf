---
layout: default
title: "Canonical evidence reconciliation and record-013 pressure tests"
parent: "Conformance"
nav_order: 49
---

# Canonical evidence reconciliation and record-013 pressure tests

## Authority and baseline

The current authoritative specification is `trustoverip/dtgwg-zkp-spec@aa4e285bbed35ecb2cacb660f798968c9a9793b5`. The upstream task-force guide is `trustoverip/dtgwg-zkp-tf@14a347bf5d75b6d8212c595247e767076d978f31`. This downstream repository remains an implementation/assurance fork. Its pre-reconciliation evidence was pinned to `cfd94063e5cfee7ba6df4dcfd28c10399a0ffd0a`.

The reviewed impact manifest is [canonical-reconciliation.json](canonical-reconciliation.json). The manifest is deliberately conservative. `stale` means material semantic change invalidates the old claim as a current-baseline assertion; `retest_required` means the old evidence can potentially be reused, but has not been demonstrated current; `not_assessed` means no successful assessment is asserted. The manifest does not claim all canonical records have been independently inspected clause by clause.

## Reproduction

```sh
python3 scripts/reconcile_canonical_evidence.py --output-dir results
python3 -m pytest -q scripts/tests
python3 scripts/validate_all.py
```

The first command writes a generated JSON view and Markdown dashboard from the reviewed impact manifest plus the existing evidence-promotion inventory. Each existing evidence asset is checked for existence and recorded with its SHA-256 and byte length. Missing assets and paths escaping the repository fail validation. Asset digests provide byte-level provenance for the local checkout; they do **not** show upstream proposition correspondence, test execution, independence, or evidence freshness. The complete repository validator invokes this validator and the new tests.

## Record 013 bounded adversarial evidence

`scripts/record013_pressure_tests.py` models consumer-side behavior around record 013, which moved to canonical `specified` on 30 September 2026. It exercises: matched negotiation and policy epoch; asymmetric approval; replay across negotiations; stale epochs; mixed-session substitution; abort after admissibility; and Boolean response-channel policy inference.

**Test claim:** a relying application must not infer completed bilateral publication or fairness from mutual admissibility, or infer confidentiality of a policy threshold from zero-knowledge treatment of witnesses.

**Non-claims:** The model does not implement a canonical record-013 prover/verifier, a published negotiation protocol, concurrent state-machine persistence, or proof of a privacy bound. Its Boolean threshold is a synthetic illustration of oracle leakage, not a deployment measurement. The functions model an acceptance policy chosen for pressure testing; they are not normative DTG policy.

## Pending evidence and follow-up

- Run and record CI on the exact PR head; no green CI is asserted by the manifest.
- Perform clause-level 007/010/013 correspondence analysis against current canonical records before retiring `stale` labels.
- Broaden the registry to immutable evidence artifacts with run digests, operator provenance and dependency fingerprints; these initial views reuse the v0.6 evidence-promotion inventory.
- Reconcile the upstream companion guide and fork-specific `docs/implementation-guide/` under #38 rather than copying guide content.
- Assess real concurrent/persistent record-013 commit/abort behavior with an implementation profile before any interoperability claims.
- Complete #54 construction and #55 independent reproduction separately; this tranche does not establish them.
- Advance the task-force content checkpoint only through the governed synchronization workflow.

No new release is justified by these validation and assurance scaffolds alone.
