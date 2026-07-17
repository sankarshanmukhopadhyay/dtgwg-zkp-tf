# Pressure-Test Use Case Corpus for DTG Privacy-Preserving ZK Proofs

**Status:** Draft for task-force discussion  
**Purpose:** Implementation validation, architectural pressure testing, and conformance planning  
**Audience:** DTG ZKP Task Force, Credentials TF, Trust Task Protocols TF, cryptographers, biometric providers, wallet implementers, relying parties, trust-registry operators, and governance-framework designers

---

## 1. Purpose

This document defines a pressure-test corpus for the outputs of the DTG ZKP Task Force. It is not a catalogue of attractive applications. It is a validation instrument intended to expose where a proof profile may be cryptographically sound yet operationally incomplete, privacy-preserving in isolation yet correlatable in composition, or interoperable at the message level yet ambiguous at the assurance and governance boundaries.

The corpus is designed to test whether a specification can support independent implementations across biometric providers, issuers, wallets, verifiable trust agents, verifiers, accreditation frameworks, trust registries, and trust-task protocols.

The task-force output should be considered ready for implementation only when the selected profiles can be applied to representative scenarios in this corpus without requiring each implementer to invent unstated semantics.

## 2. Alignment with the task-force mission

The DTG ZKP Task Force is defining how verifiable trust agents can produce privacy-preserving proofs of DTG credentials, biometric liveness, personhood-related predicates, and other trust signals without disclosing identity or underlying biometric material.

This corpus assumes the following architectural boundaries:

1. A ZKP proves possession of, and selected properties about, an attestation.
2. It does not prove that the underlying biometric determination was correct.
3. Accreditation and governance carry assurance about the issuer and its process.
4. Context-dependent unlinkability is achievable; full unlinkability alongside Sybil resistance is not.
5. Holder-key control does not establish agent authority.
6. Nullifiers do not independently establish one-human-one-record.
7. Every privacy claim must identify its adversary and time horizon.
8. Every predicate must state what it does not establish.

## 3. How to use this corpus

Each use case should be used in four ways:

- **Requirements validation:** Can the use case be expressed using defined predicates and profiles?
- **Threat validation:** Are the named adversaries and collusion models explicit?
- **Conformance validation:** Can two independent implementations produce the same verifier outcome?
- **Operational validation:** Are lifecycle, recovery, fallback, audit, and redress behaviours defined?

A use case is not considered covered merely because a proof can be generated. Coverage requires an answer to the full implementation contract: request, proof, verification, reliance decision, failure handling, lifecycle state, privacy boundary, and accountability.

## 4. Canonical use-case template

Each use case contains:

- **Objective**
- **Actors**
- **Context boundary**
- **Preconditions**
- **Required predicates**
- **Nominal flow**
- **Verifier output**
- **Privacy claim**
- **Named adversaries**
- **Privacy horizon**
- **Governance dependencies**
- **Failure and abuse cases**
- **What the proof does not establish**
- **Specification pressure points**
- **Conformance tests**
- **Priority**

## 5. Cross-cutting validation dimensions

| Dimension | Question the specification must answer |
|---|---|
| Predicate semantics | What exactly is proven, and what is not? |
| Context | What defines the scope within which linkability is permitted? |
| Adversary | Is the claim against the verifier, issuer, or issuer-verifier collusion? |
| Horizon | For how long does the privacy or assurance claim hold? |
| Assurance | Which policy, class, and accreditation framework support the claim? |
| Freshness | What transcript elements prevent replay and cross-context reuse? |
| Uniqueness | Is the claim one action, one enrolment, or one natural person? |
| Holder binding | What key or secret is controlled, and what does that control imply? |
| Agent authority | How is delegation proven without conflating it with holder control? |
| Lifecycle | How do expiry, revocation, suspension, and policy change affect verification? |
| Interoperability | Can independent implementations agree on the same result? |
| Fallback | What happens when the preferred proof cannot be generated or verified? |
| Accessibility | Is there a non-discriminatory alternative route? |
| Audit and redress | Can a failed or harmful decision be explained and challenged? |
| Crypto agility | Can profiles and algorithms evolve without semantic breakage? |

---

## 6. Use-case catalogue

### UC-001 — Privacy-Preserving Account Creation

**Objective:** Allow a person to create one account in a defined service context while proving liveness and scoped uniqueness without disclosing civil identity.

**Actors:** Human principal; biometric provider; accredited issuer; wallet or VTA; relying-party verifier; enrolment-root or registry operator.

**Context boundary:** One service, application family, or governance-defined account domain. The specification must state whether different brands, subsidiaries, and regions are one context or several.

**Preconditions:** The principal has completed an enrolment accepted by the relevant framework; the issuer is accredited; the verifier supports the negotiated proof profile.

**Required predicates:** Liveness attestation; personhood-policy predicate; scoped uniqueness; holder binding; freshness.

**Nominal flow:** The verifier sends a profile-specific request and canonical challenge. The wallet obtains or presents a qualifying liveness attestation, derives the context-scoped nullifier, binds the proof to the transcript, and returns the proof. The verifier validates the proof, the accreditation framework, the enrolment root, freshness, status, and whether the nullifier has already been accepted in the same scope and epoch.

**Expected verifier output:** A policy result such as `eligible-for-first-account=true`, assurance class, policy version, context identifier, and nullifier acceptance result.

**Privacy claim:** The verifier learns only that the person satisfies the required policy and has not already used the same enrolled secret in this scope and epoch.

**Named adversaries:** Malicious verifier; malicious issuer; issuer-verifier collusion; user attempting multiple enrolments.

**Privacy and assurance horizon:** The proof artefact is session-bound. The nullifier remains linkable for the stated account-creation epoch. The enrolment root may persist longer and must have its own lifecycle.

**Governance dependencies:** Definition of the account context; issuer accreditation; enrolment governance; re-enrolment and recovery rules; dispute process.

**Failure and abuse cases:** Replay; multiple issuer enrolments; stale root; revoked attestation; profile mismatch; user loses holder key after registration; verifier silently expands the context.

**What the proof does not establish:** It does not prove one natural person globally, civil identity, account suitability, or that the biometric determination was correct.

**Specification pressure points:** Context definition; cross-issuer deduplication; root discovery; nullifier retention; account recovery; issuer-verifier collusion.

**Minimum conformance tests:** Same person, same scope and epoch produces repeated nullifier; same person in a different legitimate context is unlinkable; stale root fails deterministically; verifier cannot substitute another audience in the transcript.

**Priority:** `P0`

---

### UC-002 — Anonymous or Pseudonymous Community Participation

**Objective:** Permit one human to participate in a community or forum without requiring identity disclosure while resisting duplicate accounts or coordinated Sybil behaviour.

**Actors:** Human principal; community platform; accredited issuer; wallet or VTA; moderator or governance body.

**Context boundary:** A single community, governance space, or participation period.

**Preconditions:** The community publishes the applicable proof profile, context identifier, participation period, and acceptable accreditation frameworks.

**Required predicates:** Personhood-policy predicate; scoped uniqueness; optional liveness; freshness.

**Nominal flow:** The platform requests proof for the community context. The holder proves eligibility and emits a community-scoped nullifier. The platform creates or activates a pseudonymous account without receiving identity or issuer-specific details unless required by profile.

**Expected verifier output:** `one-participant-per-context=true`, policy and assurance metadata, and accepted nullifier.

**Privacy claim:** Pseudonymous activity should not be linkable to other communities by the platform, issuer, or their collusion if that adversary model is selected.

**Named adversaries:** Platform; issuer; platform-issuer collusion; other community members; user operating several wallets.

**Privacy and assurance horizon:** Community epoch, which may be indefinite or periodically reset. The specification must state whether a reset permits renewed participation.

**Governance dependencies:** Community boundary; moderation and appeal; re-entry after exclusion; transfer between pseudonyms; lawful disclosure process if any.

**Failure and abuse cases:** Platform correlates presentation metadata; issuer embeds covert identifiers; nullifier changes after wallet recovery; context IDs differ across mobile and web clients.

**What the proof does not establish:** It does not prove good behaviour, non-collusion between humans, or non-transfer of account control.

**Specification pressure points:** Collusion-resistant context boundaries; metadata leakage; recovery without duplicate accounts; indefinite epochs.

**Minimum conformance tests:** Proofs across two communities are unlinkable under the chosen adversary; same community across two clients yields the same nullifier; recovery follows a normative continuity rule.

**Priority:** `P0`

---

### UC-003 — Age-Threshold Access Without Date-of-Birth Disclosure

**Objective:** Allow a verifier to learn only that the principal meets an age threshold and is live, without learning date of birth or civil identity.

**Actors:** Principal; age-attribute issuer; liveness issuer; wallet; verifier; jurisdiction or policy authority.

**Context boundary:** The transaction and legal jurisdiction governing the age threshold.

**Preconditions:** An authoritative age attribute is available; the threshold and jurisdiction are explicit; liveness is required only where policy justifies it.

**Required predicates:** Demographic range; optional liveness; freshness; holder binding.

**Nominal flow:** The verifier requests `age >= threshold` under a named jurisdiction and policy version. The wallet proves the range predicate and, where needed, a fresh liveness/holder binding.

**Expected verifier output:** Boolean threshold result, policy identifier, assurance class, and proof freshness.

**Privacy claim:** The verifier learns no exact age, date of birth, identity, or unrelated demographic attribute.

**Named adversaries:** Verifier; attribute issuer; issuer-verifier collusion; colluding verifiers making multiple threshold queries.

**Privacy and assurance horizon:** Single transaction or short-lived access session. Repeated thresholds can create inference risk over time.

**Governance dependencies:** Authority for the age attribute; applicable jurisdiction; threshold updates; accessibility and alternative verification routes.

**Failure and abuse cases:** Adaptive threshold probing; stale age credential; conflicting jurisdiction; reused liveness proof; verifier requests excessive predicates.

**What the proof does not establish:** It does not prove identity, legal capacity beyond the stated threshold, or that the person will not transfer access.

**Specification pressure points:** Range-proof composition; query minimisation; inference through repeated requests; policy negotiation.

**Minimum conformance tests:** Exact value remains hidden; transcript binds threshold and jurisdiction; verifier cannot reuse proof for a stricter threshold; multiple proofs do not expose precise age beyond unavoidable inference.

**Priority:** `P1`

---

### UC-004 — High-Value Financial Transaction Step-Up

**Objective:** Require fresh human presence and holder binding before a high-value or high-risk transaction is authorised.

**Actors:** Account holder; wallet; biometric provider; issuer; financial institution; transaction-risk engine; optional agent.

**Context boundary:** A specific transaction, amount, destination, currency, and time window.

**Preconditions:** The holder is already enrolled; the institution has a policy threshold; transaction details can be canonically hashed into the transcript.

**Required predicates:** Liveness; freshness; holder binding; optional same-human-as-enrolment; optional delegation evidence.

**Nominal flow:** The institution creates a challenge bound to the transaction details. The holder performs liveness or presents a qualifying fresh attestation. The proof binds holder control and the transaction transcript. The institution verifies before execution.

**Expected verifier output:** `step-up-satisfied=true`, assurance class, transaction binding digest, expiry, and status result.

**Privacy claim:** The liveness or biometric evidence is not disclosed to the institution. Transaction data is disclosed only as already required for execution.

**Named adversaries:** Malware on device; malicious agent; malicious verifier; compromised issuer; replay attacker.

**Privacy and assurance horizon:** Minutes. Proof must become unusable after transaction execution or expiry.

**Governance dependencies:** Transaction-risk policy; liability for false acceptance; fallback and manual review; customer redress.

**Failure and abuse cases:** Proof replay against another transaction; amount substitution; malicious wallet UI; device unable to generate proof; issuer becomes suspended during processing.

**What the proof does not establish:** It does not prove informed consent, absence of coercion, or that the holder understands the transaction.

**Specification pressure points:** Canonical transaction binding; one-time use; rollback; offline approval; coercion and intent remain outside proof.

**Minimum conformance tests:** Any change in amount or destination invalidates proof; replay is rejected; fallback does not silently lower assurance; revocation timing is deterministic.

**Priority:** `P0`

---

### UC-005 — Sensitive Account Recovery

**Objective:** Restore access after key or device loss without revealing unnecessary identity and without allowing recovery to create duplicate enrolments.

**Actors:** Principal; recovery service; biometric provider; issuer; wallet provider; verifier; help-desk operator.

**Context boundary:** A specific account or credential domain and recovery event.

**Preconditions:** Recovery policy exists; enrolment continuity artefact is available; old key may be unavailable or compromised.

**Required predicates:** Liveness; personhood; same-human-as-enrolment; scoped uniqueness; freshness.

**Nominal flow:** The recovery service issues a challenge. The principal proves fresh liveness and continuity with the prior enrolment. The service rotates the holder key, invalidates the old key, and updates continuity state without creating a second enrolment.

**Expected verifier output:** `recovery-authorised=true`, continuity result, new key binding, old-key revocation status.

**Privacy claim:** The recovery service learns only what is needed to restore the account and must not receive raw biometric material.

**Named adversaries:** Attacker with stolen device; malicious help-desk operator; issuer-verifier collusion; insider modifying recovery state.

**Privacy and assurance horizon:** Recovery proof is one-time and short-lived; continuity state may be long-lived.

**Governance dependencies:** Recovery eligibility; escalation; audit; appeals; treatment of biometric changes or disability; loss of all factors.

**Failure and abuse cases:** Old and new keys both remain active; recovery resets nullifier and permits duplicate enrolment; false non-match excludes legitimate user; root migration loses continuity.

**What the proof does not establish:** It does not prove non-coercion, sole ownership of the account, or correctness of the biometric match.

**Specification pressure points:** Key rotation; continuity semantics; revocation ordering; duplicate prevention; human override.

**Minimum conformance tests:** Old key is unusable after successful recovery; nullifier continuity follows the policy; failed recovery does not leak enrolment membership; audit events contain no correlating biometric data.

**Priority:** `P0`

---

### UC-006 — Recurring Login With Same-Human Continuity

**Objective:** Allow a returning user to prove that the current live presenter is the same enrolled subject without exposing a global identifier.

**Actors:** Principal; service; biometric provider; issuer; wallet.

**Context boundary:** The service account or device trust domain.

**Preconditions:** Initial enrolment established a privacy-preserving binding artefact; service knows the appropriate context.

**Required predicates:** Liveness; freshness; same-human-as-enrolment; holder binding.

**Nominal flow:** The service requests a fresh proof tied to the account context. The wallet proves continuity with the enrolled commitment and possession of the holder key.

**Expected verifier output:** `same-enrolled-subject=true`, liveness freshness, policy and assurance class.

**Privacy claim:** No raw biometric or reusable global subject identifier is revealed.

**Named adversaries:** Service; issuer; service-issuer collusion; attacker with copied wallet key; attacker presenting synthetic media.

**Privacy and assurance horizon:** Per login. The account-context continuity artefact persists for the account lifetime.

**Governance dependencies:** Re-enrolment; changes in appearance; device migration; account sharing policy.

**Failure and abuse cases:** Key copied to another person; biometric commitment becomes unusable; service expands context; login across federated services correlates user.

**What the proof does not establish:** It does not prove the key was never transferred or that the user is acting voluntarily.

**Specification pressure points:** Separation of key control and human continuity; privacy-preserving biometric commitment; federated context boundaries.

**Minimum conformance tests:** Copied key without matching continuity fails; valid user after device migration succeeds under recovery policy; cross-service proofs remain unlinkable.

**Priority:** `P0`

---

### UC-007 — One-Person-One-Benefit-Claim Per Period

**Objective:** Prevent duplicate benefit claims within a programme and period while avoiding unnecessary identity disclosure to the claim-processing channel.

**Actors:** Beneficiary; benefit authority; issuer; enrolment operator; wallet; payment provider.

**Context boundary:** A specific benefit programme, jurisdiction, and claim period.

**Preconditions:** Programme enrolment is governed; eligibility may be established separately; context and epoch are published.

**Required predicates:** Personhood; scoped uniqueness; optional liveness; credential predicates; freshness.

**Nominal flow:** The beneficiary proves programme eligibility and emits a programme-period nullifier. The verifier checks that the nullifier has not been accepted for the period and authorises the claim.

**Expected verifier output:** Eligibility result, uniqueness result, programme and period identifiers, assurance class.

**Privacy claim:** The claim channel does not learn unrelated identity data or claims in other programmes.

**Named adversaries:** Fraudulent claimant; corrupt enrolment operator; verifier; issuer-verifier collusion; payment intermediary.

**Privacy and assurance horizon:** One benefit period; historical nullifiers may need retention for audit under strict purpose limitation.

**Governance dependencies:** Eligibility rules; appeals; household versus individual entitlements; recovery; duplicate resolution; lawful audit.

**Failure and abuse cases:** Programme changes context mid-period; household benefit incorrectly modeled as person uniqueness; multiple enrolment roots; offline claims race before synchronization.

**What the proof does not establish:** It does not prove eligibility unless eligibility predicates are separately included; it does not prove one person globally.

**Specification pressure points:** Offline double-spend; household models; privacy-preserving audit; cross-jurisdiction recognition.

**Minimum conformance tests:** Concurrent duplicate claims resolve deterministically; unrelated programmes cannot correlate nullifiers; appeal can distinguish error from fraud without exposing biometrics.

**Priority:** `P1`

---

### UC-008 — Anonymous Public Consultation or Digital Ballot

**Objective:** Permit one eligible human to submit one response or ballot in a defined consultation without revealing identity.

**Actors:** Participant; consultation authority; issuer; enrolment authority; wallet; ballot collector; auditor.

**Context boundary:** A specific consultation or election event, not a global civic identity domain.

**Preconditions:** Eligibility and enrolment rules are established; anonymous collection channel exists; context and epoch are immutable.

**Required predicates:** Eligibility credential proof; scoped uniqueness; optional liveness; freshness.

**Nominal flow:** The authority publishes the event context. The participant proves eligibility and emits an event-scoped nullifier. The collector accepts one submission per nullifier without learning identity.

**Expected verifier output:** `eligible=true`, `not-previously-used=true`, event ID, proof validity.

**Privacy claim:** Ballot content must not be linkable to identity, issuer, or other events under the selected adversary model.

**Named adversaries:** Ballot collector; issuer; collector-issuer collusion; network observer; coercer; malicious participant.

**Privacy and assurance horizon:** Event duration plus defined audit period.

**Governance dependencies:** Eligibility; recount; dispute resolution; coercion resistance; nullification of compromised ballots; public verifiability.

**Failure and abuse cases:** Collector links timing and network metadata; issuer encodes covert tags; proof can be sold or transferred; context collision; revoting policy undefined.

**What the proof does not establish:** It does not prove freedom from coercion, secrecy against endpoint compromise, or democratic legitimacy.

**Specification pressure points:** Metadata privacy; issuer-verifier collusion; revoting; coercion; transparent audit without identity exposure.

**Minimum conformance tests:** Cross-event unlinkability; duplicate submission rejection; authorised re-vote follows explicit policy; proof artefacts do not reveal issuer when profile requires concealment.

**Priority:** `P1`

---

### UC-009 — Human Authorises an AI Agent

**Objective:** Bind an AI agent to a live human principal and a defined delegation without exposing unnecessary identity data.

**Actors:** Human principal; wallet/VTA; AI agent; delegation issuer or registry; service verifier; liveness issuer.

**Context boundary:** A named agent, set of permissions, relying-party domain, and validity period.

**Preconditions:** Agent has a stable key; principal can issue or hold delegation evidence; service understands the delegation schema.

**Required predicates:** Liveness; personhood where required; holder binding; freshness; separate delegation evidence.

**Nominal flow:** The service or agent requests authorisation. The principal proves fresh liveness and holder control, then signs or presents structured delegation evidence bound to the agent key, scope, duration, and relying-party context.

**Expected verifier output:** Proof that a live principal authorised the named agent under the stated delegation; delegation validity result.

**Privacy claim:** The service learns only the principal attributes necessary for the action and the delegation terms.

**Named adversaries:** Malicious agent; compromised wallet; service; issuer; service-issuer collusion.

**Privacy and assurance horizon:** Delegation validity period; liveness proof may be valid only at issuance.

**Governance dependencies:** Delegation scope; revocation; subdelegation; liability; agent replacement; redress.

**Failure and abuse cases:** Agent swaps key after authorisation; broad scope hidden in UI; liveness reused for another delegation; revocation not propagated; service treats holder binding as full authority.

**What the proof does not establish:** It does not prove the agent will follow instructions, that the human understood the delegation, or that the agent remains uncompromised.

**Specification pressure points:** Composition with trust tasks; delegation semantics; transcript binding to agent key; revocation.

**Minimum conformance tests:** Changing agent key or scope invalidates authorisation; service rejects expired or revoked delegation; liveness proof alone is insufficient.

**Priority:** `P0`

---

### UC-010 — Human Step-Up for Agent Intent Drift

**Objective:** Require a fresh human confirmation when an agent enters a new environment, requests a new permission, or materially changes intended action.

**Actors:** Principal; agent; relying-party service; policy engine; wallet; liveness issuer.

**Context boundary:** The specific proposed action, new permission, environment, and agent instance.

**Preconditions:** Existing delegation exists; step-up triggers are defined; action details can be canonically represented.

**Required predicates:** Freshness; liveness; holder binding; delegation continuity.

**Nominal flow:** The service pauses the agent and sends a challenge bound to the action and policy trigger. The principal proves fresh presence and approves a narrowly scoped delegation update.

**Expected verifier output:** `step-up-approved=true`, action digest, updated scope, expiry.

**Privacy claim:** The principal need not reveal identity beyond policy requirements; approval should not expose unrelated agent activity.

**Named adversaries:** Malicious agent; compromised service; replay attacker; issuer-verifier collusion.

**Privacy and assurance horizon:** Single action or short permission window.

**Governance dependencies:** Trigger policy; emergency override; audit; revocation; notification.

**Failure and abuse cases:** Agent reuses approval for different action; service omits material details; user unavailable; mediated prover lowers assurance.

**What the proof does not establish:** It does not prove informed comprehension or absence of coercion.

**Specification pressure points:** Action canonicalisation; user intent; precise delegation updates; fallback under time pressure.

**Minimum conformance tests:** Any material action change invalidates proof; approval cannot extend scope beyond transcript; expiry enforced consistently.

**Priority:** `P0`

---

### UC-011 — Agent Presents Proof on Behalf of Principal

**Objective:** Allow an authorised agent to present an existing proof or generate a derived proof within delegation limits.

**Actors:** Principal; agent; wallet/VTA; verifier; issuer; delegation authority.

**Context boundary:** A relying-party domain and delegated task.

**Preconditions:** Delegation permits proof presentation; proof profile supports agent-mediated presentation; holder secret remains protected.

**Required predicates:** Credential predicate; delegation evidence; agent key binding; optional fresh human presence.

**Nominal flow:** The agent receives a proof request, checks delegation, generates or obtains a proof, binds the response to its own key and the task transcript, and presents it to the verifier.

**Expected verifier output:** Predicate result, agent identity/key, delegation validity, principal privacy preserved.

**Privacy claim:** Verifier should not learn more about the principal because an agent is involved. Agent should not gain reusable secrets beyond delegation.

**Named adversaries:** Agent; verifier; issuer; agent-verifier collusion; compromised delegation registry.

**Privacy and assurance horizon:** Delegation and proof validity periods.

**Governance dependencies:** Agent duties; subdelegation; revocation; audit; principal visibility into agent actions.

**Failure and abuse cases:** Agent exceeds scope; proof request is broader than delegation; agent stores correlatable artefacts; revocation race.

**What the proof does not establish:** It does not establish human presence unless separately required and proven.

**Specification pressure points:** Proof generation custody; delegation-to-proof binding; principal consent; audit without correlation.

**Minimum conformance tests:** Agent cannot answer out-of-scope request; revocation blocks subsequent presentation; verifier distinguishes principal predicate from agent authority.

**Priority:** `P1`

---

### UC-012 — Issuer Suspension After Proof Issuance

**Objective:** Define whether and how an otherwise valid proof is treated when the issuer becomes suspended after issuing the underlying attestation.

**Actors:** Issuer; accreditation framework; status registry; holder; verifier.

**Context boundary:** A specific transaction time and applicable status policy.

**Preconditions:** Attestation was valid at issuance; issuer status later changes.

**Required predicates:** Issuer accreditation; attestation validity; status-time semantics.

**Nominal flow:** The verifier resolves issuer or set status according to profile. The profile determines whether validity is checked at issuance time, presentation time, both, or under a grace policy.

**Expected verifier output:** Deterministic status result and reason code.

**Privacy claim:** Status checking must not reveal the holder or create a correlatable per-holder query.

**Named adversaries:** Verifier; status registry; issuer; collusion between them.

**Privacy and assurance horizon:** Attestation lifetime and status-history retention.

**Governance dependencies:** Suspension versus revocation; retroactivity; emergency action; appeal and reinstatement.

**Failure and abuse cases:** Online status endpoint leaks holder activity; different verifiers apply different time semantics; stale cached set accepts suspended issuer.

**What the proof does not establish:** It does not determine whether a past biometric decision was correct.

**Specification pressure points:** Privacy-preserving status; temporal semantics; cached sets; retroactive invalidation.

**Minimum conformance tests:** All implementations return same result for status changes at defined times; cache expiry enforced; no holder-specific status query is required.

**Priority:** `P0`

---

### UC-013 — Accreditation Framework or Policy Version Change

**Objective:** Ensure a verifier can distinguish proofs made under different assurance policies and apply migration rules consistently.

**Actors:** Framework operator; issuer; holder; verifier; registry.

**Context boundary:** A policy family, version, and effective date.

**Preconditions:** Old and new policies coexist; attestations may remain valid across transition.

**Required predicates:** Policy identifier/version; assurance class; issuer accreditation.

**Nominal flow:** The proof discloses the framework and policy version required by profile. The verifier evaluates against its acceptance policy and effective dates.

**Expected verifier output:** Accepted, rejected, or accepted-with-deprecation result with reason.

**Privacy claim:** Policy disclosure should not reveal the specific issuer unless required.

**Named adversaries:** Verifier; issuer; framework operator.

**Privacy and assurance horizon:** Policy transition period and attestation validity.

**Governance dependencies:** Versioning; grandfathering; deprecation; emergency withdrawal.

**Failure and abuse cases:** Semantic version changes without identifier; verifier silently treats old assurance as new; proof omits policy version.

**What the proof does not establish:** It does not prove the policy was well designed or correctly executed.

**Specification pressure points:** Semantic stability; policy discovery; migration; conformance reason codes.

**Minimum conformance tests:** Same proof yields predictable outcomes before, during, and after transition; unsupported versions fail explicitly.

**Priority:** `P0`

---

### UC-014 — Trust Registry Unavailable or Partitioned

**Objective:** Permit safe verification when issuer-set or status infrastructure is temporarily unavailable.

**Actors:** Verifier; trust registry; holder; issuer; cache operator.

**Context boundary:** A transaction under degraded network conditions.

**Preconditions:** Verifier has cached registry data with a known age; profile defines offline rules.

**Required predicates:** Issuer accreditation; registry snapshot validity; proof validity.

**Nominal flow:** Verifier evaluates cached signed registry material, its freshness, and transaction risk. It either verifies offline, defers, or falls back according to profile.

**Expected verifier output:** Accepted-offline, deferred, or rejected with cache-age and policy reason.

**Privacy claim:** Offline behaviour must not require later holder-identifying reconciliation.

**Named adversaries:** Network attacker; malicious cache; verifier; registry operator.

**Privacy and assurance horizon:** Configured cache lifetime and outage duration.

**Governance dependencies:** Maximum staleness; risk tiers; emergency overrides; audit.

**Failure and abuse cases:** Stale cache accepts revoked issuer; forced outage creates denial of service; different implementations choose different fallback.

**What the proof does not establish:** It does not prove current status beyond the snapshot horizon.

**Specification pressure points:** Signed snapshots; cache semantics; deterministic fallback; operational resilience.

**Minimum conformance tests:** Known stale snapshot yields same outcome across implementations; tampered snapshot fails; high-risk profile refuses beyond configured staleness.

**Priority:** `P1`

---

### UC-015 — Multiple Trust Registries Disagree

**Objective:** Resolve cases where different registries or governance frameworks disagree about issuer accreditation or status.

**Actors:** Verifier; two or more registries; issuer; holder; recognition authority.

**Context boundary:** A cross-ecosystem transaction with explicit trust-policy precedence.

**Preconditions:** The verifier accepts more than one framework; recognition relationships are defined or intentionally absent.

**Required predicates:** Issuer accreditation under named framework; policy version; registry evidence.

**Nominal flow:** The verifier receives proof referencing an accreditation framework. It evaluates recognition and precedence rules, not merely set membership.

**Expected verifier output:** Accepted under framework X, rejected due to conflict, or manual review.

**Privacy claim:** Framework evaluation must not expose holder identity or correlate presentations across registries.

**Named adversaries:** Registry operators; verifier; issuer; colluding registries.

**Privacy and assurance horizon:** Recognition agreement and registry snapshot validity.

**Governance dependencies:** Recognition; precedence; dispute resolution; federation governance.

**Failure and abuse cases:** Registry shopping; ambiguous precedence; framework identifier collision; verifier combines registries in a way that deanonymises issuer.

**What the proof does not establish:** It does not resolve governance conflict automatically.

**Specification pressure points:** Trust-policy expression; recognition semantics; issuer-set composition; privacy under federation.

**Minimum conformance tests:** Conflict cases produce deterministic outcomes; recognition rule is explicit; verifier cannot silently widen the accepted set.

**Priority:** `P1`

---

### UC-016 — Cross-Border Recognition of Liveness Assurance

**Objective:** Allow a verifier in one jurisdiction to rely on a liveness attestation issued under another jurisdiction's accredited framework.

**Actors:** Principal; foreign issuer; domestic verifier; two framework operators; recognition authority.

**Context boundary:** A named cross-border transaction and recognition arrangement.

**Preconditions:** Framework recognition exists; policy and assurance mapping are published.

**Required predicates:** Liveness attestation; issuer accreditation; policy mapping; freshness.

**Nominal flow:** The holder presents a proof under the foreign framework. The verifier maps assurance class and policy to domestic requirements and applies recognition conditions.

**Expected verifier output:** Recognition result, mapped assurance class, and any limitations.

**Privacy claim:** Cross-border verification must not require identity disclosure or create a global correlator.

**Named adversaries:** Domestic verifier; foreign issuer; both frameworks; cross-border collusion.

**Privacy and assurance horizon:** Recognition agreement and proof validity.

**Governance dependencies:** Legal effect; liability; redress; policy equivalence; sanctions or suspension.

**Failure and abuse cases:** Assurance classes appear equivalent but differ materially; recognition withdrawn; data localisation rules conflict with verification.

**What the proof does not establish:** It does not prove legal identity or universal legal recognition.

**Specification pressure points:** Policy mapping; framework discovery; liability; cross-border status.

**Minimum conformance tests:** Mapping is versioned; withdrawal takes effect predictably; verifier cannot infer specific issuer when profile conceals it.

**Priority:** `P1`

---

### UC-017 — Low-End or Constrained Consumer Device

**Objective:** Test whether the selected proof profile is deployable on low-memory, low-power, or older devices.

**Actors:** Principal; constrained device; wallet; verifier; optional mediated prover.

**Context boundary:** Any use case where consumer-device proof generation is required.

**Preconditions:** Device capabilities are below reference hardware; profile defines resource limits and fallback.

**Required predicates:** Depends on target profile.

**Nominal flow:** Wallet negotiates profile, estimates capability, generates proof locally or invokes a permitted fallback without silently weakening privacy or assurance.

**Expected verifier output:** Proof, explicit fallback indicator, or standards-based failure.

**Privacy claim:** Mediated proving must not expose raw biometric or reusable secrets to the mediator unless explicitly allowed.

**Named adversaries:** Mediated prover; wallet provider; verifier; device malware.

**Privacy and assurance horizon:** Per proof session; mediator logs may create long-term privacy risk.

**Governance dependencies:** Minimum device support; accessibility; fallback policy; user disclosure and consent.

**Failure and abuse cases:** Out-of-memory; excessive battery drain; hidden cloud proving; timeout; fallback changes adversary model.

**What the proof does not establish:** It does not guarantee device integrity.

**Specification pressure points:** Resource ceilings; profile negotiation; mediated proving; transparency of fallback.

**Minimum conformance tests:** Benchmarks on defined low-end hardware; deterministic failure code; no automatic downgrade without policy signal; mediator cannot reconstruct protected inputs.

**Priority:** `P0`

---

### UC-018 — Intermittent Connectivity and Offline Presentation

**Objective:** Allow proof presentation where either holder or verifier lacks continuous connectivity.

**Actors:** Holder; verifier; issuer; registry; synchronization service.

**Context boundary:** Field, rural, travel, emergency, or disconnected environment.

**Preconditions:** Required credentials, roots, status snapshots, and challenges can be provisioned offline.

**Required predicates:** Liveness or credential predicate; freshness; holder binding; cached status.

**Nominal flow:** Verifier creates a local challenge. Holder generates proof offline. Verifier validates with cached trusted material and records acceptance for later synchronization.

**Expected verifier output:** Offline verification result, snapshot age, and reconciliation requirement.

**Privacy claim:** Later synchronization must not turn offline pseudonyms into cross-context correlators.

**Named adversaries:** Offline verifier; synchronization service; replay attacker; malicious cache.

**Privacy and assurance horizon:** Offline window and reconciliation period.

**Governance dependencies:** Maximum offline duration; double-use resolution; liability; emergency policy.

**Failure and abuse cases:** Concurrent offline acceptance of same nullifier; stale revocation; clock drift; duplicate reconciliation.

**What the proof does not establish:** It does not prove current online status beyond cached material.

**Specification pressure points:** Offline freshness; double-spend; clock trust; reconciliation privacy.

**Minimum conformance tests:** Clock skew boundaries; duplicate nullifiers reconciled predictably; stale snapshots handled by profile; audit does not expose cross-context identity.

**Priority:** `P1`

---

### UC-019 — Shared Device and Multi-User Wallet

**Objective:** Support multiple people using the same device without cross-user correlation or accidental proof substitution.

**Actors:** Several principals; shared device; wallet; verifier; issuer.

**Context boundary:** Separate user profiles on one physical device.

**Preconditions:** Wallet supports secure separation; device identifiers are not part of the proof unless explicitly required.

**Required predicates:** Holder binding; liveness; freshness; optional same-human continuity.

**Nominal flow:** The selected user activates their isolated holder context, responds to the challenge, and generates a proof bound to their key and session.

**Expected verifier output:** Valid proof for the selected holder only.

**Privacy claim:** Verifier must not learn that several principals share the device; wallet must not mix roots, keys, or nullifiers.

**Named adversaries:** Other device users; wallet provider; verifier; device malware.

**Privacy and assurance horizon:** Device lifetime and account sessions.

**Governance dependencies:** Household use; minors; assisted use; device loss.

**Failure and abuse cases:** Wrong user selected; device identifier correlates users; shared biometric cache; wallet backup merges identities.

**What the proof does not establish:** It does not prove exclusive device control.

**Specification pressure points:** Key isolation; metadata leakage; user selection; recovery.

**Minimum conformance tests:** One user's proof cannot be generated from another user's context; no common device identifier appears in proof artefacts; backups preserve separation.

**Priority:** `P1`

---

### UC-020 — Accessibility Alternative to Facial Liveness

**Objective:** Provide an equivalent assurance path for users unable to complete the default biometric liveness interaction.

**Actors:** Principal; accessibility service; alternative biometric or assisted process; issuer; verifier.

**Context boundary:** Same transaction and assurance objective as the default profile.

**Preconditions:** Alternative method is defined and accredited; verifier recognises equivalent or explicitly different assurance.

**Required predicates:** Liveness or human-presence predicate under alternative policy; holder binding; freshness.

**Nominal flow:** The principal selects an accessible route. An accredited provider performs an alternative process and issues an attestation under a named policy. The holder proves the required predicates.

**Expected verifier output:** Human-presence result, policy identifier, assurance class, without unnecessary disclosure of disability.

**Privacy claim:** Verifier should not infer disability unless operationally unavoidable and explicitly permitted.

**Named adversaries:** Verifier; provider; issuer-verifier collusion.

**Privacy and assurance horizon:** Transaction and attestation validity.

**Governance dependencies:** Equivalence; non-discrimination; appeal; assisted participation; fraud controls.

**Failure and abuse cases:** Verifier rejects alternative profile despite policy; alternative method reveals disability; lower assurance is hidden.

**What the proof does not establish:** It does not prove equivalence unless the governance framework establishes it.

**Specification pressure points:** Profile negotiation; policy disclosure; privacy of accessibility needs; fallback without discrimination.

**Minimum conformance tests:** Alternative profile produces explicit assurance; verifier cannot demand default method when equivalent accepted; disability is not encoded as an unnecessary attribute.

**Priority:** `P0`

---

### UC-021 — Compromised Wallet Key but Live Human Present

**Objective:** Determine how the system responds when holder-key control and human continuity diverge.

**Actors:** Principal; attacker; wallet; verifier; issuer; recovery service.

**Context boundary:** Login, high-value action, or recovery.

**Preconditions:** Attacker has copied key; legitimate principal can satisfy liveness and continuity.

**Required predicates:** Holder binding; liveness; same-human-as-enrolment; freshness.

**Nominal flow:** A risk policy requires both key control and same-human continuity. An attacker with key alone fails. The legitimate user may recover and rotate the key.

**Expected verifier output:** Composite result distinguishing key control from human continuity.

**Privacy claim:** Failure responses must not reveal enrolment membership to attackers.

**Named adversaries:** Key thief; verifier; issuer; recovery operator.

**Privacy and assurance horizon:** Until key rotation and revocation complete.

**Governance dependencies:** Recovery; liability; notification; evidence handling.

**Failure and abuse cases:** System treats key control as sufficient; attacker probes continuity; race between attacker transaction and recovery.

**What the proof does not establish:** It does not prove the legitimate person is uncoerced or that the device is clean.

**Specification pressure points:** Predicate composition; non-enumerable errors; race handling; key revocation.

**Minimum conformance tests:** Key-only attacker fails without learning why; legitimate recovery invalidates old key; composite policy is consistent across verifiers.

**Priority:** `P0`

---

### UC-022 — Malicious or Compromised Biometric Provider

**Objective:** Test accountability and containment when an accredited provider issues false liveness determinations.

**Actors:** Biometric provider; issuer; framework operator; holder; verifier; auditor.

**Context boundary:** Any proof relying on provider determination.

**Preconditions:** Provider is accredited but compromised, negligent, or adversarial.

**Required predicates:** Issuer-signature proof; policy and assurance disclosure; status.

**Nominal flow:** Cryptographic verification succeeds because the attestation is validly signed. Governance monitoring later detects provider failure and changes accreditation or status.

**Expected verifier output:** At presentation time, proof may be valid under then-current policy; later actions follow suspension, incident, and remediation rules.

**Privacy claim:** Incident response should not require mass disclosure of holder biometrics.

**Named adversaries:** Provider; issuer; verifier; collusion.

**Privacy and assurance horizon:** Attestation lifetime and incident-review period.

**Governance dependencies:** Accreditation; audit; liability; suspension; notification; remediation; redress.

**Failure and abuse cases:** Verifiers assume ZKP proves model correctness; retroactive revocation harms legitimate users; no way to identify affected policy class without deanonymising holders.

**What the proof does not establish:** The ZKP does not prove the biometric determination was correct.

**Specification pressure points:** Plain-language assurance boundary; incident semantics; selective remediation; status privacy.

**Minimum conformance tests:** Conformance language prevents overclaim; issuer suspension propagates; affected proofs can be handled by policy without biometric disclosure.

**Priority:** `P0`

---

### UC-023 — Malicious Verifier Attempts Cross-Context Correlation

**Objective:** Test whether a verifier can manipulate context, transcript, or request fields to correlate a principal across services.

**Actors:** Principal; malicious verifier; issuer; wallet; other verifier.

**Context boundary:** Two nominally separate contexts controlled by one organisation or colluding organisations.

**Preconditions:** Wallet receives context identifiers from verifier; context governance rules exist.

**Required predicates:** Any proof using scoped nullifiers or transcript binding.

**Nominal flow:** Verifier tries to reuse the same context ID, audience, or root across separate services. Wallet validates whether the requested context is authorised and visible to the user or policy engine.

**Expected verifier output:** Proof only for a valid context or explicit rejection.

**Privacy claim:** Separate contexts remain unlinkable against verifier-only or verifier-collusion adversary, according to selected profile.

**Named adversaries:** One verifier operating several services; colluding verifiers; issuer-verifier collusion.

**Privacy and assurance horizon:** Context lifetime.

**Governance dependencies:** Who assigns context IDs; discoverability; user notice; audit; anti-abuse controls.

**Failure and abuse cases:** Verifier self-declares global context; wallet accepts opaque context; domain aliasing; context changes without migration.

**What the proof does not establish:** It does not guarantee unlinkability if the governance model intentionally defines one shared context.

**Specification pressure points:** Context authority; domain separation; wallet policy; collusion model.

**Minimum conformance tests:** Unauthorized context reuse is rejected; canonical context identifiers are stable and auditable; two valid contexts produce unlinkable artefacts.

**Priority:** `P0`

---

### UC-024 — Issuer and Verifier Collude

**Objective:** Determine whether the selected privacy profile survives the issuer and verifier sharing all observable data.

**Actors:** Issuer; verifier; principal; wallet; framework operator.

**Context boundary:** Any proof profile claiming collusion resistance.

**Preconditions:** Issuer knows issuance events and verifier knows presentation events.

**Required predicates:** Issuer concealment where applicable; context unlinkability; transcript binding.

**Nominal flow:** Issuer and verifier combine issuance timing, commitments, roots, proof artefacts, and network metadata to attempt re-identification.

**Expected verifier output:** A documented privacy result: resistant, partially resistant, or not resistant, with explicit assumptions.

**Privacy claim:** The claim must state exactly what remains unlinkable and for how long under collusion.

**Named adversaries:** Issuer-verifier collusion, including shared infrastructure and logs.

**Privacy and assurance horizon:** Credential and enrolment lifetime, not merely proof session.

**Governance dependencies:** Separation duties; logging limits; audit; accreditation controls.

**Failure and abuse cases:** Issuer embeds tags; unique policy combinations fingerprint holder; timing correlation; enrolment root becomes a long-lived correlator.

**What the proof does not establish:** No claim of collusion resistance is valid unless the profile and implementation prevent these channels.

**Specification pressure points:** Foundational context question; artefact lifetime; metadata; covert tagging; governance controls.

**Minimum conformance tests:** Red-team correlation across issuance and presentation datasets; proof artefacts contain no issuer tag; timing and root leakage documented.

**Priority:** `P0`

---

### UC-025 — Proof Composition Across Credentials and Trust Tasks

**Objective:** Ensure several individually private proofs do not become identifying or inconsistent when combined in one task.

**Actors:** Principal; wallet/VTA; verifier; several issuers; trust-task orchestrator.

**Context boundary:** A composite transaction requesting several predicates.

**Preconditions:** Each credential proof is independently valid; composition rules exist.

**Required predicates:** Multiple credential predicates; liveness; holder binding; freshness; optional uniqueness.

**Nominal flow:** The verifier requests a composite proof or bundle. The wallet binds all components to one transcript and reveals only the minimum required conjunction.

**Expected verifier output:** One composite policy result or a structured bundle with explicit binding.

**Privacy claim:** Joint disclosure should not create a unique fingerprint or allow cross-proof correlation beyond the task context.

**Named adversaries:** Verifier; multiple issuers; verifier-issuer collusion; task orchestrator.

**Privacy and assurance horizon:** Task session and any retained audit artefact.

**Governance dependencies:** Data minimisation; purpose; orchestration responsibility; retention.

**Failure and abuse cases:** Different holder secrets used across proofs; selective disclosure combination uniquely identifies user; one proof replayed in another bundle.

**What the proof does not establish:** Individually private proofs do not guarantee private composition.

**Specification pressure points:** Common transcript; subject binding; correlation analysis; responsibility split with Trust Task Protocols TF.

**Minimum conformance tests:** Bundle fails if component transcript differs; minimal disclosure analysis; repeated composition does not expose stable cross-task identifier.

**Priority:** `P0`

---

### UC-026 — Algorithm Upgrade and Mixed-Version Ecosystem

**Objective:** Maintain semantic interoperability while proof algorithms and profiles are upgraded.

**Actors:** Holder wallet; verifier; issuer; registry; software vendor; framework operator.

**Context boundary:** Transition from profile or algorithm version A to B.

**Preconditions:** Old and new implementations coexist; identifiers and deprecation policy exist.

**Required predicates:** Any.

**Nominal flow:** Verifier advertises supported profiles. Wallet selects a mutually supported option. Policy determines whether older proofs remain acceptable.

**Expected verifier output:** Negotiated profile, algorithm identifier, deprecation status, verification result.

**Privacy claim:** Negotiation should not create a unique client fingerprint beyond necessary capability disclosure.

**Named adversaries:** Verifier fingerprinting clients; downgrade attacker; compromised update channel.

**Privacy and assurance horizon:** Migration period.

**Governance dependencies:** Deprecation; minimum versions; emergency disablement; post-quantum migration.

**Failure and abuse cases:** Silent downgrade; semantic changes under same profile ID; unsupported verifier; old proving key accepted indefinitely.

**What the proof does not establish:** Algorithm agility does not guarantee post-quantum security.

**Specification pressure points:** Negotiation; downgrade protection; semantic versioning; test vectors across versions.

**Minimum conformance tests:** Downgrade attack fails; same predicate semantics maintained; unsupported profile gives standard error; deprecation dates enforced.

**Priority:** `P0`

---

### UC-027 — Verifier Policy Error, Appeal, and Redress

**Objective:** Allow a person to challenge an adverse decision without disclosing the protected biometric or collapsing anonymity.

**Actors:** Principal; verifier; issuer; framework operator; appeals body; auditor.

**Context boundary:** A rejected transaction or account action.

**Preconditions:** Verifier records a privacy-preserving decision receipt and reason code.

**Required predicates:** Any relevant proof plus decision evidence.

**Nominal flow:** Verifier rejects or downgrades the proof. Holder receives a receipt identifying profile, policy, status snapshot, and failure class. An appeal can verify the process without accessing raw biometric evidence unless separately governed.

**Expected verifier output:** Machine-readable failure reason and appeal reference.

**Privacy claim:** Appeal should not force identity disclosure unless strictly necessary and governed.

**Named adversaries:** Verifier; appeals operator; issuer; collusion.

**Privacy and assurance horizon:** Retention and appeal period.

**Governance dependencies:** Explanation; correction; liability; audit access; confidentiality.

**Failure and abuse cases:** Opaque `invalid proof`; verifier stores full proof indefinitely; appeal requires biometric resubmission; inconsistent reason codes.

**What the proof does not establish:** A valid proof does not guarantee a favourable policy decision.

**Specification pressure points:** Decision receipts; standard errors; auditability; privacy-preserving evidence retention.

**Minimum conformance tests:** Same failure produces same reason class; receipt is non-replayable; appeal can distinguish proof failure from policy rejection.

**Priority:** `P0`

---

### UC-028 — Emergency or Disaster Operations

**Objective:** Support urgent transactions when normal issuer, registry, or network infrastructure is degraded without creating permanent privacy exceptions.

**Actors:** Principal; emergency service; verifier; issuer; registry; local authority.

**Context boundary:** Declared emergency, bounded geography, and time period.

**Preconditions:** Emergency profile and fallback rules are pre-defined.

**Required predicates:** Liveness; holder binding; cached credential predicates; optional reduced assurance.

**Nominal flow:** Verifier invokes emergency profile, discloses reduced assurance, verifies against cached material, and records an auditable, expiring exception.

**Expected verifier output:** Accepted under emergency profile with limitations and expiry.

**Privacy claim:** Emergency handling should not create reusable global identifiers or indefinite retention.

**Named adversaries:** Verifier abusing emergency mode; attacker inducing outage; cache operator.

**Privacy and assurance horizon:** Emergency period plus limited audit window.

**Governance dependencies:** Who declares emergency; permitted uses; post-event review; redress.

**Failure and abuse cases:** Emergency profile becomes permanent; lowered assurance hidden; cached issuer revoked; exception artefacts become correlators.

**What the proof does not establish:** It does not provide normal assurance under degraded conditions.

**Specification pressure points:** Explicit degraded assurance; sunset; audit; privacy under exception.

**Minimum conformance tests:** Emergency mode expires automatically; use outside declared scope fails; verifier output clearly marks reduced assurance.

**Priority:** `P2`

---

### UC-029 — Large-Scale Batch Verification

**Objective:** Test verifier throughput and privacy when millions of proofs are processed daily.

**Actors:** Many holders; high-volume verifier; issuer sets; status services; analytics systems.

**Context boundary:** A large platform or infrastructure service.

**Preconditions:** Profile supports high throughput; rate limits and caching are defined.

**Required predicates:** Varies.

**Nominal flow:** Verifier processes proofs in parallel, validates roots and status efficiently, and stores only required outputs.

**Expected verifier output:** Per-proof deterministic result and aggregate operational metrics.

**Privacy claim:** Operational analytics must not create a shadow identity graph from proof metadata.

**Named adversaries:** Verifier analytics team; infrastructure operator; issuer-verifier collusion.

**Privacy and assurance horizon:** Proof session versus retained logs and metrics.

**Governance dependencies:** Retention; purpose limitation; security monitoring; incident response.

**Failure and abuse cases:** Unique proof sizes fingerprint users; logs retain transcript and nullifier across contexts; status checks overload registry.

**What the proof does not establish:** High throughput does not imply privacy-preserving operations.

**Specification pressure points:** Batch verification; caching; logging; metadata minimisation; denial of service.

**Minimum conformance tests:** Target throughput on reference hardware; bounded memory; privacy-safe logs; registry load under peak traffic.

**Priority:** `P1`

---

### UC-030 — Partial Deployment Across Independent Implementations

**Objective:** Demonstrate that the specification produces interoperable outcomes across different issuers, wallets, and verifiers.

**Actors:** At least two issuer implementations; two wallet/prover implementations; two verifiers; one or more registries.

**Context boundary:** Conformance plugfest or reference deployment.

**Preconditions:** Shared test vectors, profiles, error codes, and registry fixtures exist.

**Required predicates:** Minimum liveness profile and extended personhood profile.

**Nominal flow:** Each wallet proves attestations from each issuer to each verifier. Positive, negative, lifecycle, version, and privacy tests are executed.

**Expected verifier output:** Interoperability report and defect classification.

**Privacy claim:** Conformance testing includes correlation and metadata analysis, not only cryptographic validity.

**Named adversaries:** Non-malicious implementation divergence; maliciously crafted proof; verifier fingerprinting.

**Privacy and assurance horizon:** Across implementation and profile versions.

**Governance dependencies:** Conformance authority; test governance; defect handling.

**Failure and abuse cases:** All implementations verify their own proofs but fail cross-vendor; ambiguous encoding; different policy outcomes; inconsistent context handling.

**What the proof does not establish:** Passing cryptographic test vectors alone does not prove ecosystem interoperability.

**Specification pressure points:** Normative encodings; canonical transcript; error semantics; profile negotiation; privacy conformance.

**Minimum conformance tests:** Full cross-product test matrix; negative tests; malformed inputs; version mismatch; privacy leakage review.

**Priority:** `P0`

---

## 7. Coverage matrix

| Capability or pressure area | Primary use cases |
|---|---|
| Minimum liveness profile | UC-004, UC-006, UC-017, UC-020 |
| Extended personhood profile | UC-001, UC-002, UC-007, UC-008 |
| Scoped nullifiers | UC-001, UC-002, UC-007, UC-008, UC-023 |
| Same-human-as-enrolment | UC-005, UC-006, UC-021 |
| Holder-key binding | UC-004, UC-006, UC-009, UC-021 |
| Agent delegation | UC-009, UC-010, UC-011 |
| Canonical transcript and freshness | UC-004, UC-006, UC-010, UC-025 |
| Issuer accreditation | UC-012, UC-013, UC-015, UC-016 |
| Trust registry lifecycle | UC-012, UC-014, UC-015 |
| Cross-border recognition | UC-016 |
| Offline and degraded operation | UC-014, UC-018, UC-028 |
| Accessibility | UC-017, UC-019, UC-020 |
| Recovery and key rotation | UC-005, UC-021 |
| Malicious issuer/provider | UC-022 |
| Malicious verifier | UC-023 |
| Issuer-verifier collusion | UC-024 |
| Proof composition | UC-025 |
| Algorithm agility | UC-026 |
| Audit, appeal, and redress | UC-027 |
| Scale and throughput | UC-029 |
| Cross-vendor interoperability | UC-030 |

## 8. Priority bands

### P0 — Required before a V1.0 profile can credibly be called implementable

P0 use cases validate the semantic core, assurance boundaries, context model, lifecycle, recovery, accessibility, composition, algorithm agility, and independent implementation.

Recommended P0 set:

- UC-001 Privacy-Preserving Account Creation
- UC-002 Anonymous or Pseudonymous Community Participation
- UC-004 High-Value Financial Transaction Step-Up
- UC-005 Sensitive Account Recovery
- UC-006 Recurring Login With Same-Human Continuity
- UC-009 Human Authorises an AI Agent
- UC-010 Human Step-Up for Agent Intent Drift
- UC-012 Issuer Suspension After Proof Issuance
- UC-013 Accreditation Framework or Policy Version Change
- UC-017 Low-End or Constrained Consumer Device
- UC-020 Accessibility Alternative to Facial Liveness
- UC-021 Compromised Wallet Key but Live Human Present
- UC-022 Malicious or Compromised Biometric Provider
- UC-023 Malicious Verifier Attempts Cross-Context Correlation
- UC-024 Issuer and Verifier Collude
- UC-025 Proof Composition Across Credentials and Trust Tasks
- UC-026 Algorithm Upgrade and Mixed-Version Ecosystem
- UC-027 Verifier Policy Error, Appeal, and Redress
- UC-030 Partial Deployment Across Independent Implementations

### P1 — Required for production-readiness guidance

P1 cases validate sectoral deployment, federation, offline use, shared devices, and scale.

### P2 — Required for resilience profiles and later implementation guidance

P2 cases validate exceptional and emergency modes.

## 9. Proposed implementation programme

### Phase 1 — Corpus ratification and mapping

**Target:** 2 weeks

- Confirm the use-case template.
- Confirm P0, P1, and P2 prioritisation.
- Map every P0 use case to the Predicate & Assurance-Boundary decision document.
- Identify undefined terms, especially `context`, `scope`, `epoch`, `same-human-as-enrolment`, and `accreditation framework`.
- Record whether each privacy claim is against the verifier, issuer, or issuer-verifier collusion.

**Exit criterion:** Every P0 use case has an explicit predicate set, adversary, horizon, and context definition.

### Phase 2 — Profile and protocol mapping

**Target:** 2 to 3 weeks

- Map P0 use cases to the minimum liveness and extended personhood profiles.
- Identify which behaviours belong in ZKP profiles, credential formats, trust-task protocols, trust registries, or governance frameworks.
- Define canonical transcript fields.
- Define status, expiry, revocation, fallback, and error semantics.
- Identify proof-composition requirements.

**Exit criterion:** No P0 use case requires an implementer to invent an unstated cross-component contract.

### Phase 3 — Conformance design

**Target:** 3 weeks

- Convert P0 conformance statements into positive and negative test cases.
- Define registry fixtures, issuer sets, policy versions, and status transitions.
- Define privacy tests, including malicious verifier and issuer-verifier collusion cases.
- Define constrained-device and offline benchmark conditions.
- Define standard reason codes and decision receipts.

**Exit criterion:** A conformance suite specification exists independently of any single implementation.

### Phase 4 — Interoperability build

**Target:** aligned with the October build

- Implement at least two independent prover/wallet stacks.
- Implement at least two independent verifiers.
- Use at least two issuer implementations.
- Exercise the cross-product against UC-030.
- Run the P0 threat and lifecycle scenarios.
- Publish benchmark and interoperability results.

**Exit criterion:** Independent implementations agree on verifier outcomes and privacy properties for the P0 corpus.

### Phase 5 — Working Draft integration

**Target:** before IIW #43

- Incorporate resolved gaps into the Working Draft.
- Mark unsupported P1/P2 cases explicitly.
- Publish an implementation report.
- Record known limitations and non-goals.
- Create a backlog for production-readiness guidance.

## 10. Readiness gates

A profile should not be described as implementation-ready unless all applicable gates pass.

### Gate A — Predicate clarity

- Every predicate states what it establishes.
- Every predicate states what it does not establish.
- Public and private inputs are explicit.
- Verifier outputs are explicit.

### Gate B — Privacy clarity

- The adversary is named.
- The horizon is named.
- The context is defined.
- Permitted linkability is explicit.
- Composition leakage has been assessed.

### Gate C — Assurance clarity

- Policy and assurance class are represented.
- Accreditation framework is discoverable.
- Status-time semantics are deterministic.
- Accountability for an incorrect underlying determination is explicit.

### Gate D — Lifecycle completeness

- Expiry is defined.
- Revocation and suspension are defined.
- Policy upgrades are defined.
- Key recovery and rotation are defined.
- Registry unavailability has a defined outcome.

### Gate E — Interoperability

- Canonical encodings exist.
- Canonical transcript exists.
- Version negotiation exists.
- Error codes are standardised.
- Cross-vendor test vectors pass.

### Gate F — Operational viability

- Consumer-device resource ceilings are measured.
- Offline and constrained conditions are understood.
- Fallback behaviour is explicit.
- Accessibility alternatives are supported.
- Logging and audit do not undermine privacy.

### Gate G — Governance and redress

- Adverse decisions produce actionable reason codes.
- Appeal and correction paths exist.
- Governance dependencies are documented.
- The proof is not represented as carrying assurance it does not carry.

## 11. Standard conformance artefacts to derive from this corpus

The corpus should eventually produce:

1. A machine-readable use-case index.
2. Profile applicability statements.
3. Positive and negative test vectors.
4. Canonical transcript fixtures.
5. Issuer-set and registry fixtures.
6. Revocation, suspension, and policy-transition fixtures.
7. Nullifier scope and epoch fixtures.
8. Delegation fixtures.
9. Offline and stale-cache fixtures.
10. Privacy red-team scripts.
11. Constrained-device benchmark profiles.
12. Standard verifier reason codes.
13. Decision-receipt examples.
14. Cross-version negotiation tests.
15. A cross-vendor interoperability matrix.

## 12. Open questions exposed by the corpus

1. Who has authority to define a context identifier?
2. Must a context boundary survive issuer-verifier collusion?
3. How is context equivalence or hierarchy represented?
4. Can an enrolment root itself become a correlator?
5. What are the normative status-time semantics for issuer suspension?
6. How are recovery and key rotation prevented from resetting uniqueness?
7. Which proof-composition rules belong to this TF versus the Trust Task Protocols TF?
8. What information about the accreditation framework must always be disclosed?
9. When is specific issuer concealment optional, required, or prohibited?
10. How are offline duplicate uses resolved?
11. What fallback modes are allowed, and how is reduced assurance disclosed?
12. How does a holder challenge a verifier decision without revealing protected evidence?
13. What is the minimum acceptable accessibility alternative?
14. How are agent delegation and proof presentation bound without exposing principal identity?
15. Which privacy claims are feasible against issuer-verifier collusion in practice?
16. What metadata must be excluded from logs to preserve the stated privacy claim?
17. Which algorithm and profile negotiation mechanism prevents downgrade?
18. What evidence is required before a profile can claim production readiness?

## 13. Recommended immediate task-force action

Adopt this corpus as a living implementation-validation document rather than a normative specification.

The immediate work should be:

1. Ratify the template and P0 list.
2. Assign one or two owners to each P0 scenario.
3. Map the scenarios to the Predicate & Assurance-Boundary decision document.
4. Mark every unresolved dependency as belonging to:
   - ZKP profile,
   - credential model,
   - trust-task protocol,
   - trust registry,
   - biometric-provider contract, or
   - governance framework.
5. Convert UC-030 into the initial interoperability plan.
6. Use failures against the corpus to drive specification changes before the Working Draft is treated as stable.

The core test is straightforward:

> Can two independent teams implement the same profile, apply it to the same pressure-test scenario, and reach the same verifier result without making hidden assumptions about privacy, assurance, lifecycle, or governance?

If the answer is no, the profile is not yet interoperable, even if the underlying proof verifies.


# Deployment and adoption scenarios

## UC-031 — Migration from conventional identity checks

**Objective.** Pressure-test authority, enforcement, revocation and evidence under migration from conventional identity checks.

**Required outcome.** The implementation produces a deterministic decision, identifies the accountable authority, preserves minimized evidence and invokes the applicable deployment control or operational runbook.

**Failure condition.** The system silently broadens authority, accepts stale or downgraded state, loses revocation history, crosses tenant boundaries or cannot explain the decision.

## UC-032 — Managed enterprise wallet deployment

**Objective.** Pressure-test authority, enforcement, revocation and evidence under managed enterprise wallet deployment.

**Required outcome.** The implementation produces a deterministic decision, identifies the accountable authority, preserves minimized evidence and invokes the applicable deployment control or operational runbook.

**Failure condition.** The system silently broadens authority, accepts stale or downgraded state, loses revocation history, crosses tenant boundaries or cannot explain the decision.

## UC-033 — Multi-tenant verifier isolation

**Objective.** Pressure-test authority, enforcement, revocation and evidence under multi-tenant verifier isolation.

**Required outcome.** The implementation produces a deterministic decision, identifies the accountable authority, preserves minimized evidence and invokes the applicable deployment control or operational runbook.

**Failure condition.** The system silently broadens authority, accepts stale or downgraded state, loses revocation history, crosses tenant boundaries or cannot explain the decision.

## UC-034 — Federated issuer ecosystem

**Objective.** Pressure-test authority, enforcement, revocation and evidence under federated issuer ecosystem.

**Required outcome.** The implementation produces a deterministic decision, identifies the accountable authority, preserves minimized evidence and invokes the applicable deployment control or operational runbook.

**Failure condition.** The system silently broadens authority, accepts stale or downgraded state, loses revocation history, crosses tenant boundaries or cannot explain the decision.

## UC-035 — Registry federation and authority transition

**Objective.** Pressure-test authority, enforcement, revocation and evidence under registry federation and authority transition.

**Required outcome.** The implementation produces a deterministic decision, identifies the accountable authority, preserves minimized evidence and invokes the applicable deployment control or operational runbook.

**Failure condition.** The system silently broadens authority, accepts stale or downgraded state, loses revocation history, crosses tenant boundaries or cannot explain the decision.

## UC-036 — Multi-region verifier deployment

**Objective.** Pressure-test authority, enforcement, revocation and evidence under multi-region verifier deployment.

**Required outcome.** The implementation produces a deterministic decision, identifies the accountable authority, preserves minimized evidence and invokes the applicable deployment control or operational runbook.

**Failure condition.** The system silently broadens authority, accepts stale or downgraded state, loses revocation history, crosses tenant boundaries or cannot explain the decision.

## UC-037 — Proof service or cloud-region outage

**Objective.** Pressure-test authority, enforcement, revocation and evidence under proof service or cloud-region outage.

**Required outcome.** The implementation produces a deterministic decision, identifies the accountable authority, preserves minimized evidence and invokes the applicable deployment control or operational runbook.

**Failure condition.** The system silently broadens authority, accepts stale or downgraded state, loses revocation history, crosses tenant boundaries or cannot explain the decision.

## UC-038 — Software supply-chain compromise

**Objective.** Pressure-test authority, enforcement, revocation and evidence under software supply-chain compromise.

**Required outcome.** The implementation produces a deterministic decision, identifies the accountable authority, preserves minimized evidence and invokes the applicable deployment control or operational runbook.

**Failure condition.** The system silently broadens authority, accepts stale or downgraded state, loses revocation history, crosses tenant boundaries or cannot explain the decision.

## UC-039 — Emergency signing-key rotation

**Objective.** Pressure-test authority, enforcement, revocation and evidence under emergency signing-key rotation.

**Required outcome.** The implementation produces a deterministic decision, identifies the accountable authority, preserves minimized evidence and invokes the applicable deployment control or operational runbook.

**Failure condition.** The system silently broadens authority, accepts stale or downgraded state, loses revocation history, crosses tenant boundaries or cannot explain the decision.

## UC-040 — Incorrect policy rollout and rollback

**Objective.** Pressure-test authority, enforcement, revocation and evidence under incorrect policy rollout and rollback.

**Required outcome.** The implementation produces a deterministic decision, identifies the accountable authority, preserves minimized evidence and invokes the applicable deployment control or operational runbook.

**Failure condition.** The system silently broadens authority, accepts stale or downgraded state, loses revocation history, crosses tenant boundaries or cannot explain the decision.

## UC-041 — Audit or regulatory evidence request

**Objective.** Pressure-test authority, enforcement, revocation and evidence under audit or regulatory evidence request.

**Required outcome.** The implementation produces a deterministic decision, identifies the accountable authority, preserves minimized evidence and invokes the applicable deployment control or operational runbook.

**Failure condition.** The system silently broadens authority, accepts stale or downgraded state, loses revocation history, crosses tenant boundaries or cannot explain the decision.

## UC-042 — Data-subject challenge and state correction

**Objective.** Pressure-test authority, enforcement, revocation and evidence under data-subject challenge and state correction.

**Required outcome.** The implementation produces a deterministic decision, identifies the accountable authority, preserves minimized evidence and invokes the applicable deployment control or operational runbook.

**Failure condition.** The system silently broadens authority, accepts stale or downgraded state, loses revocation history, crosses tenant boundaries or cannot explain the decision.

## UC-043 — High-volume burst and abuse traffic

**Objective.** Pressure-test authority, enforcement, revocation and evidence under high-volume burst and abuse traffic.

**Required outcome.** The implementation produces a deterministic decision, identifies the accountable authority, preserves minimized evidence and invokes the applicable deployment control or operational runbook.

**Failure condition.** The system silently broadens authority, accepts stale or downgraded state, loses revocation history, crosses tenant boundaries or cannot explain the decision.

## UC-044 — Compromised administrative operator

**Objective.** Pressure-test authority, enforcement, revocation and evidence under compromised administrative operator.

**Required outcome.** The implementation produces a deterministic decision, identifies the accountable authority, preserves minimized evidence and invokes the applicable deployment control or operational runbook.

**Failure condition.** The system silently broadens authority, accepts stale or downgraded state, loses revocation history, crosses tenant boundaries or cannot explain the decision.

## UC-045 — Expired privacy or assurance horizon

**Objective.** Pressure-test authority, enforcement, revocation and evidence under expired privacy or assurance horizon.

**Required outcome.** The implementation produces a deterministic decision, identifies the accountable authority, preserves minimized evidence and invokes the applicable deployment control or operational runbook.

**Failure condition.** The system silently broadens authority, accepts stale or downgraded state, loses revocation history, crosses tenant boundaries or cannot explain the decision.

## UC-046 — Cross-organization plugfest onboarding

**Objective.** Pressure-test authority, enforcement, revocation and evidence under cross-organization plugfest onboarding.

**Required outcome.** The implementation produces a deterministic decision, identifies the accountable authority, preserves minimized evidence and invokes the applicable deployment control or operational runbook.

**Failure condition.** The system silently broadens authority, accepts stale or downgraded state, loses revocation history, crosses tenant boundaries or cannot explain the decision.

## UC-047 — Cryptographic library vulnerability

**Objective.** Pressure-test authority, enforcement, revocation and evidence under cryptographic library vulnerability.

**Required outcome.** The implementation produces a deterministic decision, identifies the accountable authority, preserves minimized evidence and invokes the applicable deployment control or operational runbook.

**Failure condition.** The system silently broadens authority, accepts stale or downgraded state, loses revocation history, crosses tenant boundaries or cannot explain the decision.

## UC-048 — Partial rollback during ecosystem upgrade

**Objective.** Pressure-test authority, enforcement, revocation and evidence under partial rollback during ecosystem upgrade.

**Required outcome.** The implementation produces a deterministic decision, identifies the accountable authority, preserves minimized evidence and invokes the applicable deployment control or operational runbook.

**Failure condition.** The system silently broadens authority, accepts stale or downgraded state, loses revocation history, crosses tenant boundaries or cannot explain the decision.
