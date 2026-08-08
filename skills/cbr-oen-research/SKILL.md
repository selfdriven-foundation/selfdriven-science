---
name: cbr-oen-research
description: Design, specify, review, govern, analyse, and extend the Compute-Based Reality Open Experimental Network (CBR-OEN). Use for CBR-OEN founding protocol or roadmap work; experiments CBR-E001 through CBR-E010 or proposals for E011+; geometry-free computation, emergent dimension, 3-manifolds, simplicial dynamics, emergent metrics, structure-metric coupling, geodesics, causality, or quantitative gravity; preregistration, evidence graphs, reproducibility, institutional collaboration, adversarial review, GO/REVISE/STOP gates, or anti-overfitting controls.
---

# Operate the CBR Open Experimental Network

## Hold the scientific posture

Treat CBR as a falsifiable research programme, not a conclusion. Preserve this founding statement:

> CBR-OEN does not exist to prove Compute-Based Reality. It exists to make Compute-Based Reality testable.

Count rigorous null results, contradictions, and failed replications as successful network outputs. Never infer a later-layer claim from an earlier-layer success. Distinguish demonstration in a computational model from correspondence with physical reality.

## Load only the necessary references

- Read [programme.md](references/programme.md) for the E001-E010 hypotheses, dependencies, controls, gates, and phase progression.
- Read [protocol.md](references/protocol.md) when drafting or reviewing an experiment, preregistration, governance plan, collaboration, replication, analysis, or claim.
- Read [schemas-and-extension.md](references/schemas-and-extension.md) when creating machine-readable records, evidence graphs, identifiers, decision records, or E011+ proposals.

For work affecting programme dependencies or gates, read all three references before finalising.

## Follow the operating workflow

1. **Classify the request.** Identify the experiment, phase, claim level, and whether the task concerns proposal, specification, implementation, execution, analysis, replication, challenge, governance, or extension.
2. **Trace prerequisites.** Verify every upstream dependency and its decision state. Do not silently promote qualified evidence into an unqualified premise.
3. **State the claim pair.** Write the hypothesis and a genuine null hypothesis before choosing measurements.
4. **Run an assumption audit.** Separate primitives, derived observables, operational constraints, and prohibited assumptions. Reject circular tests that encode the desired outcome in rules, fitness, labels, stopping, or selection.
5. **Draft the specification.** Make the experiment implementation-independent and preregistration-ready using the conventions in `protocol.md`.
6. **Design adversarial controls.** Include null ensembles, matched controls, ablations, finite-size tests, sensitivity tests, alternative explanations, and negative controls appropriate to the experiment.
7. **Bind decisions before results.** Register primary endpoints, sample sizes, exclusions, seeds or seed-generation, analysis, multiplicity treatment, thresholds, stopping rules, and GO / GO_WITH_QUALIFICATION / REVISE / STOP logic.
8. **Separate roles.** Record who proposes, specifies, implements, executes, analyses, replicates, and challenges. Require independence appropriate to the claim level.
9. **Capture provenance.** Link specification versions, code commits, environments, runs, datasets, analyses, claims, and replications in the evidence graph.
10. **Report symmetrically.** Present positive, null, contradictory, and failed-replication evidence with limitations and alternative explanations.
11. **Issue a gate decision.** Provide evidence, rationale, qualifications, dissent, and downstream consequences. A gate permits a next experiment; it does not validate CBR as a whole.

## Enforce programme invariants

- Treat the specification—not CBR-Lab or any one codebase—as the experiment.
- Keep physical target properties out of foundational rules and fitness unless a later, explicitly controlled experiment requires them.
- Use coordinates only when a registered downstream comparison requires them; never retrofit them into geometry-free experiments.
- Keep exploratory and confirmatory analyses separate. Label post-hoc findings and require fresh confirmatory data.
- Freeze specifications and analysis plans before confirmatory execution. Version amendments; never overwrite history.
- Preserve all registered runs, including crashes, nulls, exclusions, and adverse outcomes.
- Never use the same data to discover and confirm a threshold, model, observable, or parameter.
- Require predictions on unseen runs or held-out regimes before using “predictive.”
- Require a common parameter set across multiple observables before claiming E010 correspondence.
- Use calibrated language: `consistent with`, `supports within scope`, `contradicts`, `fails to distinguish`, or `not tested`. Avoid “proves reality is computational.”

## Apply claim and reproducibility levels

Use the lowest level fully supported:

- **CL0 Speculative** — articulated but untested.
- **CL1 Demonstrated example** — one constructed or observed case.
- **CL2 Ensemble effect** — repeated across a registered ensemble.
- **CL3 Controlled effect** — survives matched controls, ablations, and confound tests.
- **CL4 Independent reproduction** — reaches R2.
- **CL5 Institutional replication** — reaches R3.
- **CL6 Predictive** — preregistered prediction succeeds on unseen data or regimes.
- **CL7 Physical correspondence** — quantitatively maps to physical observations with explicit units, calibration, uncertainties, and competing-model comparisons.

Track reproducibility separately:

- **R1 Computational reproduction:** same specification, implementation, environment, inputs, and seed reproduce the result.
- **R2 Independent implementation reproduction:** a separately written implementation reproduces the registered phenomenon.
- **R3 Institutional replication:** an independent organisation reproduces the preregistered finding.

Do not collapse claim level and reproducibility into one score. Require R3 for strong physical claims.

## Make decisions conservatively

- **GO:** Preregistered primary criteria pass, required controls and reproducibility are satisfied, no fatal confound remains, and prerequisites for named downstream work are earned.
- **GO_WITH_QUALIFICATION:** The core result is credible but bounded by a declared limitation. Propagate the qualification downstream.
- **REVISE:** The question remains viable but the representation, design, measurement, implementation, power, or assumptions require a new version and fresh confirmatory run.
- **STOP:** The registered claim is contradicted across adequate tests, a foundational premise fails, circularity cannot be removed, or repeated broad controls leave no meaningful effect. Preserve the branch and state what remains testable.

Never convert STOP to REVISE merely to protect the programme. Never convert REVISE to GO because a post-hoc subset looks favourable.

## Produce usable outputs

For a new or revised experiment, return:

1. identity, version, status, owners, and dependencies;
2. scientific question, hypothesis, null, and scope;
3. primitives, permitted operations, and prohibited assumptions;
4. design, controls, datasets, sample size, randomness, and compute limits;
5. primary/secondary endpoints and analysis plan;
6. falsifiers, confounds, failure modes, and sensitivity tests;
7. reproducibility target and role separation;
8. GO / GO_WITH_QUALIFICATION / REVISE / STOP criteria;
9. evidence-graph outputs and required artifacts;
10. downstream consequences and unresolved questions.

For a review, lead with blocking scientific-integrity issues, then major design risks, missing evidence, and precise revisions. For a roadmap update, show dependency changes and gate consequences. For a claim, cite its complete evidence path and state its ceiling.

## Extend beyond E010

Treat E001-E010 as the frozen v1.0 baseline. Do not renumber or silently alter them. Propose E011+ only when the new work tests a distinct question, closes a registered limitation, adjudicates competing explanations, extends a surviving result, or attempts stronger correspondence. Follow the extension rules and templates in `schemas-and-extension.md`.
