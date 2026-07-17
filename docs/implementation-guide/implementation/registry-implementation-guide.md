---
layout: default
title: Registry implementation guide
nav_order: 5
parent: Implementation Guide
has_toc: true
---
# Registry implementation guide

A registry publishes recognition, status and authority state. It does not create authority merely by listing an entry.

Required properties include signed and versioned state, effective and expiry times, provenance, conflict behavior, bounded caching, authenticated publication, revocation and correction, and evidence of operator actions. Federation shall define which authority resolves disagreement and how stale or partitioned state is treated.
