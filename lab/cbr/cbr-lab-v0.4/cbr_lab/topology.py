"""Local manifold diagnostics for the flag/clique complex induced by a graph.

For an interior vertex of a triangulated 3-manifold, the vertex link should be S^2.
We therefore inspect the clique complex of each sampled vertex link and test its
homology over GF(2), Euler characteristic, and local 2D incidence.
"""
from itertools import combinations
import random
import numpy as np
import networkx as nx


def gf2_rank(matrix):
    if matrix.size == 0:
        return 0
    a = (matrix.copy() % 2).astype(np.uint8)
    rows, cols = a.shape
    rank = 0
    for col in range(cols):
        pivots = np.where(a[rank:, col] == 1)[0]
        if len(pivots) == 0:
            continue
        pivot = rank + pivots[0]
        if pivot != rank:
            a[[rank, pivot]] = a[[pivot, rank]]
        for r in range(rows):
            if r != rank and a[r, col]:
                a[r] ^= a[rank]
        rank += 1
        if rank == rows:
            break
    return rank


def cliques_by_dim(h, max_dim=3):
    simplices = {0: [(v,) for v in h.nodes]}
    nodes = list(h.nodes)
    for dim in range(1, max_dim + 1):
        size = dim + 1
        found = []
        for combo in combinations(nodes, size):
            if all(h.has_edge(a, b) for a, b in combinations(combo, 2)):
                found.append(tuple(sorted(combo)))
        simplices[dim] = found
    return simplices


def boundary_matrix(k_simplices, km1_simplices):
    if not k_simplices or not km1_simplices:
        return np.zeros((len(km1_simplices), len(k_simplices)), dtype=np.uint8)
    row = {s: i for i, s in enumerate(km1_simplices)}
    m = np.zeros((len(km1_simplices), len(k_simplices)), dtype=np.uint8)
    for j, simplex in enumerate(k_simplices):
        for face in combinations(simplex, len(simplex) - 1):
            face = tuple(sorted(face))
            if face in row:
                m[row[face], j] = 1
    return m


def betti_numbers(simplices, max_dim=3):
    ranks = {}
    for k in range(1, max_dim + 1):
        ranks[k] = gf2_rank(boundary_matrix(simplices[k], simplices[k - 1]))
    ranks[max_dim + 1] = 0
    betti = []
    for k in range(max_dim + 1):
        n = len(simplices[k])
        rank_bk = ranks.get(k, 0) if k > 0 else 0
        rank_next = ranks.get(k + 1, 0)
        betti.append(n - rank_bk - rank_next)
    return betti


def vertex_link_graph(g, v):
    # In a flag complex, the link of v is the induced graph on its neighbours.
    return g.subgraph(list(g.neighbors(v))).copy()


def assess_vertex_link(g, v, max_link_nodes=40):
    h = vertex_link_graph(g, v)
    n = h.number_of_nodes()
    if n < 4 or n > max_link_nodes:
        return {"vertex": v, "eligible": False, "reason": "link_size", "link_nodes": n}

    simplices = cliques_by_dim(h, max_dim=3)
    b = betti_numbers(simplices, max_dim=3)
    chi = sum(((-1) ** k) * len(simplices[k]) for k in range(4))

    triangles = simplices[2]
    edge_triangle_counts = {tuple(sorted(e)): 0 for e in simplices[1]}
    for tri in triangles:
        for e in combinations(tri, 2):
            e = tuple(sorted(e))
            if e in edge_triangle_counts:
                edge_triangle_counts[e] += 1
    incidence_two = (
        sum(1 for c in edge_triangle_counts.values() if c == 2) / len(edge_triangle_counts)
        if edge_triangle_counts else 0.0
    )

    connected = nx.is_connected(h) if n else False
    no_3simplices = len(simplices[3]) == 0
    sphere_homology = (b[0] == 1 and b[1] == 0 and b[2] == 1 and b[3] == 0)
    euler_ok = (chi == 2)
    incidence_ok = incidence_two >= 0.9
    passed = connected and no_3simplices and sphere_homology and euler_ok and incidence_ok

    return {
        "vertex": v,
        "eligible": True,
        "link_nodes": n,
        "V": len(simplices[0]), "E": len(simplices[1]), "F": len(simplices[2]), "T3": len(simplices[3]),
        "beta0": b[0], "beta1": b[1], "beta2": b[2], "beta3": b[3],
        "chi": chi,
        "edge_triangle_incidence_two": incidence_two,
        "connected": connected,
        "passed_s2": passed,
    }


def local_manifold_report(g, rng: random.Random, samples=40, max_link_nodes=40):
    candidates = [v for v in g.nodes if 4 <= g.degree(v) <= max_link_nodes]
    if not candidates:
        return {"sampled": 0, "eligible": 0, "s2_pass_fraction": 0.0, "mean_incidence_two": 0.0, "details": []}
    chosen = rng.sample(candidates, min(samples, len(candidates)))
    details = [assess_vertex_link(g, v, max_link_nodes=max_link_nodes) for v in chosen]
    eligible = [x for x in details if x.get("eligible")]
    if not eligible:
        return {"sampled": len(chosen), "eligible": 0, "s2_pass_fraction": 0.0, "mean_incidence_two": 0.0, "details": details}
    return {
        "sampled": len(chosen),
        "eligible": len(eligible),
        "s2_pass_fraction": sum(x["passed_s2"] for x in eligible) / len(eligible),
        "mean_incidence_two": float(np.mean([x["edge_triangle_incidence_two"] for x in eligible])),
        "details": details,
    }


def classify_geometry(dh, ds, report, dim_tolerance=0.6, manifold_threshold=0.65):
    finite = np.isfinite(dh) and np.isfinite(ds)
    scaling3 = finite and abs(dh - 3.0) <= dim_tolerance and abs(ds - 3.0) <= dim_tolerance
    manifold_like = report.get("s2_pass_fraction", 0.0) >= manifold_threshold
    if scaling3 and manifold_like:
        return "candidate_3_manifold"
    if scaling3:
        return "3d_scaling_not_manifold"
    if manifold_like:
        return "manifold_like_links_non3d_scaling"
    return "no_3_manifold_evidence"
