# CBR-OEN Experiment CBR-E008
## Emergent Geodesic Motion in a Computationally Distorted Metric
### Preregistered Experimental Specification — Draft v1.0

---

## 1. Experiment Identity

**Experiment ID:** CBR-E008  
**Version:** 1.0  
**Title:** Emergent Geodesic Motion in a Computationally Distorted Metric  
**Protocol:** CBR-OEN Experimental Protocol v1.0  
**Experiment class:** Confirmatory computational-dynamics experiment  
**Predecessor:** CBR-E007 — Persistent Computational Structures and Emergent Metric Distortion

---

# 2. Scientific Question

CBR-E008 asks:

> **When one persistent computational structure generates an emergent metric distortion, will a second freely evolving persistent structure follow trajectories correlated with minimum-cost geodesics in that metric, even though no attractive force or target motion is explicitly encoded?**

The intended causal chain is:

\[
\boxed{
P_1
\rightarrow
\Delta C
\rightarrow
\Delta d
\rightarrow
\gamma^*
\rightarrow
\text{motion of }P_2
}
\]

where:

- \(P_1\) = persistent source structure;
- \(\Delta C\) = computational cost redistribution;
- \(\Delta d\) = emergent metric distortion;
- \(\gamma^*\) = minimum-cost geodesic;
- \(P_2\) = freely evolving probe structure.

The crucial condition is:

> **No rule may instruct \(P_2\) to move toward \(P_1\).**

---

# 3. Core Hypothesis

### CBR-H008

A freely evolving persistent computational structure embedded within an endogenously distorted computational metric will exhibit statistically reproducible motion correlated with the geodesic structure of that metric.

Let:

\[
d_P
\]

be the metric generated in the presence of source structure \(P_1\).

Let the actual probe trajectory be:

\[
\Gamma_{P_2}.
\]

Let:

\[
\gamma^*
\]

represent the relevant minimum-cost trajectory predicted from \(d_P\).

The hypothesis predicts:

\[
\Gamma_{P_2}
\approx
\gamma^*
\]

to a degree significantly greater than matched controls.

---

# 4. Null Hypothesis

The null hypothesis is:

> Probe motion is unrelated to the emergent metric distortion and can be explained by unbiased local dynamics, graph topology, random drift, activity gradients, implementation artefacts or direct source–probe coupling.

Thus:

\[
\Gamma_{P_2}
\]

should show no greater alignment with metric geodesics than suitably matched controls.

---

# 5. Why E008 Is Different

E007 establishes only:

\[
\text{structure}
\rightarrow
\text{metric distortion}.
\]

That does not establish gravitationally analogous behaviour.

E008 adds a second requirement:

\[
\text{metric distortion}
\rightarrow
\text{motion}.
\]

This distinction is critical.

A computational structure may distort metric geometry without other structures responding to that distortion in any physically meaningful way.

---

# 6. No Force Law

The probe structure must not receive:

```text
source location
distance to source
direction to source
gravitational force
potential
acceleration toward source
inverse-square term
curvature gradient
target geodesic
```

The only information available to its dynamics is local computational state.

---

# 7. No Direct Source–Probe Attraction

The update rules must contain no term of the form:

\[
P_1\rightarrow P_2.
\]

For example, prohibited logic includes:

```text
if source is nearby:
    move toward source
```

or:

```text
probability_of_move ∝ 1 / distance_to_source
```

Such rules would invalidate the experiment.

---

# 8. Substrate

The preferred E008 substrate is:

\[
(K_t,C_t)
\]

validated through E006 and E007.

Requirements:

- manifold topology remains stable;
- computational metric remains measurable;
- source structure creates reproducible metric distortion;
- spatial coordinates remain absent.

---

# 9. Source Structure

Define a persistent source:

\[
P_S.
\]

During E008-A, \(P_S\) remains approximately stationary in relational terms.

Its role is to maintain the metric distortion already validated in E007.

The source does not emit an explicit attractive signal.

---

# 10. Probe Structure

Define a second persistent pattern:

\[
P_T
\]

for “test” or “probe” structure.

The probe must:

- preserve identity;
- be capable of relational displacement;
- have local update dynamics;
- receive no source position.

Its motion is generated entirely through local computational transitions.

---

# 11. Relational Motion

No coordinates are required.

Let:

\[
S(P_T,t)
\]

be the support of the probe at time \(t\).

Define displacement by change in relational centre or matched pattern support:

\[
\Delta x_C
=
d_C(
P_T(t),
P_T(t+\Delta t)
).
\]

Here \(x_C\) is conceptual notation only; no Cartesian coordinate exists.

---

# 12. Probe Mobility Rule

A baseline mobile pattern should have multiple locally valid continuation states.

For example:

\[
P_T(t)
\rightarrow
\{
P_T^{(1)},
P_T^{(2)},\ldots,P_T^{(k)}
\}.
\]

Selection among these continuations may depend upon local computational feasibility or cost, but not source identity.

---

# 13. Minimal Local Rule

A simple candidate rule is:

> Among locally valid pattern-preserving transitions, lower computational-cost transitions occur with greater probability.

For candidate transition \(i\):

\[
p_i
=
\frac{
e^{-\beta \Delta C_i}
}{
\sum_j e^{-\beta \Delta C_j}
}.
\]

This is a local cost-sensitive rule.

It does not know where the source is.

---

# 14. Important Control

The cost-sensitive mobility rule itself may produce geodesic motion in any cost field.

Therefore E008 must compare:

\[
\text{source-generated cost field}
\]

against:

\[
\text{matched shuffled/random cost fields}.
\]

The experiment concerns whether the **endogenous E007 metric distortion** produces systematic motion.

---

# 15. Zero-Bias Probe

A second important track should use maximally neutral mobility.

For example:

> Choose uniformly among all valid local pattern-preserving transitions.

This asks whether the substrate dynamics themselves bias the probe without explicit cost preference.

Call this:

\[
\text{E008-A0}.
\]

---

# 16. Cost-Sensitive Probe

A second track uses locally cost-sensitive transition probability.

Call this:

\[
\text{E008-A1}.
\]

Comparing A0 and A1 helps distinguish:

- motion arising automatically from substrate dynamics;
- motion requiring local optimisation of computational accessibility.

---

# 17. E008-A — Single Source, Single Probe

Initial experiment:

```text
one stationary source
one mobile probe
stable manifold
stable endogenous metric
```

Question:

> Does the probe trajectory systematically align with source-distorted geodesics?

---

# 18. Initial Conditions

For every source–probe separation class, generate multiple initial probe placements.

No placement may be selected because it happens to produce desirable motion.

Preregister:

- separation distribution;
- orientation distribution;
- initial local state;
- random seeds.

---

# 19. Baseline Metric

Before inserting the source, calculate:

\[
d_0.
\]

After source equilibration:

\[
d_S.
\]

The probe should then be introduced.

This separates source field formation from probe movement.

---

# 20. Source-Induced Metric Difference

Define:

\[
\Delta d_S(A,B)
=
d_S(A,B)-d_0(A,B).
\]

E008 should only run confirmatory motion tests in conditions where E007 independently demonstrated statistically significant distortion.

This prevents testing motion in a nonexistent field.

---

# 21. Geodesic Prediction

Before running the probe trajectory, calculate the preregistered geodesic prediction:

\[
\gamma^*.
\]

This prediction must be frozen before the trajectory is observed.

If several geodesics are equivalent, the admissible geodesic set must be recorded.

---

# 22. No Post-Hoc Path Selection

After observing probe motion, researchers may not search for whichever geodesic best resembles it and call that confirmation.

The prediction procedure must be fixed beforehand.

This is essential.

---

# 23. Trajectory Alignment

Define geodesic alignment:

\[
A_\gamma.
\]

One possible metric is average distance between the observed probe path and the preregistered geodesic set.

For probe state \(p_t\):

\[
D_\gamma
=
\frac{1}{T}
\sum_t
\min_{x\in\gamma^*}
d_C(p_t,x).
\]

Lower:

\[
D_\gamma
\]

indicates stronger alignment.

---

# 24. Normalised Alignment

Compare with random valid trajectories.

Define:

\[
A_\gamma
=
1-
\frac{
D_\gamma
}{
E[D_{\gamma,\mathrm{control}}]
}.
\]

A value:

\[
A_\gamma>0
\]

indicates better-than-control alignment.

Exact normalisation must be preregistered.

---

# 25. Cost-Regret Metric

Another useful measure compares actual accumulated trajectory cost:

\[
C(\Gamma)
\]

with minimum feasible cost:

\[
C(\gamma^*).
\]

Define regret:

\[
R_C
=
\frac{
C(\Gamma)-C(\gamma^*)
}{
C(\gamma^*)
}.
\]

A geodesic-like trajectory should exhibit relatively low regret.

---

# 26. Direct Source Separation

Define relational source–probe separation:

\[
r(t)
=
d_S(P_S,P_T(t)).
\]

Measure:

\[
\Delta r
=
r(t+\Delta t)-r(t).
\]

An apparent approach toward the source corresponds to:

\[
E[\Delta r]<0.
\]

But this is not by itself evidence for geodesic motion.

---

# 27. Why “Moving Toward the Source” Is Insufficient

A probe may move toward \(P_S\) because of:

- local network asymmetry;
- resource gradients;
- direct activity coupling;
- random drift;
- pattern density.

E008 therefore prioritises:

\[
\text{geodesic alignment}
\]

over simple radial approach.

---

# 28. Control A — Remove Source

Run identical probe dynamics without:

\[
P_S.
\]

Compare trajectory statistics.

This establishes baseline drift.

---

# 29. Control B — Metric Frozen Before Source

Use the source-free metric while the source structure is present.

If motion persists, it may result from direct source interaction rather than metric distortion.

This is one of the most important controls.

---

# 30. Control C — Shuffled Metric

Preserve the distribution of transition costs:

\[
P(c)
\]

but shuffle their positions.

The source remains present.

If source-directed motion disappears, spatial organisation of cost matters.

---

# 31. Control D — Synthetic Matched Field

Remove the source but reproduce the same measured cost field artificially.

If probe trajectories remain unchanged, this supports:

\[
\text{metric mediation}
\]

rather than direct source coupling.

---

# 32. Mediation Test

The strongest causal design compares:

### Condition 1

\[
P_S+\Delta C
\]

### Condition 2

\[
P_S+\text{baseline }C
\]

### Condition 3

\[
\text{no }P_S+\Delta C
\]

### Condition 4

\[
\text{no }P_S+\text{baseline }C.
\]

If motion occurs in Conditions 1 and 3 but not 2 and 4, the evidence supports:

\[
\boxed{
\text{metric-mediated motion}
}
\]

rather than direct source attraction.

---

# 33. Control E — Activity-Matched Source

Use a transient or incoherent computational process producing the same computational load as the source.

If it produces the same field and trajectory effect, persistent identity may be irrelevant.

This result must be reported.

---

# 34. Control F — Reversed Cost Field

Where mathematically possible, invert the source-correlated cost gradient while preserving other statistics.

If trajectory bias reverses correspondingly, this strongly supports cost-mediated motion.

This should be used cautiously because constructing a matched inverted field may be nontrivial.

---

# 35. Control G — Probe Identity

Use multiple probe motifs:

\[
P_T^{(1)},
P_T^{(2)},\ldots
\]

with different internal computational structures.

A truly geometry-mediated effect should not depend completely on one probe design.

---

# 36. Equivalence-Like Question

A particularly important exploratory question is:

> Do different probe structures follow approximately the same trajectories when placed in the same emergent metric?

If yes, this begins to resemble universality of free motion.

Do not label this the equivalence principle yet.

---

# 37. Probe Computational Burden

Each probe may have an intrinsic maintenance cost:

\[
Q_T.
\]

Test whether trajectory depends on:

\[
Q_T.
\]

If probes with different internal computational burdens follow the same paths, that is notable.

---

# 38. Trajectory Universality

Define trajectory discrepancy between probes \(i,j\):

\[
U_{ij}
=
D(
\Gamma_i,\Gamma_j
)
\]

after matching initial relational conditions.

Low:

\[
U_{ij}
\]

across diverse probes indicates universal motion.

---

# 39. No Primitive Inertia

E008 should not initially assign a primitive inertial mass.

Instead probes differ through computational properties such as:

- persistence;
- support size;
- maintenance cost;
- transition redundancy.

Observed resistance to changes in motion, if any, must emerge from those properties.

---

# 40. Initial Velocity

A moving probe may begin with a persistent directional propagation state.

Define relational momentum-like history through previous support transitions.

For example:

\[
P_T(t-1)
\rightarrow
P_T(t).
\]

No vector in Euclidean space is required.

---

# 41. Free-Motion Baseline

Without a source, establish the probe's normal trajectory statistics:

- persistence length;
- directional memory;
- diffusion coefficient;
- transition entropy.

The source experiment must be compared against this baseline.

---

# 42. Deflection Experiment

Instead of initially placing the probe at rest, send a mobile structure past the source region.

Measure whether its trajectory is deflected relative to source-free propagation.

This may be scientifically cleaner than testing “falling.”

---

# 43. Deflection Observable

Let:

\[
\Gamma_0
\]

be the expected source-free trajectory.

Let:

\[
\Gamma_S
\]

be the trajectory with source metric distortion.

Define deflection:

\[
\Delta_\Gamma
=
D(\Gamma_S,\Gamma_0).
\]

Then test whether:

\[
\Gamma_S
\]

aligns with:

\[
\gamma_S^*
\]

better than with:

\[
\Gamma_0.
\]

---

# 44. Closest Approach

For passing trajectories, define:

\[
r_{\min}
=
\min_t d_S(P_S,P_T(t)).
\]

Compare source and control conditions.

A metric field may change:

- closest approach;
- path duration;
- exit direction.

---

# 45. Path Delay

Even if the probe does not visibly bend, the distorted metric may alter traversal time.

Define:

\[
\Delta\tau
=
\tau_S-\tau_0.
\]

This may reveal geodesic effects before large positional deflection appears.

---

# 46. Static-Probe Release

Another track places a probe in a locally stable state, then releases it.

Measure whether motion develops preferentially along the cost metric.

This could resemble free fall, but that terminology should remain interpretive.

---

# 47. E008-B — Passing Probe

A moving persistent pattern crosses the distorted metric region.

Primary measurement:

\[
\text{trajectory deflection}.
\]

---

# 48. E008-C — Released Probe

A minimally moving or locally unbiased probe is released into the field.

Primary measurement:

\[
\text{spontaneous trajectory bias}.
\]

---

# 49. E008-D — Multiple Probe Types

Repeat B/C with several structurally distinct probes.

Primary measurement:

\[
\text{trajectory universality}.
\]

---

# 50. Metric Gradient

For analysis only, define local metric-cost gradient:

\[
\nabla_C
\]

using relational finite differences.

No gradient is exposed to the probe rule.

Test whether observed displacement direction correlates with:

\[
-\nabla_C.
\]

---

# 51. Gradient Correlation

Define:

\[
\rho_G
=
\operatorname{corr}
(
\text{probe displacement},
-\nabla_C
).
\]

This requires an appropriate relational directional representation.

High correlation would support metric-mediated motion.

---

# 52. Computational Arbitrage Hypothesis

CBR has proposed that gravitational-like behaviour may represent resolution of computational imbalance.

E008 gives this idea an operational form.

If local motion preferentially follows paths that reduce unresolved computational cost, then:

\[
\text{motion}
\]

can be interpreted as:

\[
\text{local computational arbitrage}.
\]

The experiment must test the measurable behaviour before adopting the interpretation.

---

# 53. Cost-Reduction Observable

For each probe transition:

\[
P_T(t)\rightarrow P_T(t+1),
\]

calculate environmental cost:

\[
C_{\mathrm{env}}(t).
\]

Define:

\[
\Delta C_{\mathrm{env}}
=
C_{\mathrm{env}}(t+1)-C_{\mathrm{env}}(t).
\]

Test whether probe trajectories produce systematically different:

\[
\Delta C_{\mathrm{env}}
\]

than controls.

---

# 54. Critical Distinction

The probe must not be explicitly programmed to minimise **global** cost.

Local transition probabilities may depend on local feasibility.

If the overall trajectory nevertheless approaches a global geodesic, the result is much more interesting.

Thus:

\[
\boxed{
\text{local rule}
\rightarrow
\text{global geodesic}
}
\]

is the target phenomenon.

---

# 55. Local Versus Global Optimality

Measure:

\[
R_C
\]

for different trajectory lengths.

If global cost regret remains low despite only local information being used, geodesic behaviour is emergent.

---

# 56. Internal Observer

An embedded observer may measure:

- probe trajectory;
- signal travel times;
- source location inferred from E007;
- local cost.

The observer should not receive the global graph.

Ask whether it can predict probe motion using its reconstructed metric.

---

# 57. Internal Prediction Error

Let the observer predict:

\[
\hat\Gamma.
\]

Compare with:

\[
\Gamma.
\]

Define:

\[
E_\Gamma
=
D(\hat\Gamma,\Gamma).
\]

If embedded agents can predict motion from locally reconstructed geometry, the geometry acquires operational dynamical meaning.

---

# 58. Two Independent Predictions

Compare:

### External prediction

Computed from complete metric:

\[
\gamma^*.
\]

### Internal prediction

Computed from locally reconstructed metric:

\[
\hat\gamma.
\]

A strong result would yield:

\[
\Gamma
\approx
\gamma^*
\approx
\hat\gamma.
\]

---

# 59. Source Strength

Use source structures with varying intrinsic computational burden:

\[
Q_S.
\]

Measure deflection as:

\[
\Delta_\Gamma(Q_S).
\]

No particular scaling is targeted.

---

# 60. Separation Dependence

Vary initial source–probe separation:

\[
r_0.
\]

Measure:

\[
\Delta_\Gamma(r_0).
\]

This determines whether the motion effect has an extended relational range.

---

# 61. No Inverse-Square Assumption

Do not preregister:

\[
\Delta_\Gamma\propto\frac{1}{r^2}
\]

as the primary hypothesis.

Any such fit is exploratory.

A later experiment may preregister a discovered quantitative law.

---

# 62. Source Symmetry

Use source patterns with approximately symmetric relational activity.

Test whether trajectory effects are correspondingly isotropic.

Then deliberately use asymmetric sources.

A geometry-based mechanism should reflect source-induced metric geometry.

---

# 63. Multiple Sources

A later E008 extension places:

\[
P_{S1},P_{S2}.
\]

Measure whether probe motion follows geodesics in the combined metric.

This tests nonlinear field effects identified in E007-C.

---

# 64. No Pairwise Force Addition

The probe still receives no force from either source.

Motion must arise through:

\[
C_{\mathrm{combined}}
\]

and:

\[
d_{\mathrm{combined}}.
\]

This provides a clean distinction from Newtonian pair-force coding.

---

# 65. Time-Reversal Analysis

Where underlying local rules permit, initialise the reverse of a completed probe trajectory.

Ask whether the system approximately retraces it.

Failure or success may reveal dissipative properties.

This is secondary.

---

# 66. Energy-Like Accounting

E008 may measure computational quantities along a trajectory:

- pattern maintenance cost;
- environmental transition cost;
- update activity;
- path cost.

Do not call these kinetic or potential energy until a conserved relationship is demonstrated.

---

# 67. Candidate Conserved Quantity

Search post hoc for quantities:

\[
E_C(t)
\]

that remain approximately constant along free trajectories.

Any discovered candidate must be tested independently in a later preregistered experiment.

---

# 68. Acceleration Without Coordinates

Define change in relational displacement rate.

If:

\[
v_C(t)
=
d_C(P_T(t),P_T(t+\Delta t))/\Delta t,
\]

then computational acceleration may be estimated through:

\[
a_C
=
\frac{
v_C(t+\Delta t)-v_C(t)
}{
\Delta t
}.
\]

Directional acceleration requires relational path information rather than Cartesian vectors.

---

# 69. Geodesic Acceleration

In curved geometry an object can have coordinate acceleration while following a geodesic.

CBR-E008 should therefore avoid equating:

\[
a_C\neq0
\]

with force.

The primary comparison remains actual path versus metric geodesic.

---

# 70. Source Removal During Motion

While the probe is travelling, remove:

\[
P_S.
\]

Measure whether subsequent path converges toward the source-free geodesic.

This is a strong causal intervention.

---

# 71. Field Freeze During Motion

Alternatively remove the source but freeze the cost field.

If the probe continues along the distorted geodesic, this supports metric mediation.

If motion immediately changes after source removal despite unchanged metric, direct coupling may exist.

---

# 72. Dynamic Mediation Matrix

The four key conditions are:

```text
source present / metric present
source absent  / metric present
source present / metric absent
source absent  / metric absent
```

Trajectory comparison across these conditions is central to E008.

---

# 73. Primary Endpoint

The primary E008 endpoint is:

> **Whether a freely evolving persistent probe follows preregistered geodesic predictions in an endogenous source-distorted computational metric significantly better than matched source-free, metric-shuffled and direct-coupling controls.**

---

# 74. Primary Evidence Conditions

Support for CBR-H008 requires:

1. E007 metric distortion is independently established;

2. probe motion aligns with that metric's geodesics;

3. alignment exceeds source-free control;

4. alignment disappears or changes when the metric is removed/shuffled;

5. a synthetic equivalent metric reproduces the motion without the source;

6. effects replicate across seeds;

7. effects persist with multiple probe structures;

8. independent implementations reproduce the phenomenon.

---

# 75. Stronger Evidence Conditions

A stronger result additionally shows:

- different probe structures follow equivalent geodesics;
- field strength systematically changes deflection;
- internal observers can predict motion from reconstructed metric;
- source removal/frozen-field interventions confirm metric mediation;
- global geodesic behaviour arises from local rules.

---

# 76. Failure Conditions

CBR-E008 fails to support the hypothesis if:

- probe motion is unaffected by metric distortion;
- direct source presence matters more than metric state;
- shuffled cost fields produce equivalent trajectories;
- geodesic alignment disappears with system size;
- different probe designs behave arbitrarily;
- trajectory prediction is chosen post hoc;
- independent replication fails.

---

# 77. Important Negative Result

A particularly meaningful result would be:

\[
\text{source distorts metric}
\]

but:

\[
\text{probe ignores metric}.
\]

This would show that E007-like metric distortion alone is insufficient to produce gravitationally analogous dynamics.

That would strongly constrain CBR.

---

# 78. Another Negative Result

The probe may follow lower-cost paths only when explicitly cost-sensitive.

If unbiased local dynamics show no geometric response, then geodesic motion may require an additional computational principle.

This distinction must be reported.

---

# 79. Weak Positive Result

A weak positive result would show:

> locally cost-sensitive probes approximately follow minimum-cost paths.

This is expected in many weighted-network systems and therefore limited.

---

# 80. Strong Positive Result

A stronger result would show:

> diverse persistent structures, using only local update information, exhibit globally geodesic-like motion in a metric generated endogenously by another persistent structure.

This is substantially more interesting.

---

# 81. Strongest E008 Result

The strongest outcome would establish:

\[
\boxed{
P_S
\rightarrow
\Delta C
\rightarrow
\Delta d
}
\]

followed independently by:

\[
\boxed{
P_T
\rightarrow
\gamma^*(\Delta d)
}
\]

with:

- no direct source–probe interaction;
- no attraction term;
- no coordinates;
- no target trajectory;
- no gravitational equation;
- multiple probe types following the same geometry.

At that point, the gravitational analogy becomes scientifically substantive.

---

# 82. Interpretation Boundary

Even the strongest E008 result would **not** establish general relativity.

It would establish:

> **Persistent computational structures can generate emergent metric distortion, and other persistent structures can respond to that geometry through geodesic-like motion without an explicitly encoded attractive force.**

Further work would still need to recover quantitative gravitational physics.

---

# 83. Relationship to Gravity as Computational Arbitrage

If E008 succeeds, one possible interpretation becomes:

\[
\text{persistent source}
\rightarrow
\text{computational imbalance}
\rightarrow
\text{cost redistribution}
\rightarrow
\text{metric gradient}
\rightarrow
\text{local optimisation}
\rightarrow
\text{geodesic motion}.
\]

This may be described as **computational arbitrage**.

But the interpretation must remain downstream of the experimental result.

---

# 84. Relationship to CBR-E009

E008 deals primarily with motion in an emergent metric.

The next foundational issue is causality.

CBR-E009 should ask:

> **Can local computational propagation generate a stable invariant causal structure—potentially including a universal limiting speed—without Lorentz symmetry being explicitly imposed?**

That takes the programme from:

\[
\text{space + motion}
\]

toward:

\[
\text{spacetime-like causal structure}.
\]

---

# 85. Relationship to CBR-E010

Only after metric dynamics and causal structure are established should the programme ask whether quantitative gravitational laws emerge.

E010 would compare:

- source properties;
- metric distortion;
- trajectories;
- propagation;
- curvature proxies

with predictions of known gravitational physics.

---

# 86. CBR-E008 YAML Summary

```yaml id="19q3uw"
cbr_oen:
  protocol_version: "1.0"

experiment:
  id: "CBR-E008"
  version: "1.0"

  title:
    "Emergent Geodesic Motion in a Computationally Distorted Metric"

hypothesis:
  id: "CBR-H008"

  statement: >
    A freely evolving persistent computational structure
    embedded in an endogenously distorted computational metric
    will exhibit reproducible motion aligned with that metric's
    geodesic structure without an explicitly encoded attraction rule.

null_hypothesis: >
  Probe trajectories show no relationship to source-induced
  computational metric distortion beyond random drift,
  graph topology, direct source interaction or generic cost bias.

substrate:

  topology:
    source:
      "CBR-E004 / CBR-E005"

  metric:
    source:
      "CBR-E006"

  source_distortion:
    source:
      "CBR-E007"

  coordinates:
    enabled: false

source:

  primitive_mass:
    enabled: false

  direct_attractive_force:
    enabled: false

probe:

  persistent_structure:
    required: true

  access_to_source_location:
    false

  access_to_global_metric:
    false

  target_trajectory:
    false

tracks:

  E008_A0:
    name:
      "Neutral Local Mobility"

  E008_A1:
    name:
      "Locally Cost-Sensitive Mobility"

  E008_B:
    name:
      "Passing Probe Deflection"

  E008_C:
    name:
      "Released Probe"

  E008_D:
    name:
      "Multi-Probe Universality"

measurements:

  primary:

    - geodesic_alignment
    - path_cost_regret
    - trajectory_deflection

  secondary:

    - source_probe_separation
    - traversal_delay
    - metric_gradient_alignment
    - internal_prediction_error
    - probe_universality
    - relational_acceleration

controls:

  - source_free
  - source_present_metric_removed
  - source_absent_metric_preserved
  - shuffled_metric
  - synthetic_matched_metric
  - transient_activity_matched_source
  - multiple_probe_types

forbidden_rules:

  - attraction_to_source
  - inverse_square_force
  - source_direction_lookup
  - target_geodesic
  - curvature_force
  - gravitational_potential

primary_endpoint: >
  Determine whether free persistent probes follow preregistered
  geodesic predictions in an endogenous source-distorted metric
  significantly better than matched controls.

replication:

  independent_motion_implementation_required_for_r2: true

  institutional_replication_required_for_r3: true

negative_results:
  retained: true
```

---

# 87. Experimental Progression

The first sequence has now reached:

\[
\boxed{
E001:
\text{dimension emerges}
}
\]

\[
\downarrow
\]

\[
\boxed{
E002:
\text{dimension-blind selection}
}
\]

\[
\downarrow
\]

\[
\boxed{
E003:
\text{manifold topology}
}
\]

\[
\downarrow
\]

\[
\boxed{
E004:
\text{explicit topology}
}
\]

\[
\downarrow
\]

\[
\boxed{
E005:
\text{topological resilience}
}
\]

\[
\downarrow
\]

\[
\boxed{
E006:
\text{computational metric}
}
\]

\[
\downarrow
\]

\[
\boxed{
E007:
\text{persistent structure distorts metric}
}
\]

\[
\downarrow
\]

\[
\boxed{
E008:
\text{free structure follows metric}
}
\]

This is the first point where the complete experimental chain begins to resemble:

\[
\boxed{
\text{matter}
\rightarrow
\text{geometry}
\rightarrow
\text{motion}
}
\]

without any of those physical concepts having been inserted as primitive variables.

---

# 88. Final Principle

The decisive rule of CBR-E008 is:

> **Never tell the probe where the source is.**

Do not tell it:

- which way is inward;
- which path is a geodesic;
- how far away the source is;
- that attraction exists;
- that gravity exists.

Give it only its local computational environment.

If:

\[
P_S
\]

changes that environment through the metric mechanism independently established in E007, and:

\[
P_T
\]

then follows the geodesics of that environment using only local computation, the observed “attraction” is no longer a programmed interaction between two objects.

It is an emergent consequence of the computational geometry separating them.

That is the scientific purpose of CBR-E008.