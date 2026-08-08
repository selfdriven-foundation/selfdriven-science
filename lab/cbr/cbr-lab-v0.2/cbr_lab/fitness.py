import math
from collections import Counter
import networkx as nx
import numpy as np

from .metrics import largest_component_subgraph


def _normalized_entropy(values):
    values = list(values)
    if not values:
        return 0.0
    counts = np.array(list(Counter(values).values()), dtype=float)
    p = counts / counts.sum()
    h = float(-(p * np.log(p)).sum())
    hmax = math.log(max(2, len(counts)))
    return min(1.0, h / hmax) if hmax > 0 else 0.0


def structural_signature(graph: nx.Graph):
    if graph.number_of_nodes() == 0:
        return {"giant": 0.0, "mean_degree": 0.0, "degree_entropy": 0.0, "clustering": 0.0}
    g = largest_component_subgraph(graph)
    degrees = [d for _, d in g.degree()]
    return {
        "giant": g.number_of_nodes() / graph.number_of_nodes(),
        "mean_degree": float(np.mean(degrees)) if degrees else 0.0,
        "degree_entropy": _normalized_entropy(degrees),
        "clustering": float(nx.average_clustering(g)) if g.number_of_nodes() > 1 else 0.0,
    }


def score_trajectory(signatures):
    """Dimension-blind fitness: persistence + complexity + late stability."""
    if not signatures:
        return {"fitness": 0.0, "persistence": 0.0, "complexity": 0.0, "stability": 0.0}

    final = signatures[-1]
    persistence = float(np.mean([s["giant"] for s in signatures]))

    # Reward heterogeneous local structure without targeting any dimension.
    # Entropy and clustering contribute equally; giant-component factor prevents
    # disconnected noise from looking artificially complex.
    complexity = final["giant"] * (0.5 * final["degree_entropy"] + 0.5 * final["clustering"])

    if len(signatures) < 2:
        stability = 0.0
    else:
        a, b = signatures[-2], signatures[-1]
        deltas = [
            abs(a["giant"] - b["giant"]),
            abs(a["degree_entropy"] - b["degree_entropy"]),
            abs(a["clustering"] - b["clustering"]),
            min(1.0, abs(a["mean_degree"] - b["mean_degree"]) / max(1.0, a["mean_degree"])),
        ]
        stability = max(0.0, 1.0 - float(np.mean(deltas)))

    fitness = 0.40 * persistence + 0.35 * complexity + 0.25 * stability
    return {
        "fitness": fitness,
        "persistence": persistence,
        "complexity": complexity,
        "stability": stability,
    }
