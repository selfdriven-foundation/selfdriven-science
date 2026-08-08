# CBR-Lab v0.1

A geometry-free experimental simulator for testing whether local relational rewrite rules can produce large-scale structures with emergent dimensional behaviour.

## Hypothesis

Do not encode x/y/z coordinates. Start from an unlabeled relational graph and local update rules, then measure the geometry that emerges.

Initial metrics:

- ball-growth / Hausdorff-like dimension: `N(r) ~ r^d`
- spectral dimension from random-walk return probability: `P(t) ~ t^(-d/2)`

The interesting result is not a single rule that can be tuned to 3D. The interesting result would be a broad, geometry-free rule family that repeatedly converges near dimension 3, especially if both metrics agree.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Single run

```bash
python run_single.py
```

## Batch search

Start small:

```bash
python run_batch.py --runs 100 --nodes 500 --steps 20000
```

Then scale toward the proposed first experiment:

```bash
python run_batch.py --runs 1000 --nodes 1000 --steps 100000
```

Outputs are written under `results/`:

- `results.csv`
- `hausdorff_distribution.png`
- `dimension_scatter.png`

## Current rule family

Each run samples:

- target degree
- local triangle-closing bias
- rewiring probability
- random-link probability

The rule sees graph relationships only. There are no spatial coordinates.

## What v0.1 does *not* establish

An estimated dimension near 3 does not establish that a graph is a 3-manifold. Later stages should add:

1. local homology / simplicial-complex tests
2. neighbourhood regularity and topology
3. emergent metric / geodesic tests
4. persistent computational structures (matter)
5. metric modification by those structures
6. gravity-as-computational-arbitrage tests

## Suggested experiment record

Every serious run should record:

- git commit / simulator version
- rule parameters
- PRNG seed
- node and step counts
- all metrics, including failed/NaN measurements

This keeps the search reproducible and makes negative results useful.
