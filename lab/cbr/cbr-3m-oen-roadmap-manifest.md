# CBR-OEN Experimental Roadmap Manifest
## Machine-Readable Dependency, Evidence and Decision Model
### Version 1.0

```yaml
cbr_oen:

  manifest_type: "experimental_roadmap"

  roadmap:
    id: "CBR-OEN-ROADMAP"
    version: "1.0"

    title:
      "CBR-OEN Experimental Roadmap"

    purpose: >
      Define the dependency graph, evidence requirements,
      success criteria and GO / GO-WITH-QUALIFICATION /
      REVISE / STOP decisions for the first ten CBR-OEN experiments.

    founding_principle: >
      CBR-OEN does not exist to prove Compute-Based Reality.
      It exists to make Compute-Based Reality testable.

    experimental_principle: >
      Do not encode the physical property being explained
      as an optimisation target or primitive variable unless
      explicitly required by a later controlled experiment.


  decision_states:

    - "GO"
    - "GO_WITH_QUALIFICATION"
    - "REVISE"
    - "STOP"


  reproducibility_levels:

    R1:
      name: "Computational Reproduction"
      requirement: >
        Same specification, implementation, environment and
        seed reproduce the result.

    R2:
      name: "Independent Implementation Reproduction"
      requirement: >
        An independently written implementation reproduces
        the registered phenomenon.

    R3:
      name: "Institutional Replication"
      requirement: >
        An independent organisation reproduces the registered
        result.


  claim_levels:

    CL0:
      name: "Speculative"

    CL1:
      name: "Demonstrated Example"

    CL2:
      name: "Ensemble Effect"

    CL3:
      name: "Controlled Effect"

    CL4:
      name: "Independent Reproduction"

    CL5:
      name: "Institutional Replication"

    CL6:
      name: "Predictive"

    CL7:
      name: "Physical Correspondence"


  phases:

    PHASE_1:

      name:
        "Emergent Structure"

      experiments:
        - "CBR-E001"
        - "CBR-E002"
        - "CBR-E003"

      question: >
        Can geometry-free computation generate reproducible
        dimensional and manifold-like structure?

    PHASE_2:

      name:
        "Topological Dynamics"

      experiments:
        - "CBR-E004"
        - "CBR-E005"

      question: >
        Can 3-manifold topology behave as a robust computational
        organisation rather than merely an imposed structure?

    PHASE_3:

      name:
        "Emergent Geometry"

      experiments:
        - "CBR-E006"
        - "CBR-E007"

      question: >
        Can computational transition cost become operational
        metric geometry and can persistent computation modify it?

    PHASE_4:

      name:
        "Dynamics and Causality"

      experiments:
        - "CBR-E008"
        - "CBR-E009"

      question: >
        Do free computational structures respond to emergent
        geometry and does the substrate generate causal structure?

    PHASE_5:

      name:
        "Physical Correspondence"

      experiments:
        - "CBR-E010"

      question: >
        Can the combined emergent mechanism quantitatively
        reproduce weak-field gravitational relationships?


  experiments:


    CBR-E001:

      title:
        "Emergent Dimensionality from Geometry-Free Relational Computation"

      phase:
        "PHASE_1"

      depends_on: []

      hypothesis:
        "CBR-H001"

      question: >
        Can non-trivial effective dimensionality emerge from
        relational computation containing no spatial coordinates
        or predefined dimension?

      forbidden_inputs:
        - "spatial_coordinates"
        - "predefined_dimension"
        - "target_dimension"

      primary_measurements:
        - "ball_growth_dimension"
        - "spectral_dimension"

      controls:
        - "random_graph"
        - "degree_matched"
        - "finite_size"

      go:
        requirement: >
          Reproducible non-trivial dimensional scaling survives
          seed, size and matched-control tests.

      go_with_qualification:
        requirement: >
          Only part of the dimensional evidence is robust.

      revise:
        requirement: >
          Scaling is dominated by finite-size or rule-family artefacts.

      stop:
        requirement: >
          No reproducible non-trivial dimensional structure survives
          sufficiently broad controls.

      downstream:
        - "CBR-E002"
        - "CBR-E003"


    CBR-E002:

      title:
        "Dimension-Blind Evolution of Relational Computational Systems"

      phase:
        "PHASE_1"

      depends_on:
        - "CBR-E001"

      hypothesis:
        "CBR-H002"

      question: >
        Does selection for persistence, structural complexity and
        stability change dimensional distributions when dimension
        is excluded from fitness?

      fitness:
        persistence: 0.40
        complexity: 0.35
        stability: 0.25

      prohibited_fitness_inputs:
        - "ball_growth_dimension"
        - "spectral_dimension"
        - "target_dimension"
        - "manifold_score"

      controls:
        - "random_search"
        - "neutral_evolution"
        - "shuffled_fitness"
        - "fitness_ablation"
        - "degree_matched"

      go:
        requirement: >
          Selected populations exhibit reproducible dimensional
          organisation beyond neutral controls.

      go_with_qualification:
        requirement: >
          Effect exists but is substantially mediated by a known
          structural confound.

      revise:
        requirement: >
          Effect is unstable under reasonable fitness variants.

      stop:
        requirement: >
          Selected and neutral populations exhibit no robust
          dimensional difference.

      downstream:
        - "CBR-E003"


    CBR-E003:

      title:
        "Local 3-Manifold Emergence in Geometry-Free Computational Systems"

      phase:
        "PHASE_1"

      depends_on:
        - "CBR-E001"

      optional_dependency:
        - "CBR-E002"

      hypothesis:
        "CBR-H003"

      question: >
        Do approximately three-dimensional computational structures
        exhibit local topology compatible with a 3-manifold?

      representation:
        baseline: "flag_complex"

      primary_topology_test:
        expected_vertex_link: "S2"

      required_link_properties:
        connected: true
        euler_characteristic: 2
        betti:
          beta0: 1
          beta1: 0
          beta2: 1

      primary_metric:
        "s2_link_fraction"

      controls:
        - "degree_preserving_randomisation"
        - "clustering_matched"
        - "dimension_matched"
        - "random_graph"

      go:
        requirement: >
          Experimental structures show reproducible enrichment
          of S2-like links relative to dimension-matched controls.

      go_with_qualification:
        requirement: >
          Manifold structure occurs only in a stable subset of the system.

      revise:
        requirement: >
          Graph-to-flag-complex representation appears inadequate.

      stop:
        requirement: >
          Three-dimensional scaling repeatedly fails to produce
          manifold evidence under reasonable higher-order representations.

      downstream:
        - "CBR-E004"


    CBR-E004:

      title:
        "Explicit Simplicial Dynamics and 3-Manifold Stability"

      phase:
        "PHASE_2"

      depends_on:
        - "CBR-E003"

      hypothesis:
        - "CBR-H004-A"
        - "CBR-H004-B"

      state:
        type: "explicit_simplicial_complex"
        maximum_dimension: 3

      moves:
        - "1-4"
        - "4-1"
        - "2-3"
        - "3-2"

      initial_control:
        topology: "S3"
        representation: "boundary_of_4_simplex"

      expected_invariants:
        closed_face_fraction: 1.0
        s2_link_fraction: 1.0
        global_betti:
          - 1
          - 0
          - 0
          - 1

      go:
        requirement: >
          Independent implementations preserve manifold invariants
          under long Pachner-move trajectories.

      revise:
        requirement: >
          Move validation or topology verification fails.

      stop:
        requirement: >
          No reliable explicit simplicial dynamics implementation
          can be independently validated.

      minimum_downstream_reproducibility:
        "R2"

      downstream:
        - "CBR-E005"
        - "CBR-E006"


    CBR-E005:

      title:
        "Dimension- and Topology-Blind Selection Under Manifold-Breaking Defects"

      phase:
        "PHASE_2"

      depends_on:
        - "CBR-E004"

      hypothesis:
        "CBR-H005"

      defect_moves:
        enabled: true

      fitness:
        topology_blind: true
        dimension_blind: true

      tracks:
        - "E005-A_endogenous_defects"
        - "E005-B_exogenous_defects"
        - "E005-C_mixed_defects"

      primary_measurements:
        - "defect_probability"
        - "s2_link_fraction"
        - "closed_face_fraction"
        - "repair_probability"
        - "recovery_time"

      controls:
        - "neutral_evolution"
        - "random_search"
        - "shuffled_fitness"
        - "fixed_defect_probability"
        - "defect_type_ablation"
        - "connectivity_matched"
        - "size_matched"

      go:
        requirement: >
          Topology-blind selected systems exhibit greater manifold
          integrity, resilience or repair than neutral controls.

      go_with_qualification:
        requirement: >
          Selection merely eliminates obviously catastrophic defects.

      revise:
        requirement: >
          Defect model is too severe, too narrow or structurally biased.

      stop:
        requirement: >
          Topology-blind selection consistently favours non-manifold
          configurations over manifold configurations.

      downstream:
        - "CBR-E006"


    CBR-E006:

      title:
        "Emergent Metric Geometry from Computational Transition Cost"

      phase:
        "PHASE_3"

      depends_on:
        - "CBR-E004"

      strengthened_by:
        - "CBR-E005"

      hypothesis:
        "CBR-H006"

      metric:
        definition:
          "minimum_accumulated_transition_cost"

        formula:
          "d_C(A,B)=min_gamma(sum_e(c_e))"

      forbidden_inputs:
        - "euclidean_coordinates"
        - "physical_distance"
        - "curvature_target"
        - "target_dimension"

      tracks:
        - "E006-A_uniform_cost"
        - "E006-B_endogenous_cost"
        - "E006-C_dynamic_cost"
        - "E006-D_internal_reconstruction"

      primary_measurements:
        - "metric_scale_stability"
        - "metric_temporal_stability"
        - "relational_isotropy"
        - "relational_homogeneity"
        - "geodesic_stability"
        - "propagation_metric_correlation"
        - "internal_reconstruction_error"

      controls:
        - "shuffled_cost"
        - "static_cost"
        - "matched_cost_distribution"
        - "random_network"
        - "non_manifold"

      go:
        requirement: >
          Endogenous computational cost produces reproducible,
          coarse-grain-stable operational geometry beyond weighted
          network controls.

      go_with_qualification:
        requirement: >
          Stable geometry exists but is recoverable only by an
          external global observer.

      revise:
        requirement: >
          Tested cost family fails but alternative local cost
          definitions remain scientifically motivated.

      stop:
        requirement: >
          No local endogenous cost model produces coherent metric
          structure beyond generic weighted-network effects.

      minimum_downstream_reproducibility:
        "R2"

      downstream:
        - "CBR-E007"


    CBR-E007:

      title:
        "Persistent Computational Structures and Emergent Metric Distortion"

      phase:
        "PHASE_3"

      depends_on:
        - "CBR-E006"

      hypothesis:
        "CBR-H007"

      source:
        type: "persistent_computational_pattern"
        primitive_mass: false

      causal_chain:
        - "persistent_structure"
        - "local_computational_activity"
        - "transition_cost_change"
        - "metric_distortion"

      prohibited_rules:
        - "gravitational_force"
        - "gravitational_potential"
        - "inverse_square_field"
        - "mass_source_term"

      primary_measurements:
        - "cost_distortion"
        - "metric_distortion"
        - "distortion_profile"
        - "field_formation_time"
        - "field_relaxation_time"
        - "internal_detectability"

      controls:
        - "structure_free"
        - "activity_matched_transient"
        - "shuffled_structure"
        - "random_activity"
        - "frozen_cost"

      go:
        requirement: >
          Persistent computational structures produce reproducible
          metric distortion beyond activity-matched controls.

      go_with_qualification:
        requirement: >
          Metric distortion is explained primarily by computational
          load rather than persistence.

      revise:
        requirement: >
          Candidate source descriptor or structure definition
          requires reformulation.

      stop:
        requirement: >
          Persistent structure produces no metric effect beyond
          matched generic activity.

      downstream:
        - "CBR-E008"


    CBR-E008:

      title:
        "Emergent Geodesic Motion in a Computationally Distorted Metric"

      phase:
        "PHASE_4"

      depends_on:
        - "CBR-E007"

      hypothesis:
        "CBR-H008"

      source_to_probe_direct_force:
        enabled: false

      probe_access:
        source_location: false
        global_metric: false
        target_trajectory: false

      primary_measurements:
        - "geodesic_alignment"
        - "path_cost_regret"
        - "trajectory_deflection"

      mediation_conditions:

        C1:
          source: true
          metric_distortion: true

        C2:
          source: true
          metric_distortion: false

        C3:
          source: false
          metric_distortion: true

        C4:
          source: false
          metric_distortion: false

      controls:
        - "source_free"
        - "metric_removed"
        - "metric_preserved_source_removed"
        - "shuffled_metric"
        - "synthetic_matched_metric"
        - "multiple_probe_types"

      go:
        requirement: >
          Probe trajectories align with preregistered geodesics and
          causal interventions support metric-mediated motion.

      go_with_qualification:
        requirement: >
          Geodesic motion requires explicit local cost sensitivity.

      revise:
        requirement: >
          Mobility or pattern-persistence mechanism requires redesign.

      stop:
        requirement: >
          Probe motion is independent of the emergent metric.

      downstream:
        - "CBR-E009"


    CBR-E009:

      title:
        "Emergent Causal Cones and Limiting Propagation Speed"

      phase:
        "PHASE_4"

      depends_on:
        - "CBR-E006"
        - "CBR-E008"

      hypothesis:
        "CBR-H009"

      primitive_physical_time:
        enabled: false

      tracks:
        - "E009-A_synchronous"
        - "E009-B_asynchronous"
        - "E009-C_moving_observers"
        - "E009-D_distorted_metric"

      forbidden_primitives:
        - "speed_of_light_constant"
        - "lorentz_transform"
        - "minkowski_metric"
        - "time_dilation_formula"

      primary_measurements:
        - "limiting_propagation_speed"
        - "signal_species_speed_variance"
        - "causal_cone_violation_rate"
        - "metric_propagation_consistency"

      stronger_measurements:
        - "observer_speed_dependence"
        - "clock_rate_dependence"
        - "preferred_frame_detectability"
        - "proper_time_candidate_agreement"

      controls:
        - "multiple_signal_species"
        - "multiple_clock_species"
        - "scheduler_variation"
        - "moving_observers"
        - "static_topology"
        - "evolving_topology"

      go:
        requirement: >
          Multiple signal species exhibit a common stable limiting
          propagation speed relative to the emergent metric.

      go_with_qualification:
        requirement: >
          Causal cones exist but a macroscopic preferred frame
          remains clearly observable.

      revise:
        requirement: >
          Causal structure depends strongly on scheduling or
          signal implementation.

      stop:
        requirement: >
          No robust common causal structure survives controls.

      downstream:
        - "CBR-E010"


    CBR-E010:

      title:
        "Quantitative Correspondence with Weak-Field Relativistic Gravity"

      phase:
        "PHASE_5"

      depends_on:
        - "CBR-E006"
        - "CBR-E007"
        - "CBR-E008"
        - "CBR-E009"

      hypothesis:
        "CBR-H010"

      objective: >
        Determine whether one emergent computational geometry
        quantitatively predicts multiple weak-field gravitational
        observables using a common parameter set.

      forbidden_primitives:
        - "newtonian_force"
        - "inverse_square_force"
        - "einstein_field_equations"
        - "gravitational_time_dilation_formula"
        - "shapiro_delay_formula"

      tests:

        E010_A:
          name: "Source-Distance Field Law"

        E010_B:
          name: "Metric-Predicted Probe Response"

        E010_C:
          name: "Probe Universality"

        E010_D:
          name: "Clock-Rate Shift"

        E010_E:
          name: "Signal Propagation Delay"

        E010_F:
          name: "Signal Geodesic Deflection"

        E010_G:
          name: "Weak-Field Superposition"

        E010_H:
          name: "Causal Field Relaxation"

      calibration:
        strategy: "single_global_mapping"
        holdout_required: true
        per_observable_refitting: false

      evidence_levels:

        Q1:
          name: "Curve Correspondence"

        Q2:
          name: "Shared Parameter Correspondence"

        Q3:
          name: "Predictive Closure"

      target_evidence_level:
        "Q3"

      go:
        requirement: >
          Common emergent source, metric, causal-speed and coupling
          parameters jointly predict independent holdout observables.

      go_with_qualification:
        requirement: >
          A narrower Newtonian-like or partial relativistic
          correspondence survives.

      revise:
        requirement: >
          Residual structure supports a new falsifiable quantitative
          model without ad hoc per-observable fitting.

      stop:
        requirement: >
          Major observables require incompatible geometries or
          independently tuned effective laws.


  dependencies:

    - from: "CBR-E001"
      to: "CBR-E002"
      type: "ENABLES"

    - from: "CBR-E001"
      to: "CBR-E003"
      type: "ENABLES"

    - from: "CBR-E002"
      to: "CBR-E003"
      type: "STRENGTHENS_INTERPRETATION"

    - from: "CBR-E003"
      to: "CBR-E004"
      type: "MOTIVATES"

    - from: "CBR-E004"
      to: "CBR-E005"
      type: "VALIDATION_PREREQUISITE"

    - from: "CBR-E004"
      to: "CBR-E006"
      type: "SUBSTRATE"

    - from: "CBR-E005"
      to: "CBR-E006"
      type: "STRENGTHENS_INTERPRETATION"

    - from: "CBR-E006"
      to: "CBR-E007"
      type: "METRIC_PREREQUISITE"

    - from: "CBR-E007"
      to: "CBR-E008"
      type: "SOURCE_METRIC_PREREQUISITE"

    - from: "CBR-E008"
      to: "CBR-E009"
      type: "DYNAMICS_CONTEXT"

    - from: "CBR-E009"
      to: "CBR-E010"
      type: "CAUSAL_PREREQUISITE"

    - from: "CBR-E006"
      to: "CBR-E010"
      type: "METRIC_INPUT"

    - from: "CBR-E007"
      to: "CBR-E010"
      type: "SOURCE_INPUT"

    - from: "CBR-E008"
      to: "CBR-E010"
      type: "MOTION_INPUT"


  programme_success_levels:

    A:
      name:
        "Emergent Computational Geometry"
      requires:
        - "CBR-E001"
        - "CBR-E003"
        - "CBR-E006"

    B:
      name:
        "Matter-Geometry Coupling"
      requires:
        - "CBR-E007"

    C:
      name:
        "Geometric Dynamics"
      requires:
        - "CBR-E008"

    D:
      name:
        "Emergent Causal Spacetime"
      requires:
        - "CBR-E009"

    E:
      name:
        "Predictive Gravitational Correspondence"
      requires:
        - "CBR-E010:Q3"


  evidence_object_types:

    - "HYPOTHESIS"
    - "EXPERIMENT"
    - "SPECIFICATION"
    - "IMPLEMENTATION"
    - "RUN"
    - "RUN_SET"
    - "DATASET"
    - "ANALYSIS"
    - "CLAIM"
    - "MATHEMATICAL_REVIEW"
    - "CHALLENGE"
    - "REPLICATION"
    - "PREDICTION"


  evidence_edge_types:

    - "DEPENDS_ON"
    - "IMPLEMENTS"
    - "EXECUTES"
    - "GENERATES"
    - "ANALYSES"
    - "SUPPORTS"
    - "CONTRADICTS"
    - "CHALLENGES"
    - "REPLICATES"
    - "FAILS_TO_REPLICATE"
    - "VALIDATES"
    - "REFINES"
    - "SUPERSEDES"


  required_repository_structure:

    - "/protocol"
    - "/roadmap"
    - "/experiments"
    - "/hypotheses"
    - "/implementations"
    - "/run-manifests"
    - "/datasets"
    - "/analysis"
    - "/mathematical-reviews"
    - "/replications"
    - "/challenges"
    - "/negative-results"
    - "/predictions"
    - "/evidence-graph"
    - "/publications"


  scientific_integrity:

    negative_results:
      retained: true

    preregistration:
      required_for_confirmatory_claims: true

    exploratory_results:
      allowed: true
      must_be_labelled: true

    post_hoc_success_criteria:
      allowed: false

    version_overwrite:
      allowed: false

    independent_implementation:
      encouraged_from: "CBR-E001"
      required_for_strong_claims: true

    institutional_replication:
      required_for_physical_claims: true


  final_programme_question: >
    Can minimal coordinate-free local computation progress from
    relational structure to dimensionality, manifold topology,
    operational metric geometry, persistent matter-like structures,
    geodesic motion and causal organisation, and ultimately generate
    quantitative physical predictions without those physical laws
    having been inserted as primitives?
```

## Canonical Decision Logic

```text
E001
  |
  +--> dimensional structure?
          |
          +-- NO --> REVISE / STOP structural branch
          |
          YES
          |
          v
E002 -----+
  |
  v
E003
  |
  +--> manifold structure?
          |
          +-- NO --> alternative higher-order model
          |             |
          |             +-- NO --> STOP emergent-space branch
          |
          YES
          |
          v
E004
  |
  +--> validated simplicial substrate?
          |
          +-- NO --> FIX BEFORE PROCEEDING
          |
          YES
          |
          v
E005
  |
  +--> emergent manifold resilience?
          |
          +-- NO --> proceed only with imposed-topology qualification
          |
          v
E006
  |
  +--> operational emergent metric?
          |
          +-- NO --> STOP physical-geometry branch
          |
          YES
          |
          v
E007
  |
  +--> persistent structure distorts metric?
          |
          +-- NO --> STOP tested matter-geometry mechanism
          |
          YES
          |
          v
E008
  |
  +--> free structures follow metric?
          |
          +-- NO --> STOP geodesic-gravity mechanism
          |
          YES
          |
          v
E009
  |
  +--> coherent causal structure?
          |
          +-- NO --> retain non-relativistic branch only
          |
          YES
          |
          v
E010
  |
  +--> Q1 : qualitative/curve correspondence
  |
  +--> Q2 : shared-parameter effective model
  |
  +--> Q3 : predictive closure
```

## Founding Machine-Readable Principle

```yaml
final_principle:

  statement: >
    The programme must not infer success from resemblance alone.

  progression:

    - "specify"
    - "preregister"
    - "implement"
    - "execute"
    - "analyse"
    - "reproduce"
    - "replicate"
    - "challenge"
    - "predict"

  strongest_evidence: >
    Independently defined emergent quantities predict previously
    unseen outcomes using parameters fixed before the confirmation run.
```