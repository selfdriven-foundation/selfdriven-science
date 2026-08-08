# CBR-OEN Experiment CBR-E002
## Dimension-Blind Evolution of Relational Computational Systems
### Preregistered Experimental Specification — Draft v1.0

---

## 1. Experiment Identity

**Experiment ID:** CBR-E002  
**Version:** 1.0  
**Title:** Dimension-Blind Evolution of Relational Computational Systems  
**Protocol:** CBR-OEN Experimental Protocol v1.0  
**Experiment class:** Confirmatory computational experiment  
**Predecessor:** CBR-E001 — Emergent Dimensionality from Geometry-Free Relational Computation

---

# 2. Scientific Question

CBR-E002 asks:

> **When computational rule systems are selected only for persistence, structural complexity and stability, does effective dimensionality emerge as a reproducible side effect of that selection?**

The experiment specifically investigates whether dimensional structure may arise because it supports persistent and stable computational organisation rather than because dimensionality itself is explicitly optimised.

---

# 3. Core Hypothesis

### CBR-H002

Dimension-blind evolutionary selection over local relational computational rules can produce reproducible attractors in effective dimensionality.

Formally, let a computational rule be:

\[
R_i.
\]

Let fitness depend only upon:

\[
F(R_i)
=
f(P_i,C_i,S_i)
\]

where:

- \(P_i\) = persistence;
- \(C_i\) = structural complexity;
- \(S_i\) = dynamical stability.

The hypothesis is that optimisation of \(F\) may indirectly produce convergence in measured dimensionality:

\[
R_i
\xrightarrow{\text{selection}}
R_i^*
\]

such that:

\[
d(R_i^*)
\]

has a narrower or otherwise structured distribution compared with the unselected rule population.

---

# 4. Stronger CBR Interpretation

CBR-E002 does not test whether three-dimensional space necessarily emerges.

Its primary claim is weaker:

> **Dimensional structure may be a consequence of selecting computational systems for persistence and stability.**

A stronger exploratory possibility is:

\[
d\approx3.
\]

However, this value is not part of the primary endpoint.

Any specific convergence toward three dimensions must be treated as an observed result requiring subsequent independent confirmation.

---

# 5. Null Hypothesis

The null hypothesis is:

> Evolutionary selection for persistence, complexity and stability does not produce a reproducible dimensional attractor beyond that expected from neutral search, finite-size effects, parameter correlations or properties of the underlying rule family.

Under the null:

\[
P(d\mid\text{selected})
\]

should not differ materially from suitable controls once confounding factors are accounted for.

---

# 6. Experimental Principle

The central constraint is:

\[
\boxed{\text{dimension must never influence selection}}
\]

The evolutionary system must not receive:

- Hausdorff-like dimension;
- spectral dimension;
- target dimension;
- dimensional error;
- manifold score;
- curvature;
- geometry;
- spatial coordinates.

These variables may be measured for later analysis but must not be available to the evolutionary objective.

---

# 7. State Representation

At computational time \(t\), each simulated system is represented by:

\[
G_t=(V_t,E_t)
\]

where:

- \(V_t\) is a set of computational entities;
- \(E_t\) is a set of relationships.

No spatial embedding is provided.

There is no function:

\[
V_t\rightarrow\mathbb{R}^n.
\]

No node has an intrinsic spatial coordinate.

---

# 8. Rule Genome

The initial CBR-E002 rule family uses:

\[
R=
(k,b_t,p_r,p_l)
\]

where:

### \(k\) — Target relational degree

Preferred local node connectivity.

### \(b_t\) — Triangle-closing bias

Probability of preferentially connecting within local relational neighbourhoods.

### \(p_r\) — Rewiring probability

Probability of replacing an existing relationship.

### \(p_l\) — Random-link probability

Probability of forming a relationship outside the immediate local neighbourhood.

Example admissible ranges:

\[
k\in\{3,\ldots,10\}
\]

\[
b_t\in[0,1]
\]

\[
p_r\in[0,0.15]
\]

\[
p_l\in[0,0.10].
\]

These ranges must be frozen before confirmatory execution.

---

# 9. Local Rewrite Rule

A node is sampled according to the registered update procedure.

The rule may inspect only relational information, such as:

- its degree;
- neighbouring nodes;
- second-order neighbours;
- local triangle structure;
- existing edges.

The rule may:

- add an edge;
- remove an edge;
- rewire an edge;
- perform no operation.

It may not inspect measured dimensionality.

---

# 10. Evolutionary Population

A population contains:

\[
N_P
\]

independent rule genomes.

Proposed baseline:

```text id="yrh99l"
Population size: 50
Generations:     30
Replicates:       3
```

Each genome is evaluated on multiple independent computational runs.

Fitness is averaged across replicates.

---

# 11. Fitness Function

The preregistered baseline fitness is:

\[
F=
0.40P
+
0.35C
+
0.25S.
\]

No dimensional variable appears in this equation.

---

# 12. Persistence

Persistence measures whether the relational structure remains coherently connected through the evaluation period.

One baseline measure is the fraction of vertices contained in the largest connected component:

\[
P_t=
\frac{|V_{\text{giant}}|}
{|V|}.
\]

Persistence is averaged across preregistered checkpoints:

\[
P=
\frac{1}{n}
\sum_t P_t.
\]

Alternative persistence definitions may be tested in separate experimental versions.

---

# 13. Structural Complexity

Complexity must not encode a preferred dimension.

The baseline measure combines local structural diversity measures such as:

- degree-distribution entropy;
- clustering diversity;
- local connectivity heterogeneity.

Example:

\[
C=
G
\left(
\alpha H_D
+
\beta C_L
\right)
\]

where:

- \(G\) = giant-component fraction;
- \(H_D\) = normalised degree entropy;
- \(C_L\) = clustering measure.

The exact implementation must be frozen before preregistration.

---

# 14. Stability

Stability measures whether macroscopic structural statistics remain relatively consistent across late computational checkpoints.

Let:

\[
X_t
\]

represent a vector of structural statistics.

Then stability may be represented as:

\[
S=
1-
\frac{1}{m}
\sum_j
\Delta_j(X_{t_1},X_{t_2}).
\]

Values should be normalised into:

\[
S\in[0,1].
\]

---

# 15. Forbidden Fitness Variables

The following must be excluded from fitness:

```text id="ldkb7e"
ball-growth dimension
spectral dimension
target d=3
distance from d=3
manifold score
homology
Euler characteristic
curvature
metric regularity
Lorentz behaviour
geodesic behaviour
```

These may only be used for observation after fitness is determined.

---

# 16. Evolutionary Operators

The baseline evolutionary process may use:

### Selection

Tournament selection.

### Elitism

Top-performing individuals carried forward unchanged.

### Mutation

Random parameter perturbations.

### Crossover

Parameter inheritance from two parent genomes.

The precise probabilities must be preregistered.

Example:

```yaml id="12qv92"
evolution:
  selection:
    type: "tournament"
    tournament_size: 3

  elite_count: 4

  mutation_probability: 0.30

  crossover_probability: 1.00
```

---

# 17. Randomness

Every evolutionary experiment must be reproducible from a master seed.

Derived seeds should determine:

- initial genome population;
- mutations;
- crossover choices;
- graph initial conditions;
- simulation updates;
- dimensional measurement walks.

The seed derivation procedure must be deterministic.

---

# 18. Primary Experimental Comparison

CBR-E002 compares:

\[
P(d\mid E)
\]

with:

\[
P(d\mid N)
\]

where:

- \(E\) = evolution under persistence/complexity/stability fitness;
- \(N\) = neutral or random rule sampling.

The primary question is:

> Does evolutionary selection materially change the dimensional distribution?

---

# 19. Control A — Random Rule Search

Generate the same number of evaluated rule genomes without fitness selection.

This provides:

\[
P(d\mid\text{random search}).
\]

---

# 20. Control B — Neutral Evolution

Use the same evolutionary machinery but select parents independently of fitness.

This tests whether any apparent dimensional convergence results merely from:

- mutation;
- crossover;
- population bottlenecks;
- genetic drift.

---

# 21. Control C — Shuffled Fitness

Fitness values are randomly permuted between individuals before selection.

This preserves the fitness distribution but destroys the relationship between fitness and genome.

---

# 22. Control D — Single-Objective Ablations

Run separate experiments using only:

\[
F=P
\]

or:

\[
F=C
\]

or:

\[
F=S.
\]

This tests whether a dimensional effect depends upon one particular fitness component.

---

# 23. Control E — Fitness-Weight Variations

Repeat with alternative preregistered weights.

For example:

\[
(0.50,0.25,0.25)
\]

\[
(0.25,0.50,0.25)
\]

\[
(0.25,0.25,0.50).
\]

A dimensional attractor that exists only under one arbitrary weight combination should be treated cautiously.

---

# 24. Primary Measurement — Ball-Growth Dimension

For each final relational graph:

\[
N(r)\propto r^{d_H}.
\]

Estimate:

\[
d_H=
\frac{d\log N(r)}
{d\log r}.
\]

The fitting range must avoid:

- very small-radius transient behaviour;
- finite-size saturation.

---

# 25. Primary Measurement — Spectral Dimension

Using random walks:

\[
P(t)\propto t^{-d_S/2}.
\]

Estimate:

\[
d_S=
-2
\frac{d\log P(t)}
{d\log t}.
\]

---

# 26. Dimensional Agreement

Define:

\[
\Delta_d=
|d_H-d_S|.
\]

This is observational only.

Lower \(\Delta_d\) indicates agreement between independent estimators.

It must not enter the fitness function.

---

# 27. Population-Level Dimensional Metrics

At each generation measure:

### Mean dimension

\[
\bar d_g
\]

### Dimensional variance

\[
\sigma_d^2(g)
\]

### Interquartile range

\[
IQR_d(g)
\]

### Multimodality

Test whether multiple dimensional attractors exist.

### Estimator agreement

Distribution of:

\[
|d_H-d_S|.
\]

---

# 28. Definition of a Dimensional Attractor

A dimensional attractor is not defined merely by observing several values near one another.

A candidate attractor must satisfy preregistered criteria such as:

1. dimensional variance decreases across generations;

2. final distribution differs significantly from neutral controls;

3. convergence is reproducible across master seeds;

4. the result persists at larger graph sizes;

5. the result is reproduced by independent implementation.

The exact statistical threshold should be defined by the Statistics Working Group.

---

# 29. Specific Treatment of \(d\approx3\)

The experiment must not initially classify \(d=3\) as success.

If the evolved population unexpectedly converges toward:

\[
d_H\approx3
\]

and:

\[
d_S\approx3,
\]

this must be reported as an exploratory finding.

A separate confirmatory protocol should then preregister:

\[
H:
d^*=3
\]

and execute previously unused seeds and preferably independent implementations.

This prevents post-hoc targeting.

---

# 30. Finite-Size Scaling

Final candidate rules must be rerun at multiple system sizes:

\[
N=
250,\;
500,\;
1000,\;
2000,\;
4000.
\]

A dimensional attractor should not disappear as the computational system grows.

Estimate:

\[
d(N).
\]

A stronger result satisfies:

\[
d(N)
\rightarrow d_\infty.
\]

---

# 31. Cross-Seed Reproducibility

The complete evolutionary search should be repeated using multiple master seeds.

Example:

```text id="5rp88s"
Master seeds: 30
Population:   50
Generations:  30
Replicates:    3
```

The scientific result concerns the distribution across evolutionary histories, not one unusually interesting run.

---

# 32. Cross-Implementation Replication

At least one independent implementation should recreate CBR-E002 from the written specification.

Recommended architecture:

```text id="ynq34f"
Reference:
Python / CBR-Lab

Independent:
Julia, Rust, C++, or another implementation
```

Agreement should be statistical rather than necessarily bit-for-bit.

---

# 33. Blind Analysis Option

The analysis group may receive population histories labelled:

```text id="7te24s"
Population A
Population B
Population C
Population D
```

without knowing whether each belongs to:

- fitness evolution;
- neutral evolution;
- shuffled fitness;
- random search.

The analysis plan is run before labels are revealed.

---

# 34. Primary Endpoint

The primary endpoint is:

> **Whether dimension-blind evolutionary selection produces a reproducible reduction, shift or multimodal concentration in effective dimensionality relative to preregistered neutral controls.**

The endpoint does not require any specific dimension.

---

# 35. Primary Evidence Conditions

Evidence for CBR-H002 requires all of the following:

### Selection effect

Evolved populations differ materially from controls.

### Replication

The effect occurs across independent evolutionary seeds.

### Scale robustness

The effect persists under increasing graph size.

### Metric robustness

It appears in more than one dimensional estimator or otherwise has a principled explanation for estimator differences.

### Implementation robustness

An independent implementation reproduces the broad phenomenon.

---

# 36. Failure Conditions

CBR-E002 fails to support the hypothesis if:

- selected and neutral populations have indistinguishable dimensional distributions;
- dimensional convergence disappears with graph size;
- convergence depends on one master seed;
- only one estimator shows the effect;
- the effect disappears under independent implementation;
- the effect results from a trivial correlation with target degree;
- the rule family mathematically fixes the apparent dimension.

All failures must remain publishable.

---

# 37. Confounding Analysis

Several obvious confounders must be tested.

## 37.1 Mean degree

Perhaps dimensionality simply correlates with:

\[
k.
\]

Compare evolved rules with controls matched for mean degree.

---

## 37.2 Clustering

A dimensional signal may simply reflect triangle density.

Use clustering-matched controls.

---

## 37.3 Component size

Disconnected networks may artificially lower dimensional estimates.

Compare graphs with matched giant-component fractions.

---

## 37.4 Finite graph diameter

Ensure fits are not dominated by saturation.

---

## 37.5 Rule-family bias

Repeat with alternative local rule families.

---

# 38. Rule-Family Replication

CBR-E002 v1.0 uses one intentionally simple rule family.

Later versions should test whether dimensional effects survive under different computational primitives.

Examples:

### Edge rewrite family

Current CBR-Lab model.

### Node-splitting family

Rules create/remove computational entities.

### Hypergraph family

Relations can involve more than two entities.

### Cellular relational family

State values evolve on graph neighbourhoods.

A true general effect should not depend entirely on one encoding.

---

# 39. Proposed Initial Run Scale

A practical first institutional execution:

```text id="e07lbe"
30 evolutionary master seeds
×
50 population
×
30 generations
×
3 replicate simulations

=
135,000 primary simulations
```

Plus matched control runs.

This is large enough to expose systematic effects while remaining computationally manageable.

---

# 40. Experimental Output

Each individual evaluation should record:

```yaml id="i9taqe"
individual:
  generation: 12
  genome_id: "<id>"

  rule:
    target_degree: 6
    triangle_bias: 0.47
    rewire_probability: 0.026
    random_link_probability: 0.031

  fitness:
    total: 0.812
    persistence: 0.996
    complexity: 0.512
    stability: 0.942

  observational_metrics:
    hausdorff_like_dimension: 2.81
    spectral_dimension: 2.94
```

The separation between:

```text id="51arqi"
fitness
```

and:

```text id="e6yout"
observational_metrics
```

should be explicit in the data model.

---

# 41. Generation Manifest

Each generation may receive a manifest:

```yaml id="281msh"
generation:
  experiment: "CBR-E002:v1.0"
  master_seed: 71921
  generation: 17

  population_size: 50

  population_hash: "<hash>"

  selection_algorithm: "tournament"

  parent_selection_hash: "<hash>"

  output_dataset_hash: "<hash>"
```

This makes evolutionary provenance reproducible.

---

# 42. Evolutionary Lineage

A powerful addition is to preserve lineage:

\[
R_0
\rightarrow
R_1
\rightarrow
R_2
\rightarrow
\cdots.
\]

Each genome records:

- parent;
- mutations;
- crossover;
- generation;
- fitness;
- observational dimensions.

This permits later analysis of when dimensional shifts arose.

---

# 43. Evidence Graph

CBR-E002 may produce evidence relations such as:

```text id="0cal8n"
CBR-H002
   │
   ├── SUPPORTED_BY → CBR-E002
   │
   ├── CHALLENGED_BY → degree-confound analysis
   │
   ├── REPLICATED_BY → CBR-RP014
   │
   └── REFINED_BY → CBR-E002:v1.1
```

No single conclusion removes competing interpretations.

---

# 44. Relationship to CBR-E003

CBR-E002 asks whether dimensional attractors emerge.

CBR-E003 then asks:

> **If a structure exhibits effective dimension near three, does it possess local topology compatible with a 3-manifold?**

Thus:

\[
\boxed{
E001:
\text{Can dimension emerge?}
}
\]

\[
\boxed{
E002:
\text{Does evolution select dimensions?}
}
\]

\[
\boxed{
E003:
\text{Are selected 3D structures actually manifold-like?}
}
\]

This progression prevents dimensional scaling from being mistaken for topology.

---

# 45. Relationship to CBR-E004 and E005

CBR-E004 moves from graphs to explicit simplicial complexes.

CBR-E005 introduces topology-breaking perturbations and asks whether dimension- and topology-blind selection suppresses them.

The sequence becomes:

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

Each step requires a stronger emergent property.

---

# 46. Interpretation Boundaries

If CBR-E002 succeeds, the correct conclusion is:

> Selection for persistence, complexity and stability can indirectly organise effective dimensional behaviour in this computational rule family.

It is not:

> Space has been explained.

It is not:

> The universe evolved three dimensions this way.

It is not:

> CBR is proven.

Those stronger claims require additional experiments.

---

# 47. Falsification Value

CBR-E002 is useful even if it fails.

If repeated dimension-blind evolutionary searches show:

\[
P(d\mid E)
\approx
P(d\mid N),
\]

then a simple version of the claim that computational persistence naturally selects dimensionality is weakened.

That is valuable information for the CBR research programme.

The framework should adapt to evidence rather than protect the hypothesis.

---

# 48. Registered CBR-E002 YAML Summary

```yaml id="w93caf"
cbr_oen:
  protocol_version: "1.0"

experiment:
  id: "CBR-E002"
  version: "1.0"
  title: "Dimension-Blind Evolution of Relational Computational Systems"

hypothesis:
  id: "CBR-H002"

  statement: >
    Evolutionary selection based only on persistence,
    structural complexity and stability can produce
    reproducible attractors in effective dimensionality.

null_hypothesis: >
  Selected populations show no reproducible dimensional
  organisation beyond neutral search and finite-size effects.

state:
  type: "abstract relational graph"
  spatial_coordinates: false
  predefined_dimension: false

fitness:
  persistence_weight: 0.40
  complexity_weight: 0.35
  stability_weight: 0.25

  prohibited_inputs:
    - hausdorff_dimension
    - spectral_dimension
    - target_dimension
    - manifold_score
    - geometry
    - topology

evolution:
  population: 50
  generations: 30
  replicates_per_individual: 3

  selection:
    type: "tournament"
    tournament_size: 3

  elite_count: 4
  mutation_probability: 0.30

measurements:
  primary:
    - ball_growth_dimension
    - spectral_dimension

  secondary:
    - dimensional_variance
    - estimator_agreement
    - finite_size_scaling

controls:
  - random_rule_search
  - neutral_evolution
  - shuffled_fitness
  - fitness_ablation
  - degree_matched_controls

primary_endpoint: >
  Determine whether dimension-blind selection causes a
  reproducible concentration or shift in dimensional
  distributions relative to neutral controls.

specific_dimension_target:
  enabled: false

negative_results:
  retained: true

independent_replication:
  required_for_r3: true
```

---

# 49. Founding Criterion

The scientifically interesting result is not:

\[
\text{we searched until something looked 3D}.
\]

It is:

\[
\boxed{
\begin{aligned}
&\text{dimension never enters fitness}\\
&\qquad\downarrow\\
&\text{selection improves persistence/complexity/stability}\\
&\qquad\downarrow\\
&\text{dimensional distribution changes reproducibly}\\
&\qquad\downarrow\\
&\text{independent controls fail to explain the shift}.
\end{aligned}
}
\]

Only then is it reasonable to investigate whether a particular dimensional value has deeper significance.

---

# 50. Final Experimental Principle

CBR-E002 embodies a broader methodological principle for CBR:

> **Do not ask the computational system to produce the physical property we hope to explain. Ask it to satisfy more primitive computational constraints, then measure what physical structure appears without being requested.**

If dimensionality emerges under those conditions, it becomes an observation requiring explanation rather than an assumption built into the model.

That distinction is the scientific purpose of CBR-E002.