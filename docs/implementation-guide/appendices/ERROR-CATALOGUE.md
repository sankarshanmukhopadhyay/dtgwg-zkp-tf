---
layout: default
title: "Error catalogue"
parent: "Appendices"
grand_parent: "Implementation Guide"
nav_order: 1
has_toc: true
---
# Error catalogue

| ID | Condition | Retry or fallback | Audit requirement |
|---|---|---|---|
| ERR-MALFORMED | request or presentation cannot be parsed canonically | correct and resubmit | record digest and parser reason |
| ERR-PROFILE | profile or predicate unsupported | negotiate only if policy permits | record offered and accepted profiles |
| ERR-CRYPTO | proof verification fails | terminate unless a fresh request is authorized | retain non-sensitive reason code |
| ERR-SEMANTIC | verified statement does not satisfy requested semantics | terminate | record predicate and policy mismatch |
| ERR-CONTEXT | context or epoch differs from request | issue a new canonical request | record mismatch without correlating identifiers |
| ERR-REPLAY | nonce or permitted-use condition has already been consumed | terminate and investigate | replay evidence |
| ERR-STATUS | credential or authority is expired, suspended or revoked | follow policy; no silent fallback | status source and effective time |
| ERR-REGISTRY-STALE | cached state exceeds permitted age | refresh or fail closed as policy declares | cache metadata and policy outcome |
| ERR-REGISTRY-UNAVAILABLE | required authoritative state cannot be resolved | explicit degraded or fail-closed path only | dependency and duration |
| ERR-DELEGATION | agent authority absent, expired, revoked or out of scope | require principal step-up or terminate | delegation reference and failed constraint |
| ERR-DOWNGRADE | weaker profile or path offered without authorization | reject | requested and attempted profile |
| ERR-ACCESSIBILITY | primary path cannot be completed accessibly | invoke documented alternative path | assurance difference and assistance used |
| ERR-TIMEOUT | dependency exceeds time budget | bounded retry or deterministic failure | dependency and elapsed time |
| ERR-INTERNAL | unexpected processing failure | no success response; safe retry policy | correlation-safe incident identifier |

User-facing messages should reveal enough to support correction and redress without exposing sensitive predicate, registry or correlation data.
