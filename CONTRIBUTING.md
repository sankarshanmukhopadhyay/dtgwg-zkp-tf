# Contributing

Contributions are welcome when they preserve the repository's authority boundary and evidence discipline.

## Before opening a change

1. Identify whether the proposed change belongs to this fork or to the authoritative upstream DTG ZKP work.
2. For substantive work, open or reference an issue that states the proposition, scope, acceptance criteria and important dependencies.
3. Use the title form `<type>(<scope>): <imperative summary>` where practical. Declare consumer-visible breaking changes with `!`.
4. Keep upstream text, fork interpretation, proposed requirements, implementation profiles and open decisions distinguishable.

## Engineering expectations

- Prefer the smallest coherent change that addresses the root problem.
- Do not invent Credential, Registry, Trust Task or governance semantics that belong to another owning layer.
- Treat missing evidence as indeterminate/evidence-required, never as PASS.
- Add regression, negative or boundary tests for consequential behaviour.
- Keep experimental constructions explicitly non-normative unless a governed promotion decision says otherwise.

## Validation

From the repository root:

```sh
python3 -m pip install pyyaml jsonschema pytest -e conformance-harness
python3 scripts/validate_all.py
pytest -q conformance-harness/tests
```

Documentation and Pages changes must also remain renderable through the repository's Pages workflow.

## Pull requests

A substantive PR should identify:

- the issue or proposition addressed;
- the implementation choice and meaningful alternatives where relevant;
- tests/evidence produced;
- compatibility or migration impact;
- authority/dependency boundaries;
- residual risk or deliberately deferred work.

The repository maintainers decide whether fork-local work is accepted here. Upstream normative adoption remains with the upstream DTG ZKP Task Force.