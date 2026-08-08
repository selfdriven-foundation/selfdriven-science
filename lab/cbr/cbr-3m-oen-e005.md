# CBR-OEN Experiment CBR-E005
## Dimension- and Topology-Blind Selection Under Manifold-Breaking Defects
### Preregistered Experimental Specification — Draft v1.0

---

## 1. Experiment Identity

**Experiment ID:** CBR-E005  
**Version:** 1.0  
**Title:** Dimension- and Topology-Blind Selection Under Manifold-Breaking Defects  
**Protocol:** CBR-OEN Experimental Protocol v1.0  
**Experiment class:** Confirmatory evolutionary computational-topology experiment  
**Predecessor:** CBR-E004 — Explicit Simplicial Dynamics and 3-Manifold Stability

---

# 2. Scientific Question

CBR-E005 asks:

> **When explicit simplicial computational systems are permitted to damage manifold topology, does selection based only on persistence, structural complexity and dynamical stability favour computational rules that suppress those topology-destroying defects?**

This is substantially stronger than CBR-E004.

In E004, valid Pachner moves preserve manifold topology by construction.

In E005, that protection is removed.

The computational system is permitted to enter non-manifold states.

The key question becomes:

\[
\text{Does manifold integrity remain computationally advantageous}
\]

even when:

\[
\text{manifoldness is never included in fitness?}
\]

---

# 3. Core Hypothesis

### CBR-H005

In explicit simplicial computational systems exposed to topology-destroying perturbations, selection for persistence, structural complexity and dynamical stability will indirectly favour rule populations with reduced rates of manifold-breaking defects and/or increased restoration of manifold structure.

Formally, let the genome contain a defect parameter:

\[
p_D.
\]

Fitness remains:

\[
F=
f(P,C,S)
\]

with no topological contribution.

The hypothesis predicts that evolutionary selection may nevertheless produce:

\[
p_D^{(g+1)}
<
p_D^{(g)}
\]

or otherwise produce increased topological integrity over generations.

---

# 4. Null Hypothesis

The null hypothesis is:

> Selection for persistence, complexity and stability has no systematic tendency to suppress topology-destroying defects or increase manifold integrity beyond neutral evolutionary controls.

Under the null:

\[
P(p_D\mid\text{selected})
\]

should not differ materially from:

\[
P(p_D\mid\text{neutral}).
\]

Likewise, manifold quality should not improve except through accidental correlations.

---

# 5. Stronger Interpretation

If CBR-H005 is supported, the appropriate conclusion would be:

> **Manifold-preserving computational dynamics can be indirectly selected because of more primitive computational properties, without manifold topology itself appearing in the objective function.**

This would not establish that physical space arose this way.

But it would provide evidence for a more general proposition:

\[
\boxed{
\text{stable manifold structure may be computationally favourable}
}
\]

rather than merely mathematically imposed.

---

# 6. Experimental State

The computational state is an explicit simplicial complex:

\[
K_t=(V_t,E_t,F_t,T_t).
\]

The primary maximal simplices are tetrahedra:

\[
T_i=[v_a,v_b,v_c,v_d].
\]

No spatial coordinates exist.

There is no predefined metric.

There is no embedding in:

\[
\mathbb{R}^3.
\]

The dynamics operate entirely through combinatorial relationships.

---

# 7. Initial State

The baseline E005 experiment begins with a verified triangulation of:

\[
S^3.
\]

The preferred control seed is the boundary of a 4-simplex.

Initially:

\[
M_L=1,
\]

\[
F_C=1,
\]

and:

\[
(\beta_0,\beta_1,\beta_2,\beta_3)
=
(1,0,0,1).
\]

Thus the system begins in a known closed 3-manifold state.

---

# 8. Allowed Move Classes

CBR-E005 introduces two categories of local computational transition.

## 8.1 Manifold-Preserving Moves

Valid 3-dimensional Pachner moves:

\[
1\leftrightarrow4
\]

and:

\[
2\leftrightarrow3.
\]

These preserve the PL topology of the manifold when validly applied.

---

## 8.2 Defect-Producing Moves

A separate class of topology-agnostic transitions is introduced.

Examples include:

- arbitrary tetrahedron addition;
- arbitrary tetrahedron removal;
- invalid simplex reconnection;
- duplicate-face attachment;
- local incidence violation;
- non-Pachner simplex replacement.

These moves do not receive information about whether they damage the manifold.

They are simply alternative computational transitions.

---

# 9. Defect Probability

Each genome includes:

\[
p_D
\]

representing the probability that a computational step attempts a topology-agnostic defect move instead of a Pachner move.

Thus:

\[
p_D\in[0,p_{D,\max}].
\]

A proposed baseline range is:

\[
p_D\in[0,0.20].
\]

The precise range must be preregistered.

---

# 10. Simplicial Genome

The initial E005 genome is:

\[
R=
(
w_{14},
w_{41},
w_{23},
w_{32},
p_D
).
\]

The Pachner weights satisfy:

\[
w_{14}+w_{41}+w_{23}+w_{32}=1.
\]

The genome therefore controls:

- local refinement;
- local coarse-graining;
- local retriangulation;
- defect exposure.

It does not contain a manifold score.

---

# 11. Fitness Function

The preregistered fitness remains:

\[
\boxed{
F=
0.40P+
0.35C+
0.25S
}
\]

where:

- \(P\) = computational persistence;
- \(C\) = structural complexity;
- \(S\) = dynamical stability.

Topology does not contribute.

---

# 12. Forbidden Fitness Inputs

The evolutionary algorithm must never receive:

```text
defect probability outcome
manifold score
S² vertex-link fraction
face incidence validity
Euler characteristic
Betti numbers
homology
topology class
dimension
spectral dimension
Hausdorff dimension
distance from d=3
```

Even though \(p_D\) is encoded in the genome, its value must not be directly rewarded or penalised.

Selection sees only the resulting computational fitness.

---

# 13. Persistence

Persistence measures whether the computational complex remains structurally coherent through time.

Potential components include:

### Tetrahedral connectivity

Let \(G_T\) be the tetrahedral adjacency graph.

Then:

\[
P_T=
\frac{
|T_{\mathrm{giant}}|
}{
|T|
}.
\]

### Temporal persistence

Measure connectivity at several late checkpoints:

\[
P=
\frac{1}{n}
\sum_iP_T(t_i).
\]

No manifold test appears.

---

# 14. Complexity

Complexity must remain topology-blind.

Candidate components include:

- vertex-incidence entropy;
- face-incidence entropy;
- tetrahedral adjacency diversity;
- local configuration diversity;
- transition entropy.

For example:

\[
C=
G_T
\left(
\alpha H_V+
\beta H_F
\right)
\]

where \(H_V\) and \(H_F\) are normalised incidence entropies.

---

# 15. Stability

Stability measures whether macroscopic statistics remain relatively stable over time.

Possible state vector:

\[
X_t=
(
G_T,
H_V,
H_F,
N_T,
N_V
).
\]

Then:

\[
S=
1-
\frac{1}{m}
\sum_j
\Delta_j(X_{t_1},X_{t_2}).
\]

Again, topology is not included.

---

# 16. Evolutionary Population

Proposed baseline:

```text
Population:             50
Generations:            30
Replicates/genome:       3
Elite individuals:       4
Tournament size:         3
Mutation probability: 0.30
```

These values should be frozen before confirmatory execution.

---

# 17. Mutation

Mutation may modify:

\[
w_{14},
w_{41},
w_{23},
w_{32},
p_D.
\]

For example:

\[
p_D'
=
\operatorname{clip}
(
p_D+\epsilon,
0,
p_{D,\max}
).
\]

No mutation direction is preferred.

---

# 18. Primary Evolutionary Prediction

The simplest E005 prediction is:

\[
\boxed{
E[p_D(g)]
\downarrow
}
\]

as generation \(g\) increases.

However, this is not the only possible positive result.

A system might tolerate high defect rates while evolving dynamics that repair damage.

Therefore E005 must also measure realised manifold integrity.

---

# 19. Topological Measurements

After fitness has been calculated, independently measure:

### Closed-face fraction

\[
F_C=
\frac{
|\{f:I_T(f)=2\}|
}{
|F|
}.
\]

### Local manifold score

\[
M_L=
\frac{
|\{v:\operatorname{Lk}(v)\cong S^2\}|
}{
|V_{\mathrm{eligible}}|
}.
\]

### Global homology

Where practical:

\[
(\beta_0,\beta_1,\beta_2,\beta_3).
\]

### Euler characteristic

\[
\chi=
N_0-N_1+N_2-N_3.
\]

### Singular fraction

\[
\rho_S=1-M_L.
\]

None influences reproduction.

---

# 20. Defect Rate Versus Defect Damage

CBR-E005 must distinguish:

\[
p_D
\]

from actual damage.

A high defect probability may not always produce severe topological disruption.

Therefore record both:

\[
p_D
\]

and:

\[
D_{\mathrm{observed}}.
\]

A possible observed defect measure is:

\[
D_{\mathrm{observed}}
=
1-M_L.
\]

Another is:

\[
1-F_C.
\]

---

# 21. Repair

A particularly interesting phenomenon would be spontaneous repair.

Define a manifold-defect event at time \(t\):

\[
M_L(t)<1.
\]

If subsequent dynamics return to:

\[
M_L(t+k)=1,
\]

without topology being explicitly optimised, this is a repair event.

Define repair probability:

\[
P_R=
P(
M_L(t+k)=1
\mid
M_L(t)<1
).
\]

---

# 22. Recovery Time

For a defect introduced at time \(t_D\), define:

\[
\tau_R=
t_R-t_D
\]

where \(t_R\) is the first step at which the preregistered manifold condition is restored.

The distribution:

\[
P(\tau_R)
\]

becomes an important secondary observable.

---

# 23. Persistent Defects

Some defects may never repair.

Define:

\[
P_{\mathrm{persistent}}
=
P(
\text{defect survives until experiment termination}
).
\]

Evolution may reduce this probability even if \(p_D\) itself does not fall.

This distinction allows selection for **fault tolerance** rather than merely defect avoidance.

---

# 24. Three Possible Evolutionary Strategies

CBR-E005 may discover at least three broad strategies.

### Strategy A — Avoidance

\[
p_D\rightarrow0.
\]

The system evolves to reduce defect-generating moves.

### Strategy B — Robustness

\[
p_D>0
\]

but defects have little impact on persistence and structure.

### Strategy C — Repair

Defects occur but are dynamically corrected.

This suggests:

\[
\text{stable topology}
\]

may arise through more than one computational mechanism.

---

# 25. Primary Endpoint

The primary endpoint is:

> **Whether dimension- and topology-blind selection produces a statistically reproducible improvement in manifold integrity relative to neutral evolutionary controls.**

This may manifest through:

- reduced \(p_D\);
- increased \(M_L\);
- increased \(F_C\);
- increased repair probability;
- reduced defect persistence.

---

# 26. Strongest Primary Metric

A useful preregistered primary metric is:

\[
\Delta M=
M_L^{\mathrm{selected}}
-
M_L^{\mathrm{neutral}}.
\]

The primary comparison becomes:

\[
\Delta M>0.
\]

A parallel analysis measures:

\[
\Delta p_D=
p_D^{\mathrm{selected}}
-
p_D^{\mathrm{neutral}}.
\]

---

# 27. Control A — Neutral Evolution

Run identical mutation, crossover and population dynamics but select parents randomly.

This produces:

\[
P(p_D\mid\text{neutral})
\]

and:

\[
P(M_L\mid\text{neutral}).
\]

---

# 28. Control B — Random Search

Sample genomes independently without generational selection.

This tests whether successful low-defect rules simply occupy a large region of parameter space.

---

# 29. Control C — Shuffled Fitness

Calculate fitness normally, then randomly assign fitness values to genomes before selection.

This preserves the fitness distribution but destroys genotype-fitness correspondence.

---

# 30. Control D — Fixed Defect Probability

Hold:

\[
p_D
\]

constant across evolution while allowing Pachner weights to evolve.

This asks whether rule dynamics can evolve **robustness or repair** without reducing defect exposure.

---

# 31. Control E — Fixed Pachner Weights

Allow only:

\[
p_D
\]

to evolve.

This isolates pure defect avoidance.

---

# 32. Control F — Defect-Type Ablation

Run separate experiments for:

- tetrahedron addition only;
- tetrahedron removal only;
- face-incidence corruption;
- arbitrary reconnection.

A general manifold-stability effect should not depend entirely on one defect implementation.

---

# 33. Control G — Fitness Ablation

Run:

\[
F=P,
\]

\[
F=C,
\]

and:

\[
F=S.
\]

This identifies which computational property, if any, creates indirect pressure toward manifold integrity.

---

# 34. Key Confounder: Size

Defects may simply reduce or increase simplex count, indirectly affecting fitness.

Therefore selected and control complexes should also be compared under matched:

- tetrahedron counts;
- vertex counts;
- average incidence.

A manifold advantage must not merely be a size advantage.

---

# 35. Key Confounder: Connectivity

Non-manifold complexes may fragment.

If fitness directly rewards giant-component size, the evolutionary pressure could simply be:

\[
\text{connected}
>
\text{disconnected}.
\]

This is still computationally meaningful, but it must not be misrepresented as a specific manifold preference.

Therefore analyse topology among controls matched for connectivity.

---

# 36. Key Confounder: Move Validity

Some defect moves may cause immediate catastrophic failure.

If so, selection against them is trivial.

The defect family should therefore include perturbations spanning:

- mild;
- moderate;
- severe

topological consequences.

This tests whether manifold integrity matters beyond avoiding obviously destructive operations.

---

# 37. Defect Severity

Each defect event may be classified retrospectively using an observational severity measure:

\[
D_s.
\]

For example:

\[
D_s
=
\alpha(1-F_C)
+
\beta(1-M_L)
+
\gamma\Delta H.
\]

This measure must not influence fitness.

---

# 38. Evolution of Defect Tolerance

For each generation calculate:

\[
\bar p_D(g),
\]

\[
\bar M_L(g),
\]

\[
\bar F_C(g),
\]

\[
\bar P_R(g),
\]

\[
\bar\tau_R(g).
\]

This creates an evolutionary trajectory of topology without making topology part of selection.

---

# 39. Correlation Analysis

After the experiment, analyse:

\[
\operatorname{corr}(F,M_L),
\]

\[
\operatorname{corr}(F,F_C),
\]

\[
\operatorname{corr}(F,p_D),
\]

\[
\operatorname{corr}(P,M_L),
\]

\[
\operatorname{corr}(C,M_L),
\]

\[
\operatorname{corr}(S,M_L).
\]

This may reveal why manifold-like structures perform differently.

---

# 40. Mediation Analysis

A stronger statistical analysis can test whether:

\[
p_D
\rightarrow
M_L
\rightarrow
F
\]

better explains evolution than:

\[
p_D
\rightarrow
F
\]

directly.

This matters because the theoretical proposition concerns manifold integrity, not merely mutation rate.

---

# 41. Dimension Remains Observational

As in previous experiments, measure:

\[
d_H
\]

and:

\[
d_S
\]

on the tetrahedral dual graph.

These remain prohibited fitness variables.

This allows investigation of whether topology preservation and dimensional behaviour become correlated.

---

# 42. Possible Topology–Dimension Relationship

One exploratory possibility is:

\[
M_L\uparrow
\quad\Rightarrow\quad
|d_H-d_S|\downarrow.
\]

Another is that manifold degradation causes unstable or anomalous spectral dimension.

No relationship should be assumed in advance.

---

# 43. Cross-Seed Replication

The entire evolutionary process should run across many master seeds.

Proposed baseline:

```text
Master seeds:          30
Population:            50
Generations:           30
Replicates/genome:      3
```

This produces:

\[
135,000
\]

primary individual simulations before controls.

---

# 44. Confirmation Population

If exploratory experiments reveal strong:

\[
p_D\rightarrow0
\]

or:

\[
M_L\rightarrow1,
\]

the exact phenomenon must be tested on previously unused confirmation seeds.

Exploratory seeds cannot serve as independent confirmation.

---

# 45. Independent Implementation

At least one independent implementation should reproduce the experiment.

Recommended arrangement:

```text
Implementation A
Python / CBR-Lab

Implementation B
Julia / Rust / C++

Topology verifier
Independent mathematical package or codebase
```

The strongest design separates:

- evolutionary simulation;
- topology verification;
- statistical analysis.

---

# 46. Blinded Analysis

An analysis group may receive evolutionary histories with conditions hidden.

For example:

```text
SET-A
SET-B
SET-C
SET-D
```

may correspond to:

- selected evolution;
- neutral evolution;
- shuffled fitness;
- random search.

The group computes preregistered endpoints before unblinding.

---

# 47. Replication Requirement

A strong CBR-E005 claim should require R3 status:

### R1

Reference implementation reproducible.

### R2

Independent implementation reproduces the phenomenon.

### R3

Independent institution reproduces the phenomenon.

---

# 48. Candidate Positive Result

Suppose the initial population has:

\[
\bar p_D=0.10.
\]

After evolution:

\[
\bar p_D=0.012
\]

while neutral evolution remains near:

\[
0.10.
\]

If topology was not measured by fitness and this repeats independently, the result is noteworthy.

However, the analysis must still determine whether selection was for manifold integrity or merely against catastrophic mutation.

---

# 49. More Interesting Positive Result

A stronger result would be:

\[
p_D^{\mathrm{selected}}
\approx
p_D^{\mathrm{neutral}},
\]

but:

\[
M_L^{\mathrm{selected}}
\gg
M_L^{\mathrm{neutral}}.
\]

This would imply the evolved rules did not avoid defects.

They became **more resilient to them**.

That would be scientifically more interesting than simple defect suppression.

---

# 50. Strongest Result: Self-Repair

A still stronger result would show:

\[
p_D>0,
\]

persistent defect generation,

but:

\[
P_R\rightarrow1
\]

and:

\[
\tau_R\rightarrow\text{small}.
\]

This would indicate emergent topology-maintenance dynamics.

Conceptually:

\[
\boxed{
\text{computation}
\rightarrow
\text{damage}
\rightarrow
\text{self-restoration}
}
\]

without a manifold repair objective.

---

# 51. Negative Result

An important negative outcome would be:

\[
M_L^{\mathrm{selected}}
\approx
M_L^{\mathrm{neutral}}.
\]

This would weaken the claim that manifold topology is naturally favoured by the chosen computational fitness.

Another valuable negative result would be:

\[
p_D\rightarrow0
\]

only because every defect destroys connectivity.

This would show that the result is trivial rather than specifically topological.

---

# 52. Another Important Negative Result

Selection might actually favour non-manifold configurations.

For example:

\[
M_L\downarrow
\]

while:

\[
F\uparrow.
\]

This would be especially significant.

It would imply that the selected computational properties do not naturally favour manifold organisation under the tested model.

CBR-OEN must publish such a result prominently.

---

# 53. Manifold Integrity as an Emergent Variable

If E005 succeeds, manifoldness becomes a derived property:

\[
M_L=
g(R,\text{history},\text{environment})
\]

rather than an objective.

The key conceptual relationship is:

\[
F(P,C,S)
\]

with:

\[
\frac{\partial F}{\partial M_L}
\]

never explicitly supplied to the evolutionary process.

Yet:

\[
M_L
\]

may systematically increase.

---

# 54. Robustness Across Fitness Definitions

The result should be repeated with multiple reasonable definitions of:

- persistence;
- complexity;
- stability.

If manifold preservation occurs only under one carefully tuned fitness definition, it should not be considered a robust CBR result.

The stronger proposition is:

> manifold-like organisation emerges across a family of computational viability criteria.

---

# 55. Robustness Across Defect Models

Likewise, repeat with several defect families.

A general effect should survive different mechanisms of topological damage.

This avoids accidentally discovering:

> Rule X happens to undo Mutation Y.

The desired phenomenon is more general.

---

# 56. Environmental Defects

A later extension could separate genomic defect probability from externally imposed perturbations.

Instead of evolving:

\[
p_D,
\]

apply a fixed external defect rate:

\[
p_E.
\]

Then ask whether rule systems evolve robustness.

This creates:

\[
\text{environmental damage}
+
\text{topology-blind evolution}.
\]

This may provide an even cleaner self-repair experiment.

---

# 57. E005-A — Endogenous Defects

The baseline experiment:

> Defect probability is encoded in the genome and can evolve.

Question:

\[
p_D\rightarrow?
\]

---

# 58. E005-B — Exogenous Defects

A stronger follow-up:

> Every system experiences the same externally imposed defect rate.

Thus:

\[
p_E=\text{constant}.
\]

The genome cannot escape damage by lowering exposure.

It can only evolve:

- robustness;
- repair;
- resilience.

This may ultimately be the most informative version of E005.

---

# 59. E005-C — Mixed Defects

Combine:

\[
p_D
\]

and:

\[
p_E.
\]

This distinguishes evolutionary avoidance from environmental resilience.

---

# 60. Suggested Experimental Sequence

The recommended order is:

\[
\boxed{
E005-A:
\text{Can selection suppress endogenous defects?}
}
\]

then:

\[
\boxed{
E005-B:
\text{Can selection evolve resilience to unavoidable defects?}
}
\]

then:

\[
\boxed{
E005-C:
\text{How do avoidance and repair interact?}
}
\]

---

# 61. Topological Memory

An interesting secondary question is whether a damaged system appears to retain computational information about its previous manifold state.

For example, after a perturbation:

\[
K_t\not\cong M
\]

but local dynamics may preferentially return toward:

\[
K_{t+k}\cong M.
\]

This could be described operationally as **topological memory**.

The term should remain descriptive unless a precise mathematical definition is established.

---

# 62. Attractor Interpretation

If independently evolved systems repeatedly return to manifold-like states after defects, a candidate interpretation is that the manifold region forms an attractor in computational state space.

Let:

\[
\mathcal{S}
\]

be the space of possible simplicial configurations.

Let:

\[
\mathcal{M}\subset\mathcal{S}
\]

be configurations satisfying manifold criteria.

A strong E005 result may suggest:

\[
P(
K_{t+k}\in\mathcal{M}
\mid
K_t\notin\mathcal{M}
)
\]

is enhanced under selected dynamics.

---

# 63. Basin of Attraction

The next mathematical question would be the size of the basin:

\[
B(\mathcal{M}).
\]

How much damage can occur while the system still returns to manifold organisation?

This could lead to a measurable topology-recovery threshold.

---

# 64. Critical Defect Rate

There may exist:

\[
p_c
\]

such that:

\[
p_D<p_c
\]

permits stable manifold organisation, while:

\[
p_D>p_c
\]

causes persistent topological failure.

This suggests a possible computational phase transition.

---

# 65. Phase Diagram

A later experiment could map:

\[
(p_D,\;R)
\]

against:

\[
M_L.
\]

Potential regimes might include:

```text
MANIFOLD-STABLE
REPAIR-DOMINATED
INTERMITTENT
DEFECT-DOMINATED
FRAGMENTED
```

Such a phase diagram would be valuable independently of CBR interpretation.

---

# 66. Information-Theoretic Analysis

A further secondary analysis could ask whether manifold-preserving states have different information properties.

Examples:

- lower transition entropy;
- higher predictive information;
- greater mutual information across time;
- improved persistence of local patterns.

These could eventually help explain why selection favours particular topologies.

---

# 67. Computational Cost

Measure the computational resources associated with maintaining different regimes:

\[
C_{\mathrm{compute}}.
\]

It is possible that manifold-like configurations support more efficient propagation or stabilisation.

This should be measured rather than assumed.

---

# 68. Relationship to CBR's Broader Claim

CBR proposes that physical organisation may emerge from deeper computational constraints.

E005 tests a concrete version:

\[
\text{computational viability}
\rightarrow
\text{topological organisation}.
\]

If this fails, the hypothesis must be revised.

If it succeeds robustly, the next question becomes:

> Does the resulting manifold support an emergent metric with physically meaningful dynamics?

This leads toward CBR-E006.

---

# 69. Relationship to E006

E005 concerns:

\[
\text{topological stability}.
\]

CBR-E006 should concern:

\[
\text{emergent metric}.
\]

Once manifold organisation exists without being hard-coded, assign no Euclidean coordinates but derive effective distance from relational transition cost.

Then test whether:

\[
d(A,B)
\]

behaves like a stable metric.

---

# 70. CBR-E005 YAML Summary

```yaml
cbr_oen:
  protocol_version: "1.0"

experiment:
  id: "CBR-E005"
  version: "1.0"

  title:
    "Dimension- and Topology-Blind Selection Under Manifold-Breaking Defects"

hypothesis:
  id: "CBR-H005"

  statement: >
    Selection for computational persistence, structural
    complexity and dynamical stability will indirectly
    favour increased manifold integrity when topology
    destroying transitions are allowed.

null_hypothesis: >
  Topology-blind selection produces no reproducible increase
  in manifold integrity relative to neutral controls.

state:
  type: "explicit_simplicial_complex"

  spatial_coordinates:
    enabled: false

dynamics:
  pachner_moves:
    - "1-4"
    - "4-1"
    - "2-3"
    - "3-2"

  defect_moves:
    enabled: true

genome:
  parameters:
    - w14
    - w41
    - w23
    - w32
    - defect_probability

fitness:
  persistence_weight: 0.40
  complexity_weight: 0.35
  stability_weight: 0.25

  prohibited_inputs:
    - manifold_score
    - closed_face_fraction
    - homology
    - euler_characteristic
    - dimension
    - spectral_dimension
    - defect_damage

measurements:
  observational_only:
    - defect_probability
    - closed_face_fraction
    - s2_link_fraction
    - singular_fraction
    - global_homology
    - repair_probability
    - recovery_time
    - ball_growth_dimension
    - spectral_dimension

controls:
  - neutral_evolution
  - random_search
  - shuffled_fitness
  - fixed_defect_rate
  - fixed_pachner_weights
  - defect_type_ablation
  - fitness_ablation
  - connectivity_matched_controls
  - size_matched_controls

primary_endpoint: >
  Determine whether topology-blind evolutionary selection
  increases manifold integrity relative to neutral controls.

tracks:

  E005_A:
    defect_type: "endogenous"
    question: >
      Does selection suppress evolvable defect probability?

  E005_B:
    defect_type: "exogenous"
    question: >
      Does selection evolve resilience or repair when
      defect exposure cannot be reduced?

  E005_C:
    defect_type: "mixed"
    question: >
      How do avoidance, robustness and repair interact?

replication:
  independent_implementation_required_for_r2: true
  institutional_replication_required_for_r3: true

negative_results:
  retained: true
```

---

# 71. Experimental Progression

With E005, the experimental sequence becomes:

\[
\boxed{
E001:
\text{Can dimension emerge?}
}
\]

\[
\downarrow
\]

\[
\boxed{
E002:
\text{Does dimension-blind selection organise dimensionality?}
}
\]

\[
\downarrow
\]

\[
\boxed{
E003:
\text{Does 3D scaling correspond to manifold topology?}
}
\]

\[
\downarrow
\]

\[
\boxed{
E004:
\text{Can explicit manifold topology support local computation?}
}
\]

\[
\downarrow
\]

\[
\boxed{
E005:
\text{Does topology-blind selection favour manifold stability?}
}
\]

The important methodological change at E005 is:

> **The system is now allowed to be wrong.**

Manifold integrity is no longer guaranteed.

That makes its persistence experimentally meaningful.

---

# 72. Strong CBR-E005 Result

The most significant possible outcome is not simply:

\[
p_D\rightarrow0.
\]

It would be:

\[
\boxed{
p_D>0
}
\]

while:

\[
\boxed{
M_L\rightarrow1
}
\]

and:

\[
\boxed{
P_R\rightarrow1.
}
\]

In words:

> **The computational system continues to experience topology-breaking perturbations, yet evolves local dynamics that repeatedly restore manifold structure, despite manifold structure never appearing in its objective function.**

That would suggest that manifold topology behaves as a **computational attractor associated with viability rather than an imposed geometric assumption**.

It would be a substantially stronger result than simply constructing a 3-manifold.

---

# 73. Interpretation Boundary

Even the strongest E005 result would not establish that our physical universe arose through this mechanism.

It would establish something narrower:

> In at least one sufficiently general class of computational systems, 3-manifold integrity can emerge as an indirect consequence of selection for non-geometric computational properties.

Only subsequent experiments could determine whether such structures also support:

- stable metrics;
- causal propagation;
- curvature;
- matter-like structures;
- gravitational dynamics.

---

# 74. Final Principle

CBR-E005 embodies perhaps the most important methodological principle in the programme so far:

> **A physical property becomes significantly more interesting when the computational system is permitted to lose it, is never rewarded for possessing it, and nevertheless evolves to preserve or restore it.**

The experimental signature is therefore:

\[
\boxed{
\begin{aligned}
&\text{topology-breaking transitions permitted}\\
&\qquad\downarrow\\
&\text{topology absent from fitness}\\
&\qquad\downarrow\\
&\text{selection acts on persistence, complexity and stability}\\
&\qquad\downarrow\\
&\text{manifold integrity increases}\\
&\qquad\downarrow\\
&\text{defects are avoided, tolerated or repaired}.
\end{aligned}
}
\]

If that pattern survives controls, scale tests, independent implementations and institutional replication, then the CBR programme has moved beyond demonstrating that computation **can represent** a manifold.

It has begun testing whether computation can have a reason to **become and remain manifold-like**.