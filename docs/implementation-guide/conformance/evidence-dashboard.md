---
layout: default
title: "Evidence Dashboard"
parent: "Conformance"
nav_order: 55
---

# Downstream construction evidence dashboard

**Source:** [Evidence-promotion gates](evidence-promotion-gates.json). This is a generated view, not upstream normative lifecycle or a claim of verified interoperability.

Run `python3 scripts/generate_evidence_dashboard.py` after changing the evidence-promotion register; `--check` rejects stale output.

| Canonical record | Declared evidence classes | Local labels | Gaps / next evidence |
|---|---|---|---|
| 003 | `deterministic_semantic` | `implemented` | independent_reproduction, cross_implementation |
| 006 | `deterministic_semantic`, `currentness_status` | `implemented`, `assurance_reviewed` | authoritative_freshness_policy, independent_reproduction, cross_implementation |
| 007 | `deterministic_semantic` | `assurance_reviewed` | normative_commitment_profile, cryptographic_execution, independent_reproduction, cross_implementation |
| 008 | `deterministic_semantic`, `cryptographic_execution`, `privacy_adversarial`, `performance` | `implemented`, `assurance_reviewed` | independent_reproduction, cross_implementation, credential_member_profile |
| 009 | no registered evidence | none | **missing evidence registration** |
| 010 | `deterministic_semantic` | none | clause_3_witness_contract, cryptographic_execution, independent_reproduction, cross_implementation, performance |
| 021 | `deterministic_semantic`, `privacy_adversarial`, `currentness_status` | `implemented`, `assurance_reviewed` | production_construction, independent_reproduction, cross_implementation, cryptographic_implementation_correspondence |

## Interpretation

- These are declared evidence classes and downstream labels from the existing register; they are **not** independently substantiated by this projection.
- A missing row is not a failed proof, nor a proof of absence: it is **unregistered**.
- No downstream label advances canonical upstream `requested/specified/constructed/run/vetted/published` states.
- The CAP component experiments remain insufficient for complete record-010 cryptographic execution or independent reproduction.
- Missing upstream Credential/Registry authority or independent operator evidence cannot be silently upgraded by CI.
