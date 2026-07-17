---
layout: default
title: Federated registry deployment profile
nav_order: 7
parent: Implementation Guide
has_toc: true
---
# Federated registry deployment profile

Federation separates publication authority, recognition authority, distribution and caching. Each record identifies its source authority, version, effective time, expiry and signature chain.

Conflict policy defines whether disagreement causes rejection, bounded fallback or escalation. Cache freshness and partition behavior are explicit. Federation does not permit a distributor to rewrite authority or status.
