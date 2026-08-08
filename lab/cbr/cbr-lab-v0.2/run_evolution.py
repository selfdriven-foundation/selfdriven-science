import argparse
import csv
from dataclasses import asdict
from pathlib import Path
import random
import numpy as np
import matplotlib.pyplot as plt

from cbr_lab.evolution import random_rule, mutate, crossover, tournament
from cbr_lab.sim import evaluate_rule


def parse_args():
    p = argparse.ArgumentParser(description="Dimension-blind evolutionary rule search for CBR-Lab")
    p.add_argument("--generations", type=int, default=20)
    p.add_argument("--population", type=int, default=30)
    p.add_argument("--nodes", type=int, default=400)
    p.add_argument("--steps", type=int, default=12000)
    p.add_argument("--replicates", type=int, default=2)
    p.add_argument("--elite", type=int, default=4)
    p.add_argument("--mutation-rate", type=float, default=0.30)
    p.add_argument("--seed", type=int, default=1)
    p.add_argument("--out", default="results/evolution.csv")
    return p.parse_args()


def mean_finite(values):
    a = np.asarray(values, dtype=float)
    a = a[np.isfinite(a)]
    return float(np.mean(a)) if len(a) else float("nan")


def main():
    args = parse_args()
    rng = random.Random(args.seed)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    population = [random_rule(rng) for _ in range(args.population)]
    rows = []
    best_history = []
    mean_history = []

    for generation in range(args.generations):
        scored = []
        generation_fitness = []

        for idx, rule in enumerate(population):
            evals = []
            for rep in range(args.replicates):
                sim_seed = args.seed + generation * 1_000_000 + idx * 1000 + rep
                row, _, _, _ = evaluate_rule(
                    seed=sim_seed,
                    node_count=args.nodes,
                    initial_edges=max(args.nodes, int(args.nodes * 1.5)),
                    steps=args.steps,
                    params=rule,
                )
                evals.append(row)

            summary = {
                "generation": generation,
                "individual": idx,
                **asdict(rule),
                "fitness": float(np.mean([x["fitness"] for x in evals])),
                "persistence": float(np.mean([x["persistence"] for x in evals])),
                "complexity": float(np.mean([x["complexity"] for x in evals])),
                "stability": float(np.mean([x["stability"] for x in evals])),
                # Dimensions are observational only; never used in selection.
                "hausdorff_like_dimension": mean_finite([x["hausdorff_like_dimension"] for x in evals]),
                "spectral_dimension": mean_finite([x["spectral_dimension"] for x in evals]),
            }
            rows.append(summary)
            scored.append((summary["fitness"], rule, summary))
            generation_fitness.append(summary["fitness"])

        scored.sort(key=lambda x: x[0], reverse=True)
        best = scored[0][2]
        best_history.append(best["fitness"])
        mean_history.append(float(np.mean(generation_fitness)))
        print(
            f"gen={generation:03d} best={best['fitness']:.4f} mean={mean_history[-1]:.4f} "
            f"P={best['persistence']:.3f} C={best['complexity']:.3f} S={best['stability']:.3f} "
            f"H={best['hausdorff_like_dimension']:.3f} Sd={best['spectral_dimension']:.3f}"
        )

        elites = [rule for _, rule, _ in scored[:max(1, min(args.elite, len(scored)))]]
        next_population = list(elites)
        selectable = [(score, rule) for score, rule, _ in scored]
        while len(next_population) < args.population:
            a = tournament(selectable, rng)
            b = tournament(selectable, rng)
            child = crossover(a, b, rng)
            child = mutate(child, rng, args.mutation_rate)
            next_population.append(child)
        population = next_population

    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    plt.figure()
    plt.plot(range(args.generations), best_history, label="best")
    plt.plot(range(args.generations), mean_history, label="mean")
    plt.xlabel("Generation")
    plt.ylabel("Dimension-blind fitness")
    plt.title("CBR-Lab evolutionary search")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out.with_name("evolution_fitness.png"), dpi=160)
    plt.close()

    final_rows = [r for r in rows if r["generation"] == args.generations - 1]
    h = np.array([r["hausdorff_like_dimension"] for r in final_rows], dtype=float)
    s = np.array([r["spectral_dimension"] for r in final_rows], dtype=float)
    valid = np.isfinite(h) & np.isfinite(s)
    plt.figure()
    plt.scatter(h[valid], s[valid])
    plt.axvline(3.0)
    plt.axhline(3.0)
    plt.xlabel("Hausdorff-like dimension (observed)")
    plt.ylabel("Spectral dimension (observed)")
    plt.title("Final population: dimensions not used by fitness")
    plt.tight_layout()
    plt.savefig(out.with_name("evolution_dimensions.png"), dpi=160)
    plt.close()

    best_overall = max(rows, key=lambda r: r["fitness"])
    print("\nBest rule found (dimension not in objective):")
    for k in ["target_degree", "triangle_bias", "rewire_probability", "random_link_probability", "fitness", "persistence", "complexity", "stability", "hausdorff_like_dimension", "spectral_dimension"]:
        print(f"  {k}: {best_overall[k]}")
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
