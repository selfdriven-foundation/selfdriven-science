from collections import Counter
from itertools import combinations
import numpy as np
import networkx as nx
from .topology import gf2_rank, boundary_matrix


def explicit_vertex_link(c, v):
    triangles = set()
    for t in c.tetrahedra:
        if v in t:
            triangles.add(tuple(sorted(x for x in t if x != v)))
    edges = {tuple(sorted(e)) for tri in triangles for e in combinations(tri, 2)}
    vertices = {(x,) for tri in triangles for x in tri}
    return {0: sorted(vertices), 1: sorted(edges), 2: sorted(triangles)}


def link_betti(link):
    b1 = boundary_matrix(link[1], link[0])
    b2 = boundary_matrix(link[2], link[1])
    r1, r2 = gf2_rank(b1), gf2_rank(b2)
    return [len(link[0]) - r1, len(link[1]) - r1 - r2, len(link[2]) - r2]


def assess_explicit_vertex_link(c, v):
    link = explicit_vertex_link(c, v)
    if len(link[0]) < 4:
        return {"vertex": v, "eligible": False, "passed_s2": False}
    b = link_betti(link)
    chi = len(link[0]) - len(link[1]) + len(link[2])
    g = nx.Graph()
    g.add_nodes_from(x[0] for x in link[0]); g.add_edges_from(link[1])
    edge_tri = Counter()
    for tri in link[2]:
        for e in combinations(tri, 2):
            edge_tri[tuple(sorted(e))] += 1
    incidence_two = (sum(cn == 2 for cn in edge_tri.values()) / len(edge_tri)) if edge_tri else 0.0
    passed = bool(nx.is_connected(g) and chi == 2 and b == [1, 0, 1] and incidence_two == 1.0)
    return {
        "vertex": v, "eligible": True, "passed_s2": passed,
        "V": len(link[0]), "E": len(link[1]), "F": len(link[2]),
        "beta0": b[0], "beta1": b[1], "beta2": b[2], "chi": chi,
        "edge_triangle_incidence_two": incidence_two,
    }


def global_betti(c):
    simplices = {
        0: sorted((v,) for v in c.vertices()),
        1: sorted(c.edges()),
        2: sorted(c.triangles()),
        3: sorted(c.tetrahedra),
    }
    ranks = {k: gf2_rank(boundary_matrix(simplices[k], simplices[k-1])) for k in (1,2,3)}
    return [
        len(simplices[0]) - ranks[1],
        len(simplices[1]) - ranks[1] - ranks[2],
        len(simplices[2]) - ranks[2] - ranks[3],
        len(simplices[3]) - ranks[3],
    ]


def simplicial_manifold_report(c, samples=None, rng=None):
    incidence = c.face_incidence()
    vals = list(incidence.values())
    face_closed_fraction = (sum(x == 2 for x in vals) / len(vals)) if vals else 0.0
    face_valid_fraction = (sum(x in (1, 2) for x in vals) / len(vals)) if vals else 0.0

    verts = list(c.vertices())
    if samples is not None and rng is not None and len(verts) > samples:
        verts = rng.sample(verts, samples)
    details = [assess_explicit_vertex_link(c, v) for v in verts]
    eligible = [d for d in details if d.get("eligible")]
    s2_fraction = (sum(d["passed_s2"] for d in eligible) / len(eligible)) if eligible else 0.0

    # Exact global homology can be expensive; only compute on moderate complexes.
    betti = global_betti(c) if len(c.tetrahedra) <= 250 else None
    return {
        "tetrahedra": len(c.tetrahedra), "vertices": len(c.vertices()),
        "face_closed_fraction": face_closed_fraction,
        "face_valid_fraction": face_valid_fraction,
        "s2_pass_fraction": s2_fraction,
        "global_betti": betti,
        "details": details,
    }
