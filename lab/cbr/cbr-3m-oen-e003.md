# CBR-OEN Experiment CBR-E003
## Local 3-Manifold Emergence in Geometry-Free Computational Systems
### Preregistered Experimental Specification — Draft v1.0

---

## 1. Experiment Identity

**Experiment ID:** CBR-E003  
**Version:** 1.0  
**Title:** Local 3-Manifold Emergence in Geometry-Free Computational Systems  
**Protocol:** CBR-OEN Experimental Protocol v1.0  
**Experiment class:** Confirmatory computational and mathematical experiment  
**Predecessors:** CBR-E001, CBR-E002

---

# 2. Scientific Question

CBR-E003 asks:

> **When a geometry-free computational system exhibits effective dimensional behaviour near three, does the underlying relational structure also possess local topology consistent with a 3-manifold?**

This distinction is critical.

A graph may exhibit:

\[
d_H \approx 3
\]

or:

\[
d_S \approx 3
\]

without representing anything resembling a 3-manifold.

CBR-E003 therefore tests whether apparent three-dimensional scaling corresponds to genuine local topological structure.

---

# 3. Core Hypothesis

### CBR-H003

A subset of geometry-free computational systems exhibiting effective dimension near three will also develop local topological structure compatible with a 3-manifold.

Conceptually:

\[
\text{relational computation}
\rightarrow
d\approx3
\rightarrow
\text{local 3-manifold structure}.
\]

The experiment tests whether the second implication actually occurs.

---

# 4. Null Hypothesis

The null hypothesis is:

> Apparent three-dimensional scaling in geometry-free computational systems does not correspond to local 3-manifold topology and can instead be explained by graph-scaling behaviour, finite-size effects, clique structure or other non-manifold network properties.

Thus:

\[
d\approx3
\not\Rightarrow
M^3.
\]

---

# 5. Why CBR-E003 Is Necessary

CBR-E001 asks:

> Can effective dimension emerge?

CBR-E002 asks:

> Can dimension-blind selection organise dimensional behaviour?

Neither establishes manifold structure.

A generic network may possess effective spectral dimension three while containing:

- singular vertices;
- branching topology;
- non-manifold junctions;
- high-dimensional cliques;
- disconnected links;
- local holes;
- arbitrary simplicial defects.

CBR-E003 therefore imposes a substantially stronger requirement.

---

# 6. Mathematical Basis

For an interior vertex \(v\) of a triangulated 3-manifold \(M\), the vertex link satisfies:

\[
\operatorname{Lk}(v)\cong S^2.
\]

Informally, a sufficiently small neighbourhood around every regular interior point must look like a 3-ball.

The boundary surrounding the point therefore looks like a 2-sphere.

This gives CBR-E003 its central local test:

\[
\boxed{
\operatorname{Lk}(v)\approx S^2
}
\]

for a large fraction of sampled vertices.

---

# 7. Experimental Input

CBR-E003 does not search directly for 3-manifolds.

Its primary inputs are structures generated independently through registered computational experiments such as:

- CBR-E001 rule populations;
- CBR-E002 evolved rule populations;
- matched random controls;
- neutral-evolution controls.

This prevents topology from influencing the generative process.

---

# 8. Selection Independence

For structures originating from CBR-E002, the evolutionary fitness remains:

\[
F=
0.40P+
0.35C+
0.25S.
\]

The following remain prohibited fitness inputs:

```text id="z5y4lu"
manifold score
homology
Euler characteristic
vertex-link topology
S² similarity
dimension target
distance from dimension 3
```

Topology is measured only after the structures exist.

---

# 9. Candidate Selection

A preregistered rule determines which structures enter the manifold analysis.

One baseline criterion is:

\[
|d_H-3|\leq\epsilon_H
\]

and:

\[
|d_S-3|\leq\epsilon_S.
\]

Example preregistered tolerance:

\[
\epsilon_H=\epsilon_S=0.6.
\]

Therefore a candidate must satisfy:

\[
2.4\leq d_H\leq3.6
\]

and:

\[
2.4\leq d_S\leq3.6.
\]

These thresholds must be frozen before confirmatory execution.

---

# 10. Important Anti-Selection Rule

Candidate thresholds may determine which structures receive expensive topology analysis.

They may not modify the computational dynamics.

In particular, a simulation may not adapt itself toward passing the manifold tests.

---

# 11. From Graph to Simplicial Complex

CBR-E003 v1.0 initially interprets the generated graph as a **flag or clique complex**.

Given graph:

\[
G=(V,E),
\]

every complete subgraph of \(k+1\) vertices becomes a \(k\)-simplex.

Thus:

```text id="e193zl"
vertex       → 0-simplex
edge         → 1-simplex
triangle     → 2-simplex
4-clique     → 3-simplex
```

This creates:

\[
K(G).
\]

---

# 12. Limitation of the Flag-Complex Model

The clique-complex interpretation is intentionally conservative and reproducible, but restrictive.

A graph does not contain enough information to represent every possible simplicial complex.

In a flag complex:

> every clique is automatically filled.

Consequently, CBR-E003 must not claim that failure under the flag-complex representation proves that no alternative higher-order representation could be manifold-like.

This limitation motivates CBR-E004.

---

# 13. Vertex Link

For vertex \(v\), define the simplicial link:

\[
\operatorname{Lk}(v).
\]

In the flag-complex representation, this corresponds to the clique complex induced by neighbours of \(v\), excluding \(v\) itself.

For a regular interior point of a 3-manifold:

\[
\operatorname{Lk}(v)\simeq S^2.
\]

---

# 14. Test 1 — Link Connectedness

The link must be connected:

\[
\beta_0=1.
\]

A disconnected link indicates multiple locally separated regions meeting at one vertex.

Such a vertex is not locally manifold-like.

---

# 15. Test 2 — Euler Characteristic

For a 2-sphere:

\[
\chi(S^2)=2.
\]

For a finite simplicial complex:

\[
\chi
=
V-E+F.
\]

Thus the preregistered test requires:

\[
\chi(\operatorname{Lk}(v))=2.
\]

---

# 16. Test 3 — Homology

Over the preregistered coefficient field, initially:

\[
\mathbb{Z}_2,
\]

the homology of \(S^2\) is:

\[
H_0(S^2)=\mathbb{Z}_2,
\]

\[
H_1(S^2)=0,
\]

\[
H_2(S^2)=\mathbb{Z}_2.
\]

Therefore the required Betti signature is:

\[
\boxed{
(\beta_0,\beta_1,\beta_2)
=
(1,0,1)
}
\]

for an \(S^2\)-like link.

---

# 17. Test 4 — Dimensional Purity

A valid 2-sphere link should not itself be filled with unintended 3-simplices.

Therefore the baseline flag-complex test requires:

\[
N_3(\operatorname{Lk}(v))=0.
\]

This helps reject links that are locally higher-dimensional.

---

# 18. Test 5 — Triangle Incidence

For a closed triangulated 2-manifold, every edge belongs to exactly two triangles.

For edge \(e\):

\[
I(e)=
|\{
f:
e\subset f
\}|.
\]

The ideal condition is:

\[
I(e)=2
\]

for every link edge.

Because generated structures may be noisy, the baseline candidate threshold may initially allow:

\[
\frac{
|\{e:I(e)=2\}|
}{
|E_{\text{link}}|
}
\geq0.90.
\]

A stricter confirmatory version should test:

\[
100\%.
\]

---

# 19. Local S² Classifier

A vertex link passes the baseline \(S^2\) test if:

1. link is connected;

2. \(\chi=2\);

3. \((\beta_0,\beta_1,\beta_2)=(1,0,1)\);

4. no 3-simplices exist in the link;

5. at least 90% of link edges have triangle incidence two.

Define:

\[
L(v)=
\begin{cases}
1,&\text{if all tests pass}\\
0,&\text{otherwise}.
\end{cases}
\]

---

# 20. Local Manifold Score

For sampled vertices:

\[
v_1,\ldots,v_n,
\]

define:

\[
M_L=
\frac{1}{n}
\sum_{i=1}^{n}L(v_i).
\]

Thus:

\[
M_L\in[0,1].
\]

A value:

\[
M_L=1
\]

means all sampled links pass the local \(S^2\) test.

---

# 21. Candidate 3-Manifold Classification

A baseline structure may receive:

```text id="fngmkj"
CANDIDATE_3_MANIFOLD
```

if:

\[
|d_H-3|\leq0.6,
\]

\[
|d_S-3|\leq0.6,
\]

and:

\[
M_L\geq0.65.
\]

This is a candidate classification only.

It is not a proof of global manifold structure.

---

# 22. Classification States

Every analysed structure receives one of:

```text id="68t9ib"
CANDIDATE_3_MANIFOLD

3D_SCALING_NOT_MANIFOLD

MANIFOLD_LIKE_LINKS_NON3D_SCALING

NO_3_MANIFOLD_EVIDENCE
```

These categories separate scaling from topology.

---

# 23. Primary Endpoint

The primary endpoint is:

> **Whether structures generated without topology as an optimisation objective exhibit a rate of \(S^2\)-like vertex links significantly greater than matched control structures.**

The primary endpoint is therefore not simply the existence of one attractive example.

It is population-level enrichment.

---

# 24. Primary Comparison

Define:

\[
M_E
\]

as local manifold score for candidate structures from the experimental computational process.

Define:

\[
M_C
\]

as the corresponding score for matched controls.

The primary test concerns whether:

\[
M_E>M_C
\]

in a reproducible and statistically significant manner.

---

# 25. Control A — Degree-Preserving Randomisation

For every candidate graph:

1. preserve the degree sequence;

2. randomise edges;

3. recompute dimensionality and local topology.

This tests whether manifold-like structure is explained simply by degree distribution.

---

# 26. Control B — Clustering-Matched Networks

Construct control graphs with similar:

- node count;
- edge count;
- mean degree;
- clustering.

Then compare:

\[
M_L.
\]

---

# 27. Control C — Random Graphs

Use matched random-network families.

Potential controls include:

- Erdős–Rényi;
- random regular;
- configuration-model networks.

---

# 28. Control D — Non-Evolved Rule Population

Compare topology from:

\[
\text{CBR-E002 evolved rules}
\]

with topology from:

\[
\text{randomly sampled rules}.
\]

This tests whether evolution increases local manifold structure accidentally.

---

# 29. Control E — Dimension-Matched Controls

This is particularly important.

Select control networks satisfying:

\[
d_H\approx3
\]

and:

\[
d_S\approx3,
\]

then compare manifold scores.

This directly tests:

> Is local manifold topology something more than simply having dimension near three?

---

# 30. Sampling Vertices

For large structures, exhaustive local topology analysis may be expensive.

The preregistered analysis may therefore sample:

\[
n_v
\]

vertices per graph.

Proposed baseline:

```text id="tivkdo"
Topology sample: 50 vertices per graph
```

Sampling must be deterministic from the registered seed.

---

# 31. Sampling Eligibility

Vertices whose links are too small to meaningfully test may be labelled:

```text id="ilweic"
INELIGIBLE_LINK_SIZE
```

They must not silently disappear.

The proportion of ineligible vertices is itself recorded.

---

# 32. Global Topology

Where computationally practical, CBR-E003 should also calculate global homology:

\[
H_k(K(G)).
\]

This may include:

\[
\beta_0,\beta_1,\beta_2,\beta_3.
\]

However, no particular global topology is required in E003.

For example, a 3-torus and \(S^3\) are both 3-manifolds with different global homology.

---

# 33. Local Versus Global Manifoldness

The experiment must distinguish:

\[
\text{locally manifold-like}
\]

from:

\[
\text{globally identified manifold}.
\]

CBR-E003 primarily tests the former.

More rigorous global classification belongs to subsequent mathematical analysis.

---

# 34. Boundary Conditions

A 3-manifold may have a boundary.

For a vertex on the boundary:

\[
\operatorname{Lk}(v)
\]

may resemble a 2-disk rather than \(S^2\).

CBR-E003 v1.0 initially focuses on **closed-manifold-like interior structure**.

Boundary-manifold detection should be a registered extension.

---

# 35. Singular Vertices

A structure may be mostly manifold-like but contain isolated singular vertices.

Define:

\[
\rho_{\text{singular}}
=
1-M_L.
\]

The distribution and persistence of singularities should be recorded.

This may become important in later CBR studies.

---

# 36. Defect Geography

If non-manifold links appear, record whether defects:

- cluster;
- remain isolated;
- propagate;
- disappear;
- correlate with high degree;
- correlate with dimensional variation.

These analyses are secondary and exploratory in E003.

---

# 37. Dimensional Agreement

Record:

\[
\Delta_d=
|d_H-d_S|.
\]

Test whether manifold score correlates with:

\[
\Delta_d.
\]

For example, one possibility is:

\[
M_L\uparrow
\quad\text{as}\quad
\Delta_d\downarrow.
\]

This must not be assumed in advance.

---

# 38. Local Dimensionality

Where feasible, estimate dimension around each tested vertex.

Then compare local dimension with local topology.

This enables questions such as:

> Do \(S^2\)-link vertices also lie inside regions with locally three-dimensional volume growth?

A stronger candidate would exhibit both.

---

# 39. Finite-Size Scaling

Repeat candidate topology analysis for:

\[
N=
250,\;
500,\;
1000,\;
2000,\;
4000.
\]

A credible manifold-like phenomenon should not vanish as system size increases.

Measure:

\[
M_L(N).
\]

Possible evidence of convergence would be:

\[
M_L(N)
\rightarrow M_\infty>0.
\]

A particularly strong result would approach:

\[
M_\infty\rightarrow1.
\]

---

# 40. Strong-Manifold Threshold

If exploratory experiments indicate high manifold scores, a subsequent stricter preregistered test should require:

\[
M_L\geq0.95
\]

or ultimately:

\[
M_L=1
\]

for all eligible vertices.

The current 65% threshold is intended only as an early candidate-detection threshold.

---

# 41. Cross-Seed Replication

Candidate manifold emergence must occur across independent seeds.

The scientific unit of interest is therefore:

\[
P(M_L\mid R)
\]

rather than:

\[
M_L
\]

for a single graph.

---

# 42. Cross-Rule Replication

If one particular rule family produces local manifold structure, test neighbouring rule configurations.

A robust phenomenon should occupy a non-zero region of rule space.

A result that exists only at one extremely fine-tuned parameter vector requires stronger scrutiny.

---

# 43. Cross-Implementation Replication

At least one implementation of the topology pipeline should be independent of CBR-Lab.

For example:

```text id="vmz5a0"
Reference simulation:
Python

Independent topology validation:
SageMath / GAP / Regina / custom C++ / Julia
```

Ideally the simulation and topology calculation are implemented by different groups.

---

# 44. Mathematical Verification Group

CBR-E003 particularly benefits from institutional separation.

Recommended roles:

```text id="ig4wr7"
Simulation Group
generates candidate structures

Topology Group
defines and calculates manifold tests

Statistics Group
performs comparison with controls

Replication Group
repeats the experiment
```

The Topology Group should be encouraged to strengthen or reject the proposed classifier.

---

# 45. Blinded Topology Analysis

A topology group may receive complexes identified only as:

```text id="xp4mtl"
K-0001
K-0002
K-0003
...
```

without knowing whether each is:

- evolved;
- random;
- degree-matched;
- dimension-matched.

Labels are revealed only after registered tests are complete.

---

# 46. Expected Dataset Structure

Each candidate graph produces:

```yaml id="evbuwr"
structure:
  id: "<structure-id>"

  source:
    experiment: "CBR-E002"
    genome: "<genome-id>"
    seed: "<seed>"

  dimension:
    hausdorff_like: 2.94
    spectral: 3.07

  topology:
    sampled_vertices: 50
    eligible_vertices: 48

    s2_links: 39

    local_manifold_score: 0.8125

    singular_fraction: 0.1875

  classification:
    "CANDIDATE_3_MANIFOLD"
```

---

# 47. Vertex-Level Dataset

Each vertex test should be retained.

Example:

```yaml id="9dpx1r"
vertex:
  id: 175

  link:
    vertices: 8
    edges: 18
    triangles: 12

    connected: true

    euler_characteristic: 2

    betti:
      beta0: 1
      beta1: 0
      beta2: 1

    triangle_incidence_two_fraction: 1.0

    higher_simplices: 0

  result:
    s2_link: true
```

This makes the manifold classifier independently auditable.

---

# 48. Primary Evidence Conditions

Evidence supporting CBR-H003 requires:

1. candidate structures exhibit reproducible local \(S^2\)-like links;

2. manifold scores exceed matched controls;

3. results survive dimension-matched controls;

4. results persist under increasing system size;

5. independent topology implementations reproduce the finding;

6. no hidden topology target existed in the generating fitness.

---

# 49. Failure Conditions

CBR-E003 fails to support CBR-H003 if:

- \(d\approx3\) structures have negligible manifold score;
- random dimension-matched controls perform equally well;
- the result disappears at larger \(N\);
- local links systematically contain singularities or higher-dimensional fillings;
- independent homology calculations disagree;
- results depend on the clique-complex interpretation in a non-robust way.

Any such failure remains a meaningful result.

---

# 50. Especially Important Negative Result

One particularly important possible outcome is:

\[
d_H\approx d_S\approx3
\]

while:

\[
M_L\approx0.
\]

This would demonstrate that:

> **emergent three-dimensional scaling does not imply emergent three-dimensional space in the manifold sense.**

Such a result would materially constrain CBR.

---

# 51. Strong Positive Result

A substantially stronger result would be:

\[
d_H\approx3,
\]

\[
d_S\approx3,
\]

\[
M_L\rightarrow1
\]

with increasing system size, without any dimensional or manifold objective being encoded.

That would justify deeper investigation.

It would still not establish that the resulting structure reproduces physical space.

---

# 52. Relationship to CBR-E004

CBR-E003 uses a graph-derived flag complex.

CBR-E004 removes this limitation by making higher-order simplices explicit computational objects:

\[
V,\;
E,\;
F,\;
T.
\]

Thus topology can evolve independently of clique completion.

CBR-E004 asks:

> **Can local simplicial computation produce and dynamically maintain genuine 3-manifold structures?**

---

# 53. Relationship to CBR-E005

CBR-E005 introduces topology-destroying defects.

It then asks whether selection based only on computational properties such as persistence, complexity and stability causes those defects to be suppressed.

Conceptually:

\[
\text{manifold}
+
\text{defects}
+
\text{dimension-blind selection}
\]

followed by measurement of:

\[
p_{\text{defect}}.
\]

---

# 54. CBR-E003 YAML Summary

```yaml id="4av1pb"
cbr_oen:
  protocol_version: "1.0"

experiment:
  id: "CBR-E003"
  version: "1.0"

  title:
    "Local 3-Manifold Emergence in Geometry-Free Computational Systems"

hypothesis:
  id: "CBR-H003"

  statement: >
    A reproducible subset of geometry-free computational
    structures with effective dimension near three will
    develop local topology compatible with a 3-manifold.

null_hypothesis: >
  Three-dimensional scaling does not correspond to
  local 3-manifold structure beyond matched controls.

generation:
  topology_in_fitness: false
  dimension_in_fitness: false

candidate_dimension:
  target: 3.0
  hausdorff_tolerance: 0.6
  spectral_tolerance: 0.6

representation:
  type: "flag_complex"

local_manifold_test:
  expected_vertex_link: "S2"

  requirements:
    connected: true

    euler_characteristic: 2

    betti:
      beta0: 1
      beta1: 0
      beta2: 1

    link_3_simplices: 0

    edge_triangle_incidence_two:
      minimum_fraction: 0.90

sampling:
  vertices_per_structure: 50

candidate_classification:
  minimum_s2_link_fraction: 0.65

controls:
  - random_graph
  - degree_preserving_randomisation
  - clustering_matched
  - dimension_matched
  - non_evolved_rule_population

primary_endpoint: >
  Determine whether generated structures exhibit
  significantly more S2-like vertex links than matched
  controls when topology has not influenced their generation.

negative_results:
  retained: true

independent_mathematical_validation:
  required_for_r3: true
```

---

# 55. Scientific Interpretation Boundary

If CBR-E003 succeeds, the appropriate conclusion is:

> **Some geometry-free computational systems can generate structures exhibiting both approximately three-dimensional scaling and local topology compatible with a 3-manifold.**

It would not establish:

> physical spacetime has been derived.

Further experiments would still need to address:

- explicit manifold dynamics;
- metric emergence;
- curvature;
- causal propagation;
- persistent matter-like structures;
- gravitational behaviour;
- Lorentz symmetry.

---

# 56. Final Principle

CBR-E003 introduces an important discipline into the research programme:

> **Do not confuse dimensional scaling with space.**

A structure becomes substantially more interesting only when independent mathematical properties begin to agree:

\[
\boxed{
d_H\approx3
}
\]

\[
\boxed{
d_S\approx3
}
\]

\[
\boxed{
\operatorname{Lk}(v)\approx S^2
}
\]

\[
\boxed{
\text{homology and incidence consistent with a 3-manifold}
}
\]

If these properties emerge together without having been placed into the computational objective, the result becomes much harder to dismiss as a superficial network analogy.

That is the scientific purpose of CBR-E003.