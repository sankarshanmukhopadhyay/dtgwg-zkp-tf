---
layout: default
title: Delegated-agent implementation guide
nav_order: 6
parent: Implementation Guide
has_toc: true
---
# Delegated-agent implementation guide

Agent authority shall be explicit, scoped, time-bounded and revocable. Holder binding does not establish agent authorization.

A delegation record identifies principal, agent, permitted actions, contexts, limits, validity, step-up triggers and revocation source. The verifier checks delegation after proof validity but before relying-party authorization. High-impact actions require step-up or direct human authorization where the policy demands it.
