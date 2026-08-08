import math
import random
import numpy as np
import networkx as nx


def giant_fraction(g):
    if g.number_of_nodes() == 0:
        return 0.0
    return len(max(nx.connected_components(g), key=len)) / g.number_of_nodes()


def degree_entropy(g):
    degrees = [d for _, d in g.degree()]
    if not degrees:
        return 0.0
    values, counts = np.unique(degrees, return_counts=True)
    p = counts / counts.sum()
    h = float(-(p * np.log2(p)).sum())
    return h / max(1.0, math.log2(len(values) + 1))


def structural_snapshot(g):
    return {
        "giant": giant_fraction(g),
        "entropy": degree_entropy(g),
        "clustering": nx.average_clustering(g) if g.number_of_nodes() else 0.0,
        "mean_degree": (2 * g.number_of_edges() / g.number_of_nodes()) if g.number_of_nodes() else 0.0,
    }


def complexity_score(g):
    s = structural_snapshot(g)
    # Dimension-blind: connectedness, degree diversity, and nontrivial local structure only.
    return s["giant"] * (0.65 * s["entropy"] + 0.35 * min(1.0, 2.0 * s["clustering"]))


def stability_score(a, b):
    diffs = [
        abs(a["giant"] - b["giant"]),
        abs(a["entropy"] - b["entropy"]),
        abs(a["clustering"] - b["clustering"]),
        min(1.0, abs(a["mean_degree"] - b["mean_degree"]) / 10.0),
    ]
    return max(0.0, 1.0 - float(np.mean(diffs)))


def estimate_ball_dimension(g, rng: random.Random, samples=32, max_radius=8):
    nodes = list(g.nodes)
    if len(nodes) < 4:
        return float("nan")
    sample_nodes = rng.sample(nodes, min(samples, len(nodes)))
    radii, counts = [], []
    for r in range(1, max_radius + 1):
        vals = []
        for v in sample_nodes:
            lengths = nx.single_source_shortest_path_length(g, v, cutoff=r)
            vals.append(len(lengths))
        mean = float(np.mean(vals))
        if mean < 0.75 * len(nodes) and mean > 1:
            radii.append(r)
            counts.append(mean)
    if len(radii) < 3:
        return float("nan")
    slope, _ = np.polyfit(np.log(radii), np.log(counts), 1)
    return float(slope)


def estimate_spectral_dimension(g, rng: random.Random, walks=1200, steps=24):
    nodes = [v for v in g.nodes if g.degree(v) > 0]
    if not nodes:
        return float("nan")
    returns = np.zeros(steps + 1)
    for _ in range(walks):
        start = rng.choice(nodes)
        current = start
        for t in range(1, steps + 1):
            nbrs = list(g.neighbors(current))
            if not nbrs:
                break
            current = rng.choice(nbrs)
            if current == start:
                returns[t] += 1
    p = returns / walks
    # Use even t to reduce bipartite/parity noise; omit zeros and earliest transient.
    xs, ys = [], []
    for t in range(4, steps + 1, 2):
        if p[t] > 0:
            xs.append(t)
            ys.append(p[t])
    if len(xs) < 3:
        return float("nan")
    slope, _ = np.polyfit(np.log(xs), np.log(ys), 1)
    return float(-2.0 * slope)
