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
