import argparse
import csv
from pathlib import Path
import random
import numpy as np
import matplotlib.pyplot as plt

from cbr_lab.sim import run_one
from cbr_lab.rules import RuleParams


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--runs", type=int, default=100)
    p.add_argument("--nodes", type=int, default=500)
    p.add_argument("--steps", type=int, default=20000)
    p.add_argument("--seed", type=int, default=1)
    p.add_argument("--out", default="results/results.csv")
    return p.parse_args()


def main():
    args = parse_args()
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    meta_rng = random.Random(args.seed)
    rows = []

    for i in range(args.runs):
        params = RuleParams(
            target_degree=meta_rng.choice([4, 5, 6, 7, 8]),
            triangle_bias=meta_rng.uniform(0.0, 1.0),
            rewire_probability=meta_rng.uniform(0.0, 0.10),
            random_link_probability=meta_rng.uniform(0.0, 0.08),
        )
        row, _, _, _ = run_one(
            seed=args.seed + i,
            node_count=args.nodes,
            initial_edges=max(args.nodes, int(args.nodes * 1.5)),
            steps=args.steps,
            params=params,
        )
        rows.append(row)
        print(
            f"{i+1:04d}/{args.runs} "
            f"H={row['hausdorff_like_dimension']:.3f} "
            f"S={row['spectral_dimension']:.3f} "
            f"deg={row['target_degree']}"
        )

    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    h = np.array([r["hausdorff_like_dimension"] for r in rows], dtype=float)
    s = np.array([r["spectral_dimension"] for r in rows], dtype=float)

    plt.figure()
    plt.hist(h[np.isfinite(h)], bins=20)
    plt.xlabel("Hausdorff-like dimension")
    plt.ylabel("Run count")
    plt.title("CBR-Lab emergent dimension distribution")
    plt.tight_layout()
    plt.savefig(out.with_name("hausdorff_distribution.png"), dpi=160)
    plt.close()

    plt.figure()
    valid = np.isfinite(h) & np.isfinite(s)
    plt.scatter(h[valid], s[valid], alpha=0.7)
    plt.axvline(3.0)
    plt.axhline(3.0)
    plt.xlabel("Hausdorff-like dimension")
    plt.ylabel("Spectral dimension")
    plt.title("CBR-Lab dimensional agreement")
    plt.tight_layout()
    plt.savefig(out.with_name("dimension_scatter.png"), dpi=160)
    plt.close()

    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
