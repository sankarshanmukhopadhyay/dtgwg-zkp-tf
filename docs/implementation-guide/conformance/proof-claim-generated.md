---
layout: default
title: "Proof Claim Matrix (Generated)"
parent: "Conformance"
nav_order: 58
---

# Proof-claim boundary matrix

Generated from [the bounded claim catalogue](proof-claim-boundaries.json). The table expresses permitted **semantic inference given an independently established premise**, never proof validity or governance authorization.

| Canonical record | Established premise | Forbidden stronger claim | Reason |
|---|---|---|---|
| 003 | `transcript_binding` | `policy_acceptance` | Binding to a transcript does not validate relying-party policy. |
| 003 | `transcript_binding` | `source_authenticity` | A bound digest does not authenticate the source document. |
| 006 | `status_proof_validity` | `authoritative_freshness` | Valid status proof does not establish that the chosen root is current. |
| 006 | `status_proof_validity` | `registry_authorization` | Status validity is not authorization by a registry. |
| 008 | `hidden_value_commitment` | `presentation_unlinkability` | Visible metadata and reuse may correlate presentations. |
| 008 | `hidden_value_commitment` | `source_authenticity` | Commitment validity does not authenticate the committed source. |
| 010 | `cap_semantic_composition` | `cryptographic_cap_execution` | The existing CAP adapter exercises semantics, not the complete proof construction. |
| 010 | `cap_semantic_composition` | `unique_human` | Distinct membership leaves do not establish distinct persons. |
| 010 | `cap_semantic_composition` | `voucher_consent` | Voucher membership and linkage do not establish consent to the current request. |
| 021 | `vac_chain_semantics` | `delegation` | Acting as a principal under a chain is not a separate delegated authority grant. |
| 021 | `vac_chain_semantics` | `task_completion` | Authority to act is not evidence of a completed task. |

## Consumer contract

- A positive semantic match does not authenticate an input or establish successful cryptographic verification.
- Prohibited claims return `REJECTED`; unknown or unproven claims return `INDETERMINATE` rather than authorization.
- No downstream assurance finding promotes an upstream construction lifecycle.
- CAP record 010 remains a semantic/construction-feasibility track without an accepted end-to-end prover.

Regenerate with `python3 -m scripts.generate_claim_boundary_guide`; validate with `--check`.
