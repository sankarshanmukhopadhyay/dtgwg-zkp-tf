---
layout: default
title: Wallet and holder implementation guide
nav_order: 3
parent: Implementation Guide
has_toc: true
---
# Wallet and holder implementation guide

The wallet protects holder-controlled keys, renders requests intelligibly, enforces consent and context boundaries, and prevents delegated agents from exceeding granted authority.

## Required controls

- protected key storage and recovery;
- request origin and policy display;
- local minimization before proving;
- anti-replay transcript binding;
- separation of holder binding from delegation;
- shared-device user separation;
- recovery that preserves revocation and uniqueness state;
- evidence of consent without retaining unnecessary proof material.
