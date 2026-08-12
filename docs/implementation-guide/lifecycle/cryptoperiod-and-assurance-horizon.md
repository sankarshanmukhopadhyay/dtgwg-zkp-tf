---
layout: default
title: "Cryptoperiods and assurance horizons"
parent: "Lifecycle and Migration"
grand_parent: "Implementation Guide"
nav_order: 1
has_toc: true
---
# Cryptoperiods and assurance horizons

Different artefacts operate on different clocks. Each profile records at least:

| Artefact or claim | Required temporal control |
|---|---|
| proof transcript | validity and replay window |
| attestation | issuance, expiry and status freshness |
| enrolment root | cryptoperiod, backup treatment and rotation trigger |
| nullifier | epoch, retention and deletion |
| privacy claim | assurance horizon over which unlinkability is asserted |
| biometric method | assurance review horizon and model-change trigger |
| registry/policy state | effective time and cache age |
| logs and receipts | retention, access and deletion |

An unbounded epoch, indefinite enrolment root or privacy claim without an assurance horizon fails profile review.

## Retention is not validity

A retention obligation can outlive the assurance that supported the original decision. A profile that retains evidence for an extended period, including a profile designed for a seven-year KYC/AML hold, records separately:

- the original evaluation time and status snapshot;
- the cryptoperiod and suite-security horizon;
- the nullifier/reuse-state retention period;
- the audit or legal retention period; and
- whether later verification is a historical “as of T” evaluation or a new present-time reliance decision.

Long retention does not extend cryptographic, biometric, accreditation, governance, or privacy validity by implication.

## Post-quantum migration

V1 may use pre-quantum constructions, but every profile records migration triggers and overlap rules. Hash chaining or another succession mechanism may preserve evidence lineage across rotations only for the properties it explicitly claims; it does not restore a security property lost when an underlying primitive is no longer trustworthy.
