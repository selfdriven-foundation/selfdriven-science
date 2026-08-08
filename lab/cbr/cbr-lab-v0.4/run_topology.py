#!/usr/bin/env python3
import argparse, csv, json, math, os, random
import matplotlib.pyplot as plt
from cbr_lab.rules import Genome, random_genome
from cbr_lab.sim import run_simulation


def main():
    p = argparse.ArgumentParser(description="CBR-Lab v0.3 local 3-manifold experiment")
    p.add_argument("--runs", type=int, default=20)
    p.add_argument("--nodes", type=int, default=400)
    p.add_argument("--steps", type=int, default=10000)
    p.add_argument("--topology-samples", type=int, default=30)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--out", default="results")
    args = p.parse_args()

    os.makedirs(args.out, exist_ok=True)
    rng = random.Random(args.seed)
    rows = []

    for i in range(args.runs):
        genome = random_genome(rng)
        result = run_simulation(genome, args.nodes, args.steps, args.seed + i * 9973, args.topology_samples)
        row = {"run": i, **genome.as_dict(), "fitness": result["fitness"], "persistence": result["persistence"],
               "complexity": result["complexity"], "stability": result["stability"], "dH": result["dH"], "dS": result["dS"],
               "s2_pass_fraction": result["topology"]["s2_pass_fraction"],
               "mean_incidence_two": result["topology"]["mean_incidence_two"],
               "classification": result["classification"]}
        rows.append(row)
        print(f"run={i:03d} fit={row['fitness']:.3f} dH={row['dH']:.2f} dS={row['dS']:.2f} "
              f"S2={row['s2_pass_fraction']:.2f} {row['classification']}")

    csv_path = os.path.join(args.out, "topology_runs.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader(); w.writerows(rows)

    # Diagnostic scatter: dimension vs local manifold score (observation only; not fitness).
    xs = [r["dH"] for r in rows if math.isfinite(r["dH"])]
    ys = [r["s2_pass_fraction"] for r in rows if math.isfinite(r["dH"])]
    plt.figure()
    plt.scatter(xs, ys)
    plt.axvline(3.0, linestyle="--")
    plt.xlabel("Hausdorff-like dimension dH")
    plt.ylabel("Fraction of sampled vertex links passing S² test")
    plt.title("Emergent dimension vs local 3-manifold evidence")
    plt.tight_layout()
    plt.savefig(os.path.join(args.out, "dimension_vs_manifold.png"), dpi=160)
    print(f"wrote {csv_path}")

if __name__ == "__main__":
    main()
