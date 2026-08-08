import math
import random
import numpy as np
import networkx as nx
from .simplicial import SimplicialComplex3D
from .simplicial_rules import apply_simplicial_rule
from .metrics import estimate_ball_dimension, estimate_spectral_dimension
from .simplicial_topology import simplicial_manifold_report


def entropy_normalized(values):
    if not values:
        return 0.0
    _, counts = np.unique(values, return_counts=True)
    p = counts / counts.sum()
    h = float(-(p * np.log2(p)).sum())
    return h / max(1.0, math.log2(len(counts) + 1))


def simplicial_snapshot(c):
    tg = c.tetra_adjacency_graph()
    giant = 0.0
    if tg.number_of_nodes():
        giant = len(max(nx.connected_components(tg), key=len)) / tg.number_of_nodes()
    vi = list(c.vertex_incidence().values())
    fi = list(c.face_incidence().values())
    return {
        "giant": giant,
        "vertex_entropy": entropy_normalized(vi),
        "face_entropy": entropy_normalized(fi),
        "tetrahedra": len(c.tetrahedra),
        "vertices": len(c.vertices()),
    }


def complexity_score(c):
    s = simplicial_snapshot(c)
    diversity = 0.6 * s["vertex_entropy"] + 0.4 * s["face_entropy"]
    return s["giant"] * diversity


def stability_score(a, b):
    if not a or not b:
        return 0.0
    diffs = [
        abs(a["giant"] - b["giant"]),
        abs(a["vertex_entropy"] - b["vertex_entropy"]),
        abs(a["face_entropy"] - b["face_entropy"]),
        min(1.0, abs(a["tetrahedra"] - b["tetrahedra"]) / max(10, a["tetrahedra"])),
        min(1.0, abs(a["vertices"] - b["vertices"]) / max(10, a["vertices"])),
    ]
    return max(0.0, 1.0 - float(np.mean(diffs)))


def run_simplicial_simulation(genome, steps=2000, seed=1, seed_mode="s3", max_tetrahedra=800):
    rng = random.Random(seed)
    c = SimplicialComplex3D.s3_boundary_seed() if seed_mode == "s3" else SimplicialComplex3D.random_seed(rng)
    checkpoints = []
    move_counts = {}
    accepted = 0

    marks = {int(steps * 0.7), int(steps * 0.9), steps - 1}
    for step in range(steps):
        # Resource guard only; it is not part of fitness.
        if len(c.tetrahedra) >= max_tetrahedra:
            # Bias attempt toward reducing moves without using geometry/topology metrics.
            name, ok = ("4-1", c.pachner_41(rng))
            if not ok:
                name, ok = ("3-2", c.pachner_32(rng))
        else:
            name, ok = apply_simplicial_rule(c, genome, rng)
        move_counts[name] = move_counts.get(name, 0) + 1
        accepted += int(ok)
        if step in marks:
            checkpoints.append(simplicial_snapshot(c))

    snap = simplicial_snapshot(c)
    persistence = sum(x["giant"] for x in checkpoints) / len(checkpoints) if checkpoints else snap["giant"]
    complexity = complexity_score(c)
    stability = stability_score(checkpoints[-2], checkpoints[-1]) if len(checkpoints) >= 2 else 0.0
    # Dimension- and topology-blind fitness.
    fitness = 0.40 * persistence + 0.35 * complexity + 0.25 * stability

    # Primary geometry probe: the tetrahedral dual graph. It is sparse (degree ~4
    # for a closed manifold) and avoids the rapid saturation of the dense 1-skeleton.
    dual = c.tetra_adjacency_graph()
    dh = estimate_ball_dimension(dual, rng, samples=min(32, len(dual)), max_radius=8)
    ds = estimate_spectral_dimension(dual, rng, walks=1200, steps=24)

    # Keep 1-skeleton dimensions as secondary diagnostics.
    g = c.one_skeleton()
    dh_vertex = estimate_ball_dimension(g, rng, samples=min(32, len(g)), max_radius=8)
    ds_vertex = estimate_spectral_dimension(g, rng, walks=800, steps=20)
    topo = simplicial_manifold_report(c, samples=40, rng=rng)

    return {
        "complex": c, "fitness": fitness, "persistence": persistence,
        "complexity": complexity, "stability": stability,
        "dH": dh, "dS": ds, "dH_vertex": dh_vertex, "dS_vertex": ds_vertex, "topology": topo,
        "move_counts": move_counts, "accepted_fraction": accepted / max(1, steps),
        "snapshot": snap,
    }
