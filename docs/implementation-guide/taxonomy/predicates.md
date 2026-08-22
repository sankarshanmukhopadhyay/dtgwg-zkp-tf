---
layout: default
title: "Predicate taxonomy"
parent: "Taxonomy"
grand_parent: "Implementation Guide"
nav_order: 2
has_toc: true
---
# Predicate taxonomy

| ID | Predicate | Establishes | Does not establish |
|---|---|---|---|
| [`PR-LIV`](../reference/identifier-register.md#pr-liv) | liveness attestation | qualifying attestation possession | correctness of biometric determination |
| [`PR-PER`](../reference/identifier-register.md#pr-per) | personhood policy | satisfaction of named policy | civil identity or global uniqueness |
| [`PR-ISS`](../reference/identifier-register.md#pr-iss) | accredited issuer | membership in accepted framework/set | quality of every issuer operation |
| [`PR-UNQ`](../reference/identifier-register.md#pr-unq) | scoped uniqueness | reuse detection for scope and epoch | one natural person globally |
| [`PR-HLD`](../reference/identifier-register.md#pr-hld) | holder binding | control of holder key/secret | agent authority or non-transfer |
| [`PR-FRE`](../reference/identifier-register.md#pr-fre) | freshness | challenge/transcript binding | non-coercion or comprehension |
| [`PR-RNG`](../reference/identifier-register.md#pr-rng) | range predicate | attested value falls in range | exact value, except inference risk |
| [`PR-DEL`](../reference/identifier-register.md#pr-del) | delegated/current authority | presenter has current authority for the requested action under the selected delegation profile | liveness, holder identity, or authority outside the proved scope/time/context |
| [`PR-CMP`](../reference/identifier-register.md#pr-cmp) | composed-presentation privacy | declared privacy class survives the complete evidence closure required for the relying decision | privacy of any omitted or separately resolved evidence not included in the analysis |
| [`PR-REL`](../reference/identifier-register.md#pr-rel) | privacy-preserving relationship proof | required relationship between credentials, tasks, delegation or other evidence is established without an undeclared durable cross-context correlator | semantics or authority not contained in the governed relationship statement |
| [`PR-HID`](../reference/identifier-register.md#pr-hid) | confidential binding | bound value satisfies the profile's required hiding property, including against feasible enumeration | integrity or authenticity of the bound value unless separately established |
| [`PR-RES`](../reference/identifier-register.md#pr-res) | privacy-preserving external resolution | required external status/registry/accreditation/authorisation state is evaluated without an undeclared verifier-to-subject correlation channel | freshness or authority beyond the external state and evaluation time actually proved |
