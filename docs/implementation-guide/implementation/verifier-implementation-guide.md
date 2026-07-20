---
layout: default
title: "Verifier implementation guide"
parent: "Implementation"
grand_parent: "Implementation Guide"
nav_order: 5
has_toc: true
---
# Verifier implementation guide

The verifier executes a staged decision pipeline:

`parse → request validation → transcript binding → cryptographic verification → predicate evaluation → registry and status resolution → delegation validation → relying-party policy → outcome and evidence`

Each stage shall emit a stable failure code, evidence reference and retry classification. Policy rejection is distinct from cryptographic failure. Registry unavailability is distinct from negative status.

Verifier logs should retain decision identifiers, versions, timestamps and outcome codes while excluding credentials, witnesses and correlating proof material unless explicitly justified.
