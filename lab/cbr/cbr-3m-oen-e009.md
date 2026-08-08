# CBR-OEN Experiment CBR-E009
## Emergent Causal Cones and Limiting Propagation Speed
### Preregistered Experimental Specification — Draft v1.0

---

## 1. Experiment Identity

**Experiment ID:** CBR-E009  
**Version:** 1.0  
**Title:** Emergent Causal Cones and Limiting Propagation Speed  
**Protocol:** CBR-OEN Experimental Protocol v1.0  
**Experiment class:** Confirmatory computational-causality experiment  
**Predecessors:** CBR-E006, CBR-E007, CBR-E008

---

# 2. Scientific Question

CBR-E009 asks:

> **Can a coordinate-free computational system with only local state transitions generate a stable causal structure, including an effective maximum propagation speed, without a relativistic spacetime metric or Lorentz symmetry being explicitly encoded?**

The experimental progression is now:

\[
\text{computation}
\rightarrow
\text{topology}
\rightarrow
\text{metric}
\rightarrow
\text{motion}
\rightarrow
\boxed{\text{causality}}.
\]

The key question is whether computational locality itself can generate something that embedded observers experience as a finite causal horizon.

---

# 3. Core Hypothesis

### CBR-H009

Local computational update rules can generate a large-scale causal structure in which disturbances propagate inside an emergent causal cone with a reproducible limiting velocity.

Let:

\[
x
\]

represent a computational event.

Let:

\[
J^+(x)
\]

represent the set of events that can be influenced by \(x\).

The hypothesis predicts that, under suitable coarse-graining:

\[
J^+(x)
\]

will be bounded by an approximately stable relation of the form:

\[
d_C(x,y)
\leq
v_{\max}\Delta t
\]

where:

- \(d_C\) is the emergent computational metric;
- \(\Delta t\) is computational evolution;
- \(v_{\max}\) is an emergent limiting propagation speed.

---

# 4. Null Hypothesis

The null hypothesis is:

> Local computational systems produce no robust observer-independent causal cone beyond trivial restrictions imposed directly by the update algorithm.

Possible null outcomes include:

- propagation speed depends strongly on location;
- propagation speed depends strongly on direction;
- coarse-graining destroys the apparent bound;
- different signal types have unrelated limiting velocities;
- the limiting velocity is merely a programmer-imposed step limit;
- preferred-frame effects remain macroscopically observable.

---

# 5. Important Distinction

Every local update system has some trivial notion of finite information propagation.

For example, if information can move only one graph edge per update, then:

\[
v\leq1
\]

in graph-edge units.

That alone is not scientifically interesting.

CBR-E009 asks the stronger question:

> **Does a stable effective causal structure emerge when distance itself is already an emergent computational quantity?**

The relevant ratio is:

\[
\frac{\text{emergent metric distance}}
{\text{computational time}},
\]

not merely edges-per-update.

---

# 6. Time in E009

CBR continues to distinguish spatial structure from computational evolution.

Let:

\[
K_t
\]

represent the computational state after \(t\) update steps.

Then:

\[
t
\]

is initially an ordering variable, not a physical time coordinate.

The experiment asks whether an operational physical time can be reconstructed from computational processes.

---

# 7. Fundamental Computational Order

The underlying system contains events:

\[
e_1,e_2,\ldots
\]

and causal dependencies:

\[
e_i\prec e_j
\]

when event \(e_j\) requires information resulting from \(e_i\).

This produces a partial order:

\[
(\mathcal{E},\prec).
\]

A causal structure may therefore be more fundamental than a global clock.

---

# 8. Synchronous Baseline

E009-A begins with a synchronous update model.

All eligible local regions advance through discrete computational rounds:

\[
t=0,1,2,\ldots
\]

This is experimentally convenient but contains a preferred computational frame.

Therefore E009-A is only a baseline.

---

# 9. Asynchronous Extension

E009-B removes the globally synchronised update assumption.

Local events occur according to preregistered asynchronous scheduling.

The causal structure is derived from dependency relations rather than a universal external timestep.

This is a substantially stronger test.

---

# 10. Why Asynchrony Matters

If relativistic-like causal behaviour appears only because a globally synchronised simulator imposes a speed limit, the result is weak.

A more compelling result is:

\[
\text{local asynchronous computation}
\rightarrow
\text{stable macroscopic causal cones}.
\]

This reduces dependence on an external computational clock.

---

# 11. Experimental Substrate

Use a substrate previously validated through E006–E008:

\[
(K,C)
\]

with:

- manifold-like topology;
- stable emergent metric \(d_C\);
- local computational dynamics;
- persistent structures;
- no external spatial coordinates.

---

# 12. Signal

Define a minimal computational disturbance:

\[
S.
\]

A signal should be:

- local;
- identifiable;
- propagating;
- minimally invasive;
- independent of persistent matter-like structures where possible.

Examples include:

- state-bit flip;
- tagged local excitation;
- temporary update-state change;
- propagation token.

---

# 13. Signal Propagation Rule

A signal may influence only computationally adjacent states according to local transition rules.

No global routing is permitted.

No shortest path is provided.

No destination coordinates are known.

The disturbance propagates through ordinary computational dynamics.

---

# 14. Signal Front

Inject signal \(S\) at event:

\[
(x,t_0).
\]

At later computational time \(t\), define the affected region:

\[
R_S(t).
\]

The propagation front is:

\[
\partial R_S(t).
\]

Using emergent metric \(d_C\), measure maximum reach:

\[
r_{\max}(t)
=
\max_{y\in R_S(t)}
d_C(x,y).
\]

---

# 15. Effective Propagation Velocity

Define:

\[
v_S(t)
=
\frac{
r_{\max}(t)
}{
t-t_0
}.
\]

If the system possesses a stable limiting propagation rate:

\[
v_S(t)
\rightarrow
v_*.
\]

---

# 16. Causal Cone

A candidate causal cone exists if influence satisfies approximately:

\[
d_C(x,y)
\leq
v_*(t_y-t_x)
\]

for reachable event pairs.

Events outside this region should be causally inaccessible within the corresponding interval.

---

# 17. Causal Classification

For event pair:

\[
(e_i,e_j),
\]

define computational separation:

\[
\Delta s_C^2
=
v_*^2\Delta t^2
-
d_C^2.
\]

This is initially an analytical construct only.

Then classify:

### Timelike-like

\[
\Delta s_C^2>0.
\]

### Null-like

\[
\Delta s_C^2\approx0.
\]

### Spacelike-like

\[
\Delta s_C^2<0.
\]

The terminology is analogical unless later experiments establish relativistic correspondence.

---

# 18. Primary Endpoint

The primary E009 endpoint is:

> **Whether multiple locally propagating signal classes exhibit a common, reproducible large-scale limiting speed relative to the independently emergent computational metric.**

The crucial phrase is:

\[
\boxed{\text{common limiting speed}}.
\]

---

# 19. Why Multiple Signals Matter

One particular signal may simply propagate at a speed defined by its own update rule.

Therefore test:

\[
S_1,S_2,\ldots,S_n
\]

with distinct local implementations.

A stronger result would show:

\[
v_{S_1}^{\max}
\approx
v_{S_2}^{\max}
\approx
\cdots
\approx
v_*.
\]

This suggests a property of the substrate rather than of one signal implementation.

---

# 20. E009-A — Synchronous Propagation

Use globally stepped computation.

Measure:

- propagation front;
- limiting velocity;
- directional variation;
- location variation;
- signal-class variation.

This validates measurement machinery.

---

# 21. E009-B — Asynchronous Causality

Replace global rounds with local event scheduling.

Each event records parent causal dependencies.

The resulting causal relation is:

\[
e_i\prec e_j.
\]

Measure causal depth:

\[
\tau_C(e_i,e_j)
\]

as the longest or otherwise preregistered causal-chain measure between events.

---

# 22. Causal Time

A candidate operational duration may be defined from event chains rather than simulator wall-clock.

For example:

\[
\Delta\tau_C
=
\text{causal depth}.
\]

This provides an internal notion of elapsed computational time.

---

# 23. Internal Clock

Introduce persistent periodic computational processes:

\[
C_1,C_2,\ldots
\]

that function as clocks.

A clock counts recurring internal state cycles.

Define:

\[
\tau_P
=
N_{\text{cycles}}.
\]

This allows embedded observers to measure time without access to simulator timestep.

---

# 24. Clock Universality

Use multiple clock designs.

Test whether:

\[
\tau_{C_1}
\]

and:

\[
\tau_{C_2}
\]

remain proportional under identical computational conditions.

A useful operational time should not depend arbitrarily on one clock architecture.

---

# 25. Embedded Observer

An observer has access only to:

- local clock cycles;
- received signals;
- local metric reconstruction;
- neighbouring events.

It cannot inspect:

- global graph;
- simulator timestep;
- global execution order.

Ask whether it can reconstruct the causal cone.

---

# 26. Observer-Measured Signal Speed

Observer \(O\) estimates:

\[
\hat v
=
\frac{
\hat d
}{
\Delta\tau_O
}.
\]

Compare across observers.

A strong result would show:

\[
\hat v_O
\approx
v_*
\]

for different observers and signal sources.

---

# 27. Preferred Frame Problem

A computational substrate often has a natural preferred execution frame.

This is a major challenge.

CBR-E009 must therefore explicitly search for preferred-frame signatures rather than ignore them.

Potential observables include:

- directional propagation asymmetry;
- clock-rate dependence on motion;
- signal-speed variation with observer motion;
- update-order effects.

---

# 28. Moving Observer

Introduce observer-like persistent structure:

\[
O
\]

with nonzero relational motion.

The observer carries an internal clock and exchanges signals.

Ask whether measured limiting signal speed depends on observer motion.

---

# 29. E009-C — Observer Motion

For observers with different relational velocities:

\[
u_1,u_2,\ldots,
\]

measure:

\[
\hat v_*(u).
\]

A Lorentz-like result would require approximately:

\[
\hat v_*(u)
\approx
\text{constant}.
\]

This is not expected automatically and represents a much stronger test.

---

# 30. No Lorentz Transformation Encoded

The observer must not be given:

\[
\gamma
=
\frac{1}{\sqrt{1-v^2/c^2}}
\]

or any Lorentz transformation rule.

Any transformation behaviour must arise operationally from:

- signal propagation;
- clock behaviour;
- emergent metric;
- computational dynamics.

---

# 31. Two-Way Signal Measurement

To avoid requiring synchronised distant clocks, observers should initially measure round-trip speed.

Observer \(A\):

1. sends signal to \(B\);
2. receives reflected response;
3. records local clock duration.

Define radar distance:

\[
d_R(A,B)
=
\frac{
v_*\Delta\tau
}{
2
}.
\]

This is operationally close to how relativistic distance can be defined.

---

# 32. Radar Geometry

Compare:

\[
d_R
\]

with computational metric:

\[
d_C.
\]

A strong result would yield:

\[
d_R
\approx
\lambda d_C
\]

over an appropriate scale range.

This connects causality and geometry.

---

# 33. Signal-Speed Isotropy

For observer \(O\), send signals through different relational directions.

Measure:

\[
v_i.
\]

Define:

\[
I_v
=
\frac{
\operatorname{std}(v_i)
}{
\operatorname{mean}(v_i)
}.
\]

A low value indicates approximate signal-speed isotropy.

---

# 34. Signal-Speed Homogeneity

Repeat at many locations.

Define:

\[
H_v
=
\frac{
\operatorname{std}_x(v_*(x))
}{
\operatorname{mean}_x(v_*(x))
}.
\]

A low value indicates approximate homogeneous causal behaviour.

---

# 35. Causal-Cone Stability

Measure the propagation cone at different computational epochs.

Define:

\[
C_t.
\]

Compare:

\[
C_t
\]

and:

\[
C_{t+\Delta t}.
\]

A stable causal structure should survive ordinary substrate evolution.

---

# 36. Topological Evolution Control

Allow Pachner-like substrate changes while signals propagate.

Ask whether causal-cone structure remains stable despite microscopic topological retriangulation.

This is important because physical causality should not depend upon one triangulation.

---

# 37. Metric Dynamics Control

Allow the E006 cost field to evolve.

Measure whether:

\[
v_*
\]

remains meaningful when metric geometry changes gradually.

This tests causal robustness in a dynamical geometry.

---

# 38. Source Metric Distortion

Introduce an E007 persistent source structure.

The metric changes near:

\[
P_S.
\]

Ask whether local propagation times also change consistently with the altered metric.

This begins connecting causal propagation with the source-distorted geometry.

---

# 39. Local Coordinate Speed Versus Operational Speed

A signal may traverse fewer/more graph edges per update near a source.

But the relevant quantity is:

\[
\frac{
d_C
}{
\tau_C
}.
\]

If metric and clock effects compensate, internal observers might still measure a stable limiting speed.

This would be highly significant.

---

# 40. E009-D — Distorted-Metric Causality

Place signal propagation inside an E007 metric distortion.

Measure:

\[
v_{\text{local}}.
\]

Compare:

- source-free;
- source-distorted;
- synthetic metric control.

This tests whether causal cones respect emergent geometry.

---

# 41. Time Dilation Analogue

If clocks near different computational-cost environments tick at different rates, define:

\[
R_\tau
=
\frac{
\Delta\tau_A
}{
\Delta\tau_B
}.
\]

Do not call this gravitational time dilation unless later quantitative correspondence is established.

For E009 it is simply:

> environmental clock-rate variation.

---

# 42. Clock Coupling

An internal clock is computational.

Its cycle time may depend on local transition cost.

This creates a potential relationship:

\[
\text{metric cost}
\rightarrow
\text{clock rate}.
\]

If distance and time respond coherently to the same computational environment, spacetime-like structure begins to emerge.

---

# 43. Local Clock Rate

For clock \(C\):

\[
f_C
=
\frac{
N_{\text{cycles}}
}{
N_{\text{underlying causal events}}
}.
\]

Measure:

\[
f_C(q)
\]

as a function of local computational conditions.

---

# 44. Clock-Control Requirement

Use multiple clock architectures.

If all slow or accelerate by similar ratios under the same local environment, the effect is substrate-wide.

If only one design changes, it may be a clock-specific artefact.

---

# 45. Motion-Dependent Clock Rate

For moving clocks, measure whether clock rates depend on relational velocity:

\[
f_C(u).
\]

A Lorentz-like regime might exhibit systematic motion-dependent clock rates.

No functional form is assumed in the primary experiment.

---

# 46. Exploratory Lorentz-Factor Fit

Only after data exists may researchers explore whether:

\[
\frac{
\tau(u)
}{
\tau(0)
}
\]

resembles:

\[
\sqrt{1-\frac{u^2}{v_*^2}}.
\]

This is exploratory.

If promising, it requires a separately preregistered confirmatory experiment.

---

# 47. Length-Contraction Analogue

Persistent moving structures may exhibit different relational extent.

Define rest support length:

\[
L_0.
\]

Define motion-state relational length:

\[
L(u).
\]

Again, no Lorentz formula is assumed.

Measure whether motion systematically affects internal metric extent.

---

# 48. Relativity Principle

The strongest version of E009 asks whether local experiments can identify absolute motion through the computational substrate.

If an observer can easily determine:

> I am moving relative to the underlying update lattice,

then a preferred frame remains physically observable.

A relativistic-like regime requires this information to become inaccessible or irrelevant at coarse scales.

---

# 49. Preferred-Frame Detectability

Define a classifier:

\[
A_F
\]

that attempts to infer an observer's velocity relative to the underlying simulation frame using only local observations.

If:

\[
A_F
\rightarrow
\text{chance}
\]

at increasing coarse-graining scales, preferred-frame information becomes operationally hidden.

This would be significant.

---

# 50. Emergent Versus Exact Lorentz Symmetry

CBR-E009 does not require exact microscopic Lorentz invariance.

A plausible computational model could have:

\[
\text{preferred microscopic dynamics}
\]

while producing:

\[
\text{effective macroscopic Lorentz symmetry}.
\]

The relevant question is whether Lorentz-violating effects vanish sufficiently at larger scales.

---

# 51. Scale Dependence of Lorentz Violation

Define a generic anisotropy or preferred-frame measure:

\[
L_V(\ell).
\]

Test whether:

\[
L_V(\ell)\rightarrow0
\]

as observation scale:

\[
\ell
\]

increases.

This would indicate emergent symmetry.

---

# 52. Causal Universality

Different microscopic rule families may generate the same large-scale limiting speed and causal structure.

If:

\[
R_1\rightarrow C^*
\]

and:

\[
R_2\rightarrow C^*
\]

then causal behaviour may belong to a universality class.

This would be a stronger result than one fine-tuned rule.

---

# 53. Multiple Signal Species

Define distinct signal types:

\[
S_A,S_B,S_C.
\]

They may differ in:

- internal pattern;
- propagation mechanism;
- state representation.

Measure:

\[
v_A,v_B,v_C.
\]

A universal causal speed implies:

\[
v_A^{\max}
\approx
v_B^{\max}
\approx
v_C^{\max}.
\]

---

# 54. Massive-Like Versus Massless-Like Patterns

Some persistent structures may propagate more slowly than the limiting signal.

If a universal maximum exists:

\[
v_P<v_*
\]

for persistent structures,

while minimal disturbances approach:

\[
v_*,
\]

the distinction may become analogous to massive and massless propagation.

E009 should keep this terminology provisional.

---

# 55. Saturation Test

Attempt to increase signal propagation through stronger local update bias.

Does speed continue increasing indefinitely?

Or approach:

\[
v_*?
\]

A genuine limiting speed should resist further acceleration under allowed local dynamics.

---

# 56. No Explicit Speed Cap Control

Crucially, compare systems where no code contains:

```text id="wtwv7s"
if speed > vmax:
    reject
```

A nontrivial limiting speed should arise from local computational architecture rather than a direct numerical constraint.

---

# 57. Computational Bandwidth

One candidate mechanism is finite local information-processing bandwidth.

Let each relation support finite processing:

\[
B_e.
\]

Then information propagation may possess an emergent maximum throughput and velocity.

CBR-E009 should measure whether \(v_*\) derives from such constraints.

---

# 58. Update Dependency Depth

Another candidate mechanism is causal dependency depth.

A disturbance cannot influence event \(e_j\) until a chain:

\[
e_0\prec e_1\prec\cdots\prec e_j
\]

has occurred.

The number of required dependencies may itself determine effective causal distance.

---

# 59. Causal Distance

Define:

\[
d_{\prec}(A,B)
\]

as a preregistered function of shortest or longest admissible causal chains.

Compare:

\[
d_{\prec}
\]

with metric distance:

\[
d_C.
\]

A coherent spacetime-like system should exhibit systematic correspondence.

---

# 60. Metric-Causal Consistency

One possible relation is:

\[
\tau_{\min}(A,B)
\geq
\frac{
d_C(A,B)
}{
v_*
}.
\]

Test violations.

A stable causal metric should exhibit very few or no violations beyond measurement tolerance.

---

# 61. Superluminal-Like Events

Define a propagation event as superluminal-like if:

\[
d_C
>
v_*\Delta\tau.
\]

Record every such event.

They must not be discarded as noise.

Their rate:

\[
P_{\text{SL}}
\]

is a critical E009 observable.

---

# 62. Causal Leakage

If:

\[
P_{\text{SL}}>0,
\]

investigate whether events arise from:

- topology changes;
- nonlocal rewiring;
- metric redefinition;
- asynchronous scheduler artefacts;
- true causal leakage.

This may identify which computational rules are incompatible with stable causal structure.

---

# 63. Nonlocal Computational Edges

If the substrate permits arbitrary long-range edge creation, causal cones may collapse.

Therefore E009 should compare:

### Local-rewrite systems

with:

### Systems containing controlled nonlocal transitions.

Measure how causal structure degrades.

---

# 64. Causal Integrity as Emergent Constraint

A later evolutionary experiment could test whether persistence/stability selection suppresses nonlocal causal violations without a speed-limit objective.

That would extend the E005 methodology into causal structure.

It should not be part of the first E009 confirmatory experiment.

---

# 65. Source and Probe Interaction

Combine E008 and E009.

A free probe follows a distorted metric while signals define causal structure.

Ask whether:

\[
\Gamma_{P_T}
\]

always remains inside the causal cone:

\[
J^+.
\]

This links matter-like motion and causal geometry.

---

# 66. Causal Geodesics

For limiting-speed signals, define null-like minimum-time trajectories:

\[
\gamma_{\text{null}}.
\]

Compare actual signal propagation with these computational null geodesics.

This gives a stronger connection between metric and causality.

---

# 67. Timelike-Like Probe Paths

Persistent probes should satisfy:

\[
d_C
<
v_*\Delta\tau
\]

for their motion.

Measure whether this relationship is stable across probe types.

---

# 68. Proper-Time-Like Quantity

If a stable limiting speed exists, define experimentally:

\[
d\tau^2
=
dt^2
-
\frac{
d_C^2
}{
v_*^2
}.
\]

Initially this is an analytical candidate, not an assumed law.

Then ask whether internal clock cycles correlate with:

\[
\tau.
\]

---

# 69. Proper-Time Test

For moving observer trajectories, calculate candidate:

\[
\tau_{\text{geom}}.
\]

Compare with internal clock:

\[
\tau_{\text{clock}}.
\]

A strong result would yield:

\[
\tau_{\text{clock}}
\propto
\tau_{\text{geom}}.
\]

This would be a major step toward emergent relativistic spacetime.

---

# 70. No Minkowski Metric Assumption

The experiment must not optimise the system to satisfy:

\[
ds^2
=
-c^2dt^2+dx^2+dy^2+dz^2.
\]

If a Minkowski-like relationship is tested, it is calculated only after independent metric and causal measurements exist.

---

# 71. Curved Causal Structure

Inside E007 source-induced metric distortion, the effective causal cone may vary relationally.

Signals may follow paths different from the source-free case.

This may become analogous to propagation through curved spacetime.

E009 only measures the behaviour.

---

# 72. Signal Deflection

Send limiting-speed signals past a persistent source.

Compare:

\[
\Gamma_S
\]

with source-free:

\[
\Gamma_0.
\]

If the signal path follows the E007/E008 metric geodesic, this would link matter-like and signal propagation through the same geometry.

---

# 73. Universality of Geometry

A particularly strong result is:

\[
\text{persistent probes}
\]

and:

\[
\text{minimal signals}
\]

respond to the same emergent metric.

This would suggest that geometry is universal rather than object-specific.

---

# 74. Primary Controls

CBR-E009 requires at least:

### Control A — Uniform-cost substrate

No endogenous metric variation.

### Control B — Shuffled metric

Same cost distribution, random placement.

### Control C — Scheduler variation

Different synchronous/asynchronous execution strategies.

### Control D — Multiple signal species

Tests substrate universality.

### Control E — Multiple clock species

Tests operational-time universality.

### Control F — Static versus evolving topology

Tests causal robustness.

### Control G — Moving versus stationary observers

Tests preferred-frame effects.

---

# 75. Primary Evidence Conditions

Support for CBR-H009 requires:

1. a reproducible limiting propagation speed exists relative to \(d_C\);

2. multiple signal types approach the same limit;

3. the causal bound persists across locations and directions;

4. the result survives increasing system size;

5. the result survives reasonable scheduler changes;

6. embedded observers can reconstruct the causal limit;

7. independent implementation reproduces the phenomenon.

---

# 76. Stronger Evidence Conditions

A stronger result would additionally show:

- approximate observer-independence of limiting speed;
- moving clocks exhibit systematic rate changes;
- preferred-frame signatures decrease under coarse-graining;
- internal clock time correlates with a proper-time-like quantity;
- signal and matter-like structures respond to the same emergent geometry.

---

# 77. Failure Conditions

CBR-E009 fails to support the hypothesis if:

- limiting speed is purely a hard-coded edge-per-step cap;
- different signal classes possess unrelated maximum velocities;
- large directional anisotropies remain;
- causal violations grow with system size;
- observer motion reveals a strong preferred frame;
- the emergent metric does not predict propagation time;
- asynchronous implementations destroy the result.

---

# 78. Important Negative Result

One especially important result would be:

\[
\text{stable metric}
\]

and:

\[
\text{geodesic matter motion}
\]

but:

\[
\text{no universal causal speed}.
\]

That would show that E006–E008 are insufficient to recover relativistic causal structure.

This would significantly constrain the CBR programme.

---

# 79. Another Important Negative Result

A universal speed might exist only in the simulator's preferred frame.

If moving observers measure:

\[
v_*(u)
\neq
v_*,
\]

then the system has an observable absolute rest frame.

That would distinguish it sharply from relativistic physics.

---

# 80. Weak Positive Result

A weak positive result would establish:

> finite local computation creates a reproducible maximum propagation rate.

This is useful but not surprising.

---

# 81. Strong Positive Result

A stronger result would establish:

> several independent signal species, measured using internally reconstructed distance and local clocks, converge toward the same causal limit.

This indicates a substrate-level causal structure.

---

# 82. Strongest E009 Result

The strongest result would show:

\[
\boxed{
\text{local asynchronous computation}
}
\]

produces:

\[
\boxed{
\text{stable emergent metric}
}
\]

plus:

\[
\boxed{
\text{universal causal cone}
}
\]

such that:

- different signal species share the same limiting velocity;
- moving embedded observers measure approximately the same limit;
- preferred-frame signatures decrease at large scales;
- clock behaviour correlates with trajectory geometry;
- signals and persistent structures respond to the same geometry.

At that point, CBR would no longer merely have:

\[
\text{emergent space}.
\]

It would possess the beginnings of:

\[
\boxed{
\text{emergent spacetime structure}.
}
\]

---

# 83. Interpretation Boundary

Even the strongest E009 outcome would not prove exact Lorentz invariance.

Nor would it establish special or general relativity quantitatively.

The appropriate conclusion would be:

> **Coordinate-free local computation can generate an operational causal structure with a universal or approximately universal limiting propagation speed and potentially relativistic-like observer behaviour.**

Exact correspondence must be tested separately.

---

# 84. Relationship to CBR-E010

E010 should become the first **quantitative physics correspondence experiment**.

The prior sequence deliberately asks qualitative structural questions:

\[
\text{dimension}
\]

\[
\text{topology}
\]

\[
\text{metric}
\]

\[
\text{matter-like persistence}
\]

\[
\text{geodesic motion}
\]

\[
\text{causality}.
\]

CBR-E010 can then ask:

> **Does the combined emergent system quantitatively approximate known relativistic gravitational relationships?**

That is a much higher evidentiary bar.

---

# 85. CBR-E009 YAML Summary

```yaml id="6k3zfd"
cbr_oen:
  protocol_version: "1.0"

experiment:
  id: "CBR-E009"
  version: "1.0"

  title:
    "Emergent Causal Cones and Limiting Propagation Speed"

hypothesis:
  id: "CBR-H009"

  statement: >
    Local coordinate-free computational dynamics can generate
    a stable causal structure with a reproducible limiting
    propagation speed relative to an independently emergent
    computational metric.

null_hypothesis: >
  Apparent causal cones arise only from explicit simulator
  constraints, preferred execution frames or signal-specific
  propagation rules and do not form a robust emergent causal geometry.

substrate:

  topology:
    source:
      "CBR-E004 / E005"

  metric:
    source:
      "CBR-E006"

  matter_metric_coupling:
    source:
      "CBR-E007"

  motion:
    source:
      "CBR-E008"

  coordinates:
    enabled: false

time:

  primitive_physical_time:
    enabled: false

  computational_order:
    enabled: true

  internal_clocks:
    enabled: true

tracks:

  E009_A:
    name:
      "Synchronous Propagation Baseline"

  E009_B:
    name:
      "Asynchronous Causal Structure"

  E009_C:
    name:
      "Moving Observer Measurements"

  E009_D:
    name:
      "Causality in Distorted Metric"

signals:

  multiple_species:
    required: true

  global_routing:
    forbidden: true

  predefined_destination:
    forbidden: true

measurements:

  primary:

    - limiting_propagation_speed
    - signal_speed_variance
    - causal_cone_violations
    - metric_propagation_consistency

  secondary:

    - signal_speed_isotropy
    - signal_speed_homogeneity
    - observer_speed_dependence
    - clock_rate_dependence
    - preferred_frame_detectability
    - radar_distance_accuracy
    - proper_time_candidate_agreement

controls:

  - uniform_metric
  - shuffled_metric
  - synchronous_scheduler
  - asynchronous_scheduler
  - multiple_signal_species
  - multiple_clock_species
  - moving_observers
  - static_topology
  - evolving_topology

forbidden_primitives:

  - speed_of_light_constant
  - Lorentz_transform
  - Minkowski_metric
  - time_dilation_formula
  - length_contraction_formula
  - preferred_geodesic
  - global_signal_router

primary_endpoint: >
  Determine whether distinct local signals exhibit a common,
  reproducible limiting propagation speed relative to the
  emergent computational metric and whether that causal bound
  remains operationally meaningful to embedded observers.

replication:

  asynchronous_independent_implementation_required_for_r2: true

  institutional_replication_required_for_r3: true

negative_results:
  retained: true
```

---

# 86. Experimental Progression

The programme now has a remarkably clean chain:

\[
\boxed{
E001:
\text{dimension}
}
\]

\[
\downarrow
\]

\[
\boxed{
E002:
\text{dimension-blind organisation}
}
\]

\[
\downarrow
\]

\[
\boxed{
E003:
\text{3-manifold topology}
}
\]

\[
\downarrow
\]

\[
\boxed{
E004:
\text{explicit topological dynamics}
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
\text{distance from computational cost}
}
\]

\[
\downarrow
\]

\[
\boxed{
E007:
\text{persistent structure distorts distance}
}
\]

\[
\downarrow
\]

\[
\boxed{
E008:
\text{free structure follows geometry}
}
\]

\[
\downarrow
\]

\[
\boxed{
E009:
\text{computation generates causal structure}
}
\]

The progression has therefore moved from:

\[
\text{pure relational computation}
\]

toward:

\[
\boxed{
\text{topology + geometry + matter-like structures + motion + causality}.
}
\]

---

# 87. Final Principle

The decisive idea in CBR-E009 is not simply that information takes time to propagate.

Any computer can do that.

The real question is whether embedded processes infer a consistent relationship:

\[
\boxed{
\text{distance}
\leftrightarrow
\text{time}
\leftrightarrow
\text{causal reachability}
}
\]

even though none of these were provided as a conventional spacetime coordinate system.

If different signals, clocks and observers discover the same causal structure from within the computation, then the system has begun to acquire something much stronger than a graph with an update loop.

It has acquired an internally operational notion of:

\[
\boxed{
\text{what can influence what, and how quickly}.
}
\]

That is the scientific purpose of CBR-E009.