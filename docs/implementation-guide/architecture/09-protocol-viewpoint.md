---
layout: default
title: "Protocol viewpoint"
parent: "Architecture"
grand_parent: "Implementation Guide"
nav_order: 9
has_toc: true
---
# Protocol viewpoint

A typical transaction proceeds through request construction, authorization, proof generation, presentation, verification, policy evaluation and evidence recording.

1. The verifier constructs a canonical request containing context, epoch, nonce, predicates, policy version and accepted profiles.
2. The wallet validates requester authority and displays or evaluates the request against holder policy.
3. An agent-mediated request also supplies delegation evidence and may trigger a human step-up.
4. The proof generator binds the proof to the canonical transcript and required credential or registry state.
5. The verifier validates syntax, freshness, transcript binding, proof semantics, status, accreditation and relying-party policy.
6. The verifier returns a disclosure-safe result and records a decision receipt.
7. A rejected transaction follows deterministic retry, fallback or termination rules.

The protocol must not downgrade a missing predicate, stale registry result or invalid delegation into successful verification. Any degraded path has a distinct policy outcome and evidence record.
