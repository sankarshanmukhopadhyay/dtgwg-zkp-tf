# Trust boundaries

| Boundary | Principal risk | Required treatment |
|---|---|---|
| Human ↔ wallet | coercion, misleading UI, key compromise | request visibility, consent, recovery |
| Wallet ↔ biometric provider | raw-data exposure, replay | session binding, minimisation |
| Provider ↔ issuer | false determination | policy, assurance, accountability |
| Issuer ↔ holder | subject-binding failure | issuance semantics, status |
| Holder/agent ↔ verifier | replay, overbroad request, correlation | canonical transcript, context |
| Verifier ↔ registry | stale or conflicting status | time semantics, caching, errors |
| Registry ↔ governance | published state diverges from policy | authority, audit, recognition |
| Principal ↔ agent | authority exceeds intent | explicit delegation and step-up |
