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

## Documentation architecture and implementation-guide quality pass — 2026-08-12

- Component implementation landing page expanded into a role-oriented implementation contract with prerequisite decisions, shared obligations, cross-role interaction model, implementation sequence, separation-of-duty guidance and evidence expectations.
- Issuer, wallet/holder, verifier, registry, delegated-agent and auditor/assessor guides expanded with responsibilities, authority dependencies, failure behaviour, security/privacy controls, evidence outputs and onward navigation.
- Top-level GitHub Pages navigation reordered into a deterministic lifecycle sequence; duplicate top-level `nav_order` values removed.
- Guided learning expanded from 3 paths / 12 steps to 5 paths / 24 steps, separating sponsor, implementer, operator, assessor and specification-contributor journeys.
- `scripts/validate_navigation.py` now rejects duplicate top-level navigation order values.
- `scripts/validate_links.py` now validates internal Markdown anchors in addition to repository-local targets.
- DTG Portfolio Monitor and Portfolio Status links added as non-authoritative situational-awareness references with an explicit governance boundary.
- External references used by the rendered documentation and interoperability register were manually resolved on 2026-08-12, including the upstream ZKP and RAHP repositories, pinned RAHP commit, ZKP discussions, IACR ePrint 2026/333, Credential Spec issue #9, Trust Tasks repository/design note, and DTG Portfolio Monitor pages.

Validation results for this pass:

```text
Documentation validation passed.
Conformance validation passed: 96/96 test rows across 4 levels.
Style validation passed.
Link validation passed (targets and internal Markdown anchors).
Fixture validation passed: 49 JSON files parsed.
Navigation validation passed for 192 rendered Markdown pages.
Diagram validation passed: 30 diagrams.
Operational validation passed.
Threat-model validation passed: 52 canonical threats.
Deployment profile validation passed.
Generated count validation passed: 96 conformance cases.
Interoperability validation passed: 3 governed DTG dependencies and 10 executable fixtures.
Learning-path validation passed: 5 paths and 24 steps.
Security-assurance validation passed: 14 guardrails mapped; 52 threats; RAHP provenance pinned.
```

A local Jekyll render was not executed in this workspace because the Ruby `bundle` executable was unavailable. Repository-level documentation, navigation, link, style, diagram and generated-artifact validators all completed successfully.

## Visual modelling and operational maturity pass — 2026-08-12

- Diagram register expanded from 30 to 38 governed visual models.
- Added registry authority/status lifecycle, verifier decision/failure pipeline, delegated-agent swimlane, credential/issuer lifecycle, operational incident lifecycle, wallet recovery swimlane, decision-ratification flow and conformance/assurance evidence pipeline.
- Diagram convention strengthened to express **authority → transition/event → evidence** where a visual represents governed state or operational action.
- Lifecycle landing page expanded into an orientation and evidence guide spanning credential/status, authority, key, delegation, policy and proof-system lifecycle.
- Operations landing page expanded into a common incident-state model and runbook index.
- Ten event/change runbooks plus the incident-evidence guide now implement a common structure for trigger, authority, containment, evidence, recovery, recovery test, redress and closure.
- `scripts/validate_operations.py` now enforces that runbook structure rather than checking only file presence.
- The GitHub Pages workflow now runs the full documentation, style, link, decision-governance, harness, interoperability and security-assurance validator set before the Jekyll build.
- YAML front matter and Liquid delimiter preflight completed successfully across 218 Markdown files.

Validation results for the consolidated pass:

```text
Documentation validation passed.
Conformance validation passed: 96/96 test rows across 4 levels.
Fixture validation passed: 49 JSON files parsed.
Threat-model validation passed: 52 canonical threats.
Deployment profile validation passed.
Operational validation passed: 10 runbooks + incident evidence guide structurally complete.
Navigation validation passed for 200 rendered Markdown pages.
Learning-path validation passed: 5 paths and 24 steps.
Diagram validation passed: 38 diagrams.
Generated count validation passed: 96 conformance cases.
Style validation passed.
Link validation passed (targets and internal Markdown anchors).
Decision governance validation passed: 20 decisions and 9 B1/B2 tests registered.
Conformance harness validation passed: 16 executable, 80 governed non-executable cases.
Interoperability validation passed: 3 governed DTG dependencies and 10 executable fixtures.
Security-assurance validation passed: 14 guardrails mapped; 52 threats; RAHP provenance pinned.
Front matter and Liquid-delimiter preflight passed across 218 Markdown files.
```

The local execution environment contains Ruby but does not contain the Jekyll/theme gems required by the repository, and outbound package installation is unavailable. The GitHub Pages build job remains the authoritative render gate: it installs the Gemfile dependencies with `ruby/setup-ruby`, runs the full validator set, executes `bundle exec jekyll build --trace`, then runs `scripts/validate_site_output.py`. No source-level front-matter, Liquid delimiter, navigation, link or diagram issue remains from this pass.
