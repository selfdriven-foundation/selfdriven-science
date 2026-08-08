# Evidence Schemas and E011+ Extension Rules

## Contents

1. Evidence graph
2. Minimal records
3. Decision logic
4. Extending the programme
5. Proposal checklist

## 1. Evidence graph

Represent the scientific record as a directed, versioned provenance graph:

`Hypothesis -> Experiment -> Specification -> Implementation -> Run -> Dataset -> Analysis -> Claim -> Replication`

Use typed nodes at minimum:

- `HYPOTHESIS`, `EXPERIMENT`, `SPECIFICATION`, `IMPLEMENTATION`, `ENVIRONMENT`, `RUN`, `DATASET`, `ANALYSIS`, `CLAIM`, `REPLICATION`, `DECISION`, `REVIEW`, `CHALLENGE`, `DEVIATION`, `INSTITUTION`, `PERSON`, `ARTIFACT`.

Use typed edges at minimum:

- `TESTS`, `DEPENDS_ON`, `SPECIFIES`, `IMPLEMENTS`, `CONFORMS_TO`, `EXECUTES`, `GENERATES`, `DERIVES_FROM`, `ANALYSES`, `SUPPORTS`, `CONTRADICTS`, `FAILS_TO_DISTINGUISH`, `REPLICATES`, `FAILS_TO_REPLICATE`, `CHALLENGES`, `REFINES`, `SUPERSEDES`, `QUALIFIES`, `DECIDES`, `AUTHORED_BY`, `PERFORMED_BY`, `FUNDED_BY`.

Edges are assertions with author, timestamp, scope, rationale, and evidence. Never delete a superseded node or adverse edge. Add a new node/edge and link with `SUPERSEDES` or a correction relation.

## 2. Minimal records

### Experiment specification

```yaml
schema: cbr-oen/experiment-spec/v1
experiment:
  id: CBR-E0XX
  version: 1.0.0
  status: PREREGISTERED
  phase: PHASE_N
  title: "..."
  question: "..."
  hypothesis_id: CBR-H0XX
  null_hypothesis: "..."
  claim_ceiling: CL3
dependencies:
  - id: CBR-E0YY
    version: 1.2.0
    kind: required
    accepted_decision: GO
model:
  primitives: []
  allowed_operations: []
  prohibited_assumptions: []
design:
  ensembles: []
  controls: []
  sample_size: {}
  randomness: {}
  resource_guards: {}
measurements:
  primary: []
  secondary: []
analysis:
  estimand: "..."
  model: "..."
  multiplicity: "..."
  exclusions: []
decisions:
  GO: []
  GO_WITH_QUALIFICATION: []
  REVISE: []
  STOP: []
reproducibility:
  target: R2
  independence_requirements: []
artifacts: []
roles: []
registration:
  timestamp: "..."
  content_hash: "..."
```

### Run record

```yaml
schema: cbr-oen/run/v1
run_id: CBR-RUN-...
specification: {id: CBR-E0XX, version: 1.0.0, hash: "..."}
implementation: {id: CBR-IMP-..., commit: "...", hash: "..."}
environment: {id: CBR-ENV-..., hash: "..."}
seed: "..."
configuration_hash: "..."
start_time: "..."
end_time: "..."
status: COMPLETED # COMPLETED | FAILED | CENSORED | INVALIDATED
failure_or_exclusion_reason: null
inputs: []
outputs: []
logs: []
```

### Claim record

```yaml
schema: cbr-oen/claim/v1
claim_id: CBR-CLM-...
statement: "..."
scope: "..."
claim_level: CL3
reproducibility_level: R1
supported_by: []
contradicted_by: []
qualifications: []
alternatives_not_excluded: []
status: ACTIVE # ACTIVE | QUALIFIED | CONTRADICTED | SUPERSEDED
```

### Decision record

```yaml
schema: cbr-oen/decision/v1
decision_id: CBR-DEC-...
experiment: {id: CBR-E0XX, version: 1.0.0}
decision: REVISE # GO | GO_WITH_QUALIFICATION | REVISE | STOP
criteria_results: []
reproducibility_level: R2
claim_ceiling: CL4
qualifications: []
deviations: []
unresolved_confounds: []
downstream_effects: []
panel: []
recusals: []
dissent: []
timestamp: "..."
```

Validate records against a published schema when one exists. Until then, preserve these fields and explicitly version local extensions.

## 3. Decision logic

Apply this order:

1. If the implementation or data fail validity/conformance, choose REVISE; choose STOP only if no non-circular valid test is feasible.
2. If a preregistered fatal falsifier occurs under adequate power and controls, choose STOP for the scoped hypothesis/version.
3. If primary success criteria and all mandatory controls/reproducibility pass, choose GO.
4. If the core criterion passes but a declared non-fatal boundary limits downstream interpretation, choose GO_WITH_QUALIFICATION.
5. Otherwise choose REVISE only when a scientifically motivated, prospectively testable correction exists; if repeated adequate revisions converge on null, choose STOP.

Do not aggregate criteria into an opaque score. Publish criterion-level outcomes.

## 4. Extending the programme

Freeze E001-E010 as v1.0 identifiers. Revise an existing experiment when the same hypothesis is tested with corrected methods. Create E011+ when the scientific question is distinct.

An E011+ proposal must do at least one of the following:

- discriminate two surviving mechanisms;
- test generalisation beyond an established regime;
- close a named qualification or confound;
- derive and test a novel preregistered prediction;
- connect to a new physical observable with an explicit operational map;
- attempt stronger mathematical, implementation, or institutional validation;
- test failure boundaries or universality classes.

Reject proposals that merely search for a favourable rule, add target information, rename a failed hypothesis, duplicate an experiment without replication intent, or leap to physical claims over missing dependencies.

Assign the next available number only after governance approval. Never use suffixes to disguise a new hypothesis; use subexperiments such as `E011-A` only for preregistered tracks under one shared primary question.

Every extension must declare:

- parent claims and exact evidence-graph paths;
- novelty relative to E001-E010 and other extensions;
- dependency types and minimum gate/reproducibility states;
- assumption budget: new primitives, parameters, mappings, and target knowledge;
- competing hypotheses and discriminating outcomes;
- claim ceiling and what remains outside scope;
- prospective controls, holdouts, replication target, and stop rule;
- whether failure closes only the extension or also weakens upstream claims.

Prefer extensions that reduce free choices, predict unseen results, unify multiple observables, or expose the programme to stronger falsification.

## 5. Proposal checklist

Before approving E011+ answer yes to all:

1. Is the question falsifiable and non-duplicative?
2. Are upstream decisions and qualifications explicit?
3. Is the desired result absent from primitives, objectives, and selection?
4. Can at least one plausible outcome contradict the hypothesis?
5. Do controls distinguish the leading alternatives?
6. Are discovery and confirmation separated?
7. Are parameters and mappings identifiable and bounded?
8. Is the reproducibility target proportional to the claim?
9. Are downstream effects of GO, qualification, revision, and stop explicit?
10. Can another institution implement the specification without private interpretation?
