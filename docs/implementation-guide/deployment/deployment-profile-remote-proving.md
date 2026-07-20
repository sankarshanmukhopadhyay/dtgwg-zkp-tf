---
layout: default
title: "Remote proving deployment profile"
parent: "Secure Deployment"
grand_parent: "Implementation Guide"
nav_order: 8
has_toc: true
---
# Remote proving deployment profile

A remote proving service may observe credentials, witnesses, requests, timing or network metadata. Its role and non-retention obligations must therefore be explicit and testable.

Controls include mutually authenticated channels, isolated jobs, encrypted transient storage, deletion verification, tenant separation, restricted telemetry, operator dual control and independent evidence that credential or witness material is not retained. Remote proving must not become an undeclared issuer, verifier or policy authority.
