# DTG ZKP Implementation & Interoperability Guide

## Pressure-Test Corpus and Validation Companion

## Table of Contents

1.  Identity & Personhood
2.  Privacy & Unlinkability
3.  AI Agents & Delegation
4.  Trust Registries & Governance
5.  Lifecycle & Revocation
6.  Federation & Cross-Border Recognition
7.  Consumer Devices & Accessibility
8.  Adversarial & Threat Scenarios
9.  Performance & Operational Readiness
10. Conformance & Plugfest Programme

------------------------------------------------------------------------

# 1. Identity & Personhood

## Summary

  --------------------------------------------------------------------------
  ID                Scenario             Core Predicates   Pressure
  ----------------- -------------------- ----------------- -----------------
  UC-001            Privacy-Preserving   Liveness,         Sybil resistance
                    Account Creation     Personhood,       
                                         Scoped Uniqueness 

  UC-005            Account Recovery     Liveness,         Recovery
                                         Continuity        semantics

  UC-006            Same Human Login     Liveness, Holder  Continuity
                                         Binding           

  UC-007            Benefit Claims       Personhood,       Duplicate
                                         Uniqueness        prevention
  --------------------------------------------------------------------------

### Design questions

-   What exactly constitutes personhood?
-   Where is uniqueness established?
-   How are recovery and re-enrolment prevented from weakening
    guarantees?

### Detailed use-case template

  Field                     Description
  ------------------------- -------------------------------------
  Objective                 Why the scenario exists
  Actors                    Participants
  Required Predicates       Proof requirements
  Threat Model              Primary adversaries
  Governance Dependencies   Accreditation, policy, registry
  Failure Modes             Operational failures
  Conformance Tests         Observable implementation behaviour

(Instantiate UC-001, UC-005, UC-006 and UC-007 using the template.)

------------------------------------------------------------------------

# 2. Privacy & Unlinkability

## Summary

  -----------------------------------------------------------------------
  ID                      Scenario                Primary Pressure
  ----------------------- ----------------------- -----------------------
  UC-002                  Anonymous Community     Cross-context
                          Participation           unlinkability

  UC-003                  Age Verification        Selective disclosure

  UC-008                  Anonymous Ballot        Privacy + uniqueness

  UC-023                  Malicious Verifier      Correlation

  UC-024                  Issuer-Verifier         Long-term
                          Collusion               deanonymisation
  -----------------------------------------------------------------------

### Pressure-test questions

-   Which adversary is the privacy claim made against?
-   How long must unlinkability hold?
-   Can metadata defeat otherwise correct cryptography?

------------------------------------------------------------------------

# 3. AI Agents & Delegation

## Summary

  ID       Scenario                 Pressure
  -------- ------------------------ ----------------------
  UC-009   Human Authorises Agent   Delegation semantics
  UC-010   Agent Step-up            Human oversight
  UC-011   Agent Presentation       Proof composition

Questions: - What belongs in the ZKP? - What belongs in delegation
evidence? - What belongs in Trust Tasks?

------------------------------------------------------------------------

# 4. Trust Registries & Governance

Summary table: UC-012 through UC-016.

Focus: - accreditation - recognition - policy versioning - registry
availability - governance semantics

------------------------------------------------------------------------

# 5. Lifecycle & Revocation

Representative scenarios: - issuer suspension - policy migration -
recovery - expiry - revocation

Expected outputs: - deterministic verifier behaviour - explicit status
semantics - auditability

------------------------------------------------------------------------

# 6. Federation & Cross-Border Recognition

Representative scenarios: - multiple registries - cross-border assurance
mapping - policy equivalence - recognition agreements

------------------------------------------------------------------------

# 7. Consumer Devices & Accessibility

Representative scenarios: - constrained devices - offline presentation -
shared devices - accessibility alternatives

Validation dimensions: - usability - fallback - performance - privacy

------------------------------------------------------------------------

# 8. Adversarial & Threat Scenarios

Representative scenarios: - compromised wallet - malicious provider -
malicious verifier - collusion - replay - downgrade

Threat matrix to be maintained by the TF.

------------------------------------------------------------------------

# 9. Performance & Operational Readiness

Representative scenarios: - batch verification - large-scale
deployments - offline operations - emergency operations

Benchmark dimensions: - proof generation - verification - memory -
bandwidth - mobile performance

------------------------------------------------------------------------

# 10. Conformance & Plugfest Programme

## Plugfest Matrix

  Category       Minimum Requirement
  -------------- -------------------------------
  Wallets        2 independent implementations
  Issuers        2 implementations
  Verifiers      2 implementations
  Registries     Independent fixtures
  Test vectors   Positive & negative
  Privacy        Correlation testing
  Lifecycle      Revocation & migration
  Performance    Reference benchmarks

## Readiness Gates

-   Predicate clarity
-   Privacy clarity
-   Assurance clarity
-   Lifecycle completeness
-   Governance completeness
-   Accessibility
-   Interoperability
-   Operational viability

## Living Coverage Matrices

Maintain matrices for: - capabilities - predicates - threats -
governance - implementation complexity - roadmap - release readiness

## Recommendation

Maintain this guide as a living implementation companion to the
normative specification. Every new feature, predicate or profile should
map to at least one pressure-test scenario and one conformance test
before it is considered complete.
