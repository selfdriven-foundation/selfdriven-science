# CBR-Lab v0.4 — Explicit Simplicial Topology

CBR-Lab v0.4 moves from graph-derived clique complexes to an **explicit evolving 3-dimensional simplicial complex**. Tetrahedra are first-class state. Evolution is driven primarily by local Pachner moves, with an optional topology-agnostic defect channel.

The purpose is to create a controlled computational-topology laboratory for the CBR hypothesis:

> Can dimension-blind selection for persistence, complexity and stability produce or retain structures that exhibit 3-manifold topology and useful emergent geometry?

## Important scientific distinction

Starting from the `s3` seed does **not** demonstrate that a 3-manifold emerged from nothing. The seed is the boundary of a 4-simplex, a known triangulation of \(S^3\). Legal Pachner moves preserve its topology. This seed is therefore the **control experiment**.

The stronger experiment uses topology-agnostic defects and/or the `random` seed, while keeping topology and dimension completely out of the evolutionary fitness. We then observe whether selected rule mixtures suppress defects or recover manifold-like local structure as a side effect of persistence, complexity and stability.

## State model

A simulation state is a finite abstract simplicial complex represented by maximal tetrahedra:

```text
vertices -> edges -> triangles -> tetrahedra
```

No x/y/z coordinates are stored.

The **tetrahedral dual graph** is the primary graph-based geometry probe for ball-growth and spectral dimension, because the vertex 1-skeleton of a triangulation can become very dense and saturate at small radius. The 1-skeleton dimensions are still recorded as secondary diagnostics.

## Pachner moves

v0.4 implements local 3D bistellar moves:

- `1-4`: subdivide one tetrahedron with a new vertex
- `4-1`: inverse of `1-4`
- `2-3`: replace two tetrahedra sharing a face with three sharing an edge
- `3-2`: inverse of `2-3`

For a triangulated 3-manifold, legal Pachner moves change the triangulation without changing the underlying PL topology.

A fifth operation, `defect`, randomly adds or removes a tetrahedron. It is deliberately topology-agnostic and allows the experiment to leave the manifold class.

## Genome

Each evolving rule genome contains:

```text
w14
w41
w23
w32
defect_probability
```

The four Pachner weights are normalised probabilities. Mutation changes both move preference and defect rate.

## Fitness remains dimension- and topology-blind

Selection uses only:

```text
fitness = 0.40 * persistence
        + 0.35 * complexity
        + 0.25 * stability
```

Where:

- **persistence** = fraction of tetrahedra in the largest tetra-adjacency component
- **complexity** = diversity of local tetrahedral incidence patterns
- **stability** = similarity of late-stage structural snapshots

The following do **not** affect fitness:

- Hausdorff-like dimension
- spectral dimension
- face-manifold incidence
- vertex-link topology
- Betti numbers
- whether the state resembles \(S^3\)

These are observations only.

## Topology diagnostics

Because tetrahedra are explicit, v0.4 can perform stronger tests than v0.3.

For each vertex, its link is constructed directly from the opposite faces of incident tetrahedra. A closed interior vertex in a triangulated 3-manifold should have a link homeomorphic to \(S^2\). The code tests:

```text
connected link
Euler characteristic = 2
Betti numbers = (1,0,1)
every link edge belongs to exactly two link triangles
```

It also measures triangle-face incidence in the full complex. For a closed 3-manifold every triangular face should be incident to exactly two tetrahedra.

For moderate complexes, global homology over GF(2) is calculated. The `s3` control seed has:

```text
Betti = [1, 0, 0, 1]
```

as expected for \(S^3\).

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run one simplicial experiment

```bash
python run_simplicial.py --steps 3000 --seed-mode s3 --defect 0.01
```

A pure Pachner control can be run with:

```bash
python run_simplicial.py --steps 3000 --seed-mode s3 --defect 0
```

A deliberately unconstrained start is:

```bash
python run_simplicial.py --steps 3000 --seed-mode random
```

## Run dimension-blind evolution

```bash
python run_simplicial_evolution.py \
  --generations 30 \
  --population 50 \
  --steps 5000 \
  --replicates 3 \
  --seed-mode s3
```

Results are written to:

```text
results-v04/simplicial_evolution_v04.csv
```

Watch in particular:

```text
defect_probability
fitness
dH
dS
face_closed_fraction
s2_pass_fraction
global_betti
```

A particularly interesting result would be evolutionary pressure toward low defect rates and high manifold diagnostics **despite none of those topology measurements appearing in the fitness function**.

## Suggested experimental programme

### Control A — Pachner invariance

Start with `s3`, set defect rate to zero, and verify that manifold diagnostics and global homology remain invariant while triangulation size and connectivity change.

### Control B — Defect sensitivity

Increase defect rate and quantify how rapidly closed-face incidence, local \(S^2\) links and homology degrade.

### Experiment C — Dimension-blind evolutionary selection

Allow defect rate to mutate. Select only for persistence, complexity and stability. Ask whether evolution drives defect probability down and manifold evidence up.

### Experiment D — Random start

Start from a random tetrahedral hypergraph. This is much harder: current Pachner moves are most productive in already manifold-like neighbourhoods. Failure to recover a manifold is therefore not yet strong evidence against CBR; it may indicate the rewrite rule family is too restrictive.

## What v0.4 establishes

v0.4 is a stronger simulation substrate, not yet a claim that CBR has derived physical space. It cleanly separates three questions:

1. Can local computation preserve and explore a 3-manifold without coordinates?
2. Does dimension-blind selection favour manifold-preserving dynamics when defects are allowed?
3. Do the resulting complexes also develop approximately three-dimensional graph/spectral geometry?

The next major step would be to replace ad-hoc defect operations with a broader set of **fully local birth/death and gluing rules** that do not presuppose manifold topology, then test whether manifold states become dynamical attractors.
