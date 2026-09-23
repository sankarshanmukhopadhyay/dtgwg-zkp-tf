---
layout: default
title: "Record 008 Blinded-Binder and Correlation Evidence"
parent: "Conformance"
nav_order: 43
---
# Record 008 blinded-binder and correlation evidence

This downstream evidence profile is pinned to canonical upstream construction record 008 at `cfd94063e5cfee7ba6df4dcfd28c10399a0ffd0a`.

It reuses the existing Pedersen-style PR-HID construction evidence as an implementation asset, while treating **record 008** as the semantic authority for the blinded task/exchange citation proposition.

## Executable cases

| Case | Expected outcome | Boundary |
|---|---|---|
| R008-POS-OPEN | accept | authenticated source plus valid hidden opening |
| R008-NEG-WRONG-OPENING | reject `binder-mismatch` | commitment does not open to verifier-held citation |
| R008-NEG-PLAINTEXT | reject `binder-plaintext-present` | carrying plaintext beside the commitment defeats the hiding purpose |
| R008-NEG-ENUMERABLE | reject `enumerable-binder-recoverable` | deterministic low-entropy digest is dictionary-recoverable |
| R008-NEG-STABLE-CORRELATION | reject `stable-binder-correlatable` | a visible reusable commitment cannot support a presentation-unlinkability claim |
| R008-POS-VISIBLE-NARROW-CLAIM | accept narrow binding claim | visible commitment can still bind while remaining correlatable |
| R008-NEG-UNAUTHENTICATED-SOURCE | reject | opening a commitment does not authenticate the credential/artifact carrying it |
| R008-NEG-TASK-COMPLETION | reject | binding to an exchange does not establish that the task completed |

## What the existing Pedersen evidence contributes

`EXP-PR-HID-PEDERSEN-01` already provides executable construction evidence for:

- valid opening;
- wrong-value rejection;
- wrong-blinding rejection;
- independently blinded commitments to the same value being distinct; and
- dictionary recovery against a deterministic low-entropy digest.

That evidence is now interpreted as **reuse_evidence for record 008**, not as a competing PR-HID semantic definition.

## Critical privacy distinction

There are three different statements:

1. **plaintext hiding** — the verifier need not receive the cited task/exchange identifier in the credential;
2. **commitment binding** — the holder can prove that the commitment opens to the verifier-held exchange;
3. **presentation unlinkability** — repeated presentations do not carry a stable value by which they can be compared.

Record 008 can support the first two. The third is false if the same visible commitment is carried across presentations.

Therefore a deployment MUST NOT upgrade "citation hidden" into "presentation unlinkable" without evidence that the commitment itself is hidden or otherwise presentation-specific.

## External boundary

Credential Spec issue #58 owns the decision about the credential member/representation that carries the committed citation and how the blinding value is provisioned.

This downstream repository does not invent that credential property.

Task completion, outcome evidence and receipts remain Trust Task/framework concerns rather than consequences of a successful binder opening.

## Reuse

The fixture suite in `fixtures/record-008-blinded-binder.json` and the existing PR-HID construction benchmark can be consumed by Trust Task integration and composed proof work without creating a stable correlation handle by accident.
