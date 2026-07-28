# GitHub copy-ready content for v0.3.0

## Commit title

`feat: add governed context and privacy-class conformance`

## Commit message

```text
feat: add governed context and privacy-class conformance

Introduce a machine-readable decision register that separates upstream
ratification state from the fork's implementation baseline.

Add governed context and privacy-claim schemas, positive and negative
fixtures, named privacy classes, B1/B2 conformance cases, decision-impact
guidance, and automated decision-governance validation.

Keep all Task Force ratification items explicitly pending and preserve the
deferral of proof-construction selection.

Prepare the repository for the v0.3.0 release.
```

## Release tag

`v0.3.0`

## Release title

`v0.3.0 — Governed Context and Privacy-Class Conformance`

## Release description

```markdown
## Summary

v0.3.0 turns the pending DTG ZKP decision set into an explicitly governed and testable implementation baseline. It does not claim upstream ratification. Instead, it cleanly separates Task Force decision state from the implementation state of this fork.

The release concentrates on the two load-bearing open decisions: the context delimiter and the issuer-verifier collusion target.

## What is new

- Machine-readable decision register for A1–A7, B1–B10 and deferred construction selection
- Ratification and amendment procedure with decision-impact controls
- Canonical governed context descriptor schema
- Named PC-1, PC-2, PC-3 and PC-R privacy classes
- Machine-readable privacy claim schema with evidence and downgrade requirements
- Positive and negative context and privacy fixtures
- Nine B1/B2 decision-conformance cases
- Automated decision-governance validation
- Explicit non-normative and pending-ratification status controls

## Scope and authority

The repository implements the proposed positions as a working baseline for review, testing and upstream contribution. All ratification items remain marked `pending-ratification`. Specific cryptographic construction selection remains deferred until boundary decisions are settled and candidate constructions are benchmarked.

## Validation

```sh
python3 scripts/validate_decision_governance.py
python3 scripts/validate_fixtures.py
python3 scripts/validate_docs.py
python3 scripts/validate_navigation.py
```

## Compatibility

This is an additive minor release. It does not change an existing proof construction or invalidate current implementation profiles. Strong privacy claims should adopt the new class model and evidence requirements.
```
