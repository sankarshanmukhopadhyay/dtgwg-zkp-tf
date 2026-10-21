---
layout: default
title: "Evidence Registry Projection"
parent: "Conformance"
nav_order: 57
---

# Machine-verifiable evidence provenance projection

**Scope:** downstream evidence-asset inventory derived from [the evidence-promotion register](evidence-promotion-gates.json). It is not a competing normative record registry, independent attestation, or an upstream lifecycle.

Run from the repository root:

```sh
python3 scripts/evidence_registry.py --check
python3 scripts/evidence_registry.py --output /tmp/zkp-evidence-inventory.json
python3 -m pytest -q scripts/tests/test_evidence_registry.py
```

The generated JSON pins the exact upstream semantic commit declared by the source, the source-register SHA-256 digest and each referenced repository-contained asset's SHA-256. Record 009 appears as `registration: missing`, **not** a failed test or invalid cryptographic construction. Classifications and local labels are copied from the source register and remain *declarations* rather than new observed outcomes.

Each projection record explicitly sets `observed_cryptographic_outcome`, `reproduction_environment` and `observation_time` to `null`: this projection alone cannot reconstruct an attributed execution run, operator identity, adversarial horizon or independent reproduction. `producer_independence: not_established` prohibits use of the projection as interoperability evidence. Run-specific evidence belongs in a future attributable record contract with measured expected/observed outcomes and provenance, not a silent backfill.

The repository validation gate checks paths, duplicate/unreviewed canonical records, known classes and labels, and missing artifact bytes. Regeneration is deterministic; changing source evidence bytes changes the emitted digest. This is suitable as a first consumer-facing inventory but **does not implement the full #67-B lifecycle invalidation graph, complete schema or cross-workflow reproduction attestation**.

No #54 CAP construction evidence state is promoted, and no Credential or Registry policy is invented. The [human-readable dashboard](evidence-dashboard.md) remains another projection of the same evidence-promotion source.
