# CBR-OEN Experiment CBR-E006
## Emergent Metric Geometry from Computational Transition Cost
### Preregistered Experimental Specification — Draft v1.0

---

## 1. Experiment Identity

**Experiment ID:** CBR-E006  
**Version:** 1.0  
**Title:** Emergent Metric Geometry from Computational Transition Cost  
**Protocol:** CBR-OEN Experimental Protocol v1.0  
**Experiment class:** Confirmatory computational-geometry experiment  
**Predecessors:** CBR-E001 through CBR-E005

---

# 2. Scientific Question

CBR-E006 asks:

> **Can a computational system with relational topology but no predefined spatial coordinates generate a stable metric geometry when only local computational transition costs are defined?**

Earlier experiments investigate:

\[
\text{relations}
\rightarrow
\text{dimension}
\rightarrow
\text{manifold topology}.
\]

CBR-E006 adds the next layer:

\[
\boxed{
\text{topology}
\rightarrow
\text{metric geometry}
}
\]

without inserting conventional physical distance beforehand.

---

# 3. Core Hypothesis

### CBR-H006

Local computational transition costs on a relational or simplicial system can generate an effective large-scale metric satisfying approximately the properties expected of spatial distance.

Let:

\[
K=(V,E,F,T)
\]

be an explicit simplicial computational state.

Assign to each permitted local transition or adjacency \(e\) a positive computational cost:

\[
c(e)>0.
\]

Define the effective separation between states \(A\) and \(B\) as:

\[
d_C(A,B)
=
\min_{\gamma:A\rightarrow B}
\sum_{e\in\gamma}c(e).
\]

The hypothesis is that under suitable computational dynamics, \(d_C\) behaves as a stable and coherent emergent metric.

---

# 4. Null Hypothesis

The null hypothesis is:

> Local transition costs produce only arbitrary graph-weight distances whose large-scale behaviour is unstable, strongly dependent upon microscopic details, or lacks reproducible geometric structure beyond generic weighted-network effects.

Thus simply obtaining a shortest-path function is not sufficient.

CBR-E006 seeks evidence for:

\[
\text{coherent emergent geometry}
\]

rather than merely:

\[
\text{weighted graph distance}.
\]

---

# 5. What E006 Does Not Assume

The experiment must not begin with:

```text id="dc54up"
x
y
z
Euclidean coordinates
Cartesian coordinates
angles
physical length
curvature tensor
metric tensor
speed of light
gravitational potential
```

The computational substrate receives only:

- incidence;
- adjacency;
- local state;
- local transition cost;
- update rules.

---

# 6. Conceptual Model

The central CBR proposition tested is:

> **Distance may represent computational separation rather than primitive spatial separation.**

Two computational regions are close if relatively little computational cost separates them.

They are distant if interaction requires greater accumulated cost.

Thus:

\[
\boxed{
\text{distance}
\sim
\text{minimum relational transition cost}
}
\]

---

# 7. Substrate

The preferred CBR-E006 substrate is the explicit 3-dimensional simplicial system validated through E004/E005.

At time \(t\):

\[
K_t=(V_t,E_t,F_t,T_t).
\]

Effective geometry may be measured on either:

- the vertex graph;
- the tetrahedral dual graph;
- another explicitly preregistered adjacency structure.

The primary E006 implementation should use the tetrahedral dual graph:

\[
G_t^*.
\]

Each dual node represents a tetrahedron.

Two dual nodes are adjacent when the associated tetrahedra share a triangular face.

---

# 8. Computational Cost

Each dual edge \(e\) receives a cost:

\[
c_e>0.
\]

This cost must be generated entirely from computational properties.

It cannot be derived from an external spatial embedding.

---

# 9. Baseline Cost Model

The simplest control uses:

\[
c_e=1.
\]

Then:

\[
d_C(A,B)
\]

reduces to ordinary graph distance.

This establishes a topology-only baseline.

CBR-E006 then introduces non-uniform computational cost.

---

# 10. Local Cost Model

A generic local cost may be represented as:

\[
c_e
=
f(X_i,X_j,L_{ij})
\]

where:

- \(X_i\) = local computational state around node \(i\);
- \(X_j\) = local computational state around node \(j\);
- \(L_{ij}\) = local relationship information.

Permitted inputs could include:

- simplex incidence;
- local update frequency;
- state-change frequency;
- computational congestion;
- local entropy;
- transition availability;
- persistent computational structures.

No global coordinate information is allowed.

---

# 11. Positive Cost Requirement

For the baseline experiment:

\[
c_e>0
\]

for every traversable relation.

This guarantees several basic shortest-path properties and avoids zero-cost collapse.

A preregistered minimum:

\[
c_e\geq\epsilon>0
\]

should be used.

---

# 12. Emergent Distance

For two dual nodes \(A,B\):

\[
d_C(A,B)
=
\min_{\gamma\in\Gamma(A,B)}
C(\gamma)
\]

with:

\[
C(\gamma)
=
\sum_{e\in\gamma}c_e.
\]

This is the primary candidate metric.

---

# 13. Metric Axioms

A mathematical metric must satisfy:

### Non-negativity

\[
d(A,B)\geq0.
\]

### Identity

\[
d(A,B)=0
\iff
A=B.
\]

### Symmetry

\[
d(A,B)=d(B,A).
\]

### Triangle inequality

\[
d(A,C)
\leq
d(A,B)+d(B,C).
\]

With positive symmetric edge costs, shortest-path distance satisfies these exactly.

Therefore satisfying metric axioms alone is **not** a positive E006 result.

The scientific question concerns whether the resulting metric has coherent large-scale geometric properties.

---

# 14. Symmetric Baseline

E006-A uses:

\[
c(A,B)=c(B,A).
\]

This produces a conventional metric.

Later experiments may allow:

\[
c(A,B)\neq c(B,A),
\]

which would produce directed or Finsler-like structures.

That is outside the primary E006 scope.

---

# 15. Primary Question Beyond the Metric Axioms

The stronger question is:

> **Does the computational metric become smooth, stable and locally coherent when viewed at scales larger than the underlying simplicial resolution?**

This introduces coarse-graining.

---

# 16. Coarse-Grained Distance

Let:

\[
\ell_0
\]

be the microscopic simplicial scale.

Consider measurements over:

\[
r\gg\ell_0.
\]

A successful emergent geometry should display reduced sensitivity to individual local rewrites at increasing scales.

Define a coarse-grained metric:

\[
d_C^{(L)}
\]

where \(L\) represents observation scale.

The experiment asks whether:

\[
d_C^{(L)}
\rightarrow
d_{\mathrm{eff}}
\]

as \(L\) increases.

---

# 17. Metric Stability

For a set of persistent reference regions \(A,B\), measure:

\[
d_t(A,B)
\]

through computational evolution.

Define relative metric fluctuation:

\[
\sigma_d(A,B)
=
\frac{
\operatorname{std}_t(d_t(A,B))
}{
\operatorname{mean}_t(d_t(A,B))
}.
\]

A stable emergent geometry should exhibit decreasing fluctuations under appropriate coarse-graining.

---

# 18. Primary Endpoint

The primary endpoint of CBR-E006 is:

> **Whether locally generated computational transition costs produce a reproducible, coarse-grain-stable metric geometry whose observable structure differs systematically from matched random weighted-complex controls.**

No predetermined Euclidean geometry is required.

---

# 19. E006-A — Uniform-Cost Baseline

Set:

\[
c_e=1.
\]

Measure:

- graph distance;
- ball growth;
- spectral dimension;
- geodesic degeneracy;
- distance distribution.

Purpose:

> establish the topology-only reference geometry.

---

# 20. E006-B — Endogenous Computational Cost

Costs depend on local computational activity.

For example:

\[
c_e
=
1+\alpha q_e
\]

where:

\[
q_e
\]

is a normalised local computational-load variable.

Potential \(q_e\) definitions include:

- update count;
- local transition entropy;
- contention;
- local state instability.

No spatial quantity enters the definition.

---

# 21. E006-C — Adaptive Cost

Transition cost itself may evolve.

For example:

\[
c_e(t+1)
=
c_e(t)
+
\eta\Delta_e(t).
\]

Here \(\Delta_e(t)\) derives from local computational activity.

This introduces feedback:

\[
\text{computation}
\rightarrow
\text{cost}
\rightarrow
\text{effective geometry}
\rightarrow
\text{future computation}.
\]

This track is more ambitious and should follow the static-cost baseline.

---

# 22. Geodesics

Given the emergent metric, define a computational geodesic:

\[
\gamma^*_{AB}
=
\operatorname*{argmin}_{\gamma:A\rightarrow B}
C(\gamma).
\]

These are minimum-cost relational paths.

The experiment can then ask whether geodesic structure is:

- stable;
- locally coherent;
- smoothly varying;
- robust to microscopic rewrites.

---

# 23. Geodesic Stability

For endpoints \(A,B\), compare geodesics at successive times.

Define overlap:

\[
O_\gamma(t,t+\Delta t)
=
\frac{
|\gamma_t\cap\gamma_{t+\Delta t}|
}{
|\gamma_t\cup\gamma_{t+\Delta t}|
}.
\]

A useful geometry may permit microscopic variation while preserving a stable coarse-grained path.

---

# 24. Geodesic Degeneracy

There may be multiple equal-cost paths.

Define:

\[
N_\gamma(A,B)
\]

as the number or estimated multiplicity of near-minimal paths.

Large degeneracy may indicate:

- geometric symmetry;
- network redundancy;
- high entropy;
- or a poorly defined effective geodesic.

The distribution should be measured.

---

# 25. Local Metric Balls

Define:

\[
B_C(v,r)
=
\{
u:
d_C(u,v)\leq r
\}.
\]

Measure:

\[
V_C(r)
=
|B_C(v,r)|.
\]

If:

\[
V_C(r)
\propto r^{d_M},
\]

then \(d_M\) provides an effective metric volume-growth dimension.

This is separate from the unweighted graph dimension.

---

# 26. Metric Dimension Agreement

Compare:

\[
d_H^{\mathrm{graph}},
\]

\[
d_S,
\]

and:

\[
d_M^{\mathrm{cost}}.
\]

A coherent emergent geometry might produce approximate agreement:

\[
d_H^{\mathrm{graph}}
\approx
d_S
\approx
d_M^{\mathrm{cost}}.
\]

Agreement is observational only.

No equality is assumed.

---

# 27. Local Isotropy

Physical space appears approximately isotropic at sufficiently small laboratory scales.

CBR-E006 should therefore measure whether cost-based distance exhibits directional bias.

Without coordinates, direction must be defined relationally.

One method is to compare growth sectors initiated through different neighbouring edges of a reference node.

If metric expansion depends strongly on which first edge is chosen, local geometry is anisotropic.

---

# 28. Relational Isotropy Metric

For a node \(v\) with neighbours:

\[
n_1,\ldots,n_k,
\]

partition outward paths by first step.

Measure cost-ball growth:

\[
V_i(r).
\]

Define isotropy variation:

\[
I(v,r)
=
\frac{
\operatorname{std}_i V_i(r)
}{
\operatorname{mean}_i V_i(r)
}.
\]

Lower values indicate more isotropic relational growth.

---

# 29. Homogeneity

Isotropy concerns directional variation around one point.

Homogeneity concerns variation between points.

Measure:

\[
V_v(r)
\]

for many reference nodes.

Define:

\[
H(r)
=
\frac{
\operatorname{std}_v V_v(r)
}{
\operatorname{mean}_v V_v(r)
}.
\]

A macroscopically homogeneous regime should produce decreasing \(H(r)\) at appropriate scales.

---

# 30. Geometry Without Euclidean Targeting

Importantly, E006 must not optimise:

\[
I\rightarrow0
\]

or:

\[
H\rightarrow0.
\]

These are measurements.

If homogeneous or isotropic geometry appears, it must emerge from the computational rules rather than a geometric fitness function.

---

# 31. Metric Smoothness

A discrete metric cannot literally be differentiable.

Instead define approximate smoothness through neighbouring measurements.

For nearby reference points \(u,v\), compare their distance profiles:

\[
D_u=
(d(u,x_1),\ldots,d(u,x_n))
\]

and:

\[
D_v.
\]

If small relational changes produce small large-scale metric changes, the geometry behaves smoothly in a coarse-grained sense.

---

# 32. Lipschitz-Like Stability

A useful discrete condition is:

\[
|d(u,x)-d(v,x)|
\leq
L\,d(u,v)
\]

for sampled points.

For exact metrics, triangle inequality already gives a related bound, so E006 should focus on **statistical smoothness of local cost fields** rather than presenting this alone as evidence.

---

# 33. Curvature Proxy

CBR-E006 should not initially claim to derive Riemann curvature.

However, discrete curvature observables may be used as exploratory diagnostics.

Examples include:

- Ollivier–Ricci curvature;
- Forman curvature;
- deficit-angle constructions where simplicial information permits them.

These are secondary measurements.

---

# 34. Why Curvature Is Secondary

Different discrete curvature definitions need not agree.

Therefore:

> E006 should first establish metric emergence before interpreting curvature.

Curvature becomes central in E007/E008 when persistent structures are allowed to influence the metric.

---

# 35. Computational Cost Field

It is useful to define:

\[
C_t:E_t\rightarrow\mathbb{R}_{>0}.
\]

The full state becomes:

\[
(K_t,C_t).
\]

Topology describes:

\[
\text{which relationships exist}.
\]

Cost describes:

\[
\text{how difficult traversal is}.
\]

The pair begins to resemble a discrete metric space.

---

# 36. Separation of Topology and Metric

Two states may have identical topology:

\[
K_A=K_B
\]

but different cost fields:

\[
C_A\neq C_B.
\]

Thus:

\[
d_A\neq d_B.
\]

This allows geometry to change without topology changing.

That is central to CBR-E006.

---

# 37. Cost Perturbation Experiment

Take a fixed simplicial complex.

Generate two cost fields:

\[
C
\]

and:

\[
C'=C+\delta C.
\]

Measure:

\[
\Delta d(A,B)
=
d_{C'}(A,B)-d_C(A,B).
\]

This establishes how local computational perturbations propagate into large-scale geometry.

---

# 38. Locality of Metric Perturbations

Suppose cost changes only within region:

\[
R.
\]

Measure the effect on distances between points increasingly far from \(R\).

This asks whether local computational changes create:

- local geometric effects;
- long-range changes;
- global reorganisation.

The behaviour should be measured rather than assumed.

---

# 39. Cost Conservation

Some E006 variants may impose a conserved total computational cost:

\[
\sum_ec_e=C_{\mathrm{total}}.
\]

Others may not.

These should be treated as separate experimental conditions.

A conserved-cost model may reveal redistribution effects.

---

# 40. Dynamic Cost Redistribution

If total cost is conserved, local increases require decreases elsewhere.

This creates the possibility of a globally coupled metric field emerging from local accounting.

Conceptually:

\[
\delta c_R>0
\]

may imply:

\[
\sum_{e\notin R}\delta c_e<0.
\]

Such models could later connect naturally to the CBR concept of computational arbitrage.

---

# 41. Computational Flow

Instead of assigning cost arbitrarily, define it from actual computational traffic.

Let:

\[
f_e
\]

be traversal or update flow through relation \(e\).

A cost rule might be:

\[
c_e=
1+\alpha f_e.
\]

This produces congestion-like geometry.

Another possibility is:

\[
c_e=
\frac{1}{1+\alpha f_e},
\]

where frequently used relationships become computationally cheaper.

These models represent distinct hypotheses and must not be mixed post hoc.

---

# 42. Learning-Like Cost

Repeated transitions could lower cost:

\[
c_e(t+1)
=
c_e(t)
-
\eta f_e(t).
\]

This creates computational path reinforcement.

The resulting geometry might develop:

- channels;
- hubs;
- anisotropy;
- preferred geodesics.

This is exploratory in E006.

---

# 43. Entropic Cost

Another model is:

\[
c_e
=
f(H_{\text{local}})
\]

where:

\[
H_{\text{local}}
\]

is a local entropy measure.

This tests whether informational complexity can induce geometric separation.

Again, no physical interpretation should be assumed beforehand.

---

# 44. Cost Model Families

CBR-E006 should compare several preregistered families:

```text id="jxnqmd"
C0  Uniform cost
C1  Local activity cost
C2  Congestion cost
C3  Reinforcement cost
C4  Entropic cost
C5  Conserved redistributed cost
```

The goal is not to search indefinitely for one model that resembles physical space.

It is to determine which classes generate robust metric behaviour.

---

# 45. Matched Random-Cost Control

For every endogenous cost field \(C\), create a control \(C_R\) by randomly permuting costs across edges.

This preserves the cost distribution:

\[
P(c)
\]

but destroys correlation between cost and computational structure.

Compare emergent geometry.

This is a critical control.

---

# 46. Degree-Matched Control

Compare systems with the same:

- topology;
- degree distribution;
- cost distribution

but shuffled cost placement.

Any difference must then arise from **where computational costs occur**, not simply how many high-cost edges exist.

---

# 47. Static-Cost Control

Freeze the cost field after initialisation.

Compare with a dynamically updated cost field.

This tests whether feedback between computation and geometry produces additional organisation.

---

# 48. Random-Network Control

Run identical cost rules on matched non-manifold/random graph structures.

This tests whether apparent geometry is specific to manifold-like substrates or generic weighted networks.

---

# 49. Manifold Versus Non-Manifold Comparison

A particularly useful E006 comparison is:

\[
K_M
\]

a manifold-like complex,

versus:

\[
K_N
\]

a non-manifold complex,

with matched:

- size;
- degree;
- cost distribution.

Then compare metric coherence.

This tests whether manifold topology contributes to geometric stability.

---

# 50. Primary Geometry Quality Measures

CBR-E006 should preregister a set of geometry-quality observables without combining them into a fitness function.

These may include:

### \(Q_S\) — scale stability

How consistent dimensional/metric statistics are across observation scales.

### \(Q_T\) — temporal stability

How stable pairwise coarse distances are over time.

### \(Q_H\) — homogeneity

Variation in metric-ball growth across locations.

### \(Q_I\) — isotropy

Variation across relational directions.

### \(Q_G\) — geodesic stability

Persistence of coarse minimum-cost paths.

---

# 51. Composite Geometry Score

A composite score may be calculated **after execution**:

\[
Q_G^{\mathrm{total}}
=
f(Q_S,Q_T,Q_H,Q_I,Q_G).
\]

However, it must not enter computational dynamics or evolutionary fitness in E006.

Its purpose is analysis only.

---

# 52. Metric Emergence Criterion

A candidate emergent metric regime should satisfy preregistered conditions such as:

1. positive path metric exists;

2. coarse distance statistics stabilise with increasing scale;

3. behaviour is reproducible across seeds;

4. endogenous cost placement differs significantly from shuffled controls;

5. metric statistics remain robust under increased system size;

6. independent implementation reproduces the effect.

---

# 53. Stronger Metric Criterion

A stronger result would additionally exhibit:

- approximate local homogeneity;
- approximate local isotropy;
- stable geodesics;
- consistent dimensional estimators;
- low sensitivity to individual microscopic rewrites.

This begins to resemble a physically useful geometry.

---

# 54. Finite-Size Scaling

Run candidate cost rules across increasing complex sizes.

For example:

\[
N_T=
250,
500,
1000,
2000,
5000,
10000.
\]

Measure:

\[
d_M(N_T),
\]

\[
Q_H(N_T),
\]

\[
Q_I(N_T),
\]

\[
Q_T(N_T).
\]

A genuine emergent regime should not disappear as the system grows.

---

# 55. Coarse-Graining Test

Partition the complex into relational regions.

Construct a coarse graph:

\[
G_L.
\]

Aggregate local costs.

Recalculate distances.

Compare fine and coarse geometries.

A promising result would satisfy:

\[
d_C^{\mathrm{coarse}}
\approx
\lambda\,d_C^{\mathrm{fine}}
\]

for some scale factor \(\lambda\).

This suggests scale-consistent geometry.

---

# 56. Renormalisation-Like Behaviour

Repeat coarse-graining:

\[
G_0
\rightarrow
G_1
\rightarrow
G_2
\rightarrow
\cdots.
\]

Observe whether metric statistics converge toward a stable family.

This can be described as a computational analogue of renormalisation.

A fixed-point-like regime would be particularly interesting.

---

# 57. Metric Universality

If different microscopic cost rules produce the same large-scale geometry, this suggests universality.

For example:

\[
C_1
\rightarrow
d_{\mathrm{eff}}
\]

and:

\[
C_2
\rightarrow
d_{\mathrm{eff}}
\]

despite very different microscopic definitions.

Such a result would be more significant than one fine-tuned cost rule.

---

# 58. Universality Class

A future CBR concept could define a computational geometry universality class:

\[
[C]
=
\{
C_i:
C_i\rightarrow G_{\mathrm{eff}}
\}.
\]

E006 should begin collecting evidence for or against such classes.

---

# 59. Metric Information Loss

Coarse-graining removes microscopic information.

Measure how much detailed cost information can be discarded while retaining large-scale distances within tolerance:

\[
|d_{\mathrm{coarse}}(A,B)
-
\lambda d_{\mathrm{fine}}(A,B)|
<\epsilon.
\]

High compressibility with preserved geometry would support an emergent description.

---

# 60. Relationship to Physical Length

E006 does not initially identify:

\[
d_C
\]

with metres.

Instead:

\[
d_C
\]

is a dimensionless or computational distance.

A physical length scale would require a mapping:

\[
L=
\ell_*d_C
\]

for some conversion scale \(\ell_*\).

Determining such a scale lies outside E006.

---

# 61. Relationship to Time

The cost metric is initially spatial/relational.

Computational update count:

\[
t
\]

is treated separately.

This preserves the CBR distinction:

> **space may be relational metric structure; time may be computational change.**

Later experiments can investigate causal spacetime relations.

---

# 62. Propagation Speed

Even before a full spacetime model, E006 can measure the rate at which information propagates with respect to computational distance.

If one computational update allows local transmission, define:

\[
v_{\mathrm{eff}}
=
\frac{
\Delta d_C
}{
\Delta t
}.
\]

The distribution of propagation velocities becomes an observational metric.

---

# 63. Candidate Causal Cone

If there exists a stable maximum:

\[
v_{\max},
\]

then reachable regions after \(t\) updates satisfy approximately:

\[
d_C\leq v_{\max}t.
\]

This begins to define a computational causal cone.

It is exploratory in E006 and becomes central to later experiments.

---

# 64. Metric and Information Propagation Agreement

A stronger geometry should align distance with propagation difficulty.

For random pairs \(A,B\), compare:

\[
d_C(A,B)
\]

with measured propagation time:

\[
\tau(A,B).
\]

A strong monotonic relationship:

\[
\tau
\sim
f(d_C)
\]

would indicate that the metric has operational meaning.

---

# 65. Operational Distance

This motivates a stronger definition:

> Two states are far apart if causal influence requires greater computational work or time to propagate between them.

Thus metric becomes measurable internally rather than imposed externally.

This is particularly important for CBR.

---

# 66. Internal Observer Test

Introduce an observer-like process that has access only to:

- local interactions;
- transition counts;
- message propagation times.

Do not provide the observer with the global graph.

Ask whether it can infer:

\[
d_C
\]

from local experiments.

If so, emergent distance becomes operationally observable from within the system.

---

# 67. Why Internal Observability Matters

A metric that exists only because an external researcher runs Dijkstra's algorithm over the entire graph is mathematically valid but physically less compelling.

A stronger result is:

> **embedded computational processes can infer the same geometry from local observations.**

This becomes an important secondary E006 track.

---

# 68. E006-D — Internal Metric Reconstruction

Create local probes.

Each probe can:

- emit signals;
- receive signals;
- count computational steps;
- record local transition costs.

It cannot inspect global topology.

Then estimate:

\[
\hat d(A,B).
\]

Compare:

\[
\hat d(A,B)
\]

with externally calculated:

\[
d_C(A,B).
\]

---

# 69. Reconstruction Error

Define:

\[
E_d
=
\frac{
|\hat d-d_C|
}{
d_C
}.
\]

If:

\[
E_d\rightarrow0
\]

with increasing observations, the geometry is internally discoverable.

That is significantly more compelling than a purely external metric.

---

# 70. E006 Tracks

The complete experiment should therefore be divided into:

### E006-A — Uniform Metric Baseline

Topology-only graph distance.

### E006-B — Endogenous Computational Costs

Static costs generated from local computational properties.

### E006-C — Dynamic Metric

Costs evolve through local computational activity.

### E006-D — Internal Reconstruction

Embedded probes infer the emergent metric without global graph access.

---

# 71. Proposed Initial Cost Function

For the first confirmatory E006-B experiment, use an intentionally simple local rule.

For edge \(e=(i,j)\):

\[
c_e=
1+
\alpha
\frac{
q_i+q_j
}{
2
}
\]

where:

\[
q_i\in[0,1]
\]

is the normalised recent local update activity around node \(i\).

Suggested preregistered:

\[
\alpha\in\{0,0.25,0.5,1,2\}.
\]

The value:

\[
\alpha=0
\]

is the uniform-cost control.

---

# 72. Cost Update Window

Let local activity be measured across a fixed window:

\[
W
\]

computational updates.

For example:

\[
W=100.
\]

Then:

\[
q_i(t)
\]

is based only on activity during:

\[
[t-W,t].
\]

The precise normalisation must be specified before execution.

---

# 73. Primary Comparison

Compare endogenous placement:

\[
C_E
\]

against cost-shuffled control:

\[
C_S.
\]

Both have identical:

\[
P(c)
\]

but different relationship to computational state.

The primary test asks whether:

\[
Q(C_E)
>
Q(C_S)
\]

for preregistered geometry-quality observables.

---

# 74. Statistical Unit

The unit of replication is an independently evolved or generated simplicial trajectory.

Do not treat every pairwise distance inside one graph as an independent experimental sample.

This avoids pseudoreplication.

---

# 75. Proposed Baseline Scale

A first institutional run might use:

```text id="75c8ox"
Independent trajectories:     100
Tetrahedra per trajectory:  1000–5000
Cost models:                    5
Master seeds per model:        20
Checkpoints:                   10+
```

Followed by matched control datasets.

---

# 76. Independent Implementation

Recommended split:

```text id="a7ksul"
Simulation:
CBR-Lab / Python

Independent metric engine:
Julia or Rust

Independent topology verifier:
specialist topology software

Statistical analysis:
separate group
```

This prevents the same code from generating and validating every level.

---

# 77. Run Dataset

Each checkpoint may record:

```yaml id="x32ip0"
metric_state:

  experiment:
    id: "CBR-E006"

  trajectory:
    id: "<id>"

  step: 50000

  topology:
    tetrahedra: 4210
    manifold_score: 1.0

  cost_model:
    type: "local_activity"
    alpha: 0.5
    window: 100

  cost_statistics:
    mean: 1.21
    stddev: 0.14

  geometry:
    cost_ball_dimension: 2.91
    spectral_dimension: 3.04
    homogeneity_score: 0.87
    isotropy_score: 0.82
    geodesic_stability: 0.79

  controls:
    shuffled_cost_geometry_id: "<id>"
```

---

# 78. Pairwise Metric Dataset

Sample reference pairs:

```yaml id="4kwqfy"
pair:
  a: 1042
  b: 2981

  graph_distance: 17

  computational_distance: 21.73

  propagation_time: 23

  geodesic_count_estimate: 4

  previous_checkpoint_distance: 21.68
```

This allows independent metric analysis.

---

# 79. Negative Results

Important negative results include:

> Computational cost produces no more coherent geometry than shuffled weights.

or:

> Metric structure is unstable under coarse-graining.

or:

> Distance changes catastrophically after microscopic local rewrites.

or:

> Internal agents cannot reconstruct the externally calculated metric.

or:

> Effective geometry is indistinguishable between manifold and non-manifold controls.

Any of these would materially constrain the proposed CBR interpretation.

---

# 80. Weak Positive Result

A weak positive result would be:

> Local computational costs generate reproducible weighted shortest-path structure that differs from shuffled controls.

Interesting, but not sufficient to claim emergent physical geometry.

---

# 81. Strong Positive Result

A stronger result would show:

\[
d_C
\]

is:

- reproducible;
- coarse-grain stable;
- approximately homogeneous;
- approximately isotropic;
- correlated with propagation time;
- inferable by embedded observers;
- robust across microscopic cost models.

This would justify treating \(d_C\) as a genuine emergent geometry candidate.

---

# 82. Strongest E006 Result

The most significant possible result would be evidence for universality:

\[
\boxed{
\text{different microscopic computational cost rules}
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{same large-scale metric regime}
}
\]

combined with:

\[
\boxed{
\text{internal observers recover that metric operationally}.
}
\]

That would suggest geometry is not a convenient external description alone.

It would behave like an internally accessible emergent property.

---

# 83. Interpretation Boundary

Even a strong E006 result would not establish:

- general relativity;
- gravity;
- spacetime curvature;
- Einstein's equations;
- physical metres;
- the observed universe.

It would establish something narrower:

> **A stable, operationally meaningful metric geometry can emerge from local computational cost on a coordinate-free relational substrate.**

That is the appropriate conclusion.

---

# 84. Relationship to CBR-E007

CBR-E006 establishes:

\[
\text{computation}
\rightarrow
\text{metric}.
\]

CBR-E007 introduces persistent computational structures and asks:

> **Do persistent structures systematically alter the computational cost field and therefore the emergent metric around them?**

This begins:

\[
\boxed{
\text{structure}
\rightarrow
\text{metric distortion}
}
\]

which is the first experimental step toward computational curvature.

---

# 85. Relationship to CBR-E008

If E007 establishes metric distortion around persistent structures, E008 can release another structure and ask:

> **Does it naturally follow minimum-cost trajectories through that distorted metric?**

The chain would become:

\[
\text{persistent structure}
\rightarrow
\text{cost redistribution}
\rightarrow
\text{metric distortion}
\rightarrow
\text{geodesic motion}.
\]

Only then does the CBR gravity-as-arbitrage hypothesis become experimentally meaningful.

---

# 86. CBR-E006 YAML Summary

```yaml id="3fk5zl"
cbr_oen:
  protocol_version: "1.0"

experiment:
  id: "CBR-E006"
  version: "1.0"

  title:
    "Emergent Metric Geometry from Computational Transition Cost"

hypothesis:
  id: "CBR-H006"

  statement: >
    Local computational transition costs on a coordinate-free
    relational substrate can generate stable and operationally
    meaningful large-scale metric geometry.

null_hypothesis: >
  Computational transition costs produce no reproducible
  geometric structure beyond generic weighted-network effects.

substrate:
  type: "explicit_simplicial_complex"

  preferred_adjacency:
    "tetrahedral_dual_graph"

  spatial_coordinates:
    enabled: false

metric:
  definition: >
    Minimum accumulated computational transition cost
    over all relational paths between two states.

  formula:
    "d_C(A,B) = min_gamma sum_e c_e"

  edge_cost:
    positive: true
    symmetric_baseline: true

tracks:

  E006_A:
    name: "Uniform Cost Baseline"
    cost: 1

  E006_B:
    name: "Endogenous Computational Cost"

  E006_C:
    name: "Dynamic Computational Metric"

  E006_D:
    name: "Internal Metric Reconstruction"

measurements:
  observational_only:

    - cost_ball_dimension
    - spectral_dimension
    - temporal_metric_stability
    - scale_stability
    - relational_isotropy
    - relational_homogeneity
    - geodesic_stability
    - propagation_time
    - internal_reconstruction_error

controls:

  - uniform_cost
  - shuffled_cost
  - static_cost
  - matched_cost_distribution
  - random_network
  - non_manifold_complex

forbidden_inputs:

  - spatial_coordinates
  - euclidean_distance
  - target_dimension
  - curvature_target
  - physical_length
  - gravitational_potential

primary_endpoint: >
  Determine whether locally generated computational transition
  costs produce reproducible coarse-grain-stable metric geometry
  beyond matched weighted-network controls.

replication:
  independent_metric_implementation_required_for_r2: true
  institutional_replication_required_for_r3: true

negative_results:
  retained: true
```

---

# 87. Experimental Progression

The CBR-OEN sequence now becomes:

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
\text{Does dimension-blind selection organise it?}
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
\text{Can explicit manifold topology support local dynamics?}
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

\[
\downarrow
\]

\[
\boxed{
E006:
\text{Can computational cost become distance?}
}
\]

This is a major conceptual transition.

Up through E005, CBR-OEN is primarily investigating:

\[
\text{topological organisation}.
\]

From E006 onward, it begins investigating:

\[
\text{physical geometry}.
\]

---

# 88. Final Principle

CBR-E006 tests a deceptively simple inversion.

Conventional thinking begins with distance and asks how difficult it is to move between two locations.

CBR-E006 begins with computational difficulty and asks whether **distance itself can emerge from it**.

Thus:

\[
\boxed{
\text{not}
\quad
\text{distance}\rightarrow\text{cost}
}
\]

but:

\[
\boxed{
\text{cost}\rightarrow\text{distance}.
}
\]

If local computational transition costs produce a stable geometry that is reproducible, coarse-grain invariant, operationally measurable and discoverable by embedded observers, then distance no longer needs to be treated as a primitive quantity of the model.

It becomes an emergent description of computational accessibility.

That is the scientific purpose of CBR-E006.