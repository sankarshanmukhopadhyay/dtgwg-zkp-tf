# Validation report

This report is generated for the Implementation and Interoperability Guide Maturity Programme. The v0.2.2 release preserves existing scenario and conformance semantics while fixing a documentation defect and carrying the normative reference (IACR ePrint 2026/333) into the implementation guide. See `RELEASE_NOTES_NORMATIVE_REFERENCE_AND_CONTEXT_ALIGNMENT.md`.

## Required checks

Run the following commands from the repository root:

```sh
python3 scripts/validate_docs.py
python3 scripts/validate_conformance.py
python3 scripts/validate_style.py
python3 scripts/validate_links.py
python3 scripts/validate_fixtures.py
python3 scripts/validate_navigation.py
python3 scripts/validate_diagrams.py
python3 scripts/validate_operations.py
python3 scripts/validate_threat_model.py
python3 scripts/validate_deployment_profiles.py
python3 scripts/validate_generated_counts.py
python3 scripts/build_traceability.py
```

The packaged release was accepted only after these commands completed successfully. `build_traceability.py` may report scenarios that do not yet have test cases; this is an informational maturity signal rather than a dangling-reference failure.

## Residual decision dependencies

The context and epoch authority model, proof construction selection, normative delegation predicate semantics, registry recognition rules, profile performance targets and any accredited certification process remain task-force decisions. They are documented as open dependencies rather than implied implementation requirements.

## Packaged results

```text
Documentation validation passed.
Conformance validation passed.
88/88 test rows OK across 4 conformance levels.
Style validation passed.
Link validation passed.
Fixture validation passed: 26 JSON files parsed.
Traceability generated: 48 scenarios, 88 conformance references and 26 assurance references.
```

This release also ran `validate_navigation.py`, `validate_diagrams.py`, `validate_operations.py`, `validate_threat_model.py`, `validate_deployment_profiles.py` and `validate_generated_counts.py`; all passed. Residual conformance-coverage gaps are tracked as before and are not affected by this release, which changes reference and boundary-decision documentation rather than scenario or test-matrix content.

## Security guardrails and RAHP adaptation — 2026-07-21

- RAHP methodological source pinned to upstream commit `94d17a6f5e8b448aae4698ff183e77a4a2f7a083`.
- Dedicated adoption/adaptation statement and machine-readable mapping added.
- Canonical threat model expanded from 36 to 45 threats without renumbering existing entries.
- Fourteen guardrails map one-to-one to fourteen assurance tests.
- Risk acceptance and metric evidence schemas added.
- Five Mermaid diagrams added to the GitHub Pages register.
- `scripts/validate_security_assurance.py` added.
