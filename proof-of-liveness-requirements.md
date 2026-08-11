# Privacy-Preserving Proof of Liveness — Requirements (fork working draft v0.4)

**Status:** Fork working draft for pressure testing and possible upstream contribution. It develops the upstream v0.3 requirements but is **not** a settled DTG ZKP specification and does not override upstream decisions.

**Upstream author:** Scott Jones (Realeyes), Chair, DTG ZKP Task Force  
**Fork expansion:** Maintained implementation/interoperability working draft based on upstream v0.3.

**Primary cryptographic reference:** [*A Cryptographic Framework for Proof of Personhood*](https://eprint.iacr.org/2026/333) — Choudhuri, Garg, Lee, Montgomery, Policharla, Sinha (IACR ePrint 2026/333). The paper formalises Sybil resistance, authenticated personhood and unlinkability across contexts, including the tension between Sybil resistance and stronger unlinkability goals.

---

## 1. Purpose

This document defines the properties that a DTG privacy-preserving liveness presentation needs to express before a proof construction can be selected responsibly.

It is intended to be precise enough that:

- a cryptographer can determine whether a requested property is constructible and under which assumptions;
- a biometric or personhood provider can determine which attestations and binding artefacts it must produce;
- a wallet or prover implementer can determine which inputs, state and transcript elements are required;
- a verifier can determine exactly what successful verification authorises it to conclude;
- a governance or assurance function can determine which claims depend on non-cryptographic controls; and
- a conformance suite can distinguish protocol failure, assurance failure and privacy failure.

The document is proof-system agnostic. It defines semantic and assurance requirements first; construction selection follows those decisions.

## 2. Scope and non-goals

### 2.1 In scope

This draft covers:

- proof of possession of a liveness/personhood attestation;
- selective disclosure of policy and assurance predicates;
- holder binding and proof-session binding;
- freshness and replay resistance;
- status, expiry, suspension and revocation handling;
- optional scoped uniqueness and same-human-as-enrolment functions;
- privacy and correlation boundaries;
- verifier-visible failure semantics;
- algorithm and profile agility;
- interoperability evidence and conformance expectations; and
- composition with separate delegation evidence when an agent acts for a human principal.

### 2.2 Explicit non-goals

This draft does not define:

- the biometric algorithm or model used to decide liveness;
- an accreditation framework for biometric/personhood providers;
- global civil identity;
- a universal one-natural-person registry;
- a mandatory ZK proof system;
- a delegation or agent-authority protocol; or
- proof that a biometric model's underlying determination was correct.

The last point is foundational. A ZKP can prove properties of an attestation and of the proof computation. Unless the biometric inference itself is proven inside the relevant computation, the proof does not establish that the biometric decision was factually correct.

## 3. Terminology that must not be collapsed

The following terms represent different claims and should not be used as synonyms.

| Term | Meaning in this document | What it does not imply |
|---|---|---|
| **Liveness** | Evidence that an upstream process determined that a capture represented a live subject under a stated policy, method class and time boundary. | Personhood, identity, uniqueness or correctness of the determination. |
| **Personhood** | Evidence that the subject satisfied an attested policy intended to distinguish a natural person from an ineligible subject class. | Civil identity or global uniqueness. |
| **Holder binding** | Evidence that the presenter controls the key or secret bound to the credential/proof transcript. | That the key is non-transferable or currently controlled by the same human who enrolled. |
| **Human continuity** | Evidence that a later event is bound, under a stated method, to the human represented at an earlier event. | Global identity or uniqueness. |
| **Scoped uniqueness** | Evidence that the same enrolled secret/subject cannot exercise a defined action more than allowed within a scope and epoch. | One natural person globally. |
| **Freshness** | Evidence that a proof or upstream determination falls within a verifier-required time/session boundary. | Liveness by itself. |
| **Agent authority** | Evidence that an agent is authorised to act for a principal under defined scope, duration and revocation conditions. | Holder binding or liveness alone. |

A conformant profile should use the narrowest term matching the actual claim.

## 4. The assurance boundary: what the proof establishes

> A privacy-preserving proof of liveness proves possession of, and selected predicates over, an attestation produced under a stated assurance regime. It does not by itself prove that the liveness determination was correct.

There are two materially different assurance models:

1. **Accreditation-carried assurance.** The issuer performs the liveness/personhood determination and issues an attestation. The ZK proof demonstrates possession and policy predicates without revealing unnecessary attestation data. Correctness risk remains with the issuer, accreditation and governance system.
2. **Execution-carried assurance.** The proof establishes properties of execution of the liveness/personhood model itself, for example through zkML or equivalent verifiable computation. This has substantially different implementation, performance and model-governance requirements.

**V1 assumption:** accreditation-carried assurance. Execution-carried assurance is an extension unless separately standardised and benchmarked.

This distinction determines accountability. Verification software must not translate `proof_valid=true` into a stronger semantic claim than the profile permits.

## 5. The constraint that shapes personhood and uniqueness

A previous form of the requirements combined strong deduplication with broad unlinkability. Those goals conflict when the same underlying enrolment state must support anti-Sybil enforcement.

The practical design space is a trade curve:

1. **One action per enrolled secret, scope and epoch.** A scoped nullifier can enforce this cryptographically, assuming correct secret binding and nullifier derivation.
2. **One enrolment per issuer or ecosystem.** This additionally depends on enrolment quality, re-enrolment controls, recovery rules and issuer coordination.
3. **One natural person globally.** This is a much stronger governance and infrastructure claim and is not implied by either of the first two.

The specification must therefore define the intended uniqueness property first and select constructions second.

## 6. Foundational context and adversary decision

Every privacy property is parameterised by a definition of **context** and by an adversary model.

> **Open decision B1:** What constitutes a context for linkability and nullifier derivation?
>
> **Open decision B2:** Must separation between contexts survive issuer/verifier collusion, verifier/verifier collusion, or only honest non-colluding participants?

Candidate context dimensions include:

- relying party or verifier identifier;
- trust community or governance domain;
- transaction purpose;
- application/service;
- legal or policy basis;
- credential/profile identifier;
- epoch; and
- combinations of the above under a canonical derivation rule.

A statement such as “unlinkable across verifiers” is incomplete until it states who may collude, what auxiliary information is available, and for how long correlation resistance is expected to hold.

## 7. Actors and trust model

A deployment may combine roles, but the logical roles remain distinct.

| Actor | Responsibility | Must not be implicitly trusted for |
|---|---|---|
| **Subject / principal** | Participates in capture/enrolment and authorises use of credentials. | Correct implementation by issuer, wallet or verifier. |
| **Liveness/personhood issuer** | Performs or relies on the upstream determination and issues the attestation. | Verifier policy or downstream purpose limitation. |
| **Accreditation/governance authority** | Defines eligible issuers, assurance classes, status and policy rules. | Correctness of every individual determination. |
| **Wallet / prover** | Holds credential material and produces a proof bound to the requested transcript. | Authority of an agent beyond separately supplied delegation evidence. |
| **Verifier / relying party** | Constructs the request, verifies proof/status/policy and applies relying-party policy. | Facts not contained in the proof/profile semantics. |
| **Status / registry service** | Supplies issuer, accreditation, revocation or policy status needed by the profile. | Semantic correctness of the original liveness decision. |
| **Mediated prover** *(optional)* | Provides proving capacity when local proving is unavailable. | Retention or use of sensitive witness material unless explicitly authorised. |
| **Agent** *(optional)* | Presents or triggers proof-related actions under delegated authority. | Principal authority without separate delegation evidence. |

Role co-location must not erase the privacy analysis. If issuer and verifier are the same legal/technical actor, the profile must analyse that combined observation surface explicitly.

## 8. Three different freshness clocks

“Fresh liveness” is ambiguous unless the system separates three clocks.

1. **Capture freshness** — how recently the biometric/liveness capture occurred.
2. **Attestation freshness** — how recently the attestation was issued or refreshed and whether its status is still acceptable.
3. **Proof freshness** — whether the presentation is bound to the current verifier request/session and cannot be replayed outside it.

A verifier may require one, two or all three. They are not interchangeable.

Example: a proof generated now from a six-month-old liveness attestation can have excellent **proof freshness** and poor **capture freshness**.

## 9. Requirement notation

The identifiers below are stable handles for review, scenarios and conformance mapping. In this fork draft, **MUST**, **SHOULD** and **MAY** express proposed requirement strength, not ratified upstream normative language.

### 9.1 Claim semantics

**LIV-CLAIM-01 — Bounded liveness claim.** A profile claiming liveness **MUST** identify the liveness policy/method class, assurance class and the time property to which the claim applies.

**LIV-CLAIM-02 — No correctness over-claim.** A verifier result **MUST NOT** state or imply that cryptographic verification proves the biometric determination was correct unless execution-carried assurance is explicitly part of the profile.

**LIV-CLAIM-03 — Personhood separation.** Liveness and personhood **MUST** be represented as separate predicates unless the attestation policy explicitly defines a compound predicate and its semantics.

**LIV-CLAIM-04 — Uniqueness separation.** Scoped uniqueness **MUST NOT** be represented as global natural-person uniqueness.

**LIV-CLAIM-05 — Agent authority separation.** Holder binding or liveness **MUST NOT** be interpreted as authorisation for an agent action. Agent authority requires separately verifiable delegation/mandate evidence.

### 9.2 Attestation and policy

**LIV-ATT-01 — Issuer authenticity.** The proof **MUST** demonstrate possession of an attestation whose issuer is acceptable under the selected profile, without disclosing more issuer information than that profile requires.

**LIV-ATT-02 — Policy binding.** The attestation **MUST** be bound to an identifiable liveness/personhood policy version and assurance class.

**LIV-ATT-03 — Time metadata.** The attestation/profile **MUST** provide enough authenticated time metadata to evaluate required capture freshness and attestation freshness.

**LIV-ATT-04 — Method semantics.** Where multiple liveness methods or assurance classes are accepted, the profile **MUST** define whether method identity is disclosed, hidden within an approved set, or reduced to a policy predicate.

**LIV-ATT-05 — Accreditation state.** If verifier acceptance depends on issuer accreditation, the proof flow **MUST** bind the relevant accreditation framework/policy identifier and permit the verifier to evaluate its applicable status.

### 9.3 Session, transcript and replay resistance

**LIV-SES-01 — Canonical transcript.** A presentation **MUST** be bound to a canonical, domain-separated transcript.

At minimum, the transcript must commit to:

- protocol identifier and version;
- profile identifier and version;
- verifier/audience identifier or canonical audience commitment;
- verifier challenge/nonce;
- session identifier where the protocol defines one;
- requested predicates;
- policy/accreditation version or accepted-policy commitment;
- relevant expiry/freshness boundary;
- context/scope identifier when nullifiers or linkability are in use; and
- algorithm/proof-suite identifier needed to prevent cross-suite confusion.

**LIV-SES-02 — Audience restriction.** A proof generated for one verifier/audience **MUST NOT** validate as a presentation to a different audience unless an explicitly transferable presentation profile says otherwise.

**LIV-SES-03 — Challenge uniqueness.** Verifiers **MUST** generate challenges with sufficient unpredictability and lifetime controls to prevent practical replay.

**LIV-SES-04 — Request integrity.** The prover **MUST** be able to determine the predicates, audience and context it is authorising before producing the proof. Hidden verifier-side policy changes must not retroactively strengthen the meaning of a previously generated proof.

**LIV-SES-05 — Proof expiry.** A profile **MUST** define the validity window of a generated proof/presentation independently from credential or attestation expiry.

### 9.4 Freshness and temporal policy

**LIV-TIME-01 — Explicit freshness class.** Each profile **MUST** state whether it requires capture freshness, attestation freshness, proof freshness, or a combination.

**LIV-TIME-02 — Verifier threshold.** A verifier requesting capture or attestation freshness **MUST** express an acceptable threshold or a referenced policy from which the threshold is deterministically derived.

**LIV-TIME-03 — Clock assumptions.** Profiles using wall-clock time **MUST** define tolerated skew and the trusted source/assumption for timestamps relevant to acceptance.

**LIV-TIME-04 — No freshness inference.** A recent proof-generation timestamp **MUST NOT** be treated as evidence that the biometric capture was recent.

### 9.5 Status, revocation and policy change

**LIV-STAT-01 — Status semantics.** The profile **MUST** define how attestation status is evaluated and distinguish at least valid, expired, revoked, suspended/temporarily unavailable where the underlying status mechanism supports them.

**LIV-STAT-02 — Accreditation change.** Where issuer accreditation is material, the profile **MUST** define whether verifier acceptance is based on accreditation status at issuance time, presentation time, both, or another explicitly defined evaluation time.

**LIV-STAT-03 — Historical/as-of verification.** If a use case requires historical verification, the status mechanism **MUST** support an unambiguous evaluation time and evidence sufficient to distinguish “valid as of T” from “valid now”.

**LIV-STAT-04 — Policy supersession.** A policy version becoming obsolete **MUST NOT** be conflated automatically with revocation of every attestation issued under it. Profiles must define supersession and transition rules.

**LIV-STAT-05 — Status privacy.** Status checking **SHOULD** avoid creating a verifier-to-subject correlation channel. Where privacy-preserving status is not available, the disclosure/correlation impact must be documented.

### 9.6 Holder binding and continuity

**LIV-BIND-01 — Holder-key proof.** Where holder binding is required, the presentation **MUST** prove control of the bound holder key/secret and bind that proof to the canonical transcript.

**LIV-BIND-02 — Non-transferability disclaimer.** The profile **MUST NOT** infer that holder-key control proves the key was never copied, transferred or exercised through malware/remote control.

**LIV-BIND-03 — Human continuity.** A “same human as enrolment” claim **MUST** identify the specific binding mechanism and assurance assumptions supporting continuity. Holder-key control alone is insufficient unless the profile explicitly defines key continuity as the intended, weaker claim.

**LIV-BIND-04 — Recovery impact.** Key/credential recovery **MUST** define whether continuity, scoped uniqueness or nullifier state survives, rotates or is re-established, and how duplicate recovery is prevented or detected.

### 9.7 Scoped uniqueness and nullifiers

**LIV-UNIQ-01 — Explicit scope.** Any nullifier **MUST** be derived from a canonical scope/context definition, profile identifier and epoch/purpose inputs defined by the profile.

**LIV-UNIQ-02 — No global stable nullifier.** The core profile **MUST NOT** use a globally stable nullifier or pseudonymous identifier.

**LIV-UNIQ-03 — Claim precision.** A verifier receiving a nullifier **MUST** treat it as evidence only of the anti-replay/anti-duplication property defined for that scope and epoch.

**LIV-UNIQ-04 — Rotation semantics.** Profiles using epochs **MUST** define epoch duration, rollover behaviour, late-arriving proofs, recovery interaction and whether old/new epoch values can be correlated by any party.

**LIV-UNIQ-05 — Multi-issuer semantics.** If uniqueness spans multiple issuers, the architecture **MUST** define how enrolment coordination, duplicate handling and privacy are achieved. A nullifier construction alone is insufficient.

### 9.8 Privacy and disclosure

**LIV-PRIV-01 — Named adversary.** Every unlinkability or confidentiality claim **MUST** name the relevant adversary: verifier, issuer, registry/status service, mediator, colluding parties, or another defined actor set.

**LIV-PRIV-02 — Named horizon.** Every privacy claim **MUST** state the period or event horizon over which it is expected to hold, including effects of key rotation, policy change, compromise or later data disclosure.

**LIV-PRIV-03 — Disclosure register.** A profile **MUST** state which fields/predicates are visible to each actor and which stable or quasi-stable values can be observed across sessions.

**LIV-PRIV-04 — No raw biometric disclosure.** Raw biometric samples and reversible biometric templates **MUST NOT** be included in the proof presentation or verifier-visible evidence.

**LIV-PRIV-05 — Binding artefact protection.** Biometric-derived binding artefacts **MUST** be designed and evaluated for irreversibility/non-invertibility appropriate to their threat model. “Hashed biometric” is not sufficient terminology by itself.

**LIV-PRIV-06 — Composition review.** A deployment combining multiple individually privacy-preserving proofs **MUST** assess joint correlation and reconstruction risk across the combined transcript and external metadata.

**LIV-PRIV-07 — Mediated proving.** A mediated proving profile **MUST** define witness exposure, retention, logging, operator access, transport protection, deletion and compromise assumptions. Mediation must not be presented as privacy-equivalent to local proving without evidence.

### 9.9 Algorithm and implementation agility

**LIV-ALG-01 — No semantic hard-coding.** Semantic claim identifiers **MUST NOT** encode a single proof system as the only valid construction.

**LIV-ALG-02 — Suite identification.** Proofs **MUST** identify the proof/credential/commitment suites required for deterministic verification and downgrade resistance.

**LIV-ALG-03 — Negotiation.** If multiple suites are supported, negotiation **MUST** be transcript-bound and resistant to silent downgrade.

**LIV-ALG-04 — Migration.** Profiles **MUST** define how suites are deprecated, how verifier policy changes are communicated and how long-lived attestations migrate without changing their semantic claim silently.

**LIV-ALG-05 — Dependency disclosure.** A profile **MUST** document trusted setup, common reference string, secure hardware, remote prover or registry dependencies that materially affect security or availability.

### 9.10 Failure and degraded mode

**LIV-FAIL-01 — Typed failure.** Implementations **MUST** distinguish at least cryptographic invalidity, unsupported profile/suite, stale proof, stale capture/attestation, unacceptable issuer/accreditation, revoked/suspended status and local policy rejection.

**LIV-FAIL-02 — Privacy-preserving errors.** Error responses **MUST NOT** reveal unnecessary credential, biometric, issuer or subject information beyond what is required to diagnose the failed protocol interaction.

**LIV-FAIL-03 — Fallback policy.** A deployment **MUST** define what happens when the preferred proving path is unavailable: fail closed, select another conformant profile, step down assurance, use a mediated prover or switch channel.

**LIV-FAIL-04 — No silent assurance downgrade.** Any reduction in liveness freshness, issuer assurance, proof suite or privacy class **MUST** be explicit to the relying-party policy decision and, where material to consent, to the subject/prover.

## 10. Predicate and disclosure matrix

Candidate construction mappings remain provisional until the context/adversary decisions are resolved.

| Predicate | Candidate construction family | Minimum verifier-visible result | Material disclosure/correlation surface | Does not establish |
|---|---|---|---|---|
| Liveness attestation | Issuer-signature proof + hidden credential predicates | Liveness policy satisfied; assurance class; freshness result | Policy/accreditation/profile identifiers as selected | Correctness of biometric determination |
| Personhood policy | Predicate proof over attested policy | Personhood policy satisfied | Policy/profile identifier | Civil identity; global uniqueness |
| Issuer accreditation | Set membership / trust-registry-backed predicate | Issuer belongs to acceptable set | Accreditation framework; issuer may be hidden or disclosed by profile | Correctness of issuer determination |
| Scoped uniqueness | Scope/epoch nullifier | Duplicate/not-duplicate under defined scope rule | Stable within-scope value or equivalent verifier state | One natural person globally |
| Holder binding | Proof of possession/control bound to transcript | Bound secret/key controlled in this session | Key class/identifier only if profile exposes it | Non-transferability; human continuity; agent authority |
| Human continuity | Credential/biometric-derived continuity mechanism | Same enrolment binding under stated policy | Correlation within defined continuity domain | Identity outside that domain |
| Proof freshness | Domain-separated transcript + challenge | Current request/session bound | Verifier/audience and session metadata | Recent biometric capture |
| Demographic range *(extension)* | Range/set proof over attested attribute | Requested predicate satisfied | Predicate threshold/policy | Exact attribute value |

## 11. Profile model

The draft retains a natural split between a liveness-only profile and personhood/uniqueness extensions.

### 11.1 Minimum Liveness Profile (MLP)

The MLP should be independently implementable and testable without uniqueness machinery. It includes:

- attestation possession;
- liveness policy and assurance predicate;
- explicit freshness class;
- holder binding where required by the use case;
- canonical transcript and replay resistance;
- expiry and status evaluation;
- accreditation predicate where required;
- disclosure-boundary declaration; and
- algorithm/profile agility.

It does **not** require scoped nullifiers, deduplication or global personhood claims.

### 11.2 Extended Personhood Profile (EPP)

The EPP composes the MLP with one or more of:

- personhood-policy predicate;
- same-human-as-enrolment continuity;
- scoped uniqueness/nullifier behaviour;
- issuer-set membership or ecosystem-level accreditation; and
- cross-issuer enrolment coordination where the selected uniqueness claim requires it.

The EPP must state its position on the Sybil-resistance/unlinkability trade curve explicitly.

### 11.3 Agent-mediated use

Where an agent initiates or presents a proof on behalf of a principal, the liveness/personhood proof establishes only the human-related predicates defined by its profile. A separate delegation/mandate object should carry at least:

- principal;
- delegate/agent;
- authorised action or capability scope;
- audience/environment constraints where applicable;
- effective time and expiry;
- revocation/status reference; and
- evidence linking the delegation decision to the appropriate human-authorisation event.

The two evidence sets may be cryptographically composed, but their semantics must remain separable.

## 12. Use-case requirements

| Context | Core requirement | Likely profile | Important temporal property |
|---|---|---|---|
| Account creation / sign-up | Personhood plus anti-duplicate rule within a defined service/community scope | EPP | Capture freshness + proof freshness |
| Age-gated access | Live subject plus demographic predicate where required | MLP + attribute extension | Profile-dependent capture freshness |
| Login / re-authentication | Current presenter bound to prior enrolment/credential | MLP or EPP continuity | Proof freshness; capture freshness only for step-up |
| High-value / sensitive action | Current human presence and holder binding | MLP | Tight capture + proof freshness |
| Account recovery | Human evidence sufficient to re-establish control without enabling duplicate recovery | EPP/continuity | Fresh capture; explicit recovery epoch/rules |
| Agent authorisation | Human authorisation event plus separate delegation | MLP/EPP + delegation | Fresh capture and proof; delegation effective time |
| Agent step-up | Human approval for changed scope/environment/action | MLP + delegation update | Very tight proof/capture freshness |
| Offline verification | Verifiable liveness/personhood evidence without live registry/status reachability | Profile-specific | Evidence/status freshness horizon must be bounded |

Use cases must not select a stronger profile than they need merely because stronger predicates are available. Data minimisation applies to semantic predicates as well as raw attributes.

## 13. Biometric/personhood-provider input contract

A provider integration needs an explicit contract rather than an abstract “liveness pass”. At minimum it should identify:

- determination result and policy identifier/version;
- assurance class and method class or approved-set membership;
- capture time or bounded capture-time evidence;
- attestation issue and expiry times;
- issuer identifier/key reference and status mechanism;
- accreditation framework/reference where required;
- subject/holder binding input;
- optional privacy-preserving continuity/uniqueness binding artefact;
- recovery/re-enrolment semantics; and
- session-binding material needed to prevent substitution between capture, attestation and proof sessions.

The contract must also state which values are secret witness data, credential data, public proof inputs and verifier outputs.

## 14. Verification outcome contract

A verifier should receive a structured result rather than a single boolean. A minimum semantic result model should be able to report:

- profile and suite evaluated;
- cryptographic validity;
- requested predicate results;
- proof-freshness result;
- capture/attestation-freshness result where requested;
- issuer/accreditation acceptance result;
- attestation/status result and evaluation time;
- scoped uniqueness result where requested;
- policy version evaluated; and
- typed failure or warning codes.

The result should make it difficult for an application developer to confuse `cryptographically_valid` with `business_policy_accepted` or `biometric_determination_correct`.

## 15. Interoperability and conformance evidence

A candidate profile should not be called interoperable without evidence. Before promotion toward a normative working draft, this fork proposes that each profile provide:

1. a machine-readable profile identifier and version;
2. canonical transcript serialisation rules;
3. deterministic positive and negative test vectors where the construction permits them;
4. at least two independent verifier implementations or an equivalent independent cross-check;
5. explicit status/revocation test cases;
6. replay, wrong-audience and wrong-context negative tests;
7. downgrade/version-negotiation negative tests;
8. privacy/disclosure review against the declared adversary model;
9. mobile/browser or target-platform performance measurements for the intended deployment class;
10. failure-code interoperability tests; and
11. evidence that recovery, rotation and migration rules do not silently break uniqueness or privacy guarantees.

Proof-system performance alone is not sufficient interoperability evidence.

## 16. Security and privacy acceptance questions

Before deployment, an implementer should be able to answer:

- Who can correlate two presentations and under what conditions?
- Can issuer and verifier collusion defeat the intended context boundary?
- What stable metadata remains even when credential attributes are hidden?
- What happens after issuer-key compromise?
- What happens after holder-key compromise?
- What happens after a liveness policy or model is withdrawn?
- Can old proofs be verified “as of” a historical time, and should they be?
- Does recovery create a second usable uniqueness identity?
- Does mediated proving expose witnesses or create durable logs?
- Can a verifier force a weaker privacy/suite profile through negotiation?
- Can multiple successful proofs be combined to reconstruct information that no single proof reveals?
- What evidence supports the claimed biometric-derived artefact irreversibility?

A deployment that cannot answer these questions has an assurance gap even if every proof verifies cryptographically.

## 17. Ruled out

The following are incompatible with this draft's requirements unless a future profile explicitly changes the model and documents the consequences:

- claiming that ZK verification proves biometric-decision correctness under accreditation-carried assurance;
- claiming full unlinkability alongside strong, shared Sybil-resistance state without defining the actual adversary model;
- treating a nullifier as sufficient proof of one-natural-person uniqueness;
- globally stable identifiers or nullifiers in the core profiles;
- raw biometrics or reversible templates in verifier-facing proof flows;
- mandatory civil-identity disclosure for liveness/personhood;
- mandatory issuer concealment regardless of relying-party policy;
- conflating holder-key control, human continuity and agent authority;
- a bare nonce as the entire proof transcript;
- untyped `true/false` verification results that hide status or policy failure;
- silent fallback to weaker assurance/privacy;
- undocumented composition of multiple proofs;
- proprietary verifier-only formats without interoperable evidence; and
- hard-coding one cryptographic algorithm into the semantic claim model.

## 18. Decision backlog

The remaining work should be separated into **semantic/governance decisions** and **construction/engineering decisions**. The second category should not be finalised before the first.

### 18.1 Semantic and governance decisions

1. **B1 — Context delimiter:** what fields define a privacy/nullifier context?
2. **B2 — Collusion target:** which collusions must unlinkability survive?
3. **B3 — Minimum liveness semantics:** what precisely counts as “live” for the base profile, and how is method/policy variance represented?
4. **B4 — Freshness classes:** which profiles require capture freshness versus only proof/attestation freshness?
5. **B5 — Status time:** current-time, issuance-time, transaction-time and historical verification rules.
6. **B6 — Accreditation semantics:** whether issuer identity is disclosed, hidden in a set or policy-selectable.
7. **B7 — Recovery/continuity:** how recovery changes holder binding and uniqueness state.
8. **B8 — Agent composition:** ownership boundary between this work and Trust Task Protocols for delegation composition.
9. **B9 — Offline mode:** what assurance/status horizon permits disconnected verification?
10. **B10 — Privacy class:** whether profiles expose a standard privacy/disclosure classification usable during negotiation.

### 18.2 Construction and engineering decisions

After the above are bounded:

1. proof construction per predicate/profile;
2. credential signature and selective-disclosure suite compatibility;
3. set-membership/accreditation construction;
4. nullifier derivation and epoch scheme;
5. status/revocation proof mechanism;
6. transcript canonicalisation/encoding;
7. suite negotiation and downgrade protection;
8. local versus mediated proving support;
9. secure-hardware assumptions;
10. platform performance targets;
11. parameter/trusted-setup distribution where applicable; and
12. deterministic vectors and independent implementation strategy.

## 19. Proposed progression toward a specification

A practical sequence is:

1. **Ratify terminology and assurance boundary.** Agree that liveness, personhood, holder binding, continuity and uniqueness are different claims.
2. **Decide B1/B2.** Define context and collusion target before choosing nullifier or issuer-concealment constructions.
3. **Ratify the Minimum Liveness Profile semantics.** This can progress without the uniqueness trade curve.
4. **Define the attestation and verification outcome contracts.** Make upstream biometric inputs and downstream verifier semantics testable.
5. **Select constructions for the MLP and publish vectors.** Benchmark on intended platforms.
6. **Resolve EPP uniqueness/continuity governance.** Only then select scoped-nullifier/multi-issuer mechanisms.
7. **Pressure-test recovery, revocation, policy withdrawal, offline verification and agent step-up.** Treat failures as first-class protocol states.
8. **Cross-map every proposed normative requirement to conformance evidence.** A requirement with no observable test or assurance evidence should be explicitly identified as governance-only rather than accidentally untestable.

## 20. Immediate next steps for this fork

1. Map `LIV-*` requirements into the existing predicate/boundary and conformance matrices.
2. Add pressure-test scenarios for the three freshness clocks, historical status, recovery duplication, wrong-audience replay and assurance downgrade.
3. Extend the implementation guide's information model with a minimum liveness-attestation field profile and structured verification-result profile.
4. Use the decision register for B1–B10 rather than resolving them implicitly in implementation prose.
5. Prepare a concise upstream contribution that separates broadly useful semantic improvements from fork-specific implementation machinery.

---

## Changelog

**Fork working draft v0.4**

- Reframed the document as a proof-system-agnostic semantic and assurance requirements draft.
- Added explicit terminology separating liveness, personhood, holder binding, human continuity, scoped uniqueness, freshness and agent authority.
- Added an actor/trust model.
- Split freshness into capture, attestation and proof freshness.
- Added stable `LIV-*` requirement identifiers covering claims, attestations, transcripts, replay, status, time, binding, uniqueness, privacy, algorithm agility and failure semantics.
- Added current-time versus historical/as-of status semantics.
- Added recovery, rotation, migration, mediated-proving and downgrade requirements.
- Added a structured verification-outcome contract to avoid boolean over-claiming.
- Added interoperability/conformance evidence expectations.
- Split the open backlog into semantic/governance decisions and construction/engineering decisions.
- Preserved the v0.3 assurance-boundary correction: cryptography proves attestation properties under the V1 model; it does not prove the underlying biometric determination was correct.

**Upstream v0.3**

- Corrected the contradiction between uniqueness and full cross-verifier unlinkability by adopting context-dependent unlinkability.
- Elevated the foundational context/collusion boundary question.
- Distinguished accreditation-carried assurance from execution-carried assurance.
- Added drafting rules naming adversary, horizon, negative semantics and conjecture.
- Added a disclosure column and profile split.

**Upstream v0.2**

- Clarified attestation possession versus determination correctness, key control versus agent authority, uniqueness scope, transcript binding, issuer concealment choice and demographic-range extension.

**Upstream v0.1**

- Initial strawman.
