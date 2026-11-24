---
layout: default
title: "Canonical evidence reconciliation and record-013 pressure tests"
parent: "Conformance"
nav_order: 49
---

# Canonical evidence reconciliation and record-013 pressure tests

## Authority and baseline

The authoritative specification observed on 24 November 2026 is `trustoverip/dtgwg-zkp-spec@a8ff49292bc2dc7f2a1f8014b6e2268c0e483677`. The upstream task-force guide is `trustoverip/dtgwg-zkp-tf@3161398689d2f4e9feb210b92fa90ad22f9ea77f`. This downstream repository remains an implementation/assurance fork. Its pre-reconciliation evidence was pinned to `cfd94063e5cfee7ba6df4dcfd28c10399a0ffd0a`.

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

## November 24 canonical update

Upstream [PR 26](https://github.com/trustoverip/dtgwg-zkp-spec/pull/26) materially changes records 007, 009, 022, 024 and 025. Record 025 is constructed upstream, not independently reproduced here. Record 006 now identifies a range-leaf runtime. Existing evidence inventory and release pins remain historical; the impact manifest is the current observation and invalidation surface. The Credential specification owns the disposition of salt disclosure and identifier profiles. The canonical correspondence packet retains uncovered obligations, including cryptographic range-leaf execution. No local proof outcome or upstream lifecycle promotion is implied.


## Per-run execution provenance and dependency invalidation

The `scripts/evidence_run.py` runner records the **actual exit status** of a named local command along with a UTC start/end timestamp, declared operator and implementation, Python/platform metadata, upstream canonical revision and conservative record impact, plus SHA-256 and byte length for declared repository-local dependencies. It fingerprints dependencies again after execution to reject in-run drift. Captured stdout/stderr are represented by digests and lengths, not raw output, to reduce the risk of exposing sensitive transcripts.

Example, from repository root (an *illustrative* local command, not a conformance claim):

```sh
python3 scripts/evidence_run.py run \
  --record 013 --operator local --implementation record013-synthetic \
  --dependency scripts/record013_pressure_tests.py \
  --output /tmp/record013-run.json -- \
  python3 -m pytest -q scripts/tests/test_record013_pressure_tests.py

python3 scripts/evidence_run.py verify /tmp/record013-run.json
```

The first command can succeed and produce an execution record; the second deliberately returns an invalidated/unproven result while the canonical record's evidence disposition remains `stale`. A successful local process is **not** sufficient evidence of canonical correspondence. Changing the upstream revision, the recorded canonical impact, any dependency bytes, or the report digest invalidates the record. Missing or unsafe paths fail closed; prior evidence files are never silently overwritten. Generated reports are local artifacts, not committed authoritative claims.

Limitations: this is a bounded execution-provenance facility, not a signed attestation, hermetic build or independent operator identity proof. A caller must declare all consequential dependencies; undeclared environment and network inputs are not detectable. Canonical freshness requires governed proposition-level assessment and retest. No automatic advancement to `implemented`, `vetted` or `published` is supported.


## Source-reviewed proposition correspondence: records 003 and 006

The bounded [record 003/006 correspondence packet](canonical-correspondence-003-006.json) is pinned to the authoritative `trustoverip/dtgwg-zkp-spec` commit and exact Git blob IDs for each record. It maps named canonical fields to existing downstream semantic/policy test identifiers, records residual assumptions and identifies genuinely uncovered obligations. `python3 scripts/validate_canonical_correspondence.py` validates the packet and is included in complete validation.

Record 003 retains the canonical distinction between binding a **supplied transcript scalar** and authenticating/canonicalizing the underlying request, enforcing audience/challenge/replay policy and accepting a predicate identifier. The downstream adapter exercises portions of these policy boundaries, but it is not a current-canonical Groth16 construction rerun.

Record 006 demonstrates the stronger limitation: root/epoch and policy-layer checks are covered semantically, whereas canonical `issuance[1]` explicitly requires the revocation root to commit **strictly sorted** handles for adjacent-neighbour non-membership. The existing named evidence does not verify that prerequisite. The packet marks it `uncovered` and does not relabel record 006 as current.

This machine-checkable trace is a review aid, not a claim that the downstream test source was independently reproduced or that the exact canonical record source is fetched and rechecked on every CI run. The pinned upstream blob IDs must be compared against any later authoritative revision before treating the mapping as applicable. Both records remain `retest_required` in the canonical-impact manifest.
