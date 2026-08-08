import random
from .rules import create_initial_graph, local_rewrite
from .metrics import structural_snapshot, complexity_score, stability_score, estimate_ball_dimension, estimate_spectral_dimension
from .topology import local_manifold_report, classify_geometry


def run_simulation(genome, nodes=400, steps=10000, seed=1, topology_samples=30):
    rng = random.Random(seed)
    g = create_initial_graph(nodes, rng)
    checkpoints = []
    checkpoint_steps = {int(steps * 0.7), int(steps * 0.9), steps - 1}
    giant_history = []

    for step in range(steps):
        local_rewrite(g, genome, rng)
        if step in checkpoint_steps:
            s = structural_snapshot(g)
            checkpoints.append(s)
            giant_history.append(s["giant"])

    persistence = sum(giant_history) / len(giant_history) if giant_history else 0.0
    complexity = complexity_score(g)
    stability = stability_score(checkpoints[-2], checkpoints[-1]) if len(checkpoints) >= 2 else 0.0
    fitness = 0.40 * persistence + 0.35 * complexity + 0.25 * stability

    dh = estimate_ball_dimension(g, rng)
    ds = estimate_spectral_dimension(g, rng)
    topo = local_manifold_report(g, rng, samples=topology_samples)
    classification = classify_geometry(dh, ds, topo)

    return {
        "graph": g,
        "fitness": fitness,
        "persistence": persistence,
        "complexity": complexity,
        "stability": stability,
        "dH": dh,
        "dS": ds,
        "topology": topo,
        "classification": classification,
    }
