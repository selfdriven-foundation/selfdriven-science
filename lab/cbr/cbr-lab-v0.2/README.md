# CBR-Lab v0.2

Experimental code for testing whether geometry-like structure can emerge from local relational computation **without predefining spatial coordinates**.

## Core hypothesis

A family of local graph-rewrite rules is evolved for persistence, structural complexity, and stability. **Dimension is not part of the fitness function.** Hausdorff-like and spectral dimensions are measured only after each simulation.

The interesting result would not be "we made a 3D graph". It would be evidence that rules selected for dimension-independent properties repeatedly converge toward dimension ~3.

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Evolutionary experiment

Small test:

```bash
python run_evolution.py --generations 3 --population 8 --nodes 200 --steps 3000 --replicates 1
```

More meaningful search:

```bash
python run_evolution.py --generations 30 --population 50 --nodes 1000 --steps 50000 --replicates 3
```

Outputs:

- `results/evolution.csv` — every genome and measured result
- `results/evolution_fitness.png` — best/mean dimension-blind fitness by generation
- `results/evolution_dimensions.png` — observed final-population dimensionality

## Fitness

No dimensional term appears in selection:

```text
fitness = 0.40 * persistence
        + 0.35 * complexity
        + 0.25 * stability
```

- **Persistence**: fraction of nodes retained in the giant connected component through late checkpoints.
- **Complexity**: degree-distribution entropy plus local clustering, weighted by connectedness.
- **Stability**: similarity of structural statistics between the final two checkpoints.

These are intentionally provisional. They should be varied in later experiments to ensure any dimensional result is not an artefact of one fitness definition.

## Genome / rule family

Rules currently evolve four parameters:

- target local degree
- triangle-closure bias
- rewiring probability
- random-link probability

Local rewrites see graph relationships only. There are no x/y/z coordinates.

## Measurements

### Hausdorff-like / ball-growth dimension

For graph radius `r`, measure the mean number of reachable nodes `N(r)` and fit:

```text
N(r) ~ r^d
```

### Spectral dimension

Run random walks and fit return probability:

```text
P(t) ~ t^(-d_s/2)
```

Agreement between independent dimension estimators is more interesting than either measurement alone.

## Scientific caution

This is an exploratory model, not evidence that physical space is computational. Random finite graphs have strong size and saturation effects, and the current graph rewrite family is extremely small. A credible result requires controls, alternative rule families, larger systems, independent manifold tests, repeated seeds, and preregistered analysis criteria.

## v0.3 direction

The next major test is local manifoldness: convert relational neighbourhoods into simplicial complexes and test whether vertex links/homology resemble a 3-manifold rather than merely having effective dimension near 3.
