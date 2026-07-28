# v0.3.0 — Governed Context and Privacy-Class Conformance

## Summary

v0.3.0 converts the Task Force's pending decision set into an explicitly governed, testable implementation baseline. The release does not claim upstream ratification. It separates upstream decision state from fork implementation state and adds executable artefacts for the two load-bearing open decisions: the context delimiter and issuer-verifier collusion target.

## Highlights

- Adds a machine-readable decision register covering A1–A7, B1–B10 and deferred construction selection.
- Introduces a controlled ratification and amendment procedure with impact records.
- Defines a canonical governed context descriptor with authority, purpose, verifier-set, epoch, linkability, change-control and human-legibility fields.
- Defines PC-1, PC-2, PC-3 and PC-R privacy classes with evidence and downgrade rules.
- Adds schemas, valid fixtures and negative fixtures for context and privacy claims.
- Adds nine B1/B2 decision-conformance cases.
- Adds automated decision-governance validation.
- Clarifies that an implemented fork baseline is non-normative until the Task Force records a ratified outcome.

## Governance position

All upstream ratification items remain `pending-ratification` in the release register. Specific cryptographic construction selection remains deferred. The fork's artefacts are implementation and review aids, not a substitute for Task Force authority.

## Validation

Run:

```sh
python3 scripts/validate_decision_governance.py
python3 scripts/validate_fixtures.py
python3 scripts/validate_docs.py
python3 scripts/validate_navigation.py
```

## Upgrade notes

No existing profile identifier or proof construction is changed. Implementers may adopt the new context and privacy-claim records incrementally. Claims of issuer-verifier collusion resistance should migrate to PC-3 only when the full evidence set is available; otherwise use the supported lower class or PC-R disclosure.
