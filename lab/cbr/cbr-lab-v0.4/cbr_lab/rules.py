from dataclasses import dataclass, asdict
import random
import networkx as nx

@dataclass
class Genome:
    target_degree: int = 6
    triangle_bias: float = 0.45
    rewire_probability: float = 0.04
    random_link_probability: float = 0.01

    def clipped(self):
        return Genome(
            target_degree=max(2, min(14, int(round(self.target_degree)))),
            triangle_bias=max(0.0, min(1.0, self.triangle_bias)),
            rewire_probability=max(0.0, min(0.5, self.rewire_probability)),
            random_link_probability=max(0.0, min(0.25, self.random_link_probability)),
        )

    def mutate(self, rng: random.Random, scale=0.15):
        return Genome(
            self.target_degree + rng.choice([-1, 0, 1]),
            self.triangle_bias + rng.gauss(0, scale),
            self.rewire_probability + rng.gauss(0, scale / 4),
            self.random_link_probability + rng.gauss(0, scale / 6),
        ).clipped()

    def as_dict(self):
        return asdict(self)


def random_genome(rng: random.Random):
    return Genome(
        target_degree=rng.randint(3, 10),
        triangle_bias=rng.random(),
        rewire_probability=rng.uniform(0, 0.15),
        random_link_probability=rng.uniform(0, 0.08),
    )


def create_initial_graph(n, rng: random.Random):
    # A connected seed with no spatial coordinates: ring + sparse random relations.
    g = nx.Graph()
    g.add_nodes_from(range(n))
    for i in range(n):
        g.add_edge(i, (i + 1) % n)
    for _ in range(n // 2):
        a, b = rng.randrange(n), rng.randrange(n)
        if a != b:
            g.add_edge(a, b)
    return g


def local_rewrite(g: nx.Graph, genome: Genome, rng: random.Random):
    v = rng.choice(tuple(g.nodes))
    nbrs = list(g.neighbors(v))
    degree = len(nbrs)

    if degree < genome.target_degree:
        candidate = None
        if nbrs and rng.random() < genome.triangle_bias:
            via = rng.choice(nbrs)
            local = [u for u in g.neighbors(via) if u != v and not g.has_edge(v, u)]
            if local:
                candidate = rng.choice(local)
        if candidate is None and rng.random() < genome.random_link_probability:
            candidate = rng.choice(tuple(g.nodes))
        if candidate is not None and candidate != v:
            g.add_edge(v, candidate)

    elif degree > genome.target_degree and degree > 2:
        # Prefer deleting an edge that does not disconnect the local node entirely.
        u = rng.choice(nbrs)
        g.remove_edge(v, u)
        if not nx.has_path(g, v, u):
            g.add_edge(v, u)

    current_nbrs = list(g.neighbors(v))
    if current_nbrs and rng.random() < genome.rewire_probability:
        u = rng.choice(current_nbrs)
        g.remove_edge(v, u)
        candidates = [x for x in g.nodes if x != v and not g.has_edge(v, x)]
        if candidates:
            g.add_edge(v, rng.choice(candidates))
        else:
            g.add_edge(v, u)
