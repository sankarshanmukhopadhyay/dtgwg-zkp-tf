# DTGWG ZKP conformance harness

This package is a proof-system-agnostic execution plane for declarative conformance cases. The bundled mock adapter is a **NON-CRYPTOGRAPHIC TEST DOUBLE** and **NOT A REFERENCE ZKP IMPLEMENTATION**.

Run from the repository root:

```sh
python -m pip install -e conformance-harness
dtgwg-zkp-conformance --manifest conformance-harness/examples/mock-manifest.json --schema docs/implementation-guide/conformance/schemas/conformance-test-manifest.schema.json --output results
```

Only cases declared `EXECUTABLE` are eligible for automated pass/fail.

The `semantic-fixture` adapter evaluates repository-owned JSON fixtures and
derives outcomes from their content. It does not perform cryptography. Fixture
paths are constrained to the configured fixture root, and generated evidence
records the fixture digest and schema version. This creates meaningful,
reproducible evidence for construction-independent semantics without treating
an external implementation or evidence repository as a release dependency.
