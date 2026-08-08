import random
import networkx as nx
from .rules import local_rewrite, RuleParams
from .metrics import ball_growth_dimension, spectral_dimension, largest_component_subgraph
from .fitness import structural_signature, score_trajectory


def initial_graph(node_count: int, initial_edges: int, rng: random.Random) -> nx.Graph:
    g = nx.Graph()
    g.add_nodes_from(range(node_count))
    while g.number_of_edges() < initial_edges:
        a = rng.randrange(node_count)
        b = rng.randrange(node_count)
        if a != b:
            g.add_edge(a, b)
    return g


def evolve_graph(seed: int, node_count=500, initial_edges=750, steps=20000, params=None, checkpoints=4):
    rng = random.Random(seed)
    params = params or RuleParams()
    g = initial_graph(node_count, initial_edges, rng)
    signatures = []
    checkpoint_steps = set()
    if checkpoints > 0:
        checkpoint_steps = {max(1, int(steps * (i + 1) / checkpoints)) for i in range(checkpoints)}

    for step in range(1, steps + 1):
        local_rewrite(g, rng, params)
        if step in checkpoint_steps:
            signatures.append(structural_signature(g))

    if not signatures:
        signatures.append(structural_signature(g))
    return g, signatures, rng


def evaluate_rule(seed: int, node_count=500, initial_edges=750, steps=20000, params=None):
    g, signatures, rng = evolve_graph(seed, node_count, initial_edges, steps, params)
    scores = score_trajectory(signatures)
    hdim, radii, growth = ball_growth_dimension(g, rng)
    sdim, times, returns = spectral_dimension(g, rng)
    largest = largest_component_subgraph(g)
    row = {
        "seed": seed,
        "nodes": g.number_of_nodes(),
        "edges": g.number_of_edges(),
        "largest_component": largest.number_of_nodes(),
        **scores,
        "hausdorff_like_dimension": hdim,
        "spectral_dimension": sdim,
        "target_degree": params.target_degree,
        "triangle_bias": params.triangle_bias,
        "rewire_probability": params.rewire_probability,
        "random_link_probability": params.random_link_probability,
    }
    return row, g, (radii, growth), (times, returns)


def run_one(seed: int, node_count=500, initial_edges=750, steps=20000, params=None):
    return evaluate_rule(seed, node_count, initial_edges, steps, params or RuleParams())
