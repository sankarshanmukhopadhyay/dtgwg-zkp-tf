---
layout: default
title: "Observability and data minimization"
parent: "Secure Deployment"
grand_parent: "Implementation Guide"
nav_order: 11
has_toc: true
---
# Observability and data minimization

Collect enough telemetry to operate and investigate without creating a proof-event correlation system. Prefer counters, outcome codes, latency, version and integrity events over credentials, witnesses, nullifiers or complete presentation payloads.

Every retained field has a purpose, access policy, retention period and deletion control. Debug modes are time-bounded and separately authorized.
