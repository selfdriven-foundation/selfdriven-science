import math
import random
import networkx as nx
import numpy as np


def largest_component_subgraph(graph: nx.Graph) -> nx.Graph:
    if graph.number_of_nodes() == 0:
        return graph.copy()
    largest = max(nx.connected_components(graph), key=len)
    return graph.subgraph(largest).copy()


def ball_growth_dimension(graph: nx.Graph, rng: random.Random, samples=32, max_radius=8):
    g = largest_component_subgraph(graph)
    if g.number_of_nodes() < 8:
        return math.nan, [], []

    nodes = list(g.nodes)
    sample_nodes = rng.sample(nodes, min(samples, len(nodes)))
    radii = np.arange(1, max_radius + 1)
    counts = []

    for r in radii:
        values = []
        for node in sample_nodes:
            lengths = nx.single_source_shortest_path_length(g, node, cutoff=int(r))
            values.append(len(lengths))
        counts.append(float(np.mean(values)))

    counts = np.asarray(counts)
    valid = (counts > 1.0) & (counts < g.number_of_nodes() * 0.7)
    if valid.sum() < 2:
        return math.nan, radii.tolist(), counts.tolist()

    slope, _ = np.polyfit(np.log(radii[valid]), np.log(counts[valid]), 1)
    return float(slope), radii.tolist(), counts.tolist()


def spectral_dimension(graph: nx.Graph, rng: random.Random, walks=2500, max_steps=24):
    g = largest_component_subgraph(graph)
    if g.number_of_nodes() < 8:
        return math.nan, [], []

    nodes = list(g.nodes)
    returns = np.zeros(max_steps + 1, dtype=float)

    for _ in range(walks):
        start = rng.choice(nodes)
        current = start
        for t in range(1, max_steps + 1):
            neighbors = list(g.neighbors(current))
            if not neighbors:
                break
            current = rng.choice(neighbors)
            if current == start:
                returns[t] += 1

    p = returns[1:] / walks
    t = np.arange(1, max_steps + 1)
    valid = (p > 0) & (t >= 4)
    if valid.sum() < 3:
        return math.nan, t.tolist(), p.tolist()

    slope, _ = np.polyfit(np.log(t[valid]), np.log(p[valid]), 1)
    return float(-2.0 * slope), t.tolist(), p.tolist()
