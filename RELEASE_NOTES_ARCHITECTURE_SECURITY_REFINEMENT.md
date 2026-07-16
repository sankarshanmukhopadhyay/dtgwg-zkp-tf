# Release notes: Architecture and security refinement

## Summary

This update turns the implementation guide's boundary and privacy principles into linked, machine-checkable architecture and conformance artefacts. It remains proof-system agnostic and preserves the Minimum Liveness and Extended Personhood profile split.

## Added

- paired assurance and disclosure boundary templates and predicate register;
- context decision record with collusion and human-legibility requirements;
- attestation schema profile, field register and correlation assessment;
- canonical YAML threat matrix with 36 threats, generated CSV and Markdown views;
- harm taxonomy, control catalogue, residual-risk register and deployment template;
- profile-specific threat views for minimum liveness, extended personhood and mediated proving;
- composition, reconstruction and observable-event analysis;
- mediated-proving isolation and non-retention profile;
- cryptoperiod, assurance-horizon and proof-system migration guidance;
- ADR-006 through ADR-011;
- boundary, schema, lifecycle and mediated-proving fixtures plus a boundary schema;
- 12 additional positive and negative conformance tests;
- threat-model validation script.

## Changed

- the main guide now requires every material claim to state against whom, for how long and alongside what it applies;
- conformance and evidence schemas now carry boundary, threat, lifecycle and residual-risk references;
- drafting and editorial rules now prevent transcript properties from being overstated as system properties;
- readiness gates now require bounded lifecycle, threat-control coverage and explicit residual-risk decisions.

## Deliberately unresolved

No cryptographic construction is selected or implied as ratified. Construction families remain subject to task-force decisions informed by the new boundaries, threat model and migration criteria.
