# CBR-OEN Experiment CBR-E004
## Explicit Simplicial Dynamics and 3-Manifold Stability
### Preregistered Experimental Specification — Draft v1.0

---

## 1. Experiment Identity

**Experiment ID:** CBR-E004  
**Version:** 1.0  
**Title:** Explicit Simplicial Dynamics and 3-Manifold Stability  
**Protocol:** CBR-OEN Experimental Protocol v1.0  
**Experiment class:** Confirmatory computational-topology experiment  
**Predecessors:** CBR-E001, CBR-E002, CBR-E003

---

# 2. Scientific Question

CBR-E004 asks:

> **Can a local computational system whose primitive state is an explicit simplicial complex evolve while preserving or generating 3-manifold structure, without relying on an externally imposed geometric embedding?**

This experiment moves beyond graph-derived topology.

Instead of inferring triangles and tetrahedra from cliques, higher-order simplices become explicit computational objects.

The state of the system is therefore topological rather than merely graph-like.

---

# 3. Core Hypothesis

### CBR-H004

Local rewrite dynamics over explicit simplicial complexes can sustain coherent 3-manifold topology using only combinatorial relationships between simplices.

Formally, let:

\[
K_t
\]

be a finite simplicial complex at computational step \(t\).

Then local computational transitions:

\[
K_t \xrightarrow{R} K_{t+1}
\]

can preserve or produce states satisfying the local manifold condition:

\[
\operatorname{Lk}(v)\cong S^2
\]

for regular vertices.

---

# 4. Null Hypothesis

The null hypothesis is:

> Local simplicial dynamics do not produce or maintain robust 3-manifold structure except where such structure is trivially guaranteed by the allowed moves or initial conditions.

This is an important distinction.

CBR-E004 must separate:

\[
\text{topology preserved by construction}
\]

from:

\[
\text{topology dynamically favoured}.
\]

The former is useful as a control.

The latter is the deeper CBR question.

---

# 5. Why E004 Is Different from E003

CBR-E003 begins with a graph:

\[
G=(V,E)
\]

and constructs a flag complex.

CBR-E004 instead begins directly with:

\[
K=(V,E,F,T)
\]

where:

- \(V\) = vertices;
- \(E\) = edges;
- \(F\) = triangular faces;
- \(T\) = tetrahedra.

This means:

> a clique is no longer automatically a filled simplex.

Higher-order topology becomes independent computational state.

---

# 6. Primitive Computational Objects

The minimum explicit structure is:

### 0-simplex

Vertex:

\[
v
\]

### 1-simplex

Edge:

\[
[v_0,v_1]
\]

### 2-simplex

Triangle:

\[
[v_0,v_1,v_2]
\]

### 3-simplex

Tetrahedron:

\[
[v_0,v_1,v_2,v_3].
\]

A tetrahedron is therefore not inferred from graph connectivity.

It exists only when explicitly present.

---

# 7. No Spatial Coordinates

No simplex receives:

```text
x
y
z
```

coordinates.

There is no Euclidean embedding.

There is no predefined metric.

The system knows only:

- incidence;
- adjacency;
- containment;
- local rewrite rules.

Thus:

\[
\text{topology exists before geometry}.
\]

---

# 8. State Representation

At time \(t\):

\[
K_t=(V_t,E_t,F_t,T_t).
\]

The closure condition must hold:

> If a simplex exists, all of its faces exist.

For tetrahedron:

\[
[v_0,v_1,v_2,v_3],
\]

the complex must also contain its four triangular faces, six edges and four vertices.

Implementations may store only maximal simplices if all lower-dimensional simplices can be deterministically reconstructed.

---

# 9. Baseline Initial State

The primary known-good control seed is the boundary of a 4-simplex.

A 4-simplex contains five vertices.

Its boundary consists of five tetrahedra and triangulates:

\[
S^3.
\]

The expected global homology is:

\[
(\beta_0,\beta_1,\beta_2,\beta_3)
=
(1,0,0,1).
\]

Every vertex link is:

\[
S^2.
\]

This gives E004 a mathematically clean control state.

---

# 10. Alternative Initial Conditions

Later preregistered sub-experiments should include:

### IC-A — \(S^3\) seed

Known manifold.

### IC-B — Other known closed 3-manifolds

For example suitable triangulations of:

- \(T^3\);
- lens spaces;
- other compact 3-manifolds.

### IC-C — Manifold with local defects

Used in E005-style extensions.

### IC-D — Non-manifold simplicial complex

Used to test whether manifold structure can arise rather than merely persist.

The primary E004 control begins with IC-A.

---

# 11. Pachner Moves

For triangulated manifolds, Pachner moves provide local transformations connecting triangulations of the same piecewise-linear manifold.

In three dimensions the move classes are:

\[
1\leftrightarrow4
\]

and:

\[
2\leftrightarrow3.
\]

These form the baseline local dynamics.

---

# 12. The 1→4 Move

A tetrahedron:

\[
[a,b,c,d]
\]

is replaced by a new vertex \(v\) and four tetrahedra:

\[
[v,a,b,c]
\]

\[
[v,a,b,d]
\]

\[
[v,a,c,d]
\]

\[
[v,b,c,d].
\]

This refines the triangulation locally.

It changes the number of simplices but preserves topology when performed validly.

---

# 13. The 4→1 Move

The inverse transformation removes an appropriate interior vertex surrounded by exactly the tetrahedral configuration corresponding to a prior 1→4 move.

Four tetrahedra collapse to one.

This provides local coarse-graining.

---

# 14. The 2→3 Move

Two tetrahedra sharing one triangular face are replaced by three tetrahedra sharing a new internal edge.

Schematically:

\[
2T\rightarrow3T.
\]

Topology remains unchanged under valid application.

---

# 15. The 3→2 Move

This is the inverse:

\[
3T\rightarrow2T.
\]

Three tetrahedra around a suitable internal edge are replaced by two tetrahedra sharing a face.

---

# 16. Pachner Completeness

For closed triangulated PL manifolds, two triangulations of the same manifold are related by a finite sequence of Pachner moves.

This makes Pachner moves attractive for CBR because they represent:

> **local computational change without requiring a background geometry.**

The computational system can evolve while the manifold identity remains invariant.

---

# 17. Baseline Rule Genome

The initial E004 rule family may define probabilities:

\[
R=
(w_{14},w_{41},w_{23},w_{32})
\]

with:

\[
w_i\geq0
\]

and:

\[
\sum_iw_i=1.
\]

At each computational step, one local move class is sampled.

If no valid instance exists, a registered fallback rule applies.

---

# 18. No Geometric Fitness

The baseline E004 control need not use evolutionary fitness at all.

Its first task is to establish:

> explicit local simplicial computation can execute for long periods while preserving manifold invariants.

This is a methodological foundation for later experiments.

---

# 19. Control Hypothesis

For valid Pachner-only dynamics starting from \(S^3\):

\[
K_0\cong S^3
\]

should imply:

\[
K_t\cong S^3
\]

for all valid steps \(t\).

Therefore expected invariants include:

\[
H_0=\mathbb{Z},
\]

\[
H_1=0,
\]

\[
H_2=0,
\]

\[
H_3=\mathbb{Z}.
\]

---

# 20. Primary Control Endpoint

The primary control endpoint is:

> **Whether independent implementations preserve the expected local and global topological invariants under long sequences of registered Pachner moves.**

This is primarily an implementation and methodology validation experiment.

---

# 21. Local Manifold Test

For every sampled or exhaustive vertex \(v\):

\[
\operatorname{Lk}(v)
\]

should be a triangulated \(S^2\).

The strict E004 test requires:

\[
\beta_0=1,
\]

\[
\beta_1=0,
\]

\[
\beta_2=1,
\]

and:

\[
\chi=2.
\]

Unlike E003's noisy candidate classifier, the pure manifold control should ideally require:

\[
100\%
\]

of vertices to pass.

---

# 22. Face Incidence

For a closed triangulated 3-manifold, every triangular face belongs to exactly two tetrahedra.

For face \(f\):

\[
I_T(f)=
|\{
T_i:f\subset T_i
\}|.
\]

The closed-manifold condition is:

\[
I_T(f)=2
\]

for all faces.

Define:

\[
F_C=
\frac{
|\{f:I_T(f)=2\}|
}{
|F|
}.
\]

For a valid closed control manifold:

\[
F_C=1.
\]

---

# 23. Global Homology

At preregistered checkpoints compute:

\[
\beta_0,\beta_1,\beta_2,\beta_3.
\]

For the \(S^3\) control:

\[
(1,0,0,1).
\]

If these change during pure valid Pachner evolution, one of the following is likely true:

- implementation error;
- invalid move application;
- homology computation error;
- corrupted state.

Such a result must be investigated before later experiments proceed.

---

# 24. Euler Characteristic

For a finite complex:

\[
\chi(K)
=
N_0-N_1+N_2-N_3.
\]

For every closed odd-dimensional manifold:

\[
\chi=0.
\]

Thus for \(S^3\):

\[
\chi=0.
\]

This provides an additional inexpensive invariant check.

---

# 25. Dual Graph

Each tetrahedron may be represented as a node in a dual graph.

Two dual nodes are connected when their tetrahedra share a triangular face.

This gives:

\[
G^*_K.
\]

The dual graph is useful for studying effective large-scale relational geometry without introducing coordinates.

---

# 26. Effective Dimension of the Dual Graph

CBR-E004 records the same observational metrics used previously.

### Ball-growth dimension

\[
N(r)\propto r^{d_H}.
\]

### Spectral dimension

\[
P(t)\propto t^{-d_S/2}.
\]

These do not affect the simplicial dynamics.

---

# 27. Why Dual-Graph Dimension Matters

The topology may remain exactly:

\[
S^3
\]

while the triangulation changes dramatically.

This allows a new question:

> **Can local topological computation reorganise the effective geometry of a fixed manifold?**

The manifold is invariant.

The effective relational geometry need not be.

This is an important distinction for CBR.

---

# 28. Topology Versus Geometry

E004 therefore separates:

\[
\text{topological identity}
\]

from:

\[
\text{effective geometry}.
\]

Two complexes may both triangulate \(S^3\) but have very different:

- graph distances;
- spectral dimension at finite scale;
- local density;
- simplex incidence distributions;
- diffusion properties.

This suggests a possible computational interpretation of geometry as state within fixed topology.

---

# 29. Primary Experimental Tracks

CBR-E004 should contain at least two tracks.

### E004-A — Topology Preservation

Pachner-only dynamics from known 3-manifold seeds.

### E004-B — Geometry Evolution Within Fixed Topology

Measure how dimension-like and diffusion-like properties evolve while topology remains invariant.

---

# 30. E004-A Hypothesis

### CBR-H004-A

Valid local simplicial rewrites can support indefinite computational evolution without requiring background coordinates while preserving 3-manifold structure.

This is expected mathematically under valid Pachner dynamics, so its primary role is experimental validation.

---

# 31. E004-B Hypothesis

### CBR-H004-B

Different local computational histories over the same topological 3-manifold can generate measurably different effective relational geometries.

This is more scientifically interesting.

It asks whether:

\[
\text{same topology}
+
\text{different computation}
\]

can yield:

\[
\text{different emergent geometry}.
\]

---

# 32. Geometry Observables

Candidate observables include:

- dual-graph diameter;
- ball-growth dimension;
- spectral dimension;
- average dual distance;
- local simplex density;
- vertex incidence distribution;
- face incidence;
- diffusion time;
- return probability.

None are encoded as spatial coordinates.

---

# 33. No Preferred Dimension in E004

Although the complexes are explicitly 3-dimensional simplicial complexes, E004 does **not** claim to explain why dimension three emerged.

That was the purpose of E001–E003.

E004 instead asks:

> once 3-dimensional topological organisation exists, can local computation act as its dynamical substrate?

This distinction should remain explicit.

---

# 34. Known-Manifold Control Set

To avoid overfitting to \(S^3\), later replication should include multiple known manifolds.

For each manifold \(M\):

\[
K_0\cong M
\]

and valid Pachner moves should preserve:

\[
K_t\cong M.
\]

Global homology and other invariants can verify this within their discriminatory limits.

---

# 35. Implementation Independence

At least two implementations should independently represent:

- tetrahedra;
- incidence;
- Pachner moves;
- local links;
- homology checks.

Suggested division:

```text id="m9w0p3"
Implementation A:
Python / CBR-Lab

Implementation B:
Julia / C++

Topology validation:
Regina / SageMath / GAP / independent mathematical code
```

No single software system should be trusted as both generator and sole verifier.

---

# 36. Move Manifest

Every successful local rewrite should optionally generate a compact record:

```yaml id="2n66ci"
move:
  step: 38129

  type: "2-3"

  removed:
    - [1,4,7,9]
    - [1,4,7,12]

  added:
    - [1,4,9,12]
    - [1,7,9,12]
    - [4,7,9,12]

  pre_state_hash: "<hash>"

  post_state_hash: "<hash>"
```

This allows individual topological transitions to be replayed.

---

# 37. State Checkpoints

Because storing every full complex may be expensive, define checkpoints.

For example:

```text id="9cd7fq"
step 0
step 100
step 1,000
step 10,000
step 100,000
final state
```

At each checkpoint store:

- complex hash;
- simplex counts;
- manifold diagnostics;
- topology invariants;
- geometry observables.

---

# 38. State Hashing

A canonical ordering of maximal tetrahedra should be used.

Each tetrahedron is sorted internally.

The tetrahedron list is sorted lexicographically.

Then:

\[
H_K
=
SHA256(
\operatorname{canonical}(T)
).
\]

This makes complex states content-addressable.

---

# 39. Move Acceptance

A proposed move may be:

```text id="k6pqyh"
VALID_ACCEPTED
INVALID_LOCAL_CONFIGURATION
DUPLICATE_SIMPLEX
NONMANIFOLD_RESULT
RESOURCE_LIMIT
```

In the pure Pachner control, invalid moves do not alter state.

All attempts may be counted.

---

# 40. Resource Guards

An unrestricted sequence of 1→4 and 2→3 moves can cause rapid growth.

Experiments may therefore preregister:

- maximum tetrahedron count;
- maximum vertex count;
- maximum memory;
- maximum steps.

Resource guards must not depend on topology or desired dimensional outcome.

For example:

> Once \(N_T\geq N_{max}\), only volume-reducing Pachner moves may be attempted.

This is an operational constraint, not scientific selection.

---

# 41. Growth-Balanced Dynamics

A useful experimental rule family may tune:

\[
w_{14},w_{41},w_{23},w_{32}
\]

to produce approximately stable average size.

This avoids runaway refinement while retaining local computational change.

The resulting stationary regime may be especially useful for geometric measurements.

---

# 42. Detailed-Balance Extension

A later version may explore whether move probabilities can satisfy a detailed-balance-like condition.

This could create an equilibrium distribution over triangulations.

The resulting ensemble could then be analysed statistically.

Such extensions must remain separate from the E004 v1.0 control.

---

# 43. Complexity Without Geometry

CBR-E004 may measure structural complexity through:

- vertex-incidence entropy;
- tetrahedron-adjacency diversity;
- local link diversity;
- move entropy;
- temporal state diversity.

These metrics can describe computational richness without assuming a metric space.

---

# 44. Stability Without Topology Target

A future evolutionary extension may optimise:

\[
F=
f(
\text{persistence},
\text{complexity},
\text{stability}
)
\]

while measuring manifold integrity only afterward.

This becomes CBR-E005.

E004 itself establishes the machinery required for that stronger test.

---

# 45. Baseline E004-A Run

A proposed validation run:

```text id="5okp1l"
Initial topology: S³
Initial tetrahedra: 5
Steps: 100,000
Master seeds: 100
Move family: Pachner only
Defect probability: 0
```

At every checkpoint require:

\[
F_C=1.
\]

And ideally:

\[
M_L=1.
\]

For feasible complex sizes:

\[
(\beta_0,\beta_1,\beta_2,\beta_3)
=
(1,0,0,1).
\]

---

# 46. Primary Validation Success

E004-A succeeds methodologically if:

1. all accepted moves are independently valid;

2. all closed-face incidence conditions remain satisfied;

3. all sampled or exhaustive vertex links remain \(S^2\);

4. global homology remains unchanged;

5. independent implementation reproduces the result.

This does not itself support a novel physical claim.

It validates the experimental substrate.

---

# 47. E004-B Run Design

For each manifold-preserving trajectory, record:

\[
d_H(t),
\]

\[
d_S(t),
\]

\[
D(t)
\]

and other graph/topological observables.

Then ask whether different rule weights generate reproducibly different geometric regimes.

For example:

\[
R_A
\rightarrow
d_S\approx2
\]

while:

\[
R_B
\rightarrow
d_S\approx3.
\]

If topology remains constant, the difference cannot be attributed to a topological change.

---

# 48. E004-B Primary Endpoint

> **Whether distinct local simplicial computational dynamics produce statistically distinct effective geometric regimes while preserving the same underlying 3-manifold topology.**

This begins to operationalise the CBR idea:

> **geometry may be a state of computation over topology rather than an immutable primitive.**

---

# 49. Controls for E004-B

Controls should include:

### Uniform move probabilities

Baseline random Pachner walk.

### Growth-matched ensembles

Ensure differences are not caused merely by tetrahedron count.

### Vertex-count matched states

Compare geometry at similar complex sizes.

### Move-count shuffled trajectories

Preserve move frequencies while perturbing sequence.

### Independent seeds

Test history dependence.

---

# 50. History Dependence

Two systems may have:

- identical topology;
- similar simplex counts;
- identical move frequency statistics;

yet different effective geometry because their computational histories differ.

This can be tested by comparing:

\[
K_t^{(A)}
\]

and:

\[
K_t^{(B)}.
\]

History-sensitive effects would be scientifically interesting.

---

# 51. Ergodicity Question

A later mathematical question is whether a chosen stochastic Pachner process explores triangulation space ergodically under the imposed resource constraints.

If not, apparent geometric regimes might be disconnected computational basins.

This should be analysed rather than assumed.

---

# 52. Computational Attractors

E004-B may reveal stable distributions over structural observables.

For example:

\[
P(d_S)
\]

may develop peaks under particular local dynamics.

These would be called:

> **computational geometric attractors**

provided they persist across seeds and system sizes.

No particular dimension is predeclared as desirable.

---

# 53. Finite-Size Scaling

For candidate geometric regimes, increase:

\[
N_T
\]

across preregistered scales.

For example:

\[
100,
500,
1000,
5000,
10000
\]

tetrahedra.

Measure:

\[
d_H(N_T),
\quad
d_S(N_T).
\]

A genuine large-scale regime should survive increasing triangulation size.

---

# 54. Local Geometry

The dual graph permits local measurements around each tetrahedron.

This allows investigation of spatial heterogeneity without coordinates.

For tetrahedron \(T\), calculate:

\[
N_T(r).
\]

A local effective dimension may then be estimated.

This enables detection of:

- homogeneous regions;
- dimensional gradients;
- local defects;
- multiple geometric phases.

---

# 55. Topological Invariance as Experimental Control

One powerful feature of E004 is that topology can serve as a fixed control variable.

If:

\[
K_t\cong S^3
\]

throughout the experiment, while geometric observables change, then:

\[
\Delta\text{geometry}
\]

occurs without:

\[
\Delta\text{topology}.
\]

This sharply separates two layers of CBR.

---

# 56. CBR Layering Suggested by E004

The experiment motivates:

\[
\boxed{
\text{Computation}
\rightarrow
\text{Topology}
\rightarrow
\text{Geometry}
}
\]

while showing that the second arrow need not be static.

A manifold may support many effective geometries generated by different computational arrangements.

---

# 57. Dataset Record

Each final trajectory should include:

```yaml id="yyqy7g"
trajectory:
  experiment: "CBR-E004"

  seed: 190273

  initial_topology:
    type: "S3"

  moves:
    attempted: 100000
    accepted: 82419

    counts:
      "1-4": 20620
      "4-1": 19881
      "2-3": 21142
      "3-2": 20776

  final_complex:
    vertices: 812
    tetrahedra: 2761

  manifold:
    closed_face_fraction: 1.0
    s2_link_fraction: 1.0

  homology:
    beta0: 1
    beta1: 0
    beta2: 0
    beta3: 1

  geometry:
    dual_ball_dimension: 2.74
    dual_spectral_dimension: 3.08
```

---

# 58. Negative Results

CBR-E004 must retain results such as:

> Valid Pachner dynamics preserve topology but show no stable effective geometric regime.

or:

> Apparent spectral dimension changes disappear under size matching.

or:

> Different rule weights produce no reproducible geometry difference.

These outcomes constrain the theory.

---

# 59. Stronger Positive Result

A stronger E004-B result would be:

\[
K_t\cong M^3
\]

for all \(t\),

while local rule family \(R_A\) consistently produces:

\[
d_A
\]

and rule family \(R_B\) produces:

\[
d_B
\neq
d_A
\]

across:

- seeds;
- system sizes;
- implementations.

That would indicate that effective geometry can be dynamically organised without changing topology.

---

# 60. Interpretation Boundary

Even a successful E004 does not show that physical spacetime is a simplicial complex.

It shows only that:

> local combinatorial computation is sufficient to support dynamically changing manifold triangulations and potentially distinct effective geometric regimes without external coordinates.

That is a meaningful but limited conclusion.

---

# 61. Relationship to CBR-E005

CBR-E004 uses topology-preserving Pachner moves.

This means manifold integrity is protected by the move set.

CBR-E005 removes that protection.

It introduces topology-agnostic mutations such as:

- arbitrary tetrahedron addition;
- arbitrary tetrahedron removal;
- invalid local reconnections;
- manifold-breaking defects.

Then it asks:

> **When manifold structure is allowed to fail, does dimension- and topology-blind selection favour rules that suppress those failures?**

This is the much stronger evolutionary test.

---

# 62. Why E005 Requires E004

Without E004, a failure in E005 could arise because:

- the simplicial implementation is wrong;
- link calculations are wrong;
- homology code is wrong;
- Pachner moves are wrong.

E004 establishes the verified control system.

Only then should defects be introduced.

---

# 63. CBR-E004 YAML Summary

```yaml id="zubt51"
cbr_oen:
  protocol_version: "1.0"

experiment:
  id: "CBR-E004"
  version: "1.0"

  title:
    "Explicit Simplicial Dynamics and 3-Manifold Stability"

state:
  representation:
    type: "explicit_simplicial_complex"

  dimensions:
    maximum_simplex_dimension: 3

  spatial_coordinates:
    enabled: false

initial_conditions:
  primary:
    type: "boundary_of_4_simplex"
    topology: "S3"

dynamics:
  type: "local_simplicial_rewrite"

  moves:
    - "1-4"
    - "4-1"
    - "2-3"
    - "3-2"

  defect_moves:
    enabled: false

topology_validation:
  closed_face_incidence:
    required: 1.0

  vertex_links:
    target: "S2"
    required_fraction: 1.0

  global_homology:
    expected:
      beta0: 1
      beta1: 0
      beta2: 0
      beta3: 1

  euler_characteristic:
    expected: 0

geometry_measurement:
  substrate: "tetrahedral_dual_graph"

  observational_only: true

  metrics:
    - ball_growth_dimension
    - spectral_dimension
    - graph_diameter
    - diffusion_return_probability

tracks:
  E004_A:
    question:
      "Do valid local Pachner dynamics preserve verified manifold structure?"

  E004_B:
    question:
      "Can distinct local dynamics generate different effective geometries
       while topology remains fixed?"

primary_constraints:
  geometry_in_dynamics: false
  coordinates_in_dynamics: false
  dimension_target: false

replication:
  independent_implementation_required_for_r2: true
  institutional_replication_required_for_r3: true

negative_results:
  retained: true
```

---

# 64. Primary Scientific Contribution

CBR-E004 introduces a new level into the experimental programme:

\[
\text{graphs}
\rightarrow
\text{explicit topology}.
\]

More importantly, it creates a laboratory in which:

\[
\text{topology}
\]

can remain constant while:

\[
\text{computational configuration}
\]

changes.

This makes it possible to investigate whether:

\[
\text{geometry}
\]

can be treated as an emergent dynamical property of computation over a manifold.

---

# 65. Final Principle

CBR-E004 should be interpreted through one central distinction:

> **Topology tells us how the computational structure is connected. Geometry may tell us how computation is distributed across those connections.**

Pachner dynamics allow the first to remain invariant while the computational arrangement changes.

That makes E004 a crucial experimental bridge.

The CBR progression is now:

\[
\boxed{
E001:
\text{Can dimension emerge?}
}
\]

\[
\boxed{
E002:
\text{Can dimension-blind evolution organise it?}
}
\]

\[
\boxed{
E003:
\text{Does 3D scaling correspond to manifold topology?}
}
\]

\[
\boxed{
E004:
\text{Can explicit manifold topology support computationally emergent geometry?}
}
\]

The next experiment removes the safety rail.

CBR-E005 asks whether manifold integrity remains favoured **when computation is allowed to destroy it**.