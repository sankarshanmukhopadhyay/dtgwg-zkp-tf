---
layout: default
title: "Executable conformance harness"
parent: "Conformance"
nav_order: 9
has_toc: true
---
# Executable conformance harness

**Status:** Incubating, non-normative

The repository includes a proof-system-agnostic harness under `conformance-harness/`. It executes only cases declared `EXECUTABLE` in `execution-dispositions.csv`. The bundled mock is a **non-cryptographic test double and not a reference ZKP implementation**. The semantic fixture adapter derives construction-independent outcomes from repository-owned inputs; it is also non-cryptographic.

## Run the deterministic subset

```sh
python -m pip install -e conformance-harness
dtgwg-zkp-conformance \
  --manifest conformance-harness/examples/mock-manifest.json \
  --schema docs/implementation-guide/conformance/schemas/conformance-test-manifest.schema.json \
  --output results

dtgwg-zkp-conformance \
  --manifest conformance-harness/examples/semantic-fixture-manifest.json \
  --schema docs/implementation-guide/conformance/schemas/conformance-test-manifest.schema.json \
  --output results/semantic-fixtures
```

The command produces JSON and Markdown evidence. A failed executable assertion exits non-zero. Blocked and manual cases are governed through explicit dispositions rather than treated as routine failures.

## CI gates

The dedicated `conformance-harness.yml` workflow provides a focused path-filtered signal. The repository-quality workflow and Pages pre-render job both run `scripts/validate_all.py`, so a harness, fixture, governance or assurance failure blocks release validation and documentation publication.

## Adapter contract

Implementations provide capability discovery and a construction-neutral `execute(operation, request)` boundary. The semantic adapter confines fixture paths to the configured root and records digest-bound evidence. Network-dependent and external-repository adapters are not invoked by the release workflow.
