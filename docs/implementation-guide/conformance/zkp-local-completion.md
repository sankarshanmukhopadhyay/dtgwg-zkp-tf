---
layout: default
title: "ZKP v0.7 Local Completion"
parent: "Conformance"
nav_order: 59
---

# ZKP v0.7 local completion and release disposition

**Disposition: DEFER release; #54, #67 and #32 remain open.** This is a governed acceptance checkpoint, not a declaration that the ZKP programme is finished.

The [machine-readable disposition](zkp-local-disposition.json) is validated by `python3 scripts/validate_zkp_disposition.py`; the complete repository suite also executes negative regression tests against unsupported issue closure, missing evidence and premature release. The ledger references the existing issue-owned evidence, and is not an alternative normative specification or canonical status registry.

| Issue | Local status | Remaining decisive criterion |
|---|---|---|
| [#54](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/54) | `local_unmet` | Complete privacy-preserving record-010 membership + relationship prover/verifier, end-to-end vectors, D1–D3 |
| [#67](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/67) | `local_unmet` | Attributable execution evidence, dependency-aware invalidation and completed CAP inference controls |
| [#32](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/32) | `local_partial` | Canonical clause-to-construction evidence and attributable adversarial evidence registration |

## Why the current experiments cannot be promoted

The [signed-root membership spike](cap-signed-root-membership-spike.md) discloses a Merkle leaf/path and cannot establish zero-knowledge membership. The [hidden-witness spike](cap-hidden-witness-spike.md) proves a narrow commitment-opening equality but does not prove canonical Credential/Registry membership or relationship authority. The [authenticated commitment envelopes](cap-authenticated-commitment-spike.md) rely on test-configured public keys rather than policy-backed issuer/registry authority. Therefore a composition of these component test results cannot be labelled a complete canonical CAP prover/verifier.

The [evidence inventory](evidence-registry-projection.md) still lacks attributed execution observations and complete retest/invalidation provenance; observed outcomes and independence cannot be inferred from bytes. The [non-implication matrix](proof-claim-generated.md) is semantic and cannot substitute for a verified CAP presentation in consumer testing.

The [record-013 pressure tests](record-013-policy-pressure.md) are adversarial **model counterexamples**, not canonical record-013 construction vectors or proof-system vulnerabilities.

## Execution decision

Continue engineering only where a falsifiable local proposition remains:

1. For #54, build or decisively fail a complete privacy-preserving membership/relationship circuit against pinned **experimental** Credential/Registry assumptions; retain actual positive and adversarial negative proof evidence and measured environment. No synthetic membership-path disclosure may be presented as privacy-preserving.
2. For #67, require attributable execution records (observed/expected outcomes, environment, producer, cryptographic profile, digest, adversary/privacy horizon where applicable) and invalidate evidence on semantic/dependency changes before any status promotion.
3. For #32, the construction-neutral concurrency/collusion and cross-epoch cases are now present, and record 013 is **specified** at observed upstream `aa4e285bbed35ecb2cacb660f798968c9a9793b5`. Finish clause-level executable correspondence and attributable adversarial evidence only against a reviewed adopted authority baseline; model counterexamples alone do not complete the proof profile.
4. For #55, obtain a genuinely independent operator/implementation after a frozen profile exists; same-operator CI does not qualify.

Under [#30](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/30), upstream remains authoritative. [#26](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/26) and [#27](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/27) remain external profile constraints, not a blanket excuse for unimplemented local work.

**Release rule:** No v0.7 tag or `interoperable` claim until material release gates are actually met, independently reproduced where claimed, and adopted through the repository release workflow. A repository CI PASS is not proof of those facts.
