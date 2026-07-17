---
layout: default
title: Hybrid proving deployment profile
nav_order: 5
parent: Implementation Guide
has_toc: true
---
# Hybrid proving deployment profile

Hybrid deployments select local or remote proving by device capability, policy or availability. Selection rules, user disclosure and fallback behavior are part of the profile.

The implementation shall prevent silent downgrade to a more observable mode. Decision evidence identifies the selected mode, policy version and fallback reason without retaining witness data.
