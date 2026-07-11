# DTG ZKP Task Force

A task force of the [Decentralized Trust Graph Working Group](https://lf-toip.atlassian.net/wiki/spaces/HOME/pages/257785857/Decentralized+Trust+Graph+Working+Group) (DTGWG) at the Trust over IP Foundation (ToIP), part of Linux Foundation Decentralized Trust (LFDT).

## Mission

Design and deliver a specification for how DTG verifiable trust agents (VTAs) can produce **privacy-preserving zero-knowledge proofs** of DTG credentials — for **proof of personhood** and **biometric liveness** of the principal — without revealing identity, the underlying biometric, or the proprietary means of the determination.

## Deliverable

**DTG ZKP V1.0** — a specification defining the requirements for conformant ZK proofs of:

- the DTG credentials held by the principal,
- the biometric liveness of the principal, and
- any other trust signals the principal agrees to share with a verifier.

It will also cover any trust-task protocols specific to generating, presenting, or verifying these proofs that aren't already specified in **DTG Core Trust Task Protocols V1.0** (from the Trust Task Protocols TF).

## Milestone

A complete **Working Draft ready for discussion at IIW #43 (3–5 November 2026)**. Interim target: a shareable strawman of the proof-of-liveness requirements by September, to put in front of the cryptography teams.

## How we work

A weekly working call plus async work on GitHub. The weekly call (being scheduled — watch Discord) sets the agenda and reviews progress; long-form work and decisions happen here on GitHub (issues + discussions), with short-form notices in Discord and status reports at the DTGWG weekly.

## Leadership

- **Chair:** Scott Jones (Realeyes)
- **Co-chair:** Mitchell Travers (Soulbis)

## Get involved

1. Be a member of **ToIP or DIF** (see the [DTGWG home page](https://lf-toip.atlassian.net/wiki/spaces/HOME/pages/257785857/Decentralized+Trust+Graph+Working+Group) for how to join).
2. Join the Discord channel **#toip-dtgwg-zkp-tf** for short-form discussion.
3. Comment on [issues](https://github.com/trustoverip/dtgwg-zkp-tf/issues) and [discussions](https://github.com/trustoverip/dtgwg-zkp-tf/discussions) in this repo.
4. Add your name to the [TF wiki page](https://lf-toip.atlassian.net/wiki/spaces/HOME/pages/948240390/DTG+ZKP+Task+Force).

We especially want **cryptographers and cryptographic engineers** who can pressure-test what's implementable at scale, and **implementers / relying parties** with concrete use cases that need privacy-preserving liveness.

## First work item

Our opening decision is **which ZK proof type(s) to use** for each requirement — not a survey of every proof construction, but a specific, conformant choice per predicate. Not all ZK proofs are equal, and liveness/personhood need particular constructions. The requirements draft below frames that decision, and it's the first thing we'll converge on as a group.

## Where to start

- [`proof-of-liveness-requirements.md`](./proof-of-liveness-requirements.md) — a v0.1 strawman of what a privacy-preserving proof of liveness must prove, in what context, and the inputs/outputs at each boundary, plus candidate proof-type mappings to confirm (Section 4). Starting point for discussion, not a settled position.

## Coordination with related work

- **Credentials TF** and **Trust Task Protocols TF** — define the credential formats and protocols our proofs apply to (upstream of us).
- **LFDT / UC Berkeley ZKP work** — the build priority for the October Linux Plumbers / OpenVTC track; we aim to keep our proof definitions in sync with it.

## Intellectual property

Inherits the DTGWG [JDF Charter](https://lf-toip.atlassian.net/wiki/spaces/HOME/pages/257785857/Decentralized+Trust+Graph+Working+Group) IPR terms:

- Copyright: Creative Commons Attribution 4.0
- Patent: W3C Mode
- Source code: Apache 2.0

## Links

- [TF wiki / charter page](https://lf-toip.atlassian.net/wiki/spaces/HOME/pages/948240390/DTG+ZKP+Task+Force)
- [DTGWG home](https://lf-toip.atlassian.net/wiki/spaces/HOME/pages/257785857/Decentralized+Trust+Graph+Working+Group)
- [ZKP background page](https://lf-toip.atlassian.net/wiki/spaces/HOME/pages/257949824/Zero-Knowledge+Proofs+ZKPs)
- [ToIP meeting calendar](https://zoom-lfx.platform.linuxfoundation.org/meetings/ToIP?view=month)
