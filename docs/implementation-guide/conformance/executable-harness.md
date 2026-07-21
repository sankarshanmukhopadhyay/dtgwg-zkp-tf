---
layout: default
title: "Executable conformance harness"
parent: "Conformance"
nav_order: 9
has_toc: true
---
# Executable conformance harness

**Status:** Incubating, non-normative

The repository includes a proof-system-agnostic harness under `conformance-harness/`. It executes only cases declared `EXECUTABLE` in `execution-dispositions.csv`. The bundled adapter is a **non-cryptographic test double and not a reference ZKP implementation**.

## Run the deterministic subset

```sh
python -m pip install -e conformance-harness
dtgwg-zkp-conformance \
  --manifest conformance-harness/examples/mock-manifest.json \
  --schema docs/implementation-guide/conformance/schemas/conformance-test-manifest.schema.json \
  --output results
```

The command produces JSON and Markdown evidence. A failed executable assertion exits non-zero. Blocked and manual cases are governed through explicit dispositions rather than treated as routine failures.

## CI isolation

The dedicated `conformance-harness.yml` workflow is path-filtered and independent of `pages.yml`. Harness failures remain visible, but GitHub Pages does not declare a `needs` dependency on the harness and therefore continues to publish when documentation-integrity checks pass.

## Adapter contract

Implementations provide capability discovery and a construction-neutral `execute(operation, request)` boundary. Network-dependent adapters are not invoked by the default workflow.
