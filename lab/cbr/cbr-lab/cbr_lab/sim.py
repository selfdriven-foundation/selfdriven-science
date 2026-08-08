import random
import networkx as nx
from .rules import local_rewrite, RuleParams
from .metrics import ball_growth_dimension, spectral_dimension, largest_component_subgraph


def initial_graph(node_count: int, initial_edges: int, rng: random.Random) -> nx.Graph:
    g = nx.Graph()
    g.add_nodes_from(range(node_count))
    while g.number_of_edges() < initial_edges:
        a = rng.randrange(node_count)
        b = rng.randrange(node_count)
        if a != b:
            g.add_edge(a, b)
    return g


def run_one(seed: int, node_count=500, initial_edges=750, steps=20000, params=None):
    rng = random.Random(seed)
    params = params or RuleParams()
    g = initial_graph(node_count, initial_edges, rng)

    for _ in range(steps):
        local_rewrite(g, rng, params)

    hdim, radii, growth = ball_growth_dimension(g, rng)
    sdim, times, returns = spectral_dimension(g, rng)
    largest = largest_component_subgraph(g)

    return {
        "seed": seed,
        "nodes": g.number_of_nodes(),
        "edges": g.number_of_edges(),
        "largest_component": largest.number_of_nodes(),
        "hausdorff_like_dimension": hdim,
        "spectral_dimension": sdim,
        "target_degree": params.target_degree,
        "triangle_bias": params.triangle_bias,
        "rewire_probability": params.rewire_probability,
        "random_link_probability": params.random_link_probability,
    }, g, (radii, growth), (times, returns)
