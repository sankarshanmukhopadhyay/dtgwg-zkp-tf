---
layout: default
title: "Construction Evidence Index"
parent: "Conformance"
nav_order: 47
---

# Construction evidence index

The [construction evidence manifest](construction-evidence-manifest.json) remains the repository-local source of profile declarations. The [generated index](construction-evidence-index.json) is a **derived, non-authoritative snapshot** of the current manifest and local evidence bytes. It is not a new construction record schema, proof result, or upstream lifecycle.

From the repository root:

```sh
python3 scripts/construction_evidence_index.py
python3 scripts/construction_evidence_index.py --check
python3 -m unittest scripts.tests.test_construction_evidence_index -v
```

Every indexed profile retains its existing evidence state, interoperability state and explicit claim boundary. Each referenced local file has a SHA-256 digest; the manifest itself also has a digest. If either a file or the manifest changes, `--check` fails until the index is regenerated and reviewed. Repository-contained paths are mandatory; URLs are deliberately not hashed or treated as independently authenticated external provenance.

**Scope and non-claims:** This index does not execute cryptography, authenticate the provenance of external evidence, demonstrate independence, or promote canonical upstream `requested/specified/constructed/run/vetted/published` states. A digest proves only equality to the indexed bytes. Reproduction and independent interoperability continue to require the existing [evidence-promotion gates](evidence-promotion-gates.md).

The deterministic index is useful as a baseline for subsequent #67 work: claim-boundary mappings and regression probes can detect which referenced evidence changed and require explicit reassessment. It does not automatically decide whether a change invalidates any semantic claim.

## Validation

The full repository validator executes `--check` after validating existing construction evidence and promotion controls. Changes to referenced evidence require rebuilding and committing the index in the same PR.

The first increment is intentionally limited to the existing construction manifest. Canonical records not represented there are **not** silently assigned an evidence state. Later registry expansion must reuse existing canonical correspondence and evidence-promotion authority, not duplicate or infer it.
