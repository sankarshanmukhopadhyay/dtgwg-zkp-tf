---
title: DTG ZKP Implementation and Interoperability Guide
status: incubating
normative_status: non-normative
owner: DTG ZKP Task Force
last_reviewed: 2026-07-17
---

# DTG ZKP Implementation and Interoperability Guide

## Status and use of this guide

This guide is a non-normative implementation companion. It explains how to combine proof semantics, credentials, delegation, registries, relying-party policy, lifecycle controls and conformance evidence without treating cryptographic verification as a substitute for governance authority. A future normative specification may adopt individual provisions through an explicit standards decision; placement in this guide does not make them binding.

The primary audience is implementers of issuers, wallets, verifiable trust agents, delegated agents, verifiers, registries and conformance tooling. Governance authorities, auditors, relying parties and reviewers can use the same material to identify authority boundaries and required evidence.

## 1. Scope and exclusions

The guide addresses proof-system-agnostic architecture, semantic interoperability, assurance boundaries, privacy claims, delegated action, lifecycle behavior, operational readiness and conformance. It does not select or invent a cryptographic construction, establish a certification scheme, ratify unresolved task-force policy or claim that a proof establishes the correctness of an upstream real-world determination.

The central implementation rule is that a proof establishes a defined statement under stated assumptions. Accreditation, policy, status, recognition, authorization, accountability and redress remain separate governed functions.

## 2. Conventions

Repository drafting rules and the [documentation style profile](../editorial/STYLE-GUIDE.md) apply. Guidance uses lowercase `should` and `may`; uppercase requirement keywords appear only when quoting or drafting explicitly normative material. `Open issue` marks a decision dependency. `Example` marks illustrative content.

## 3. System model

### 3.1 Actors, authority and responsibility

The system context includes governance and accreditation authorities, issuers, holders, wallets, principals, delegated agents, verifiers, registry operators, auditors and redress bodies. Their responsibilities are described in the [system context](../architecture/02-system-context.md) and [ownership model](../architecture/06-ownership-model.md).

An implementation should be able to answer six questions for every consequential action: who had authority, what was delegated, what scope applied, where policy was enforced, how authority could be suspended or revoked, and what evidence supports later review.

### 3.2 Architectural layers

The architecture separates governance, assurance, credential, proof, protocol, runtime and infrastructure layers. A lower layer must not silently absorb a decision assigned to another layer. For example, a successful proof check does not authorize an agent action, and a registry lookup does not by itself establish recognition or reliance.

### 3.3 Trust boundaries

Material boundaries include the holder and wallet, wallet and evidence provider, provider and issuer, issuer and holder, holder or agent and verifier, verifier and registry, registry and governance, and principal and agent. Each boundary requires an explicit threat, control and evidence treatment. See [trust boundaries](../architecture/05-trust-boundaries.md).

### 3.4 Information and protocol objects

A canonical proof request should identify the requester, context, epoch, nonce, predicates, accepted profiles and relying-party policy version. A presentation should bind to that request and identify its profile, disclosed claims and status references without adding unnecessary correlators. A verifier decision receipt should retain the request digest, policy version, registry or status versions, outcome and disclosure-safe reason code.

Delegation evidence is a separate object containing the principal, agent, scope, constraints, validity and revocation reference. It is not inferred from holder-key possession.

## 4. Boundary and assurance model

### 4.0 Paired boundary records

Every material predicate and profile maintains a linked assurance-boundary record and disclosure-boundary record. The assurance record states what a verifier may rely on and who is accountable for upstream correctness. The disclosure record states what each participant can observe or reconstruct. Both records use the issuer attestation schema as a common input and state **against whom**, **for how long** and **alongside what** the claim applies. See the [boundary workspace](../boundaries/README.md).

### 4.1 Predicate semantics

Every predicate has a stable identifier and records what it establishes, what it does not establish, its inputs, disclosure, evidence dependencies, governance dependencies, lifecycle behavior and conformance references. The current catalogue is maintained in [`taxonomy/predicates.md`](../taxonomy/predicates.md).

The proof of an issuer's attestation establishes possession and satisfaction of the encoded statement, subject to the proof system's assumptions. It does not establish that the issuer's enrollment or biometric determination was correct. Relying parties should evaluate the issuer, policy and assurance class separately.

### 4.2 Personhood, liveness and uniqueness

Policy-defined personhood is not civil identity. Liveness evidence is not personhood. Scoped uniqueness detects reuse inside a declared scope and epoch; it does not establish one natural person globally. Implementations should expose these distinctions in profile metadata, user-facing descriptions, verifier policy and decision receipts.

Recovery and re-enrollment require continuity rules that prevent an implementation from resetting duplicate-use protections merely by issuing a new credential or wallet secret. The authority deciding continuity, the evidence accepted and the treatment of prior nullifiers should be documented.

### 4.3 Holder binding, delegation and transaction authorization

Holder binding demonstrates control of a configured key or secret. It does not show that the presenter is a particular civil identity, that an agent is authorized, or that a transaction is permitted. Delegation should name the principal, agent, scope, purpose, duration, constraints, revocation mechanism and evidence. A relying party may require a fresh principal step-up when action value, risk, environment or requested permission changes materially.

The verifier should evaluate four independent questions: whether the proof is valid, whether the presenter controls the required holder material, whether the agent has applicable delegated authority, and whether the requested transaction is permitted by current policy.

### 4.4 Accreditation, registries and reliance

An accepted issuer set is governed state. Registry discovery, publication, accreditation, recognition, reliance and transaction authorization are distinct. A registry record should include authority, version, effective time, status and signature. A relying-party policy should define accepted record age, cache behavior, unavailable-state behavior and conflicting-state resolution.

A verifier should record the state and policy version used in a decision. Stale or unavailable registry state must not silently become successful verification. The policy may fail closed or invoke a documented degraded path whose lower or different assurance is visible and auditable.

## 5. Privacy and disclosure model

### 5.1 Claim record

A material privacy claim records the property, protected party, adversary, collusion assumptions, context, horizon, observable transcript, metadata, cryptographic and operational assumptions, exclusions, failure conditions, test method and evidence. Every claim states against whom, for how long and alongside what credentials, metadata, protocols, retained state and observable events it remains valid. This makes claims falsifiable and prevents unlinkability from being treated as an unconditional property.

### 5.2 Context, epoch and permitted linkability

A context authority determines the identifier or derivation rules used to scope linkability. The epoch authority determines time boundaries and rollover behavior. Both authorities should be explicit because an implementer cannot select a nullifier or pseudonym construction without knowing against whom and across which boundaries correlation must be resisted.

A draft V1 context definition, its required descriptor inputs, delimitation guidance and collusion-target requirements are recorded in [`boundaries/predicate-assurance-boundary-decision.md`](../boundaries/predicate-assurance-boundary-decision.md#6-foundational-context-decision) §6 and operationalized per instance in the [context decision record](../boundaries/context-decision-record.md). This is decision input, not yet a ratified specification (see the document's `normative_status`).

Open issue: the task force has a draft context model on the table but has not yet ratified it, and has not yet ratified the required resistance to issuer-verifier collusion, as raised in [Discussion #8](https://github.com/trustoverip/dtgwg-zkp-tf/discussions/8). A construction should not be selected as a normative profile ahead of that ratification.

### 5.3 Metadata and correlation

Privacy analysis covers identifiers, proof shape, nullifiers, contexts, epochs, timestamps, network metadata, registry lookups, retry patterns, error behavior, timing and device signals. Uniform cryptographic presentations can still become correlatable through operational differences. Implementers should test colluding verifier and issuer-verifier scenarios, including long-term observations over the declared horizon.

## 6. End-to-end implementation guidance

### 6.1 Profile selection

A profile should declare predicate semantics, accepted proof systems, context and epoch authority, assurance classes, accreditation and registry policy, lifecycle behavior, error policy, privacy claims and required conformance level. Experimental elements should be labelled and must not be presented as ratified interoperability requirements.

### 6.2 Issuance

Before issuance, the governance authority publishes the policy and assurance class and the accreditation authority establishes the issuer's status. The issuer validates enrollment evidence, binds the credential to holder material as the profile requires, records policy and assurance identifiers, establishes validity and status references, and produces an issuance audit record.

The issuer should disclose which determinations it made, which external providers it relied on and who is accountable for error. It should not describe the issued object as proof of an underlying fact beyond the named policy.

### 6.3 Request construction

The verifier creates a canonical request with a fresh nonce, context, epoch, requested predicates, accepted profiles, relying-party policy version and any transaction constraints. The request should be stable under canonicalization and should not contain unnecessary identifiers. The wallet validates requester authority and request compatibility before proof generation.

### 6.4 Holder authorization and proof generation

The wallet presents or evaluates the request according to holder policy, detects overbroad or unsupported predicates and selects credentials and proof material. It binds the proof to the canonical transcript. Consent or authorization evidence should record the request digest and presentation decision without retaining unnecessary sensitive data.

For a delegated agent, the wallet or verifier also validates delegation evidence. A high-risk or materially changed action triggers step-up rather than reusing a generic liveness or holder-binding proof.

### 6.5 Presentation and verification

The verifier parses the presentation canonically, checks profile support, validates freshness and transcript binding, verifies the cryptographic proof, evaluates predicate semantics, resolves status and accreditation, applies the relying-party policy and emits a deterministic outcome. Validation order should avoid expensive operations on malformed requests and avoid side-channel differences that expose sensitive failure details.

A successful cryptographic check followed by a failed policy, status or delegation check is a rejection. The decision receipt should preserve the distinct reason without claiming that the proof itself was invalid.

### 6.6 Scoped nullifiers and reuse detection

Where a profile supports scoped uniqueness, nullifier derivation binds to the approved context and epoch. Verifiers compare nullifiers only within the authorized scope and retain them only as long as policy and privacy claims permit. Epoch rollover, recovery and re-enrollment rules should prevent both unauthorized cross-context correlation and duplicate-use reset.

### 6.7 Registry and status resolution

The verifier resolves the authoritative record or a policy-valid cache entry, checks signature, version, effective time and state, and records the result. If sources disagree, the verifier follows an explicit precedence or fails with `ERR-REGISTRY-STALE` or `ERR-REGISTRY-UNAVAILABLE`; it does not choose the most convenient state.

### 6.8 Errors, retry and fallback

The [error catalogue](../appendices/ERROR-CATALOGUE.md) defines interoperable error classes. Retry is permitted only when it does not enable replay, correlation or policy bypass. A fallback path must declare its assurance difference, additional disclosure, human involvement and evidence. Silent downgrade is always rejected.

### 6.9 Logging and decision evidence

Logs and receipts should be sufficient to reconstruct the request, policy and governed state used for a decision while minimizing sensitive data. Retention, access, integrity protection, deletion and disclosure authority should be defined. A holder or principal should receive a correlation-safe reference usable for redress.

## 7. Lifecycle, cryptoperiod and migration

Implementations should model issuance, activation, renewal, expiry, suspension, revocation, replacement, recovery, re-enrollment, key rotation, wallet migration, policy change, proof-system upgrade, algorithm deprecation, registry migration and authority transition.

Each transition identifies the responsible authority, effective time, propagation expectation, verifier behavior, cache behavior, evidence and redress. Profiles separately declare proof validity, attestation lifetime, enrolment-root cryptoperiod, nullifier epoch and retention, privacy assurance horizon, biometric-method review horizon and log retention. Profiles separately declare proof validity, attestation lifetime, enrolment-root cryptoperiod, nullifier epoch and retention, privacy assurance horizon, biometric-method review horizon and log retention. Suspended or revoked state cannot be bypassed by stale cache, offline mode or an older accepted algorithm. Migration plans define overlap periods and protect against downgrade while allowing archived evidence to be interpreted under the policy active at the decision time.

## 8. Operational readiness

### 8.1 Threat, harm and control model

The [canonical threat matrix](../security/threat-matrix.md) is a central implementation artefact. It covers cryptographic, enrolment, privacy, governance, operational, lifecycle, composition, mediated-proving and human-experience threats. Every row maps the affected property, profile, component, boundary, adversary, capability, collusion assumptions, attack path, context, time horizon, accompanying information, technical effect, human or institutional harm, controls, owner, verification method, conformance requirement, residual risk and deployment disposition. Deployment-specific likelihood and impact are assessed locally, while canonical threats and minimum controls remain common.

### 8.2 Deployment and resilience

Local, remote and hybrid proof generation have different disclosure and availability properties. Remote services should document observed data and retention. Registry and status dependencies require time budgets, bounded retries, cache rules and deterministic unavailable-state behavior. Emergency operation should be a named policy, not an implicit bypass.

### 8.3 Performance

Profiles should publish reproducible measurements for proof generation, verification, memory, bandwidth, battery impact, registry resolution and batch behavior. Reports identify hardware, software revision, parameters, dataset, warm-up, repetitions and percentile results. Performance optimization must not alter semantic checks, weaken privacy or introduce an undocumented trusted service.

### 8.4 Accessibility

Alternative paths should support assistive technologies, constrained input, low bandwidth, shared or constrained devices and assisted operation. Each path declares whether assurance is equivalent, lower, different or dependent on additional human authority. Accessibility failure must not force unnecessary identity disclosure or permanent account exclusion without review.

### 8.5 Monitoring, incidents and redress

Monitoring distinguishes cryptographic, semantic, policy, lifecycle, delegation, registry and infrastructure failures. Incident response identifies the affected authority, suspends unsafe behavior, preserves evidence and publishes status where authorized. Redress procedures identify who may contest a result, what evidence is reviewable, who can correct state and how a corrected decision propagates.

## 9. Conformance and interoperability

A claim names a conformance level and profile rather than claiming generic conformance. The four levels are defined in [`conformance/levels.md`](../conformance/levels.md) and supported by 76 positive and negative cases. Negative tests remain first-class evidence because rejection behavior determines whether semantic and governance boundaries survive adversarial inputs.

An implementation should publish an [implementation conformance statement](../conformance/implementation-conformance-statement.md), a profile statement where applicable, fixture digests, environment metadata, test results, exceptions and a generated timestamp. The JSON schemas under `conformance/schemas/` define a minimum portable package.

A plugfest should include at least two independent wallets or proof generators, two issuers, two verifiers and independent registry fixtures for the profiles under test. It should exercise valid flows, malformed input, stale and conflicting state, revocation, policy mismatch, context mismatch, replay, downgrade, privacy-claim failure and delegation failure.

## 10. Readiness gates

A profile is ready for wider implementation review only when:

1. predicate meaning and negative meaning are explicit;
2. privacy claims name adversary, context and horizon;
3. assurance and governance dependencies are explicit;
4. lifecycle and migration behavior are deterministic;
5. independent implementations can reach equivalent outcomes;
6. operational and accessibility paths are documented;
7. authority, revocation, evidence and redress are testable;
8. material expectations map to scenarios and conformance evidence;
9. each material claim states against whom, for how long and alongside what it applies;
10. boundary records, threat controls and high-severity residual-risk decisions are complete;
11. cryptoperiods, assurance horizons, fallback and migration behaviour are bounded and testable.

Open technical or governance decisions remain visible in ADRs, maturity matrices or issue references. They are not resolved by rhetorical certainty.

## 11. Scenario catalogue and traceability

The detailed 30-scenario corpus is maintained in [`scenarios/pressure-test-use-case-corpus.md`](../scenarios/pressure-test-use-case-corpus.md). Matrices map scenarios to predicates, adversaries, ADRs, ownership and maturity. The [guidance and evidence index](../appendices/REQUIREMENT-INDEX.md) identifies high-value implementation expectations and their evidence paths.

Every new predicate, profile or material behavior should map to at least one pressure-test scenario and one positive or negative conformance test before being represented as implementation-ready.

## 12. Known decision dependencies

The following remain deliberate task-force decisions rather than implementation assumptions:

- ratification of the context and epoch model (a draft V1 definition exists, see §5.2, and is not yet ratified);
- the required privacy horizon and collusion resistance for each profile;
- the selected proof constructions and algorithm agility rules;
- normative delegation predicate identifiers and wire semantics;
- authoritative registry recognition and policy-equivalence rules;
- profile-specific performance targets;
- any accredited certification or compliance process.

These dependencies do not prevent implementation experiments, but experimental choices must be labelled, versioned and excluded from unqualified conformance claims.
