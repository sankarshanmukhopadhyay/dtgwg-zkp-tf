# v0.4.0 — DTG Interoperability and Cross-Specification Assurance

v0.4.0 connects the ZKP implementation and assurance workspace to evolving DTG credential, Trust Task/Trust Ceremony and RAHP work without transferring authority across specifications.

## Highlights

- governed, machine-readable DTG dependency and portfolio alignment model;
- explicit credential-linkage assurance profile for relationship-dependent ZKP constructions;
- Trust Task and Trust Ceremony binding profiles with hard separation between protocol context and authority;
- RAHP-aligned, reproducible cross-specification pressure tests;
- four new interoperability scenarios and eight conformance tests;
- ten executable interoperability fixtures;
- seven new cross-specification threats, expanding the canonical threat model from 45 to 52 threats;
- updated decision governance and requirement traceability for the new profiles.

## Assurance stance

This release deliberately fails closed when a proof statement depends on unresolved credential relationship semantics. It also prevents task or ceremony participation from being interpreted as delegated authority, and requires stable linkage/ceremony references to be assessed as correlation surfaces.

## Upstream authority boundaries

- Credential TF remains authoritative for credential and identifier relationship semantics.
- Trust Tasks TF remains authoritative for Trust Task and Trust Ceremony protocol semantics.
- RAHP remains authoritative for its reusable pressure-testing method.
- ZKP TF remains authoritative only for the ZKP profile requirements and assurance conclusions proposed here.

## Validation

The release is accepted only if repository documentation, navigation, conformance, fixtures, threat model, security assurance, decision governance, interoperability and traceability checks pass.
