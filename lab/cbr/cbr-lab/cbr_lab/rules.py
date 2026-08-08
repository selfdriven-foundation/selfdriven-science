from dataclasses import dataclass
import random
import networkx as nx


@dataclass(frozen=True)
class RuleParams:
    target_degree: int = 6
    triangle_bias: float = 0.45
    rewire_probability: float = 0.03
    random_link_probability: float = 0.02


def local_rewrite(graph: nx.Graph, rng: random.Random, p: RuleParams) -> None:
    node = rng.choice(tuple(graph.nodes))
    neighbors = list(graph.neighbors(node))
    degree = len(neighbors)

    if degree < p.target_degree:
        if neighbors and rng.random() < p.triangle_bias:
            pivot = rng.choice(neighbors)
            candidates = [
                n for n in graph.neighbors(pivot)
                if n != node and not graph.has_edge(node, n)
            ]
            if candidates:
                graph.add_edge(node, rng.choice(candidates))
                return

        if rng.random() < p.random_link_probability or not neighbors:
            other = rng.choice(tuple(graph.nodes))
            if other != node:
                graph.add_edge(node, other)

    elif degree > p.target_degree and neighbors:
        graph.remove_edge(node, rng.choice(neighbors))

    if graph.number_of_edges() and rng.random() < p.rewire_probability:
        a, b = rng.choice(tuple(graph.edges))
        graph.remove_edge(a, b)
        c = rng.choice(tuple(graph.nodes))
        if c != a and not graph.has_edge(a, c):
            graph.add_edge(a, c)
        else:
            graph.add_edge(a, b)
