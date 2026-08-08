# CBR-Lab v0.3 — Local Manifold Tests

CBR-Lab explores whether geometry-like structure can emerge from **local relational computation with no predefined x/y/z coordinates**.

v0.3 adds a stricter question to the dimension measurements:

> If a graph exhibits ~3D scaling, does its induced simplicial structure also look locally like a 3-manifold?

## Scientific separation

The evolutionary fitness remains dimension-blind and topology-blind:

```text
fitness = 0.40 persistence + 0.35 complexity + 0.25 stability
```

Neither `dH`, `dS`, nor the manifold score affects reproduction. They are observational measurements only.

## Local 3-manifold criterion

For an interior vertex of a triangulated 3-manifold, its **vertex link** should be topologically a 2-sphere `S²`.

For each sampled vertex, v0.3 builds the flag/clique complex on its neighbour graph and tests:

- link is connected;
- Euler characteristic `χ = 2`;
- GF(2) Betti signature `(β0, β1, β2) = (1, 0, 1)`;
- no 3-simplices inside the link (so the link is locally 2D rather than filled into higher dimension);
- at least 90% of link edges belong to exactly two triangles.

A simulation is classified as:

- `candidate_3_manifold`
- `3d_scaling_not_manifold`
- `manifold_like_links_non3d_scaling`
- `no_3_manifold_evidence`

The default `candidate_3_manifold` threshold requires both dimension estimates within ±0.6 of 3 and at least 65% of sampled links passing the S² test.

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run random rule survey

Smoke test:

```bash
python run_topology.py --runs 3 --nodes 120 --steps 1200 --topology-samples 10
```

Larger exploratory run:

```bash
python run_topology.py --runs 100 --nodes 1000 --steps 50000 --topology-samples 50
```

Outputs:

- `results/topology_runs.csv`
- `results/dimension_vs_manifold.png`

## Run dimension-blind evolution + topology observation

```bash
python run_evolution.py --generations 30 --population 50 --nodes 1000 --steps 50000 --replicates 3
```

The rule selection still sees only persistence, complexity, and stability. Topology and dimension are logged afterward.

## Important limitation

The current topology is the **flag/clique complex inferred from the graph**. A graph does not encode every possible simplicial complex: in a flag complex, every clique is automatically filled. This is a deliberate, reproducible first model, but it is restrictive.

A stronger v0.4 should evolve an explicit simplicial rewrite system (vertices/edges/triangles/tetrahedra) rather than inferring simplices from graph cliques. That would let topology evolve independently of graph completion and make Pachner-move-style experiments possible.

## Why this matters

A result `d ≈ 3` alone is weak. Random networks can exhibit finite-scale power laws. Requiring local `S²` links asks for something much closer to actual 3-manifold structure.

The interesting observation is therefore not:

```text
we found a graph with dimension 3
```

but:

```text
dimension-blind local rules
        ↓
stable relational computation
        ↓
dH ≈ dS ≈ 3
        ↓
most vertex links ≈ S²
```

That is a substantially harder test of the CBR hypothesis.
