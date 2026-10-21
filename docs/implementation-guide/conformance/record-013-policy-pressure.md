---
layout: default
title: "Record 013 Policy Pressure Tests"
parent: "Conformance"
nav_order: 56
---

# Construction-neutral policy and fairness pressure tests

**Authority checkpoint (21 October 2026):** canonical `trustoverip/dtgwg-zkp-spec@aa4e285bbed35ecb2cacb660f798968c9a9793b5`, record 013 **`specified`**. Upstream PR #12 merged on 30 September 2026. The downstream *adopted evidence baseline* remains separately pinned under #30; observing a newer revision does not implicitly migrate all evidence. This test model is not a construction for record 013.

The [executable test suite](../../../scripts/tests/test_record013_pressure.py) uses a **synthetic** Boolean admission response, two local parties, a negotiation identifier, an epoch, and whether an exchange was committed. It tests what a consumer **cannot** infer from apparently favourable local observations. These values are model inputs, not a proposed DTG public-input or wire format.

Run from the repository root:

```sh
python3 -m pytest -q scripts/tests/test_record013_pressure.py
python3 scripts/validate_all.py
```

## Pressure-test results and their limits

| Probe | Demonstrated model behavior | Explicit non-claim |
|---|---|---|
| Adaptive policy oracle | A synthetic threshold can be inferred with logarithmically many yes/no probes | No claim that canonical record 013 implements this threshold |
| Selective abort | An uncommitted half remains an incomplete exchange | A successful local proof does not establish fair exchange |
| Cross-negotiation replay | A mismatched negotiation identifier is rejected in the model | Does not define canonical transcript encoding |
| Policy epoch drift | Unequal/stale epochs yield indeterminate currentness | Does not authorize a normative freshness threshold |
| Asymmetric acceptance | One rejecting community prevents mutual acceptance | Does not define upstream admissibility logic |
| Locally accepted state | Both local results yield only `LOCALLY_ACCEPTED_NOT_PUBLISHED` | Admission does not establish publication or reciprocal consent |

These tests evaluate assumptions about response-channel information, protocol ordering and currentness, **not cryptographic soundness or zero-knowledge**. In a real deployment, timing, metadata, cross-verifier correlation and external authoritative state require separate evidence. Recording an adversarial counterexample does not prove the deployed protocol is vulnerable; it falsifies the broader inference under the documented model.


## Additional falsifiable adversary traces

The expanded regression suite tests **cross-epoch threshold inference**, **concurrent negotiations**, **repeated negotiation identifiers** and **colluding observers that share visible results**. A coalition view is deliberately a simple model of metadata pooling; it does not establish a real verifier network, a deployed correlation vulnerability or exposure of any hidden proof witness.

- A threshold change between epochs is inferable under a synthetic monotone yes/no oracle.
- Concurrent local acceptances still do not establish atomic publication or fair exchange.
- Identifier reuse between concurrent negotiations creates an ambiguous context and fails closed in the model.
- Multiple observers can combine separately visible Boolean outcomes for the same negotiation. This is a response/metadata channel, **not** leakage from proof internals.

The current canonical record specifies the proof relation and external exchange ordering. These tests must remain classified as `retain_downstream_extension` or `retest_when_canonical` until they are reconciled against the actual statement, profile and executable construction; they do not supply canonical cryptographic vectors.

## Evidence disposition

Retain as a downstream adversarial assurance extension for [#32](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/32). Reassess the model against the now-specified canonical record under authority-change control [#30](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/30).

## Mapping to current canonical record 013

| Canonical property at observed SHA | Existing local test/pressure evidence | Disposition |
|---|---|---|
| Clause 1: committed half opens to canonical bytes under salt (record 022) | Negotiation replay and context-collision models; no cryptographic commitment-opening proof | `retest_when_canonical`; construction correspondence missing |
| Clause 2: proposed half's form is a policy-root member | Synthetic Boolean threshold oracle and cross-epoch leakage model; no actual set-membership witness | `retain_downstream_extension` for response-channel leakage |
| Clause 3: subject membership proven if claimed | Synthetic asymmetric admission; no authenticated member-grant circuit | `retest_when_canonical`; missing cryptographic evidence |
| Clause 4: transcript bound across both commitments and challenge (record 003) | Local replay rejection and concurrency context-model negatives | `retest_when_canonical`; reuse existing record-003 transcript evidence |
| Exchange ordering: both commitments, both yes, then reveal | Incomplete/abort and concurrent negotiation tests | `retain_downstream_extension`, consistent with explicit upstream `doesNotEstablish` fairness |
| Policy-root currentness and confidentiality | Synthetic stale-epoch and adaptive oracle models | `retain_downstream_extension`, not a normative freshness rule or proof-system leakage assertion |

**Canonical non-claims confirmed:** record 013 does not establish fair exchange, currentness beyond its stated version, policy privacy or eventual acceptance/publication. The current record explicitly notes that a one-form accepted set can reveal the form from a yes answer. Our general Boolean threshold model is **not evidence that the canonical protocol implements a threshold**.

**Unmet locally controlled work:** construction/profile correspondence to specified clauses, attributable evidence registration, and any selected cryptographic vectors. This issue is no longer blocked merely by an unspecified upstream statement, but it is not complete.


No upstream lifecycle state is promoted. No Credential or Registry authority is invented. No policy confidentiality or exchange fairness claim should be made solely because individual cryptographic predicates succeed.
