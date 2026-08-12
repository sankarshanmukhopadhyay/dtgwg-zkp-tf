---
layout: default
title: "Implementation Guide"
nav_order: 2
has_children: true
has_toc: true
---
# DTG ZKP Implementation and Interoperability Guide

{: .decision }
This guide is the implementation-facing companion to the DTG ZKP Task Force work. It explains how to design, integrate, deploy, operate and assess privacy-preserving proofs of DTG credential predicates without allowing a successful cryptographic verification to stand in for governance authority, issuer competence, delegated authority, policy validity or redress.

The guide is intentionally proof-system agnostic. It defines the semantic, governance, privacy, lifecycle, operational and conformance conditions that any selected cryptographic construction must satisfy.

## Guide status

| Attribute | Current position |
|---|---|
| Publication status | Non-normative implementation workspace |
| Decision authority | DTGWG ZKP Task Force and applicable upstream governance bodies |
| Fork status | Implemented working baseline for review, experimentation and contribution |
| Construction status | Specific proof constructions remain deferred pending the construction-selection gate and independently supportable benchmark evidence |
| Primary profiles | Minimum Liveness Profile and Extended Personhood Profile |
| Core architectural rule | Cryptography carries privacy; issuer accreditation and governance carry assurance |
| Conformance approach | Profile-specific claims supported by positive and negative evidence |

The root [`proof-of-liveness-requirements.md`](../../proof-of-liveness-requirements.md) is the fork's semantic source of truth for predicate/profile meaning. This guide operationalises those requirements and must not silently strengthen them. The [decision register](decisions/decision-register.md) separates ratified foundations, adopted working positions, unresolved upstream decisions and the maturity of their implementation in this fork.

## What this guide is for

Use this guide to answer the practical questions that arise between a high-level ZKP design and an independently assessable deployment:

- What exactly does a proof establish, and what does it not establish?
- Which party is accountable for the correctness of enrolment, liveness, personhood or credential issuance?
- How are contexts, epochs, nullifiers and permitted linkability governed?
- Against which parties and collusion patterns does a privacy claim hold?
- How are issuer, wallet, verifier, registry and agent responsibilities separated?
- How is delegated agent authority represented without confusing it with holder-key control?
- Which lifecycle events invalidate, suspend, migrate or downgrade a proof path?
- What evidence must an implementation, operator or assessor retain?
- How are compromise, revocation, degraded operation, correction and redress handled?
- Which conformance profile and evidence package may be claimed?

The guide is not a proof-system tutorial, a biometric evaluation standard, a certification programme or a substitute for legal and governance analysis.

## Audience

### Governance authorities and programme sponsors

Use the guide to establish scope, authority, adoption stage, residual-risk ownership, approved profiles and production-entry conditions. Start with the [guided learning path](guided-learning.md), [adoption model](adoption/README.md), [boundary workspace](boundaries/README.md) and [risk acceptance policy](security/risk-appetite-and-acceptance-policy.md).

### Architects and system designers

Use the architecture, information model, privacy model and decision records to define system boundaries and interfaces before selecting a cryptographic construction. Start with [architecture](architecture/README.md), [predicate and assurance boundaries](boundaries/predicate-assurance-boundary-decision.md), [privacy classes](privacy/privacy-class-model.md) and the [core implementation guide](guide/implementation-interoperability-guide.md).

### Component implementers

Use the role-specific guides for issuers, wallets, verifiers, registries, delegated agents and assessors. Each guide identifies responsibilities, prohibited inferences, required evidence, lifecycle behaviour and conformance expectations. See [component implementation guides](implementation/README.md).

### Operators and security teams

Use the deployment profiles, operational runbooks, threat model, guardrails and metrics to preserve assurance after launch. Start with [secure deployment](deployment/README.md), [operations](operations/README.md), [security](security/README.md) and [operational readiness](operations/operational-readiness-checklist.md).

### Auditors, assessors and interoperability reviewers

Use the conformance levels, test matrices, schemas, fixtures, traceability maps and evidence statements to determine whether a claim is reproducible and properly bounded. Start with [conformance](conformance/README.md), [implementation conformance statement](conformance/implementation-conformance-statement.md), [test matrix](conformance/test-matrix.md) and [requirement index](appendices/REQUIREMENT-INDEX.md).

## DTG interoperability

The [DTG interoperability section](interoperability/README.md) records cross-repository dependencies on Credential semantics, Trust Tasks/Trust Ceremonies and RAHP pressure-testing as governed inputs rather than implicit assumptions. A machine-readable alignment register and validator preserve authority, evidence and unresolved dependency boundaries.

For ecosystem-level situational awareness, the independently maintained [DTG Portfolio Monitor](https://sankarshanmukhopadhyay.github.io/dtg-portfolio-monitor/) can be used to discover relevant repository movement. It is contextual monitoring, not a substitute for the authoritative source named in each dependency record.

## Foundational model

### A proof establishes a statement over an attestation

A zero-knowledge proof can establish that a prover possesses an attestation satisfying a defined predicate under stated cryptographic assumptions. It does not establish that the issuer's upstream biometric, liveness, enrolment or personhood determination was factually correct.

Consequently:

- the issuer remains accountable for the quality and governance of the upstream determination;
- the verifier remains accountable for relying-party policy and decision logic;
- the registry or trust-list operator remains accountable for the authoritative state it publishes;
- the wallet remains accountable for holder control, consent and local protection;
- a delegated agent must present separate authority evidence;
- the cryptographic mechanism remains accountable for proof soundness, privacy and binding properties within its declared model.

### Personhood, identity, liveness and uniqueness are distinct

The guide treats these as different claims:

- **Liveness** concerns whether the observed source behaved as a live subject under a defined method.
- **Personhood** is a policy-defined standing or membership claim and is not automatically civil identity.
- **Identity** concerns the binding of attributes or identifiers to a person or entity under a governance framework.
- **Scoped uniqueness** detects reuse inside a defined context and epoch. It does not prove that only one credential exists globally or that one natural person exists behind every successful presentation.

Implementations must not collapse these terms in user interfaces, verifier outputs, logs, marketing or conformance claims.

### Holder control is not delegated authority

Control of the key or secret used to create a proof establishes holder control only. It does not establish that the holder is authorised to act for another principal. Agent authority is represented as separate structured evidence containing the principal, agent, scope, constraints, validity period, revocation reference and applicable governance.

### Privacy claims are conditional and falsifiable

Every material privacy claim must state:

- **against whom** the claim holds;
- **for how long** it holds;
- **alongside what** credentials, metadata, retained state, registry interactions, network observations and operational records it is evaluated.

This prevents terms such as "unlinkable" or "privacy-preserving" from being used as unconditional properties.

## Profile model

### Minimum Liveness Profile

The Minimum Liveness Profile supports proof that a holder possesses a valid liveness-related attestation satisfying a defined policy. It is designed to be implementable and benchmarkable without requiring population-scale deduplication.

A conformant implementation should define:

- the liveness predicate and method class;
- issuer competence and accreditation requirements;
- holder-binding method;
- freshness, nonce and replay controls;
- proof, attestation and status lifetimes;
- disclosure and observability boundaries;
- fallback and accessibility paths;
- verifier policy and reason codes;
- compromise, correction and redress procedures.

The profile must not imply global uniqueness, civil identity or general personhood unless those are separately established.

### Extended Personhood Profile

The Extended Personhood Profile adds governed personhood or scoped-uniqueness semantics. It therefore introduces additional privacy and governance requirements, including context delimitation, epoch management, nullifier or equivalent reuse-detection behaviour, continuity across re-enrolment, correlation-surface analysis and a declared collusion model.

A conformant implementation should define:

- the policy meaning of personhood;
- the authority responsible for context and epoch governance;
- the scope within which reuse is detectable;
- what linkage is permitted and prohibited;
- privacy class and adversary model;
- issuer, verifier and registry observables;
- continuity and recovery rules;
- handling of false duplicate detections;
- appeal, correction and redress;
- evidence supporting the claimed privacy horizon.

### Profile selection

Do not select the Extended Personhood Profile simply because it appears stronger. Select the least invasive profile that meets the relying-party need. Use the [profile selection guide](adoption/profile-selection-guide.md) and document why a less linkable or less intrusive design was insufficient.

## Governed context and linkability

A context is a governed linkability domain, not merely a verifier hostname, vendor tenant or broad ecosystem label. The context descriptor should identify:

- the context authority;
- the governed purpose;
- the predicate and action scope;
- the verifier or governed verifier set;
- the epoch and rollover rules;
- permitted linkage within the context;
- prohibited linkage across contexts;
- change, migration and versioning rules;
- user-facing explanation;
- notice and appeal mechanisms;
- review and expiry dates.

A context must not silently expand because of common ownership, merger, federation, shared infrastructure or analytics. Changes that increase linkability should create a new version and trigger review, notice and migration controls.

The current proposed model is documented in the [context decision record](boundaries/context-decision-record.md), [B1 impact assessment](decisions/B1-context-delimiter-impact.md) and context conformance fixtures.

## Privacy classes and collusion model

The guide uses named privacy classes so deployments cannot inherit a stronger claim merely by using the same profile label.

| Class | Minimum claim |
|---|---|
| PC-1 | Cross-context separation against non-colluding verifiers under stated assumptions |
| PC-2 | Cross-context separation against colluding verifiers under stated assumptions |
| PC-3 | Cross-context separation against issuer-verifier collusion under a named adversary model and evidence package |
| PC-R | Reduced-privacy deployment with explicit correlation exposures and prohibited stronger claims |

The class is not determined by cryptography alone. It also depends on issuer-held enrolment data, schema fields, nullifier construction, status and registry interactions, timing, network metadata, retry behaviour, device signals, recovery, retention and external identifiers.

See the [privacy class model](privacy/privacy-class-model.md), [observable-event analysis](privacy/observable-event-analysis.md), [composition assessment](privacy/composition-and-reconstruction-assessment.md) and [B2 impact assessment](decisions/B2-collusion-target-impact.md).

## Paired assurance and disclosure boundaries

Every material predicate is accompanied by two linked records.

### Assurance boundary

The assurance boundary records:

- what the verifier may rely on;
- what the proof does not establish;
- upstream evidence and issuer dependencies;
- accreditation and governance dependencies;
- lifecycle and status assumptions;
- accountable parties;
- residual risk and acceptance authority;
- conformance evidence.

### Disclosure boundary

The disclosure boundary records:

- what each actor observes directly;
- what can be inferred or reconstructed;
- what metadata is exposed;
- which parties may collude;
- retention and observability horizons;
- leakage introduced by status, registries or mediated proving;
- prohibited secondary use;
- required technical and governance controls.

The issuer attestation schema is a shared determinant of both boundaries because every field can increase assurance, disclosure or both. Use the [assurance boundary template](boundaries/assurance-boundary-template.md), [disclosure boundary template](boundaries/disclosure-boundary-template.md), [predicate register](boundaries/predicate-boundary-register.md) and [attestation schema profile](information-model/attestation-schema-profile.md).

## Actors and responsibilities

| Actor | Primary responsibility | Must not be inferred from its role |
|---|---|---|
| Governance authority | Defines policy, competence, recognition, context and accountability | That technical conformance alone creates legitimacy |
| Issuer | Performs or relies on upstream determination and issues attestations | That proof verification confirms issuer correctness |
| Holder or principal | Controls presentation and exercises rights | That key control proves civil identity or authority over others |
| Wallet | Protects secrets, mediates consent and creates presentations | That wallet possession creates delegated authority |
| Delegated agent | Acts under explicit authority evidence | That a valid proof authorises the requested action |
| Verifier | Evaluates proof, status, policy and authority | That cryptographic validity equals transaction approval |
| Registry operator | Publishes authoritative or governed state | That discovery equals accreditation or reliance |
| Auditor or assessor | Evaluates evidence and conformance | That a passed test removes residual risk |
| Redress authority | Reviews disputes, corrections and harm | That an automated denial is final or unreviewable |

Detailed role guidance is available under [implementation](implementation/README.md), while cross-role allocation is maintained in the [ownership model](architecture/06-ownership-model.md).

## End-to-end implementation flow

### 1. Establish authority and scope

Identify the governance authority, relying-party purpose, accepted profiles, issuer competence rules, registry dependencies, decision authority and redress body. Record prohibited uses and non-claims before choosing a proof system.

### 2. Define predicates and schemas

For each predicate, document what it establishes, what it excludes, required issuer fields, disclosure implications, lifecycle behaviour and evidence dependencies. Remove unnecessary stable identifiers and fields that create cross-context correlation.

### 3. Define context, epoch and privacy class

Specify the context authority, linkability domain, epoch rules, continuity behaviour, adversary model and privacy class. Establish how mergers, verifier-set changes and policy changes affect the context identifier.

### 4. Select architecture and trust boundaries

Define local, remote or hybrid proving; registry and status dependencies; mediated services; wallet and device assumptions; trusted execution or hardware dependencies; and the location of policy enforcement.

### 5. Implement issuer and enrolment controls

Document enrolment method, liveness method, deduplication if applicable, evidence retention, issuer keys, schema versioning, attestation lifetime, correction, suspension, revocation and reissuance.

### 6. Implement wallet and holder controls

Protect holder secrets, bind the proof to a fresh request, explain the requested predicate and context, minimise disclosure, support recovery and accessible alternatives, and prevent silent use by agents or background services.

### 7. Implement verifier policy

Verify proof syntax and semantics, request binding, nonce, context, epoch, profile, issuer recognition, status, policy version and delegation. Generate a decision receipt containing only the evidence necessary for audit and redress.

### 8. Integrate registries and status

Distinguish discovery, accreditation, recognition, reliance and transaction authorisation. Define cache age, conflict resolution, unavailable-state behaviour, versioning and evidence retention. Stale or unavailable state must not silently become successful verification.

### 9. Test normal and adverse scenarios

Run positive and negative cases for replay, context mismatch, stale state, revocation, schema mismatch, privacy downgrade, issuer-verifier collusion, delegated-authority failure, recovery, accessibility and degraded operation.

### 10. Prepare production evidence

Publish an implementation conformance statement, profile statement, threat assessment, residual-risk decisions, deployment profile, runbooks, fixture digests, test results, environment metadata and accountable approvals.

### 11. Operate, monitor and correct

Monitor semantic, cryptographic, policy, lifecycle, registry and infrastructure failures separately. Maintain compromise, rotation, revocation, migration, correction and redress playbooks. Reassess privacy and assurance claims after material system changes.

## Information and protocol objects

A deployment normally needs the following governed objects:

- proof request;
- presentation or proof response;
- predicate definition;
- attestation schema profile;
- context descriptor;
- privacy claim;
- issuer or trust-registry record;
- status or revocation record;
- delegation evidence;
- relying-party policy;
- verifier decision receipt;
- assurance boundary record;
- disclosure boundary record;
- threat and residual-risk record;
- implementation and profile conformance statements.

Each object should be versioned, attributable, time-bounded and traceable to the authority that may create or amend it.

## Lifecycle and migration

A deployment must distinguish at least the following time horizons:

- proof freshness window;
- attestation validity;
- issuer key cryptoperiod;
- enrolment-root cryptoperiod;
- context epoch;
- nullifier or reuse-detection retention;
- registry and status cache age;
- privacy assurance horizon;
- biometric-method review horizon;
- evidence and audit retention;
- delegation validity;
- correction and appeal window.

Lifecycle events include issuance, activation, suspension, revocation, expiry, key rotation, context rollover, schema change, issuer compromise, verifier compromise, wallet recovery, re-enrolment, governance change and proof-system migration.

Every transition should identify the authority, effective time, propagation expectation, cache behaviour, downgrade risk, evidence produced and redress impact. See [lifecycle guidance](lifecycle/README.md), [cryptoperiod and assurance horizon](lifecycle/cryptoperiod-and-assurance-horizon.md) and [proof-system migration](lifecycle/proof-system-migration-profile.md).

## Security, harm and residual risk

The security model covers more than proof forgery. It includes:

- enrolment fraud and issuer error;
- correlation and reconstruction;
- context expansion;
- nullifier misuse;
- stale status and registry equivocation;
- compromised issuer, verifier, wallet or mediator;
- delegated-authority overreach;
- coercion and exclusion;
- inaccessible or discriminatory fallback;
- unreviewable automated denial;
- governance capture;
- migration and downgrade attacks;
- evidence loss and redress failure.

Each threat is mapped to affected properties, actors, boundaries, controls, verification methods, residual risk and acceptance authority. Use the [threat model](security/threat-matrix.md), [harm taxonomy](security/harm-taxonomy.md), [control catalogue](security/control-catalog.md), [security guardrails](security/security-guardrails.md) and [residual-risk register](security/residual-risk-register.md).

## Human experience, accessibility and redress

A technically valid deployment can still fail if affected people cannot understand, challenge or recover from its decisions. Implementations should provide:

- a human-readable explanation of the requested proof and context;
- notice of which services share a linkability domain;
- accessible and low-bandwidth interaction paths;
- assisted proving with explicit authority and non-retention controls;
- alternatives for device loss, disability and constrained environments;
- reason codes that are useful without exposing sensitive details;
- a process for false duplicate detection and incorrect enrolment;
- correction and propagation of corrected state;
- escalation to a human or accountable authority;
- evidence preservation for review and appeal.

See the [human-experience scenarios](scenarios/README.md), [mediated proving profile](privacy/mediated-proving-profile.md) and [redress and correction runbook](operations/redress-and-correction-runbook.md).

## Deployment models

The guide supports local, remote and hybrid proof generation. Each model changes the trust and disclosure boundary.

| Model | Primary advantage | Principal risk |
|---|---|---|
| Local proving | Stronger local control and reduced service disclosure | Device capability, key protection and recovery |
| Remote proving | Lower device requirements and centralised updates | Service observation, retention, compromise and availability |
| Hybrid proving | Flexible division of computation and controls | Boundary ambiguity and composite failure modes |
| Mediated proving | Accessibility and constrained-device support | Mediator authority, data exposure and retention |

A deployment profile should document topology, trusted services, data flows, failure modes, required controls and evidence. See [deployment](deployment/README.md).

## Operations and resilience

Production assurance depends on operational discipline. The repository provides runbooks for:

- issuer compromise;
- verifier compromise;
- wallet compromise and recovery;
- key rotation;
- revocation propagation;
- registry and status failure;
- degraded mode;
- policy updates;
- proof-system migration;
- redress and correction;
- incident evidence preservation.

Each runbook identifies trigger, authority, containment, evidence, communications, recovery, validation and closure. See [operations](operations/README.md).

## Conformance and evidence

A deployment should never claim generic "DTG ZKP conformance". It should name:

- implementation component;
- profile;
- privacy class;
- conformance level;
- supported predicates;
- decision-register version;
- schema and fixture versions;
- test environment;
- exceptions and residual risks;
- evidence timestamp and custodian.

The conformance programme includes:

- four conformance levels;
- positive and negative test cases;
- executable fixture validation;
- B1/B2 decision-conformance cases;
- implementation and profile statements;
- security assurance dispositions;
- traceability from decisions and ADRs to scenarios and tests.

Begin with [conformance levels](conformance/levels.md), [test matrix](conformance/test-matrix.md), [decision conformance tests](conformance/decision-conformance-tests.md), [executable harness](conformance/executable-harness.md) and [conformance evidence guide](guide/conformance-evidence-guide.md).

## Readiness gates

A profile or deployment should not be represented as implementation-ready until:

1. predicate meaning and prohibited interpretations are explicit;
2. issuer competence and governance dependencies are documented;
3. assurance and disclosure boundary records are complete;
4. privacy claims name adversary, context, horizon and accompanying information;
5. lifecycle, status, recovery and migration behaviour are deterministic;
6. delegation is represented separately from holder control;
7. registry and degraded-mode behaviour are defined;
8. threats, controls and high-severity residual risks have accountable owners;
9. accessibility, correction and redress paths are testable;
10. positive and negative conformance evidence is reproducible;
11. production-entry authority has recorded a decision;
12. unresolved Task Force decisions remain clearly labelled.

Use the [production-entry criteria](adoption/production-entry-criteria.md), [integration readiness checklist](adoption/integration-readiness-checklist.md) and [operational readiness checklist](operations/operational-readiness-checklist.md).

## Adoption pathway

| Stage | Objective | Minimum output |
|---|---|---|
| Exploration | Validate problem, predicate and governance need | Problem statement, non-claims, initial threat and privacy analysis |
| Controlled prototype | Exercise semantics and component interfaces | Versioned fixtures, prototype architecture and negative tests |
| Pilot | Test governed operation with bounded participants | Pilot policy, deployment profile, runbooks and evidence plan |
| Pre-production | Demonstrate repeatable assurance | Conformance package, residual-risk decisions and entry approval |
| Production | Operate under monitored and reviewable controls | Metrics, incident response, lifecycle evidence and redress |
| Expansion | Add contexts, issuers or use cases without silent scope growth | Change-impact assessment, context versioning and regression evidence |

See [adoption](adoption/README.md) and [implementation sequencing](adoption/implementation-sequencing.md).

## Decision governance

The guide tracks the foundational and open Task Force decisions separately from implementation maturity. A decision record includes:

- decision identifier;
- proposed position;
- upstream status;
- fork implementation status;
- affected ADRs, schemas, fixtures, scenarios and tests;
- amendment and supersession history;
- decision authority and source discussion.

The two most load-bearing working positions remain context delimitation and the issuer-verifier collusion target. Discussion #13 moves them from open questions to adopted working positions for v0.4; construction selection remains downstream of their evidence-backed application and the construction-selection gate. See [decisions](decisions/README.md), [decision register](decisions/decision-register.md) and [upstream crosswalk](decisions/upstream-decision-crosswalk.md).

## Guided routes

### Route A: understand the model

1. [Guided learning paths](guided-learning.md)
2. [Core implementation and interoperability guide](guide/implementation-interoperability-guide.md)
3. [Architecture](architecture/README.md)
4. [Predicate and boundary decision](boundaries/predicate-assurance-boundary-decision.md)
5. [Privacy](privacy/README.md)

### Route B: design an implementation

1. [Profile selection](adoption/profile-selection-guide.md)
2. [Information model](information-model/README.md)
3. [Component guides](implementation/README.md)
4. [Deployment profiles](deployment/README.md)
5. [Threat model](security/README.md)
6. [Scenario corpus](scenarios/README.md)

### Route C: prepare for production

1. [Production-entry criteria](adoption/production-entry-criteria.md)
2. [Operational readiness](operations/operational-readiness-checklist.md)
3. [Security guardrails](security/security-guardrails.md)
4. [Conformance programme](conformance/README.md)
5. [Evidence guide](guide/conformance-evidence-guide.md)

### Route D: review or assess a deployment

1. [Implementation conformance statement](conformance/implementation-conformance-statement.md)
2. [Profile conformance statement](conformance/profile-conformance-statement.md)
3. [Threat matrix](security/threat-matrix.md)
4. [Residual-risk register](security/residual-risk-register.md)
5. [Decision-conformance matrix](conformance/decision-conformance-matrix.csv)
6. [Requirement index](appendices/REQUIREMENT-INDEX.md)

## Repository map

| Directory | Purpose |
|---|---|
| `adoption/` | Staged adoption, pilot design, profile selection and production-entry gates |
| `adr/` | Architectural decisions and their consequences |
| `appendices/` | Glossary, references, error catalogue and requirement index |
| `architecture/` | Context, layers, viewpoints, trust boundaries, qualities and ownership |
| `boundaries/` | Predicate semantics, assurance boundaries, disclosure boundaries and context records |
| `conformance/` | Levels, tests, matrices, schemas, fixtures and evidence statements |
| `decisions/` | Decision state, ratification procedure, impact analysis and upstream traceability |
| `deployment/` | Secure topologies, production controls and deployment evidence |
| `diagrams/` | Registered Mermaid diagrams with textual interpretations |
| `editorial/` | Contribution, terminology and documentation-quality rules |
| `guide/` | Consolidated implementation guidance and checklists |
| `implementation/` | Issuer, wallet, verifier, registry, agent and assessor guidance |
| `information-model/` | Attestation schemas, field register and correlation analysis |
| `lifecycle/` | Cryptoperiods, assurance horizons and proof-system migration |
| `matrices/` | Machine-readable ownership, scenario, control and traceability maps |
| `operations/` | Runbooks for change, compromise, recovery, revocation and redress |
| `privacy/` | Privacy classes, observable events, composition and mediated proving |
| `scenarios/` | Functional, governance, deployment and operational pressure tests |
| `security/` | Threat, harm, control, guardrail, metric and residual-risk model |
| `taxonomy/` | Predicate and adversary catalogues |

## Validation and reproducibility

Run the complete repository quality gate from the repository root:

```sh
python3 scripts/validate_decision_governance.py
python3 scripts/validate_docs.py
python3 scripts/validate_conformance.py
python3 scripts/validate_style.py
python3 scripts/validate_links.py
python3 scripts/validate_fixtures.py
python3 scripts/validate_threat_model.py
python3 scripts/validate_deployment_profiles.py
python3 scripts/validate_operations.py
python3 scripts/validate_navigation.py
python3 scripts/validate_diagrams.py
python3 scripts/validate_generated_counts.py
python3 scripts/build_traceability.py
```

A successful documentation build is not itself evidence of technical or governance conformance. It establishes only that the repository artefacts satisfy the repository's structural and consistency checks.

## Known boundaries of this guide

The guide does not yet settle:

- final Task Force ratification of the context delimiter;
- final Task Force ratification of the issuer-verifier collusion target;
- selection of specific proof constructions;
- normative wire formats for every object;
- accredited certification or compliance processes;
- jurisdiction-specific legal sufficiency;
- universal performance targets;
- universal biometric or personhood assurance criteria.

These open areas are deliberate. Implementations may experiment, but must label experimental assumptions, avoid unqualified claims and retain enough evidence for later migration.

## Suggested first reading

Begin with the [guided learning paths](guided-learning.md), then read the [core implementation and interoperability guide](guide/implementation-interoperability-guide.md). Select the relevant adoption, implementation, deployment, operations and conformance route from there.

[Start the guided learning path →](guided-learning.md)
