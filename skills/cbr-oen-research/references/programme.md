# E001-E010 Programme Reference

## Contents

1. Programme architecture
2. Experiment catalogue
3. Phase gates
4. Dependency discipline

## 1. Programme architecture

The v1.0 chain is:

`relations -> effective dimension -> 3-manifold topology -> topological dynamics -> operational metric -> persistent structures -> metric distortion -> geodesic response -> causal structure -> quantitative correspondence`

| Phase | Experiments | Question |
|---|---|---|
| 1 Emergent structure | E001-E003 | Can geometry-free computation produce dimensional and manifold-like structure? |
| 2 Topological dynamics | E004-E005 | Can 3-manifold organisation support local computation and remain robust without topology-directed selection? |
| 3 Emergent geometry | E006-E007 | Can transition cost act as distance, and can persistent computation modify it? |
| 4 Dynamics and causality | E008-E009 | Do free structures respond to the metric, and does local computation yield causal cones? |
| 5 Physical correspondence | E010 | Can one calibrated mechanism predict several weak-field effects? |

## 2. Experiment catalogue

### CBR-E001 — Emergent dimensionality

- **Question:** Can non-trivial effective dimension emerge from relational computation with no coordinates or predefined dimension?
- **Primary measures:** ball-growth/Hausdorff-like dimension and spectral dimension, with registered scale windows and estimator diagnostics.
- **Prohibit:** spatial coordinates, predefined or target dimension, dimension-based selection.
- **Controls:** random graphs, degree-matched ensembles, rule-null ensembles, finite-size and estimator-bias tests.
- **GO:** Non-trivial scaling is reproducible across seeds and sizes and differs from matched controls.
- **QUALIFY/REVISE:** Only one estimator is stable, or apparent scaling is scale-window/rule-family dependent.
- **STOP:** Broad, adequately powered controls leave no reproducible non-trivial dimensional structure.
- **Feeds:** E002 and E003.

### CBR-E002 — Dimension-blind evolution

- **Question:** Does selection for persistence, structural complexity, and stability reorganise dimensional distributions when dimension is excluded from fitness?
- **Prohibit in fitness:** dimension estimators, target dimension, manifold score, proxies selected because they predict dimension.
- **Controls:** random search, neutral evolution, shuffled fitness, fitness-component ablations, degree/size/compute-matched populations.
- **GO:** Selected populations show a registered, robust dimensional shift beyond neutral and matched controls.
- **QUALIFY/REVISE:** The effect is mediated by a known confound or is unstable across defensible fitness variants.
- **STOP:** No robust difference remains between selected and neutral populations.
- **Feeds:** E003; E003 does not require E002 to be positive.

### CBR-E003 — 3-manifold emergence

- **Question:** Do approximately three-dimensional relational structures possess local topology compatible with a 3-manifold?
- **Baseline representation:** explicitly declared graph-to-complex map, initially a flag/clique complex; treat representation dependence as a limitation.
- **Primary local test:** vertex links compatible with `S^2`; record connectedness, Euler characteristic, Betti numbers, orientability, and triangulation validity where feasible.
- **Primary endpoint:** enrichment of `S^2`-like vertex links, not merely dimensional proximity to 3.
- **Controls:** degree-, clustering-, size-, and dimension-matched randomisations; alternative complex constructions as sensitivity analyses.
- **GO:** Reproducible `S^2`-link enrichment survives dimension-matched controls and representation checks.
- **QUALIFY/REVISE:** A stable manifold-like subset exists, or the graph-to-complex map is inadequate.
- **STOP:** Three-dimensional scaling repeatedly yields no manifold evidence under reasonable higher-order representations.
- **Feeds:** E004.

### CBR-E004 — Explicit simplicial dynamics

- **Question A:** Can coordinate-free local simplicial rewrites preserve a known 3-manifold?
- **Question B:** Can different computational histories create different effective geometries at fixed topology?
- **State:** explicit 3-dimensional simplicial complex; higher simplices are state, not inferred cliques.
- **Baseline moves:** valid 3D Pachner `1<->4` and `2<->3` moves.
- **Control seed:** boundary of a 4-simplex triangulating `S^3`; broaden later to other known closed 3-manifolds.
- **Invariant checks:** every triangular face incident to two tetrahedra, every vertex link `S^2`, expected global homology, Euler characteristic, canonical state hash, and independently validated move manifests.
- **Geometry observables:** dual-graph dimension, diameter, diffusion, incidence distributions, and history dependence, measured without driving moves.
- **GO:** At least R2 preservation of registered invariants over long trajectories; distinct dynamics may also yield controlled geometric regimes at fixed topology.
- **REVISE:** Move validation, topology verification, or resource policy is unreliable.
- **STOP:** No independently valid simplicial dynamics substrate can be established.
- **Minimum downstream reproducibility:** R2.
- **Feeds:** E005 and E006.

### CBR-E005 — Manifold resilience under defects

- **Question:** When topology-breaking moves are permitted, does dimension- and topology-blind selection favour avoidance, resilience, or repair of manifold structure?
- **Require:** registered defect operators and rates; fitness based only on primitive persistence/complexity/stability measures; manifold diagnostics withheld from selection.
- **Controls:** neutral defective dynamics, no-defect baseline, defect-rate curves, shuffled fitness, fitness ablations, matched computational budgets, and explicit leakage audit.
- **Endpoints:** time to first defect, manifold-integrity trajectory, recovery probability/time, survival under out-of-distribution defects.
- **GO:** Selected systems retain or recover manifold structure more than matched neutral controls, including held-out defect regimes, without topology leakage.
- **QUALIFY/REVISE:** Robustness is defect-specific or explained by a registered generic structural mediator.
- **STOP:** No advantage remains, or the result depends on topology/dimension information entering selection.
- **Feeds:** strengthens—not automatically required for—E006+ robustness claims.

### CBR-E006 — Emergent operational metric

- **Question:** Can minimum computational transition cost define a stable, non-trivial operational distance?
- **Define:** state/event set, allowed transitions, local costs, directedness, temporal dependence, and whether a metric, pseudometric, quasi-metric, or path cost is claimed.
- **Validate:** non-negativity, identity or equivalence classes, symmetry where claimed, triangle inequality where claimed, connectivity, finite-size scaling, and robustness to equivalent encodings.
- **Controls:** unweighted shortest path, randomised costs, topology/size-matched complexes, alternate admissible cost definitions, and computational shortcut tests.
- **GO:** A reproducible operational distance with declared axioms supports stable large-scale geometry beyond graph-distance relabelling.
- **QUALIFY/REVISE:** Only a pseudometric/quasi-metric emerges, or conclusions depend materially on one cost convention.
- **STOP:** No non-circular, robust operational geometry survives controls.
- **Feeds:** E007 and E008.

### CBR-E007 — Structure-metric coupling

- **Question:** Do persistent computational structures systematically change the E006 metric?
- **Define structures independently:** identify persistence/localisation before testing metric effects; avoid selecting structures by their observed distortion.
- **Endpoints:** registered local and far-field changes in distances, transition costs, diffusion, or curvature proxies versus structure-free controls.
- **Controls:** energy/complexity/size-matched nonpersistent patterns, shuffled structure locations, substrate-only evolution, observer/probe independence, backreaction directionality, and dose-response.
- **GO:** Persistent structures cause reproducible metric distortion with temporal precedence, controls, and a transferable scaling relation.
- **QUALIFY/REVISE:** Association exists but causality, localisation, or probe independence is unresolved.
- **STOP:** Distortion vanishes under matched controls or is built into the metric definition.
- **Feeds:** E008 and E010.

### CBR-E008 — Emergent geodesic motion

- **Question:** Do freely evolving probe structures follow paths predicted by the emergent metric without explicit attraction?
- **Prohibit:** gravitational force, target-seeking rule, distance-to-source term, geodesic optimiser in probe dynamics, or trajectory fitting on the test set.
- **Design:** predict trajectories from E006/E007 geometry before releasing probes; use held-out initial positions, velocities, sources, and geometries.
- **Controls:** flat/undistorted substrate, reversed or shuffled distortion, nonpersistent probes, rule-null motion, conservation and discretisation checks.
- **GO:** Preregistered geometric predictions outperform non-geometric baselines on unseen trajectories with a shared parameterisation.
- **QUALIFY/REVISE:** Only qualitative bending or restricted-regime agreement appears.
- **STOP:** Motion requires an explicit attractive rule or is not predicted by the independently measured geometry.
- **Feeds:** E010.

### CBR-E009 — Emergent causality

- **Question:** Does local computation generate stable causal cones and an approximately universal limiting propagation speed?
- **Measure:** influence reachability, front velocity, anisotropy, dispersion, signal type dependence, scale dependence, and fluctuations.
- **Prohibit:** Lorentz transformations or a desired speed inserted as a fit target. A microscopic update bound may exist but is not itself emergent Lorentz symmetry.
- **Controls:** multiple signal types, directions, energies/scales, substrates, update schedules, and lattice/graph anisotropy tests.
- **GO:** A stable limiting speed and causal-cone structure emerge across signal classes with diminishing large-scale anisotropy and registered transformation tests.
- **QUALIFY/REVISE:** A bound exists but universality, isotropy, or boost-like symmetry is incomplete.
- **STOP:** Propagation remains signal-dependent or anisotropic without a convergent regime, or causality is merely restated from the scheduler.
- **Feeds:** E010 and later relativistic extensions.

### CBR-E010 — Quantitative physical correspondence

- **Question:** Can one emergent geometry and common parameter set predict multiple weak-field gravitational phenomena?
- **Prerequisites:** controlled E006-E009 results at their declared reproducibility levels; unresolved qualifications must be propagated.
- **Candidate tests:** potential/acceleration scaling, trajectory deflection, redshift or clock-rate analogue, time delay, orbital/precession-like behaviour, and equivalence across probe classes—only where operational mappings are justified.
- **Require:** explicit dimensionful mapping or transparent dimensionless comparison, calibration set, held-out prediction set, uncertainties, domain of validity, baseline and competing models.
- **Prohibit:** inserting inverse-square laws, separate tuning for every observable, fitting and testing on the same cases, or selecting only favourable phenomena.
- **GO:** One preregistered parameter set predicts multiple unseen observables and outperforms reasonable baselines with R3 replication.
- **QUALIFY/REVISE:** A shared qualitative law or restricted quantitative regime succeeds but universality or mapping remains incomplete.
- **STOP:** Agreement requires observable-specific tuning, encoded gravitational laws, or fails held-out tests.
- **Meaning:** Even GO supports a bounded correspondence claim, not proof that physical reality is the simulation.

## 3. Phase gates

- Advance from Phase 1 only if dimensionality is non-trivial and manifold evidence is independently controlled; otherwise pursue alternative representations as explicit revisions, not hidden substitutions.
- Advance from Phase 2 only after the explicit topology substrate reaches R2. E005 may qualify robustness but cannot repair invalid E004 machinery.
- Advance from Phase 3 only if the metric is operationally defined and structure-metric coupling is not definitional circularity.
- Advance from Phase 4 only if motion is predicted from independently measured geometry and causal claims distinguish update bounds from emergent universality.
- Begin confirmatory E010 only when upstream versions, mappings, parameters, and unresolved qualifications are frozen.

## 4. Dependency discipline

Record each dependency as `required`, `optional`, `methodological`, or `interpretive`. A downstream experiment may run as a methods study without a prerequisite GO, but it must not be presented as evidence for the full CBR chain. If an upstream node is REVISE, bind the downstream work to a named version. If STOP, close dependent claims or explicitly branch to a different hypothesis family.
