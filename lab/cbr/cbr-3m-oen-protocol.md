# CBR-OEN Experimental Protocol
## Experiment Specification, Registration, Execution and Replication Standard
### Version 1.0 — Draft Founding Protocol

---

## 1. Purpose

This protocol defines how experiments are proposed, preregistered, implemented, executed, replicated and evaluated within the **CBR Open Experimental Network (CBR-OEN)**.

Its purpose is to make experiments:

- implementation-independent;
- reproducible;
- auditable;
- institutionally distributable;
- resistant to post-hoc success criteria;
- explicit about negative results;
- suitable for independent mathematical and statistical verification.

The central principle is:

> **The experiment is defined by its specification, not by its reference implementation.**

CBR-Lab may implement an experiment, but CBR-Lab does not define the experiment.

---

# Part I — Experimental Objects

## 2. Core Object Model

CBR-OEN defines the following primary objects:

\[
\text{Hypothesis}
\rightarrow
\text{Experiment}
\rightarrow
\text{Specification}
\rightarrow
\text{Implementation}
\rightarrow
\text{Run}
\rightarrow
\text{Dataset}
\rightarrow
\text{Analysis}
\rightarrow
\text{Claim}
\rightarrow
\text{Replication}
\]

Every object receives:

- a persistent identifier;
- version;
- creation timestamp;
- provenance;
- content hash where practical.

No existing object is silently overwritten.

Changes create new versions.

---

# 3. Identifier Scheme

Recommended identifier forms are:

```text
CBR-H001          Hypothesis
CBR-E001          Experiment
CBR-S001          Specification
CBR-I001          Implementation
CBR-R000001       Individual run
CBR-RS001         Run set
CBR-D001          Dataset
CBR-A001          Analysis
CBR-C001          Claim
CBR-RP001         Replication
CBR-CH001         Challenge
CBR-MR001         Mathematical review
```

Versions are appended:

```text
CBR-E001:v1.0
CBR-S001:v1.1
```

---

# Part II — Experiment Specification

# 4. Required Experiment Fields

Every registered experiment must define:

### Identity

- experiment ID;
- title;
- version;
- authors/proposers;
- date.

### Scientific statement

- hypothesis;
- null hypothesis;
- motivation;
- scope.

### Prohibited assumptions

Explicit statement of structures that must **not** be encoded.

### Initial conditions

Definition of the starting computational state.

### Computational rules

Formal description of permitted transitions.

### Search or optimisation objective

If evolution or optimisation is used, exactly what the system is allowed to optimise.

### Excluded objective information

Variables that must not influence optimisation.

### Measurements

Metrics computed after or during the experiment.

### Primary endpoint

The result upon which the preregistered conclusion depends.

### Secondary endpoints

Exploratory or supporting measurements.

### Randomness

Seed construction and PRNG requirements.

### Sample size

Number of independent runs.

### Statistical protocol

How results will be evaluated.

### Stopping rule

When computation terminates.

### Failure handling

Definition of invalid, failed and excluded runs.

### Reproducibility requirements

What must be recorded.

---

# 5. Canonical YAML Schema

CBR-OEN specifications should have a human-readable YAML representation.

```yaml
cbr_oen:
  protocol_version: "1.0"

experiment:
  id: "CBR-E001"
  version: "1.0"
  title: "Emergent Dimensionality from Geometry-Free Relational Computation"

  status: "preregistered"

  scientific_question: >
    Can local relational computational systems with no encoded
    spatial coordinates produce reproducible effective
    dimensional structure?

hypothesis:
  id: "CBR-H001"

  statement: >
    Dimension-independent local computational dynamics can
    generate reproducible non-trivial effective dimensionality.

null_hypothesis: >
  Observed dimensional estimates are fully explained by finite-size,
  random-network, measurement, or implementation effects, with no
  reproducible dimensional attractor.

prohibited_prior_structure:
  spatial_coordinates: true
  predefined_dimension: true
  euclidean_metric: true
  manifold_target: true
  curvature_target: true

initial_conditions:
  type: "abstract_relational_graph"
  spatial_embedding: false

computational_rules:
  locality: "local"
  deterministic_given_seed: true

selection:
  enabled: false

measurements:
  primary:
    - ball_growth_dimension
    - spectral_dimension

  secondary:
    - connected_component_fraction
    - degree_distribution
    - clustering
    - finite_size_scaling

randomness:
  reproducible: true
  seed_policy: "registered_seed_schedule"

runs:
  discovery: 0
  confirmation: 10000

analysis:
  preregistered: true

implementation:
  reference_allowed: true
  independent_implementation_required_for_r2: true

results:
  negative_results_retained: true
```

---

# 6. Canonical JSON Form

Every YAML specification should have an equivalent canonical JSON representation for hashing and machine processing.

Example:

```json
{
  "protocolVersion": "1.0",
  "experimentId": "CBR-E001",
  "experimentVersion": "1.0",
  "spatialCoordinatesEncoded": false,
  "predefinedDimension": false,
  "primaryMeasurements": [
    "ball_growth_dimension",
    "spectral_dimension"
  ],
  "confirmationRuns": 10000,
  "negativeResultsRetained": true
}
```

Canonicalisation rules should eventually specify:

- UTF-8;
- deterministic property ordering;
- normalised line endings;
- no insignificant whitespace;
- fixed numerical representation.

The resulting digest becomes the experiment registration hash.

---

# Part III — Registration

# 7. Experiment Registration Manifest

Before confirmatory execution, a registration manifest is produced.

```yaml
registration:
  experiment: "CBR-E001:v1.0"

  specification_hash:
    algorithm: "SHA-256"
    value: "<hash>"

  registered_at:
    timestamp: "<UTC timestamp>"

  registration_status:
    type: "confirmatory"

  frozen_fields:
    - hypothesis
    - null_hypothesis
    - primary_measurements
    - sample_size
    - exclusion_rules
    - statistical_analysis
    - seed_policy

  exploratory_analysis_allowed: true

  exploratory_results_must_be_labelled: true
```

The important distinction is:

\[
\boxed{\text{Exploration} \neq \text{Confirmation}}
\]

A result used to discover a hypothesis cannot later be presented as independent confirmation of that same hypothesis.

---

# 8. Registration Hash

Define the registered experiment object:

\[
E=
(
S,
A,
R,
M
)
\]

where:

- \(S\) = specification;
- \(A\) = analysis plan;
- \(R\) = randomness protocol;
- \(M\) = metadata.

Then:

\[
H_E=SHA256(\operatorname{canonical}(E)).
\]

Every subsequent run references \(H_E\).

This prevents the experiment definition from changing unnoticed.

---

# Part IV — Implementation

# 9. Implementation Manifest

Every software implementation receives its own manifest.

```yaml
implementation:
  id: "CBR-I001"

  experiment:
    id: "CBR-E001"
    version: "1.0"

  language: "Python"

  implementation_type: "reference"

  repository_commit: "<git commit>"

  source_hash: "<hash>"

  runtime:
    language_version: "<version>"
    operating_system: "<value>"
    architecture: "<value>"

  dependencies:
    recorded: true

  authors:
    institution: "<institution>"

  independent_from_reference:
    false
```

An independently written Julia implementation might instead state:

```yaml
implementation_type: "independent"

independent_from_reference: true
```

---

# 10. Independent Implementation Rule

An implementation may be considered independent where the implementation team primarily works from:

- the Experiment Specification;
- mathematical definitions;
- test vectors;
- required interfaces.

It should not simply translate CBR-Lab source line-by-line.

The objective is:

\[
\text{same specification}
\rightarrow
\text{different implementation}
\rightarrow
\text{same phenomenon}.
\]

---

# Part V — Run Protocol

# 11. Run Manifest

Every execution creates a Run Manifest.

```yaml
run:
  id: "CBR-R000001"

  experiment:
    id: "CBR-E001"
    version: "1.0"
    specification_hash: "<hash>"

  implementation:
    id: "CBR-I001"
    source_hash: "<hash>"

  execution_node:
    institution: "<institution>"
    node: "<node identifier>"

  seed:
    value: 428972114
    algorithm: "<specified PRNG>"

  parameters:
    nodes: 1000
    steps: 100000

  environment:
    architecture: "<value>"
    operating_system: "<value>"

  result:
    status: "complete"
    output_hash: "<hash>"

  timing:
    started: "<timestamp>"
    completed: "<timestamp>"
```

---

# 12. Run Status

A run may receive one of:

```text
COMPLETE
FAILED_COMPUTATION
INVALID_INPUT
ENVIRONMENT_FAILURE
NUMERICAL_FAILURE
SPECIFICATION_VIOLATION
EXCLUDED_BY_PREREGISTERED_RULE
```

A failed run must not simply disappear.

The failure itself becomes part of the dataset.

---

# 13. Run Sets

Large experiments group runs into Run Sets.

Example:

```text
CBR-RS001
```

with:

```yaml
run_set:
  experiment: "CBR-E001:v1.0"

  seeds:
    start: 0
    end: 99999

  total_expected: 100000

  execution_nodes:
    - NODE-A
    - NODE-B
    - NODE-C

  overlap_fraction: 0.10
```

---

# Part VI — Replication

# 14. Replication Certificate

A successful or failed replication produces a formal certificate.

```yaml
replication:
  id: "CBR-RP001"

  experiment:
    id: "CBR-E001"
    version: "1.0"

  replication_type:
    level: "R3"

  institution:
    name: "<institution>"

  implementation:
    id: "<independent implementation>"

  original_results_accessed_before_execution:
    false

  preregistered:
    true

  run_set:
    id: "<run set>"

  outcome:
    status: "REPLICATED"

  primary_endpoint:
    equivalent: true

  deviations:
    present: false

  certificate_hash: "<hash>"
```

Replication outcome values include:

```text
REPLICATED
PARTIALLY_REPLICATED
FAILED_TO_REPLICATE
INCONCLUSIVE
INVALID_REPLICATION
```

A failed replication remains part of the evidence graph.

---

# 15. Reproducibility Levels

### R1 — Computational Reproduction

Same:

\[
\text{specification}
+
\text{implementation}
+
\text{seed}
\]

produces the same result.

---

### R2 — Independent Implementation Reproduction

Different implementation produces equivalent experimental results.

---

### R3 — Institutional Replication

Independent organisations reproduce the phenomenon using registered implementations and independent execution.

---

# Part VII — CBR-E001

# 16. Experiment CBR-E001

## Emergent Dimensionality from Geometry-Free Relational Computation

### Status

Foundational experiment.

### Experimental class

Confirmatory computational experiment following an initial methodology-validation phase.

---

# 17. Scientific Question

> **Can local computational interactions between abstract relational entities generate reproducible effective dimensional behaviour when no spatial coordinates, spatial dimension or geometric metric are encoded into the system?**

---

# 18. Hypothesis

### CBR-H001

A sufficiently broad class of local relational computational systems can develop measurable effective dimensional behaviour even where no spatial dimension is specified.

Importantly, CBR-E001 does **not** hypothesise:

\[
d=3.
\]

Its first question is simply whether:

\[
d
\]

can emerge reproducibly at all.

This avoids building the desired answer into the earliest experiment.

---

# 19. Null Hypothesis

The null hypothesis is:

> Apparent dimensional behaviour can be explained by finite graph size, random-network properties, measurement artefacts, implementation artefacts or transient scaling, with no reproducible emergent dimensional structure.

---

# 20. Forbidden Information

The computational dynamics must not have access to:

```text
x
y
z

distance coordinates

target dimension

measured dimension

spectral dimension

manifold score

Euclidean embedding
```

No selection process may optimise any of these.

---

# 21. Computational State

At computational step \(t\), the system is:

\[
G_t=(V_t,E_t)
\]

where:

- \(V_t\) is the set of computational entities;
- \(E_t\) represents relationships.

No function:

\[
V\rightarrow\mathbb{R}^n
\]

is provided to the update rules.

---

# 22. Initial Conditions

CBR-E001 should use multiple preregistered initial-condition families.

### IC-A — Sparse connected random graph

No geometry.

### IC-B — Random regular graph

No geometry.

### IC-C — Minimal connected seed expanded computationally

No geometry.

The purpose of multiple initial conditions is to determine whether results are artefacts of one starting topology.

---

# 23. Rule Family

The initial rule family operates only on relational neighbourhoods.

A rule may inspect:

- degree;
- immediate neighbours;
- neighbours-of-neighbours;
- local triangle closure;
- local connectivity.

A rule may:

- add an edge;
- remove an edge;
- rewire an edge;
- perform no operation.

A rule may not inspect global spatial coordinates because none exist.

---

# 24. Initial Rule Parameters

One initial parameterisation may contain:

\[
R=
(k,b_t,p_r,p_l)
\]

where:

- \(k\) = target relational degree;
- \(b_t\) = local triangle-closing probability;
- \(p_r\) = rewiring probability;
- \(p_l\) = non-local/random relationship probability.

This parameterisation is deliberately simple and should not be treated as uniquely privileged.

Independent groups are encouraged to test additional preregistered rule families.

---

# 25. No Evolution in CBR-E001

CBR-E001 should initially avoid evolutionary optimisation entirely.

This is important.

The experiment asks:

> What dimensional behaviour occurs across the raw rule space?

Only later experiments should introduce optimisation.

Therefore:

```yaml
selection:
  enabled: false
```

---

# 26. Primary Measurement 1 — Ball-Growth Dimension

For node \(v\), define:

\[
B(v,r)=
\{
u\in V:
d_G(u,v)\leq r
\}.
\]

Measure:

\[
N_v(r)=|B(v,r)|.
\]

For a system with effective dimension \(d_H\):

\[
N(r)\propto r^{d_H}.
\]

Estimate:

\[
d_H=
\frac{d\log N(r)}
{d\log r}
\]

over a preregistered non-saturated scale interval.

---

# 27. Primary Measurement 2 — Spectral Dimension

Execute random walks on the resulting relational graph.

Let:

\[
P(t)
\]

be the return probability after \(t\) transitions.

A spectral dimension \(d_S\) satisfies approximately:

\[
P(t)\propto t^{-d_S/2}.
\]

Therefore:

\[
d_S=
-2
\frac{d\log P(t)}
{d\log t}.
\]

Ball-growth dimension and spectral dimension measure different properties.

Agreement is therefore more significant than either value independently.

---

# 28. Secondary Measurements

Secondary metrics should include:

- largest connected-component fraction;
- mean degree;
- degree variance;
- clustering coefficient;
- graph diameter where computationally practical;
- finite-size saturation;
- local dimension variance;
- seed-to-seed variance.

---

# 29. Finite-Size Scaling

A central control is to repeat experiments at increasing system size:

\[
N=
250,\;
500,\;
1000,\;
2000,\;
4000
\]

or another preregistered progression.

A dimensional estimate that disappears as \(N\) increases is not strong evidence of emergent dimensionality.

The relevant question is whether:

\[
d(N)
\rightarrow d_\infty
\]

appears to approach a stable regime.

---

# 30. Rule Sampling

CBR-E001 should sample the rule parameter space before results are observed.

Example preregistered ranges:

```yaml
target_degree:
  values: [3,4,5,6,7,8,9,10]

triangle_bias:
  range: [0.0, 1.0]

rewire_probability:
  range: [0.0, 0.15]

random_link_probability:
  range: [0.0, 0.10]
```

Sampling should use either:

- predetermined grid;
- Latin hypercube;
- registered pseudorandom sampling.

The strategy must be fixed before confirmatory execution.

---

# 31. Run Count

A proposed initial confirmatory design:

```text
Rule configurations:      1,000
Seeds per configuration:     10
────────────────────────────────
Total runs:              10,000
```

A larger institutional run could use:

```text
10,000 configurations
×
100 seeds
=
1,000,000 runs
```

The first target should prioritise reproducibility rather than sheer scale.

---

# 32. Primary CBR-E001 Endpoint

The primary endpoint should **not** be:

> Does dimension 3 occur?

Instead:

> **Do one or more regions of the registered rule space produce effective dimensional estimates that are reproducible across independent seeds, persist under increasing system size, and exhibit agreement between independent dimensional estimators beyond the registered random-network controls?**

This is a much stronger foundational test.

---

# 33. Success Criterion

CBR-E001 provides evidence for emergent dimensional structure if a preregistered region of rule space demonstrates:

1. reproducible dimensional estimates across seeds;

2. non-trivial scaling range;

3. persistence under finite-size scaling;

4. significant deviation from matched null networks;

5. partial or substantial agreement between:

\[
d_H
\]

and:

\[
d_S.
\]

A precise statistical threshold should be established by the Statistics Working Group before registration.

---

# 34. Failure Criterion

CBR-E001 does not support the hypothesis if, for example:

- apparent dimensions vary arbitrarily with graph size;
- dimensional fits are dominated by saturation;
- matched random networks produce equivalent behaviour;
- different estimators systematically disagree;
- independent implementations fail to reproduce the phenomenon;
- results depend on implementation-specific behaviour.

Any of these outcomes should be published.

---

# 35. Null Controls

Every experiment batch should include control systems.

Potential controls include:

### Random graph control

Matched node/edge count.

### Degree-preserving randomised control

Same degree sequence, rewired relationships.

### Static graph control

No evolution.

### Parameter-shuffled control

Rule relationships disrupted.

The controls help distinguish:

\[
\text{emergent consequence of dynamics}
\]

from:

\[
\text{generic property of finite graphs}.
\]

---

# 36. Blinded Analysis

For institutional replication, datasets may be labelled:

```text
DATASET-A
DATASET-B
DATASET-C
```

instead of:

```text
CBR dynamic
random control
degree-preserving control
```

The analysis group performs the preregistered dimensional tests before labels are revealed.

---

# 37. Recommended Institutional Distribution

A first CBR-E001 collaboration could operate as follows:

```text
Group 1 — Protocol
Finalises CBR-E001 specification

Group 2 — Mathematics
Reviews dimensional estimators

Group 3 — Statistics
Defines finite-size and significance criteria

Group 4 — Python
Reference implementation

Group 5 — Julia/Rust/C++
Independent implementation

Group 6 — Institution A
Runs primary dataset

Group 7 — Institution B
Runs replication dataset

Group 8 — Analysis
Performs blinded analysis
```

No single group needs to endorse CBR.

---

# 38. Expected Outputs

CBR-E001 should generate:

```text
/specification
  CBR-E001-v1.0.yaml

/registration
  CBR-E001-registration.yaml

/implementations
  CBR-I001
  CBR-I002

/run-manifests
  CBR-R*.yaml

/data
  raw
  processed

/analysis
  preregistered
  exploratory

/controls

/replications

/challenges

/negative-results

/publications
```

---

# 39. Evidence Graph Entries

A successful experimental cycle might generate:

\[
CBR-H001
\]

supported by:

\[
CBR-E001
\]

implemented by:

\[
CBR-I001,\;CBR-I002
\]

executed through:

\[
CBR-RS001,\;CBR-RS002
\]

analysed by:

\[
CBR-A001
\]

and independently replicated by:

\[
CBR-RP001.
\]

A competing challenge might simultaneously state:

\[
CBR-CH004
\rightarrow
\text{finite-size explanation}.
\]

Both remain visible.

---

# 40. Relationship to Later Experiments

CBR-E001 deliberately asks the weakest foundational question.

If dimensionality emerges, then subsequent experiments strengthen the requirements.

### CBR-E002

Does dimension-blind evolutionary selection produce dimensional attractors?

### CBR-E003

Are apparently three-dimensional structures locally manifold-like?

### CBR-E004

Can explicit simplicial computation generate or preserve 3-manifold topology?

### CBR-E005

Does dimension- and topology-blind selection suppress manifold-destroying defects?

Thus:

\[
E001
\rightarrow
E002
\rightarrow
E003
\rightarrow
E004
\rightarrow
E005.
\]

Each experiment introduces a stronger claim.

---

# 41. Institutional Replication Certificate

At completion, an institution can publish a compact result:

```yaml
cbr_oen_replication_certificate:

  certificate:
    id: "CBR-RP001"

  experiment:
    id: "CBR-E001"
    version: "1.0"

  institution:
    name: "<institution>"

  implementation:
    independent: true
    id: "CBR-I007"

  run_set:
    runs: 10000

  preregistration:
    followed: true

  primary_result:
    outcome: "REPLICATED"

  deviations:
    none: true

  raw_data_public:
    true

  analysis_public:
    true

  certificate_hash:
    algorithm: "SHA-256"
    value: "<hash>"
```

This makes replication itself a portable scientific object.

---

# 42. Protocol Evolution

CBR-OEN Protocol v1.0 should be considered deliberately minimal.

Future versions may add:

- formal JSON Schema;
- cryptographic signatures;
- distributed identity;
- content-addressed data;
- reproducible containers;
- deterministic numerical standards;
- federated compute APIs;
- automated replication;
- machine-verifiable evidence graphs;
- Verified Context Graph integration.

Protocol evolution must remain backward-readable.

---

# 43. Founding Requirement

No result should receive strong CBR-OEN evidentiary status solely because:

- one implementation produced it;
- one seed produced it;
- it visually resembles the desired answer;
- its authors believe the interpretation is plausible.

The required progression is instead:

\[
\boxed{
\text{Specify}
\rightarrow
\text{Register}
\rightarrow
\text{Implement}
\rightarrow
\text{Execute}
\rightarrow
\text{Analyse}
\rightarrow
\text{Reproduce}
\rightarrow
\text{Replicate}
\rightarrow
\text{Challenge}
}
\]

---

# 44. Final Principle

The purpose of the protocol is not to make experimentation bureaucratic.

It is to make surprising results trustworthy.

If an experiment eventually produces:

\[
d_H\approx d_S\approx3
\]

without dimension appearing anywhere in its rules or objectives, the first response should not be:

> We have demonstrated that reality is computational.

It should be:

> Can another implementation, another institution, another seed population, another mathematical method and another critic reproduce or explain this result?

Only after those questions have been answered does interpretation become scientifically interesting.

That is the purpose of CBR-OEN.

> **Make the experiment independent of the theory's advocates, and make the evidence stronger than the interpretation.**