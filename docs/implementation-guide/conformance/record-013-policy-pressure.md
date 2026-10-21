---
layout: default
title: "Record 013 Policy Pressure Tests"
parent: "Conformance"
nav_order: 56
---

# Construction-neutral policy and fairness pressure tests

**Authority:** downstream assurance experiment only. This is **not** a construction or specification for canonical record 013, and must not import unmerged upstream proposal semantics.

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

The model does not resolve record-013's authoritative policy-root schema or verifier protocol, and these additional tests must remain classified as `retain_downstream_extension` or `retest_when_canonical` until #30 confirms upstream semantics.

## Evidence disposition

Retain as a downstream adversarial assurance extension for [#32](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/32). Reassess the applicability of the model when upstream record 013 becomes sufficiently specified, under canonical authority control [#30](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/30).

No upstream lifecycle state is promoted. No Credential or Registry authority is invented. No policy confidentiality or exchange fairness claim should be made solely because individual cryptographic predicates succeed.
