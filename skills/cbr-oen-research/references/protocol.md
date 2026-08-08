# Founding Protocol and Experimental Conventions

## Contents

1. Founding commitments
2. Specification contract
3. Anti-overfitting and analysis integrity
4. Reproducibility and artifacts
5. Governance and institutional model
6. Decisions, claims, and publication

## 1. Founding commitments

1. Make every substantive claim falsifiable.
2. Earn assumptions in dependency order.
3. Treat failure as evidence and preserve it.
4. Separate mathematical truths, implementation validation, simulation findings, and physical interpretations.
5. Prefer adversarial collaboration: `Proponent + Sceptic + Verifier`.
6. Make specifications portable across languages, teams, and institutions.
7. Keep provenance immutable and public by default, subject to lawful security/privacy limits.
8. Disclose conflicts, compute sponsors, role overlap, and deviations.

## 2. Specification contract

Give every experiment an immutable ID and semantic version. Use `DRAFT`, `PREREGISTERED`, `RUNNING`, `ANALYSED`, `REPLICATING`, `DECIDED`, `SUPERSEDED`, or `STOPPED` as lifecycle states.

A confirmatory specification must contain:

- title, experiment ID/version, phase, registration timestamp, status, and parent/superseded versions;
- scientific question, hypothesis, null, estimand, scope, and claim ceiling;
- required/optional dependencies and accepted upstream decision records;
- computational primitives, state, update rules, permitted derived quantities, initial conditions, and boundary/scheduling rules;
- prohibited assumptions and an explicit target-leakage audit;
- populations/ensembles, sampling frame, sample-size or precision justification, seeds and seed-generation, run counts, compute/resource guards, and stopping rules;
- primary and secondary endpoints with units, algorithms, scale windows, thresholds, and missing/failed-run handling;
- positive, negative, null, matched, ablation, finite-size, and sensitivity controls;
- statistical model, uncertainty, multiplicity, effect-size threshold, exclusions, robustness checks, and visualisations;
- implementation conformance tests and independent validation plan;
- decision table for GO, GO_WITH_QUALIFICATION, REVISE, and STOP;
- artifact manifest, evidence-graph outputs, owners, institutional roles, conflicts, and publication plan.

Write normative requirements with `MUST`, `MUST NOT`, `SHOULD`, `MAY`, and `PROHIBITED`. Define every technical term operationally. Represent tolerances numerically. State ordering, floating-point, concurrency, random-number, timeout, and failure semantics when they can affect reproduction.

An implementation may optimise performance but must pass the specification's conformance suite. Implementation-specific behaviour is a deviation, not an undocumented interpretation.

## 3. Anti-overfitting and analysis integrity

Apply these safeguards proportionally to risk:

- **No target leakage:** Do not place dimension, manifoldness, curvature, geodesic agreement, Lorentz agreement, gravitational law, or chosen proxy into upstream objectives when it is the outcome being explained.
- **No proxy laundering:** Audit candidate fitness inputs against outcome correlation and semantic equivalence. A renamed target remains a target.
- **Discovery/confirmation split:** Explore on a sandbox set. Freeze hypotheses, thresholds, estimators, and analysis. Confirm on untouched seeds, runs, regimes, or institutions.
- **Nested tuning:** Tune models or rule families only inside training folds/ensembles. Evaluate once on held-out data.
- **Multiverse disclosure:** Register all defensible representations, estimators, windows, exclusions, and model variants or use a declared multiverse analysis. Do not report only the favourable path.
- **Negative controls:** Include conditions where the effect should not appear.
- **Matched nulls:** Match size, degree, density, clustering, computational budget, lifetime, or complexity where these could explain the result.
- **Ablation:** Remove each fitness component, rule class, metric component, and analysis choice that could carry the effect.
- **Finite-size scaling:** Test whether effects strengthen, stabilise, or disappear with scale; do not infer asymptotics from one size.
- **Seed robustness:** Register master seeds and derived seeds. Report between-seed variation, not only a representative trajectory.
- **Stopping independence:** Stop on preregistered compute/precision/safety rules, never because the desired pattern appeared.
- **Multiplicity:** Name the primary endpoint and control family-wise/FDR error or frame secondary analyses as exploratory.
- **Minimum effect:** Distinguish statistical detectability from scientific relevance using a preregistered smallest effect of interest.
- **Robustness/OOD:** Test unseen rule families, initial conditions, defect types, signal types, and scales where the claim implies transfer.
- **No HARKing:** Label hypotheses suggested by results and test them in a new version with new data.
- **Common-parameter discipline:** For E010, fit on a calibration subset and lock one parameter set before predicting multiple held-out phenomena.

Archive a deviation whenever reality forces a change. State who knew which results, why the change was necessary, its expected bias, and whether affected analyses are exploratory.

## 4. Reproducibility and artifacts

### Required artifact classes

- preregistration and machine-readable specification;
- conformance tests and reference test vectors;
- source snapshot/commit, dependency lock, build instructions, licence, and execution environment;
- seeds, configuration, hardware/runtime metadata, logs, checkpoints, hashes, and failure records;
- raw and processed datasets with schemas and transformations;
- frozen analysis code/notebook, figures, tables, and statistical outputs;
- claim records, decision records, reviews, deviations, replications, and challenges.

Use content hashes for immutable artifacts and persistent IDs for logical objects. A hash change creates a new artifact. Preserve canonical ordering where state hashes depend on combinatorial objects.

### Reproduction ladder

- For R1, replay a registered run exactly and verify declared deterministic/tolerance-bound outputs.
- For R2, use separately written code, no shared core algorithm implementation, and only the public specification/test vectors. Resolve discrepancies with a documented adjudication suite.
- For R3, require institutional independence in leadership, execution environment, and analysis. Declare shared personnel, code, infrastructure, or funding.

Replicate the claim, not merely the original p-value. Predefine equivalence, directional, interval, or effect-size criteria. A failed replication creates a `FAILS_TO_REPLICATE` edge; it does not erase the original result.

## 5. Governance and institutional model

### Roles

Separate these functions where practical:

`Propose -> Specify -> Implement -> Execute -> Analyse -> Replicate -> Challenge -> Adjudicate`

- **Programme Council:** stewards scope, identifiers, phase architecture, and constitutional changes; cannot overrule registered outcomes.
- **Methods and Standards Board:** maintains specification schemas, statistics, reproducibility, and conformance policy.
- **Experiment Team:** owns a hypothesis/specification but not its independent replication decision.
- **Implementation Teams:** produce conforming independent implementations.
- **Execution Nodes:** run frozen packages and preserve logs/artifacts.
- **Analysis Team:** may receive blinded condition labels or held-out data.
- **Replication Centres:** independently preregister and execute R3 studies.
- **Red Team/Sceptic Panel:** defines alternative explanations, controls, falsifiers, and attack analyses before execution.
- **Evidence Curators:** validate provenance, identifiers, hashes, and graph links without judging scientific truth.
- **Gate Panel:** issues decisions; include relevant domain expertise, an independent methodologist, and a sceptical member.
- **Appeals/Integrity Panel:** hears process challenges, conflicts, and misconduct allegations; does not substitute preference for evidence.

### Institutional collaboration

Participation never implies endorsement of CBR. Allow institutions to contribute mathematics/topology, algorithms, independent implementation, HPC execution, statistics, relativity/physics, replication, or adversarial review. Publish role and contribution statements.

Before a confirmatory run:

1. invite public or named adversarial review;
2. resolve or register dissent without requiring consensus;
3. freeze specification and conformance tests;
4. assign data access and blinding;
5. declare independence and conflicts;
6. timestamp the preregistration.

For material conflicts, recuse affected gate voters. Publish majority rationale and minority reports. Change the founding protocol only by versioned proposal, public comment, supermajority approval, and a compatibility statement for existing evidence.

## 6. Decisions, claims, and publication

Evaluate the preregistered primary endpoint first. A gate record must include criteria, observed results with uncertainty, controls, reproducibility status, deviations, unresolved confounds, votes/recusals, dissent, decision, claim ceiling, and exact downstream effects.

Use `GO_WITH_QUALIFICATION` only when a bounded continuation is scientifically coherent; list machine-readable qualifications. Use REVISE for a new testable version, not repeated sampling until success. Use STOP when a hypothesis branch has received a fair test and no viable registered effect remains or when the test is irredeemably circular.

Publish registered reports regardless of outcome. Lead with the primary endpoint, include all registered conditions and failed runs, distinguish confirmatory from exploratory results, report effect sizes/intervals, compare alternative explanations, and state what the experiment does not establish.

Never claim:

- dimension implies manifold topology;
- manifold topology implies metric geometry;
- metric distortion implies geodesic motion;
- a causal speed bound implies Lorentz invariance;
- simulation correspondence identifies the ontology of reality.
