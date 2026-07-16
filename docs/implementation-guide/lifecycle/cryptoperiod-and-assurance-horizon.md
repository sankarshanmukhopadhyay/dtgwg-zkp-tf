---
title: Cryptoperiods and assurance horizons
status: incubating
normative_status: non-normative
owner: DTG ZKP Task Force
last_reviewed: 2026-07-16
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
