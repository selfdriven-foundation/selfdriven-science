# CBR Open Experimental Network
## Founding Paper and Cooperative Experimental Protocol
### Version 0.1

## Abstract

The **CBR Open Experimental Network (CBR-OEN)** is proposed as an open, distributed scientific collaboration for investigating whether geometric, topological and physical structure can emerge from computation without being explicitly encoded as prior structure.

The network originates from research into **Compute-Based Reality (CBR)**, but it is deliberately designed so that participation does not require acceptance of CBR as a theory of reality.

Its purpose is narrower and scientifically testable:

> **To design, execute, replicate and critically evaluate computational experiments concerning the emergence of dimensionality, topology, geometry and physical behaviour from minimal computational systems.**

CBR-OEN separates hypothesis formation, implementation, execution, mathematical verification, statistical analysis and physical interpretation wherever practical. Experiments are preregistered, independently implementable, reproducible by seed, openly archived and explicitly designed to preserve negative results.

No central body is authorised to declare that an experiment proves CBR. Instead, evidence accumulates through a distributed graph of hypotheses, experiments, implementations, runs, replications, challenges and mathematical reviews.

The network is intended to provide scientific and mathematical institutions with a low-barrier mechanism for contributing specialised expertise while preserving institutional independence.

The founding principle is:

> **CBR-OEN does not exist to prove Compute-Based Reality. It exists to make Compute-Based Reality testable.**

---

# 1. Introduction

Questions concerning the origin of space, dimensionality, geometry and physical law sit at the boundary of mathematics, theoretical physics, computer science and philosophy.

Many contemporary approaches assume some geometric or causal substrate and investigate physical processes occurring upon it.

Compute-Based Reality proposes a different starting point.

It asks whether relational computation itself could be fundamental, with spatial and physical structures emerging as effective descriptions of deeper computational organisation.

The conceptual progression can be represented as:

\[
\text{Computation}
\rightarrow
\text{Relations}
\rightarrow
\text{Topology}
\rightarrow
\text{Geometry}
\rightarrow
\text{Physics}.
\]

Such a proposition is scientifically useful only if it can be converted into falsifiable experiments.

CBR-OEN exists to make that conversion possible.

Rather than constructing a research organisation around agreement with a theoretical position, CBR-OEN is designed around **cooperative disagreement**.

Researchers may participate because they believe:

- CBR is promising;
- CBR is unlikely;
- the mathematics is interesting independently of CBR;
- the simulations present useful complexity-science questions;
- the topology warrants investigation;
- the methodology offers a useful reproducibility experiment;
- or the hypotheses deserve rigorous falsification.

All are equally legitimate reasons to participate.

---

# 2. Founding Scientific Question

The initial research programme is organised around the question:

> **Can computational systems with no predefined spatial geometry generate persistent structures whose large-scale behaviour exhibits dimensionality, manifold topology, geometry and eventually physical dynamics?**

This question can be decomposed into progressively stronger propositions.

For example:

\[
H_1:
\text{effective dimensionality can emerge}
\]

\[
H_2:
\text{particular dimensions can behave as attractors}
\]

\[
H_3:
\text{dimensionally emergent structures can also be manifold-like}
\]

\[
H_4:
\text{manifold structure can be dynamically stable}
\]

\[
H_5:
\text{effective metric structure can emerge}
\]

\[
H_6:
\text{persistent structures can influence emergent geometry}
\]

\[
H_7:
\text{known physical behaviour can be recovered quantitatively}.
\]

Each proposition must be independently challengeable.

Failure at any stage is a scientifically meaningful result.

---

# 3. What CBR-OEN Is Not

CBR-OEN is not a standards organisation for declaring CBR correct.

It is not a centralised laboratory.

It is not an institution that requires members to adopt a shared interpretation of reality.

It is not a mechanism for publishing only positive results.

It is not restricted to a particular programming language, simulator, institution or computing platform.

CBR-Lab may provide a reference implementation, but:

> **CBR-Lab is not the experiment.**

The experiment is the specification.

Multiple independent implementations should be able to execute the same specification.

---

# 4. Founding Principles

CBR-OEN adopts ten founding principles.

### 4.1 Testability before advocacy

Claims should be expressed as falsifiable propositions whenever possible.

### 4.2 Specification before execution

Experiments should be defined before results are observed.

### 4.3 Independence of implementation

Scientific confidence increases when multiple implementations reproduce equivalent results.

### 4.4 Separation of roles

Hypothesis, implementation, execution and analysis should be separated wherever practical.

### 4.5 Negative results are first-class results

Failure to reproduce an effect must be retained and discoverable.

### 4.6 Provenance is part of the evidence

Software version, parameters, seeds and analysis procedures are integral to a result.

### 4.7 Mathematical criticism is encouraged

A result should become stronger through successful challenge.

### 4.8 Institutional autonomy

Participating institutions remain scientifically independent.

### 4.9 Open evidence

Specifications, reference implementations, results and critiques should default to public availability.

### 4.10 No experiment proves the whole theory

Evidence applies to individual claims.

---

# 5. Organisational Model

CBR-OEN is conceived as a federation rather than a conventional central research organisation.

Its high-level structure is:

\[
\boxed{\text{CBR-OEN}}
\]

\[
\begin{array}{ccc}
\text{Protocol} &
\text{Computation} &
\text{Evidence}\\
\downarrow &
\downarrow &
\downarrow\\
\text{Specifications} &
\text{Distributed Runs} &
\text{Verification}\\
\text{Mathematics} &
\text{Independent Implementations} &
\text{Replication}\\
\text{Statistics} &
\text{HPC / University Nodes} &
\text{Challenges}
\end{array}
\]

These functions need not belong to the same institution.

Indeed, separation is preferred.

---

# 6. Participant Roles

Participating institutions or researchers may undertake one or more defined roles.

## 6.1 Hypothesis Group

Develops proposed scientific claims.

Responsibilities include:

- expressing the hypothesis;
- defining the null hypothesis;
- identifying possible falsification conditions;
- distinguishing observation from interpretation.

A Hypothesis Group does not determine whether its own hypothesis has succeeded.

---

## 6.2 Mathematical Verification Group

Defines or reviews mathematical tests.

Examples include:

- effective dimensionality;
- spectral dimension;
- homology;
- cohomology;
- local manifold conditions;
- simplicial complexes;
- graph limits;
- metric properties;
- curvature;
- convergence.

A mathematics group may participate without taking any position on CBR.

---

## 6.3 Implementation Group

Builds software implementing a registered experiment specification.

Independent implementations are strongly encouraged.

Potential implementations include:

```text
Python
Julia
Rust
C++
Haskell
Mathematica
specialised HPC code
institutional simulation platforms
```

The implementation should conform to the experiment specification rather than to another implementation's source code.

---

## 6.4 Execution Node

Runs registered experiments.

Execution nodes may include:

- university laboratories;
- mathematics institutes;
- physics institutes;
- supercomputing facilities;
- distributed computing platforms;
- independent research groups;
- approved citizen-science nodes.

Execution nodes do not need to participate in theoretical interpretation.

---

## 6.5 Analysis Group

Performs statistical analysis of experimental outputs.

Where appropriate, outputs may be anonymised or blinded so that analysts do not know which rule family or implementation generated a dataset.

---

## 6.6 Replication Group

Repeats an experiment independently.

Replication groups should ideally have had no role in constructing the original implementation.

---

## 6.7 Adversarial Review Group

Attempts to identify alternative explanations, artefacts, methodological weaknesses or hidden assumptions.

A successful criticism is considered a contribution to the network.

---

# 7. Adversarial Collaboration

Major experiments should seek three explicit perspectives:

\[
\boxed{
\text{Proponent}
+
\text{Sceptic}
+
\text{Verifier}
}
\]

The Proponent explains why a result may support a hypothesis.

The Sceptic defines competing explanations and failure criteria.

The Verifier determines whether the agreed test was actually satisfied.

All three contribute before execution where possible.

This prevents the experiment from being defined only by researchers who expect a particular result.

---

# 8. Experiment Identification

Every formal experiment receives a persistent identifier.

For example:

```text
CBR-E001
CBR-E002
CBR-E003
```

Sub-experiments may use:

```text
CBR-E003-A
CBR-E003-B
```

Every experiment has a version:

```text
CBR-E003:v1.0
```

Modifications create a new version rather than silently altering the prior specification.

---

# 9. Experiment Specification

The primary scientific artefact of CBR-OEN is the **Experiment Specification**.

It must be independent of any particular implementation.

A minimal specification includes:

```yaml
experiment: CBR-E001
version: 1.0

title:
  Emergent dimensionality from relational computation

hypothesis:
  description:
    Effective dimensional structure may emerge
    from geometry-free relational computation.

null_hypothesis:
  description:
    No reproducible dimensional attractor occurs.

initial_conditions:
  geometry_encoded: false
  spatial_coordinates: false

selection_objectives:
  - persistence
  - structural_complexity
  - stability

excluded_selection_objectives:
  - spatial_dimension
  - spectral_dimension
  - manifold_score

measurements:
  - hausdorff_like_dimension
  - spectral_dimension

randomness:
  deterministic_from_seed: true

analysis:
  preregistered: true

implementation:
  independent_implementations_encouraged: true
```

The specification defines the experiment.

The code implements it.

---

# 10. Preregistration

Before primary experimental results are generated, the specification should be frozen.

A registration package includes:

\[
P =
(
H,
N,
R,
M,
A,
S
)
\]

where:

- \(H\) = hypothesis;
- \(N\) = null hypothesis;
- \(R\) = computational rules;
- \(M\) = measurements;
- \(A\) = analysis procedure;
- \(S\) = seed-generation procedure.

The package receives a cryptographic digest:

\[
ID_E=H(P).
\]

This digest is timestamped and published.

Changes after preregistration create a new experimental version.

Exploratory analysis remains permitted, but it must be clearly labelled as exploratory.

---

# 11. Randomness and Seeds

Randomness must itself be reproducible.

Each experiment specifies:

- pseudorandom algorithm;
- library or reference algorithm;
- seed width;
- seed-generation procedure;
- whether seeds are public before execution;
- whether any seeds are reserved for confirmation.

A useful design is to separate:

```text
Development Seeds
Exploration Seeds
Confirmation Seeds
Replication Seeds
```

Confirmation seeds should ideally remain unused until the experimental design is frozen.

---

# 12. Run Manifest

Every computational run generates a signed or hash-addressed manifest.

Example:

```json
{
  "experiment": "CBR-E004:v1.0",
  "implementation": "IMPLEMENTATION-JULIA-02",
  "institution": "NODE-A17",
  "seed": 428972114,
  "code_hash": "...",
  "specification_hash": "...",
  "environment_hash": "...",
  "input_hash": "...",
  "result_hash": "...",
  "started": "...",
  "completed": "...",
  "status": "complete"
}
```

A run is therefore not merely an output file.

It is:

\[
R_i =
H(
E_i,
C_i,
S_i,
ENV_i,
O_i
).
\]

---

# 13. Independent Implementation Protocol

CBR-OEN distinguishes running the same code from independently reproducing an experiment.

An independent implementation should be constructed primarily from:

- the registered specification;
- mathematical definitions;
- published test vectors;
- interface requirements.

It should not require copying the logic of the reference implementation.

This gives three increasingly strong forms of agreement:

### Implementation agreement

Same program, same input, same output.

### Algorithmic agreement

Independent programs generate equivalent outcomes.

### Scientific agreement

Independent implementations reproduce the same statistical phenomenon.

The third is the most significant.

---

# 14. Distributed Computation

Large experiment sets may be distributed across institutions.

For example:

```text
Node A    seeds 000000–099999
Node B    seeds 100000–199999
Node C    seeds 200000–299999
Node D    seeds 300000–399999
```

A deliberate overlap should be included.

For example:

\[
5\%-10\%
\]

of jobs may be duplicated between independent execution nodes.

If the experiment is deterministic:

\[
R_{A,s}
=
R_{B,s}
\]

for shared seed \(s\).

These duplicate calculations continuously test infrastructure and implementation integrity.

---

# 15. Reproducibility Levels

CBR-OEN defines three initial evidence levels.

## R1 — Computational Reproducibility

The same implementation and seed reproduce the result.

## R2 — Independent Reproducibility

An independent implementation reproduces equivalent results.

## R3 — Institutional Replication

Multiple independent institutions reproduce the experimental finding.

Strong scientific claims should normally require R3.

---

# 16. Mathematical Validation

Numerical resemblance is insufficient for many CBR claims.

For example:

\[
d\approx3
\]

does not imply that a structure is a 3-manifold.

CBR-OEN therefore separates numerical and mathematical claims.

A 3-manifold candidate may require independent tests concerning:

\[
\operatorname{link}(v)\cong S^2
\]

for appropriate interior vertices.

Additional tests may include:

- local homology;
- Euler characteristic;
- simplex incidence;
- orientability;
- boundary detection;
- global homology;
- persistent homology;
- convergence under refinement.

Mathematical Verification Groups may add stronger tests over time.

Prior results remain associated with the tests used at the time.

---

# 17. Statistical Protocol

Before confirmatory experiments, analysis should specify:

- primary endpoint;
- secondary endpoints;
- sample size;
- number of independent runs;
- confidence interval procedure;
- treatment of failed runs;
- finite-size corrections;
- multiple-comparison strategy;
- stopping criteria;
- model-selection procedure.

Rule searches must distinguish between:

\[
\text{discovery}
\]

and:

\[
\text{confirmation}.
\]

If a rule is discovered because it produces \(d\approx3\), the same runs cannot subsequently be presented as independent evidence that the rule produces \(d\approx3\).

New confirmation runs are required.

---

# 18. Negative Results

CBR-OEN explicitly rejects publication bias.

Results such as:

> No dimensional attractor was found.

or:

> Apparent \(d=3\) behaviour disappeared with increased system size.

or:

> Independent implementation did not replicate the topology result.

are first-class scientific results.

Repositories should therefore contain:

```text
/results
/replications
/challenges
/negative-results
```

Negative findings should be indexable in the same evidence system as supportive results.

---

# 19. Evidence Graph

CBR-OEN should not treat papers as the fundamental unit of scientific knowledge.

Instead, results are organised as an evidence graph.

For example:

```text
Hypothesis CBR-H003
        │
        ├── Experiment CBR-E003
        │       │
        │       ├── Implementation A
        │       ├── Implementation B
        │       │
        │       ├── Run Set 1
        │       ├── Replication R3
        │       └── Challenge CBR-C017
        │
        └── Mathematical Review MR-008
```

The graph may include relations such as:

```text
SUPPORTS
CONTRADICTS
REPLICATES
FAILS_TO_REPLICATE
CHALLENGES
IMPLEMENTS
RUNS
ANALYSES
SUPERSEDES
REFINES
INVALIDATES
```

This permits scientific disagreements to remain represented rather than being collapsed into a single consensus statement.

---

# 20. Evidence Status

Claims may accumulate evidence states such as:

```text
PROPOSED
FORMALISED
PREREGISTERED
EXECUTED
REPRODUCED
INDEPENDENTLY_REPRODUCED
INSTITUTIONALLY_REPLICATED
MATHEMATICALLY_REVIEWED
PHYSICALLY_INTERPRETED
CHALLENGED
CONTRADICTED
SUPERSEDED
```

These are provenance states, not declarations of truth.

---

# 21. Initial Experimental Programme

The initial CBR-OEN programme may consist of the following sequence.

| ID | Experimental Question |
|---|---|
| **CBR-E001** | Can effective dimensionality emerge from geometry-free relational computation? |
| **CBR-E002** | Does dimension-blind selection generate reproducible dimensional attractors? |
| **CBR-E003** | Do structures exhibiting \(d\approx3\) satisfy local manifold conditions? |
| **CBR-E004** | Can explicit simplicial computation maintain stable 3-manifold topology? |
| **CBR-E005** | Does dimension- and topology-blind selection suppress topology-destroying defects? |
| **CBR-E006** | Can computational transition cost produce an emergent metric? |
| **CBR-E007** | Can persistent computational structures modify that metric? |
| **CBR-E008** | Can geodesic-like attraction emerge without gravitational attraction being explicitly programmed? |
| **CBR-E009** | Can Lorentz-like causal behaviour emerge from local computation? |
| **CBR-E010** | Can the resulting system quantitatively recover known gravitational behaviour? |

Each experiment should be able to fail independently.

---

# 22. Relationship to CBR-Lab

CBR-Lab acts as an open reference implementation and experimental sandbox.

Its role is:

\[
\text{Specification}
\rightarrow
\boxed{\text{CBR-Lab}}
\rightarrow
\text{Reference Results}.
\]

CBR-Lab must not become the authoritative definition of the experiment.

Where code and specification disagree, the specification is authoritative until formally amended.

Independent groups are encouraged to build implementations without using CBR-Lab source code.

---

# 23. Working Groups

CBR-OEN may establish specialised working groups.

Initial groups could include:

### Computational Rules Working Group

Studies minimal computational rule systems.

### Geometry Working Group

Defines emergent distance, dimension and metric tests.

### Topology Working Group

Defines manifold and homology requirements.

### Physics Working Group

Determines relationships to known physical theories.

### Statistics Working Group

Develops preregistration and inference protocols.

### Reproducibility Working Group

Coordinates independent implementations and replication.

### Infrastructure Working Group

Maintains schemas, repositories and distributed-compute protocols.

### Evidence Working Group

Develops the evidence graph and provenance system.

Working groups advise experiments but do not control their conclusions.

---

# 24. Protocol Council

A lightweight Protocol Council maintains interoperability.

Its responsibilities include:

- experiment identifier format;
- specification schemas;
- result manifests;
- provenance formats;
- reproducibility status;
- repository conventions;
- versioning.

The Protocol Council should not determine scientific validity.

Scientific disagreements remain within the evidence graph.

---

# 25. Governance Principles

CBR-OEN governance follows:

\[
\boxed{
\text{Open participation}
+
\text{transparent provenance}
+
\text{limited central authority}
}
\]

No organisation owns the scientific conclusions of the network.

Participating institutions retain ownership of their own interpretations and publications subject to applicable licences.

Protocol changes should use documented proposals and versioned decisions.

---

# 26. Scientific Integrity

The network should preserve:

- original raw results;
- specification versions;
- software hashes;
- complete parameter sets;
- failed runs;
- excluded runs and exclusion reasons;
- analysis code;
- reviewer challenges;
- corrections.

Results should not be overwritten.

Corrections should create new linked records.

---

# 27. Open Licensing

Where legally possible, CBR-OEN should use permissive open licences for:

- specifications;
- code;
- schemas;
- experimental datasets;
- documentation.

Individual institutions remain free to apply their own publication and intellectual-property policies.

However, an experiment should not receive full open-reproducibility status unless sufficient information exists for independent reproduction.

---

# 28. Publication Model

Traditional papers remain important, but they become views over a deeper evidence structure.

A paper might therefore reference:

```text
Hypothesis:
CBR-H005

Experiment:
CBR-E005:v1.2

Implementations:
PY-REF-03
JULIA-ANU-01
RUST-INDEP-04

Run sets:
RS-1024
RS-1098
RS-1172

Replication status:
R3

Mathematical reviews:
MR-14
MR-19
```

A reader can move from the interpretation directly to the underlying experiment.

---

# 29. Verified Evidence Context

The evidence architecture can eventually be represented as a Verified Context Graph.

Conceptually:

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
\text{Replication}.
\]

Every relationship carries provenance.

The graph therefore becomes a machine-readable description of the scientific argument.

This architecture also enables computational tools and AI systems to distinguish:

- hypothesis from evidence;
- evidence from interpretation;
- replicated findings from preliminary findings;
- current claims from superseded claims.

---

# 30. How Institutions Can Participate

Participation should require minimal organisational commitment.

An institution might contribute only one element.

For example:

### Mathematics department

Review the definition of a manifold test.

### Computer-science laboratory

Build an independent implementation.

### HPC centre

Execute registered run batches.

### Statistics group

Review preregistration and inference.

### Physics department

Assess correspondence with known physical theory.

### Complexity institute

Develop alternative computational rules.

### Graduate research group

Attempt replication.

### Sceptical research team

Attempt to falsify the experiment.

All are meaningful contributions.

---

# 31. Suggested Institutional Invitation

The network should avoid asking institutions to endorse an unconventional theory.

The invitation can instead state:

> **CBR-OEN is an open research collaboration investigating whether dimensional, topological and geometric structures can emerge from computational systems that do not encode those structures as objectives. We invite independent mathematics, physics, computer-science and complexity-research groups to propose tests, implement specifications, replicate simulations, challenge methodology and analyse results. Participation does not imply endorsement of Compute-Based Reality or any associated theoretical interpretation.**

This positions the project correctly.

---

# 32. Initial Cooperation Model

A first cooperative experiment might involve five independent participants.

```text
Group A
Defines the computational experiment

Group B
Reviews mathematical validity

Group C
Builds independent implementation

Group D
Executes replication set

Group E
Performs blinded statistical analysis
```

Only after all five stages are complete are physical interpretations formally discussed.

This provides a practical template for CBR-E001 through CBR-E005.

---

# 33. Success Criteria for CBR-OEN

The success of the network should not be measured by whether CBR is supported.

CBR-OEN succeeds if it produces:

- precise hypotheses;
- reproducible simulations;
- rigorous mathematical tests;
- independent implementations;
- successful or failed replications;
- transparent negative results;
- improved scientific questions.

Thus:

\[
\text{CBR falsified rigorously}
\]

would represent a successful CBR-OEN outcome.

So would:

\[
\text{CBR hypotheses survive repeated independent challenge}.
\]

The network serves the inquiry rather than a preferred answer.

---

# 34. Founding Scientific Commitment

Participants in CBR-OEN should be able to agree on one statement regardless of theoretical position:

> **Where a claim about the computational foundations of reality can be converted into a reproducible mathematical or computational experiment, it should be tested openly, independently and adversarially.**

This is the common ground of the network.

---

# 35. Conclusion

Compute-Based Reality proposes an unusually fundamental hypothesis.

That makes methodological discipline more important, not less important.

The appropriate response is therefore not to build a community organised around belief in the theory.

It is to build infrastructure through which the theory can be repeatedly challenged.

CBR-OEN provides such a structure.

It separates theory from execution.

It separates execution from verification.

It separates verification from interpretation.

It rewards replication.

It preserves disagreement.

It publishes failure.

And it makes the complete path from hypothesis to evidence inspectable.

The ultimate goal is not:

\[
\boxed{\text{prove CBR}}
\]

but:

\[
\boxed{
\text{make foundational claims computationally testable}
}
\]

The central founding principle therefore remains:

> **CBR-OEN does not exist to prove Compute-Based Reality. It exists to make Compute-Based Reality testable.**

If CBR fails, the network should tell us why.

If it survives, the network should tell us how strongly.

If unexpected mathematics or physics emerges along the way, those discoveries stand independently of the theory that motivated the investigation.

That is the scientific purpose of the CBR Open Experimental Network.