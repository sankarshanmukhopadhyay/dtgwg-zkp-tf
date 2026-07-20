---
layout: default
title: "Mediated proving profile"
parent: "Privacy Engineering"
grand_parent: "Implementation Guide"
nav_order: 2
has_toc: true
---
# Mediated proving profile

Mediated proving is a separate deployment profile, not a transparent substitute for local proving.

A mediated prover declares input and witness exposure, isolation boundary, operator, authentication, transcript binding, logging, retention, deletion, incident response, user disclosure and verifier-visible assurance difference. Witness-related material and stable request mappings must not be retained beyond the operation unless a separately governed purpose and explicit profile permits it.

Conformance evidence includes architecture review, configuration evidence, retention tests, log inspection, operator audit, collusion analysis and a negative test demonstrating that silent fallback to mediation is rejected.
