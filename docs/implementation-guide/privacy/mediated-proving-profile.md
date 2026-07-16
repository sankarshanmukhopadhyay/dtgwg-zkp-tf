---
title: Mediated proving profile
status: incubating
normative_status: non-normative
owner: DTG ZKP Task Force
last_reviewed: 2026-07-16
---


# Mediated proving profile

Mediated proving is a separate deployment profile, not a transparent substitute for local proving.

A mediated prover declares input and witness exposure, isolation boundary, operator, authentication, transcript binding, logging, retention, deletion, incident response, user disclosure and verifier-visible assurance difference. Witness-related material and stable request mappings must not be retained beyond the operation unless a separately governed purpose and explicit profile permits it.

Conformance evidence includes architecture review, configuration evidence, retention tests, log inspection, operator audit, collusion analysis and a negative test demonstrating that silent fallback to mediation is rejected.
