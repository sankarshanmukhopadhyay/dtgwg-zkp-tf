# Validation report

This report is generated for the Implementation and Interoperability Guide Maturity Programme. The v0.4.0 release adds governed DTG interoperability profiles and cross-specification assurance while preserving the repository's explicit authority boundaries. See `RELEASE_NOTES_v0.4.0.md`.

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
python3 scripts/validate_interoperability.py
python3 scripts/build_traceability.py
```

The packaged release was accepted only after these commands completed successfully. `build_traceability.py` may report scenarios that do not yet have test cases; this is an informational maturity signal rather than a dangling-reference failure.

## Residual decision dependencies

The context and epoch authority model, proof construction selection, normative delegation predicate semantics, registry recognition rules, profile performance targets and any accredited certification process remain task-force decisions. They are documented as open dependencies rather than implied implementation requirements.

## Packaged results

```text
Documentation validation passed.
Conformance validation passed.
96/96 test rows OK across 4 conformance levels.
Style validation passed.
Link validation passed.
Fixture validation passed: 49 JSON files parsed.
Traceability generated: 52 scenarios, 96 conformance references and 26 assurance references.
```

This release also ran `validate_navigation.py`, `validate_diagrams.py`, `validate_operations.py`, `validate_threat_model.py`, `validate_deployment_profiles.py` and `validate_generated_counts.py`; all passed. Residual conformance-coverage gaps remain governed through explicit execution dispositions. This release expands both the scenario corpus and the test matrix while preserving the distinction between executable and governed non-executable cases.

## Security guardrails and RAHP adaptation — 2026-07-21

- RAHP methodological source pinned to upstream commit `94d17a6f5e8b448aae4698ff183e77a4a2f7a083`.
- Dedicated adoption/adaptation statement and machine-readable mapping added.
- Canonical threat model expanded from 36 to 45 threats without renumbering existing entries.
- Fourteen guardrails map one-to-one to fourteen assurance tests.
- Risk acceptance and metric evidence schemas added.
- Five Mermaid diagrams added to the GitHub Pages register.
- `scripts/validate_security_assurance.py` added.

## v0.4.0 interoperability assurance — 2026-08-11

- 3 governed DTG dependencies recorded in the portfolio alignment register.
- 20 architecture decisions tracked, including C2 credential-linkage and C3 task-context decisions.
- Canonical threat model expanded from 45 to 52 threats.
- Scenario corpus expanded from 48 to 52 scenarios.
- Conformance matrix expanded from 88 to 96 cases.
- 10 interoperability fixtures added; 49 JSON fixtures/schemas parse successfully repository-wide.
- Conformance harness expanded from 8 to 16 deterministic executable cases; 80 remaining cases retain governed non-executable dispositions.
- RAHP pressure-test records preserve control-plane disposition and retest triggers for cross-specification findings.
