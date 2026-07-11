# Privacy-Preserving Proof of Liveness — Requirements (v0.1)

**Status:** Strawman for discussion. It states what a privacy-preserving proof of liveness must prove, in what context, and the inputs/outputs at each boundary — the requirements that drive our **first decision: which ZK proof type(s) to use** (Section 4). The goal is a specific, conformant construction, not a survey of ZKP options. Deliberately vendor-neutral.

**Author:** Scott Jones (Realeyes), Chair, DTG ZKP Task Force · v0.1

---

## 1. Purpose

Define the task force's first work item: a precise statement of the proof(s) the decentralized trust graph needs for human liveness and personhood — specific enough that a cryptographer can answer *"can we build a ZKP that does exactly this, and which construction?"* and a biometric provider can answer *"can we supply exactly these inputs and consume this output?"*

## 2. Problem statement

Wallet and credential ecosystems have converged on zero-knowledge proofs as the path to unlinkability at population scale; batch issuance does not hold up economically or operationally. Two problems remain unsolved for human presence specifically:

- **The user-as-adversary problem.** At scale the presenter is frequently the adversary — one human spinning up many accounts, or a human handing control to a bot. The proof must be hard for the *presenter* to game, not only hard for a third party to forge.
- **The proprietary-model obscuring problem.** A determination of "a real, live human is present" rests on proprietary neural-network models. The proof must let a verifier rely on the assertion without exposing the model internals, the raw biometric, or a correlatable identity.

## 3. What must be proved

Candidate predicates, to be confirmed and prioritised. Each is a property a verifier can check without learning identity:

- **Liveness** — a live human was present at the moment of the check; not a replay, injected feed, or synthetic/deepfake artefact.
- **Personhood** — the presenter is a real, unique human, attested by an accredited issuer.
- **Uniqueness within a context** — distinct from others in a defined scope (e.g. one enrolment per service); duplicate / Sybil resistance without a global identifier.
- **Holder / agent binding** — the live human is bound to a specific holder key or authorised agent for this session.
- **Freshness** — the liveness event is recent and bound to this session transcript / challenge, defeating replay.

**Non-goals:** this proof asserts humanness and presence, not civil identity ("who you are"). Interoperable, not bound to one vendor or model.

## 4. Proof types — the first decision to converge on

Not all ZK proofs are equal; liveness and personhood call for specific constructions, not a catalogue of every proof type. The task force's **first substantive decision** is to choose the proof type(s) for each predicate, so the spec targets a specific, conformant outcome. Candidate mappings below are a **starting point to confirm with the cryptography teams** — the opening working-group discussion should converge here before we draft spec text.

| Predicate | Candidate proof construction (to confirm) |
|---|---|
| Liveness attestation | Proof of a valid issuer signature over a liveness attestation, without revealing the attestation |
| Personhood / accredited issuer | One-of-many (set-membership) proof that the issuer ∈ an accredited set, without revealing which issuer |
| Uniqueness within a context | Nullifier-based scheme (deterministic per-context pseudonym) for duplicate / Sybil resistance without a global identifier — cf. privacy-pool / Semaphore-style nullifiers |
| Holder / agent binding | Proof of knowledge of the holder key, bound to the session |
| Freshness | Binding to a verifier challenge / nonce / session transcript (a constraint layered on the above) |
| Demographic range (if in scope) | Range proof over an attested attribute |

**Design note — uniqueness needs more than a ZKP.** A ZKP proves a statement privately; it does not by itself make a person unique. Uniqueness / Sybil resistance depends on (a) an enrolment that deduplicates humans — a biometric that reliably maps one person to one value is the strongest option — and (b) a nullifier construction that yields one deterministic pseudonym per person per context. The ZKP makes this privacy-preserving; the anti-Sybil strength comes from the deduplicating enrolment, not the proof itself. Pinning down this combination, and how strong a guarantee it gives, is a core task-force question.

## 5. Context — where the proof is requested

Covers both human-facing and agent scenarios. Each context sets the predicates required.

| Context | Example | Predicates required |
|---|---|---|
| Account creation / sign-up | Dating app, marketplace, or social platform — one real person per account | Personhood + uniqueness + liveness |
| Age-gated access | Adult content, gambling, alcohol delivery | Liveness + demographic range (age) |
| Login / re-authentication | Returning user proving it's still the same human | Liveness + freshness + same-human-as-enrolment |
| High-value / sensitive action | Moving funds, changing security settings | Liveness + freshness + holder binding |
| Account recovery | Regaining access after lockout | Liveness + personhood + uniqueness |
| Agent authorisation (day-zero) | A human anchoring / authorising an AI agent | Liveness + personhood + holder binding |
| Agent step-up | Human-in-the-loop on intent drift, a new permission, or a new environment | Liveness + freshness |

## 6. Inputs the biometric provider supplies

- A liveness / human-presence determination (pass + assurance level), signed as an attestation by the accredited issuer.
- A privacy-preserving binding artefact (e.g. a commitment derived from the biometric) supporting uniqueness and same-human checks **without** storing or revealing a raw template.
- Session binding material (challenge / nonce / transcript) so the determination is fresh and non-replayable.

**Open question:** how to encode the proprietary determination so the proof carries its assurance without revealing the model.

## 7. Standard output to the verifier

- **Receives:** a verifiable proof that the required predicates hold (e.g. "live, unique human, bound to this holder, fresh as of the check"), plus the assurance level and the set the issuer belongs to.
- **Must not learn:** the person's identity, the raw biometric or template, the specific issuer (only that it is one of an accredited set), or anything that lets two verifiers correlate the same user.

## 8. Privacy & trust requirements

- Unlinkability across presentations and across verifiers; no issuer–verifier collusion can re-identify the user.
- No central biometric honeypot; binding artefacts must not be reversible to a template.
- Modular by design — this liveness/personhood proof is one block in the shared framework, able to compose with credential and trust-task proofs.
- Pre-quantum acceptable for v1, with a documented path to post-quantum.

## 9. Open questions for the cryptography teams

1. Which proof construction per predicate (Section 4) — the first decision.
2. Encoding a proprietary-model determination inside a ZKP while preserving its assurance.
3. Uniqueness / Sybil resistance scoped to a context without a global identifier — nullifier design and cost.
4. Practical proof-generation cost on a consumer device, and the claim ceiling per presentation.
5. Revocation / refresh cadence for a personhood or liveness assertion.

## 10. Next steps

1. **Converge on the proof type(s) for each predicate (Section 4)** — the first working-group decision.
2. Gather comments on this strawman from the TF and co-chair.
3. Align predicates with the Credentials TF and Trust Task Protocols TF.
4. Review feasibility with the cryptography teams (Matsuo / BGIN network, UC Berkeley, SIROS ZKP group); keep in sync with the LFDT/Berkeley build for October.
5. Target a group-endorsed Working Draft for IIW #43 (3–5 November 2026).
