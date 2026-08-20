# v0.5.0 — Executable Evidence and Release Integrity

v0.5.0 turns construction-independent requirements into reproducible semantic
evidence while strengthening the repository controls that protect releases and
upstream synchronisation.

## Highlights

- one complete quality gate covering 19 validators, harness unit tests and all
  deterministic manifests;
- resilient upstream-drift evidence even when repository Issues are disabled;
- removal and exclusion of generated Python bytecode;
- a semantic fixture adapter that derives outcomes from repository-owned JSON
  rather than returning table-driven mock responses;
- 11 new executable semantic fixtures covering revocation timing, constrained
  devices, mediated proving, attestation-schema correlation, governed context
  and lifecycle bounds;
- 27 of 96 protocol cases executable, with the remaining 69 explicitly blocked
  on construction selection rather than missing fixtures; and
- machine-readable external-evidence governance that prevents unlicensed
  sources from becoming vendored content, CI dependencies or conformance
  evidence.

## External evidence and MAGE

The public `mitchuski/dtgwg-zkp-mage` repository is recorded at reviewed
revision `e40e7f47557a1ec275cb9f22ec08585e2cb9cc28` as experimental evidence.
Its licence status is unverified in the reviewed state. Consequently v0.5.0:

- copies no MAGE source, fixtures, circuits or generated artefacts;
- does not download or execute MAGE in CI;
- grants it no conformance credit; and
- does not depend on it for release acceptance.

The register can be reconsidered only through an explicit review if licensing
or independently reproduced evidence changes.

## Assurance boundary

The semantic fixture adapter is non-cryptographic. It demonstrates that
construction-independent governance and policy inputs lead to deterministic
outcomes. It does not demonstrate proof soundness, zero-knowledge properties,
cross-vendor interoperability or production readiness. Construction selection
remains governed by C1 and the construction-selection gate.

## Validation

The release is accepted only when:

- all 19 repository validators pass;
- all harness unit tests pass;
- both deterministic manifests execute without failures or blocked cases;
- all 96 execution dispositions are complete and exactly represented;
- 27 cases are executable and 69 retain governed construction blockers;
- Pages builds and the rendered-site validator passes; and
- the release worktree contains no generated or uncommitted artefacts.
