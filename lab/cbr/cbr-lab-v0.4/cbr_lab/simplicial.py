from collections import Counter, defaultdict
from itertools import combinations
import random
import networkx as nx


def canon(simplex):
    return tuple(sorted(simplex))


class SimplicialComplex3D:
    """Finite 3D abstract simplicial complex represented by maximal tetrahedra."""

    def __init__(self, tetrahedra=None):
        self.tetrahedra = {canon(t) for t in (tetrahedra or []) if len(set(t)) == 4}
        self.next_vertex = (max(self.vertices()) + 1) if self.tetrahedra else 0

    @classmethod
    def s3_boundary_seed(cls):
        # Boundary of a 4-simplex: five tetrahedra triangulating S^3.
        verts = range(5)
        return cls([tuple(v for v in verts if v != omitted) for omitted in verts])

    @classmethod
    def random_seed(cls, rng: random.Random, vertices=10, tetrahedra=16):
        ts = set()
        while len(ts) < tetrahedra:
            ts.add(canon(rng.sample(range(vertices), 4)))
        return cls(ts)

    def copy(self):
        other = SimplicialComplex3D(self.tetrahedra)
        other.next_vertex = self.next_vertex
        return other

    def vertices(self):
        return {v for t in self.tetrahedra for v in t}

    def simplices(self, size):
        out = set()
        for t in self.tetrahedra:
            out.update(canon(s) for s in combinations(t, size))
        return out

    def edges(self):
        return self.simplices(2)

    def triangles(self):
        return self.simplices(3)

    def face_incidence(self):
        c = Counter()
        for t in self.tetrahedra:
            for face in combinations(t, 3):
                c[canon(face)] += 1
        return c

    def edge_incidence(self):
        c = Counter()
        for t in self.tetrahedra:
            for e in combinations(t, 2):
                c[canon(e)] += 1
        return c

    def vertex_incidence(self):
        c = Counter()
        for t in self.tetrahedra:
            for v in t:
                c[v] += 1
        return c

    def one_skeleton(self):
        g = nx.Graph()
        g.add_nodes_from(self.vertices())
        g.add_edges_from(self.edges())
        return g

    def tetra_adjacency_graph(self):
        g = nx.Graph()
        ts = list(self.tetrahedra)
        g.add_nodes_from(range(len(ts)))
        face_owner = defaultdict(list)
        for i, t in enumerate(ts):
            for f in combinations(t, 3):
                face_owner[canon(f)].append(i)
        for owners in face_owner.values():
            for a, b in combinations(owners, 2):
                g.add_edge(a, b)
        return g

    def add_tetra(self, t):
        t = canon(t)
        if len(set(t)) != 4:
            return False
        before = len(self.tetrahedra)
        self.tetrahedra.add(t)
        if t:
            self.next_vertex = max(self.next_vertex, max(t) + 1)
        return len(self.tetrahedra) > before

    def remove_tetra(self, t):
        t = canon(t)
        if t in self.tetrahedra:
            self.tetrahedra.remove(t)
            return True
        return False

    def pachner_14(self, rng: random.Random):
        if not self.tetrahedra:
            return False
        old = rng.choice(tuple(self.tetrahedra))
        v = self.next_vertex
        self.next_vertex += 1
        new = {canon(face + (v,)) for face in combinations(old, 3)}
        self.tetrahedra.remove(old)
        self.tetrahedra.update(new)
        return True

    def pachner_41(self, rng: random.Random):
        incident = defaultdict(list)
        for t in self.tetrahedra:
            for v in t:
                incident[v].append(t)
        candidates = []
        for v, ts in incident.items():
            if len(ts) != 4:
                continue
            others = sorted({x for t in ts for x in t if x != v})
            if len(others) != 4:
                continue
            expected = {canon(face + (v,)) for face in combinations(tuple(others), 3)}
            base = canon(others)
            if set(ts) == expected and base not in self.tetrahedra:
                candidates.append((v, set(ts), base))
        if not candidates:
            return False
        _, old, base = rng.choice(candidates)
        self.tetrahedra.difference_update(old)
        self.tetrahedra.add(base)
        return True

    def pachner_23(self, rng: random.Random):
        face_owner = defaultdict(list)
        for t in self.tetrahedra:
            for f in combinations(t, 3):
                face_owner[canon(f)].append(t)
        candidates = []
        existing_edges = self.edges()
        for face, ts in face_owner.items():
            if len(ts) != 2:
                continue
            d = next(x for x in ts[0] if x not in face)
            e = next(x for x in ts[1] if x not in face)
            if d == e or canon((d, e)) in existing_edges:
                continue
            a, b, c = face
            new = {canon((a, b, d, e)), canon((a, c, d, e)), canon((b, c, d, e))}
            if new.isdisjoint(self.tetrahedra):
                candidates.append((set(ts), new))
        if not candidates:
            return False
        old, new = rng.choice(candidates)
        self.tetrahedra.difference_update(old)
        self.tetrahedra.update(new)
        return True

    def pachner_32(self, rng: random.Random):
        edge_owner = defaultdict(list)
        for t in self.tetrahedra:
            for e in combinations(t, 2):
                edge_owner[canon(e)].append(t)
        triangles = self.triangles()
        candidates = []
        for edge, ts in edge_owner.items():
            if len(ts) != 3:
                continue
            d, e = edge
            others = sorted({x for t in ts for x in t if x not in edge})
            if len(others) != 3:
                continue
            a, b, c = others
            expected = {canon((d, e, a, b)), canon((d, e, a, c)), canon((d, e, b, c))}
            tri = canon((a, b, c))
            new = {canon((a, b, c, d)), canon((a, b, c, e))}
            if set(ts) == expected and tri not in triangles and new.isdisjoint(self.tetrahedra):
                candidates.append((set(ts), new))
        if not candidates:
            return False
        old, new = rng.choice(candidates)
        self.tetrahedra.difference_update(old)
        self.tetrahedra.update(new)
        return True

    def defect_mutation(self, rng: random.Random, add_bias=0.5):
        """Topology-agnostic perturbation: randomly add or remove one tetrahedron."""
        verts = list(self.vertices())
        if len(verts) >= 4 and (not self.tetrahedra or rng.random() < add_bias):
            for _ in range(20):
                t = canon(rng.sample(verts, 4))
                if t not in self.tetrahedra:
                    self.tetrahedra.add(t)
                    return True
        if len(self.tetrahedra) > 1:
            self.tetrahedra.remove(rng.choice(tuple(self.tetrahedra)))
            return True
        return False
