# Release notes: Security guardrails and operational assurance

## Summary

This release extends the ZKP implementation guide from a threat-and-control baseline to an executable security-assurance model. It adds activation guardrails, formal risk acceptance, privacy-bounded metrics, assurance tests, governance-abuse threats, decision-authority rules and machine-verifiable traceability.

## RAHP provenance

The methodological structure was adopted and adapted from the Trust over IP DTGWG Risk Assessment & Harms Prevention Task Force repository: [trustoverip/dtgwg-rahp-tf](https://github.com/trustoverip/dtgwg-rahp-tf), reviewed at commit [`94d17a6f5e8b448aae4698ff183e77a4a2f7a083`](https://github.com/trustoverip/dtgwg-rahp-tf/commit/94d17a6f5e8b448aae4698ff183e77a4a2f7a083).

The release adopts RAHP's distinctions among risks, controls, guardrails, assurance tests, metrics and phase gates, then adapts them to ZKP profiles, cryptographic controls, deployment activation and operational evidence. The complete mapping and attribution boundary are documented in `docs/implementation-guide/security/rahp-adoption-and-adaptation.md` and `docs/implementation-guide/matrices/rahp-adaptation-map.csv`.

## Added

- 14 ZKP security guardrails and assurance tests
- formal risk appetite, authority, expiry and revocation rules
- 14 privacy-bounded security and trust indicators
- nine governance, assurance and affected-party threat scenarios
- machine-readable assurance and metric evidence schemas
- four new traceability matrices plus a RAHP adaptation map
- five GitHub Pages-compatible Mermaid diagrams
- automated security-assurance validation

## Compatibility

The change is additive. Existing `THR-001` through `THR-036`, `CTL-xxx` control families and profile semantics are preserved. RAHP identifiers are not imported as normative ZKP identifiers.
