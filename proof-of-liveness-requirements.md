# Privacy-Preserving Proof of Liveness — Requirements (v0.2)

**Status:** Strawman for discussion. It states what a privacy-preserving proof of liveness must prove — and, just as importantly, **what it does not establish** — in what context, and the inputs/outputs at each boundary. These requirements drive our decision on **which ZK proof type(s) to use** (Section 5). The goal is a specific, conformant construction, not a survey of ZKP options. Deliberately vendor-neutral.

**Author:** Scott Jones (Realeyes), Chair, DTG ZKP Task Force
**v0.2** — revised following [Sankarshan Mukhopadhyay's review](https://github.com/trustoverip/dtgwg-zkp-tf/discussions/3). See the changelog at the end.

---

## 1. Purpose

Define the task force's first work item: a precise statement of the proof(s) the decentralized trust graph needs for human liveness and personhood — specific enough that a cryptographer can answer *"can we build a ZKP that does exactly this, and which construction?"* and a biometric provider can answer *"can we supply exactly these inputs and consume this output?"*

## 2. Problem statement

Wallet and credential ecosystems have converged on zero-knowledge proofs as the path to unlinkability at population scale; batch issuance does not hold up economically or operationally. Two problems remain for human presence specifically:

- **The user-as-adversary problem.** At scale the presenter is frequently the adversary — one human spinning up many accounts, or a human handing control to a bot. The proof must be hard for the *presenter* to game, not only hard for a third party to forge.
- **The proprietary-model problem.** A determination of "a real, live human is present" rests on proprietary neural-network models. This was long treated as the blocker for face-based personhood. Section 3 states how it is resolved.

## 3. What the proof does — and does not — establish

**This is the boundary that everything else depends on.**

> A ZKP proves possession of, and selected properties about, **an attestation**. It does not prove that the underlying biometric determination was **correct**.

So the proof does **not** encode or validate a proprietary model's judgement. Instead, the holder proves possession of a valid attestation issued by an **accredited issuer**, under a **stated policy and assurance class**. Accountability for the correctness of the determination sits with the issuer, under a governance framework — not with the cryptography.

This must be explicit in the specification. Conflating "the proof verified" with "the human was correctly determined to be live" would misrepresent what the system guarantees.

**Corollaries:**
- "Valid signature" is not the full claim. The proof must also cover whether the attestation was issued under an accepted policy, is within its validity period, is not revoked, and is bound to the relevant holder or session.
- **Key control ≠ agent authority.** Proof of holder-key control does not establish that the key was not transferred, nor that an agent's authority covers the current action. Agent authorization should be carried as separate, structured delegation evidence (principal, agent, scope, duration, revocation status) rather than folded into the cryptographic binding. *(Scoping consequences under discussion.)*

## 4. What must be proved

Candidate predicates, to be confirmed and prioritised. Each is a property a verifier can check without learning identity:

- **Liveness attestation** — the holder possesses a valid, unrevoked, in-date liveness attestation from an accredited issuer, issued under an accepted policy and assurance class, bound to this holder/session.
- **Personhood** — two propositions that a construction may combine but the spec should keep distinct: (a) the subject satisfies a personhood policy; (b) the issuer is accredited under a governance framework.
- **Uniqueness within a scope** — see the design note in Section 5; the claim must be stated narrowly.
- **Holder binding** — the holder controls the key bound to this session. (Agent authorization is separate — see Section 3.)
- **Freshness** — the proof is bound to a canonical, domain-separated transcript, defeating replay and cross-verifier correlation.

**Non-goals:** this proof asserts humanness and presence, not civil identity ("who you are"). Interoperable, not bound to one vendor or model.

## 5. Proof types — a decision to converge on

Not all ZK proofs are equal; liveness and personhood call for specific constructions, not a catalogue of every proof type. Candidate mappings below are a **starting point to confirm with the cryptography teams**.

| Predicate | Candidate proof construction (to confirm) |
|---|---|
| Liveness attestation | Proof of a valid issuer signature over a liveness attestation, plus policy / validity / revocation predicates, without revealing the attestation |
| Personhood / accredited issuer | One-of-many (set-membership) proof that the issuer ∈ an accredited set — see note on concealment below |
| Uniqueness within a scope | Nullifier-based scheme (deterministic per-scope, per-epoch pseudonym) — cf. privacy-pool / Semaphore-style nullifiers |
| Holder binding | Proof of knowledge of the holder key, bound to the session transcript |
| Freshness | Binding to a canonical, domain-separated transcript (below) |
| Demographic range | Range proof over an attested attribute — treat as an **extension**, not a dependency of the core |

**Freshness — what the transcript must bind.** A bare nonce is too narrow. Bind the proof to a canonical, domain-separated transcript containing at least: protocol ID, profile ID, verifier/audience, challenge, session ID, requested predicates, policy version, and expiry boundary. This is what makes replay resistance and cross-verifier separation testable.

**Issuer concealment is not mandatory in every profile.** A verifier may legitimately need the accreditation framework, policy version and assurance class, even where the specific issuer remains hidden. Concealment should be a profile choice, not a blanket assumption.

**Design note — uniqueness needs more than a ZKP, and the claim must be stated narrowly.** A nullifier construction supports this claim and no more:

> *The same enrolled subject secret cannot produce two accepted actions in the same scope and epoch without a repeated nullifier.*

That is materially weaker than "one unique human." Three distinct claims are easy to conflate:

1. **One action per enrolled secret, within a defined scope and epoch** — a nullifier construction can enforce this. *Cryptographic.*
2. **One enrolment per issuer or ecosystem** — depends on enrolment quality (a biometric that reliably deduplicates humans), controls against re-enrolment, recovery rules, and issuer coordination. *Not cryptographic — governance and biometrics.*
3. **One natural person globally** — much stronger, and **not implied** unless the architecture actually supports it.

The nullifier addresses (1) only. Nullifier inputs should be explicit: enrolment root/population, scope, epoch, purpose, profile ID, and rotation/recovery rules — so the guarantee is testable and we don't imply a stronger personhood claim than the system supports.

## 6. Context — where the proof is requested

Covers both human-facing and agent scenarios. Each context sets the predicates required.

| Context | Example | Predicates required |
|---|---|---|
| Account creation / sign-up | Dating app, marketplace, or social platform — one real person per account | Personhood + uniqueness + liveness |
| Age-gated access | Adult content, gambling, alcohol delivery | Liveness + demographic range (extension) |
| Login / re-authentication | Returning user proving it's still the same human | Liveness + freshness + same-human-as-enrolment |
| High-value / sensitive action | Moving funds, changing security settings | Liveness + freshness + holder binding |
| Account recovery | Regaining access after lockout | Liveness + personhood + uniqueness |
| Agent authorisation (day-zero) | A human anchoring / authorising an AI agent | Liveness + personhood + holder binding + delegation evidence |
| Agent step-up | Human-in-the-loop on intent drift, a new permission, or a new environment | Liveness + freshness + delegation evidence |

## 7. Inputs the biometric provider supplies

- A liveness / human-presence determination (pass + assurance class), signed as an attestation by an accredited issuer, under a stated policy.
- A privacy-preserving binding artefact (e.g. a commitment derived from the biometric) supporting uniqueness and same-human checks **without** storing or revealing a raw template.
- Session binding material feeding the canonical transcript (Section 5), so the determination is fresh and non-replayable.

## 8. Standard output to the verifier

- **Receives:** a verifiable proof that the required predicates hold (e.g. "holds a valid, unrevoked liveness attestation from an accredited issuer, bound to this holder, fresh as of this transcript"), plus the assurance class, policy version, and accreditation framework.
- **Must not learn:** the person's identity, the raw biometric or template, or anything that lets two verifiers correlate the same user. Whether the specific issuer is concealed is a **profile choice** (see Section 5).

## 9. Privacy & trust requirements

- Unlinkability across presentations and across verifiers; no issuer–verifier collusion can re-identify the user.
- No central biometric honeypot; binding artefacts must not be reversible to a template.
- Modular by design — composable with credential and trust-task proofs.
- Pre-quantum acceptable for v1, **provided** algorithm agility, profile identifiers, migration and deprecation are mandatory from day one. Post-quantum support should not block the first implementable release.

## 10. Ruled out (proposed)

- Claiming the ZKP proves the **correctness** of the biometric determination.
- Treating a nullifier as sufficient to establish one-human-one-record.
- Global stable identifiers or nullifiers.
- Raw biometrics or reversible templates anywhere in the proof flow.
- Mandatory civil-identity disclosure.
- Mandatory issuer concealment in every profile.
- Conflating holder-key control with human continuity or agent authority.
- Undocumented composition of multiple proofs.
- Proprietary verifier-only formats without interoperable test vectors.
- Requiring full personhood and uniqueness before anything can ship.
- Hard-coding one algorithm into the semantic model.

## 11. Open questions

1. Which proof construction per predicate (Section 5).
2. Trade-offs beyond proof size and prover cost: mobile/browser SDK support, verifier throughput, parameter distribution, library maturity, independent implementations, deterministic test vectors, revocation/refresh cost, offline verification, secure-hardware dependencies, version negotiation, error diagnosability — and **fallback behaviour** (if a device cannot generate the preferred proof: fail, step down to a lower-assurance profile, use a mediated prover, or switch channel?).
3. How strong a guarantee does claim (2) in the uniqueness note actually give, and what enrolment controls are needed to support it?
4. **Proposed sequencing, under discussion:** first deliverable becomes a short *predicate and assurance-boundary document* (what each predicate does and does not establish; who is accountable for which part of the claim), time-boxed, with construction selection sequenced behind it — and the work split into a **minimum liveness profile** (attestation possession, policy and assurance predicates, holder binding, transcript binding, expiry, revocation) and an **extended personhood profile** (set membership, scoped nullifiers, same-human-as-enrolment). To be settled at the first working call.

## 12. Next steps

1. Settle the sequencing proposal (Section 11.4) with the group at the first working call.
2. Converge on the proof type(s) per predicate (Section 5).
3. Align predicates with the Credentials TF and Trust Task Protocols TF.
4. Review feasibility with the cryptography teams; keep in sync with the LFDT/Berkeley ZKP work.
5. Target a group-endorsed Working Draft for IIW #43 (3–5 November 2026).

---

## Changelog

**v0.2** — Following review by @sankarshanmukhopadhyay:
- Added Section 3: the proof establishes possession of an attestation, **not** the correctness of the biometric determination; accountability sits with the accredited issuer under a governance framework.
- Separated key control from agent authority; agent authorization carried as structured delegation evidence.
- Narrowed the uniqueness claim; added the three-claim decomposition and explicit nullifier inputs.
- Freshness bound to a canonical, domain-separated transcript rather than a bare nonce.
- Issuer concealment made a profile choice, not a blanket assumption.
- Personhood split into two distinct propositions (subject policy; issuer accreditation).
- Demographic range moved to an extension.
- Added Section 10 (ruled out) and expanded trade-offs, including fallback behaviour.
- Recorded the proposed sequencing (boundary document first; minimum liveness vs extended personhood profiles) as an open question for the group.

**v0.1** — Initial strawman.
