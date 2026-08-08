#!/usr/bin/env python3
import argparse, csv, os, random
from cbr_lab.rules import random_genome
from cbr_lab.sim import run_simulation


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--generations", type=int, default=10)
    p.add_argument("--population", type=int, default=20)
    p.add_argument("--nodes", type=int, default=400)
    p.add_argument("--steps", type=int, default=10000)
    p.add_argument("--replicates", type=int, default=1)
    p.add_argument("--seed", type=int, default=7)
    p.add_argument("--out", default="results")
    args = p.parse_args()
    os.makedirs(args.out, exist_ok=True)
    rng = random.Random(args.seed)
    pop = [random_genome(rng) for _ in range(args.population)]
    rows = []

    for gen in range(args.generations):
        scored = []
        for idx, genome in enumerate(pop):
            reps = [run_simulation(genome, args.nodes, args.steps, args.seed + gen*100000 + idx*1000 + r, topology_samples=20)
                    for r in range(args.replicates)]
            fitness = sum(x["fitness"] for x in reps) / len(reps)
            scored.append((fitness, genome, reps[0]))
            r0 = reps[0]
            rows.append({"generation": gen, "index": idx, **genome.as_dict(), "fitness": fitness,
                         "dH": r0["dH"], "dS": r0["dS"], "s2_pass_fraction": r0["topology"]["s2_pass_fraction"],
                         "classification": r0["classification"]})
        scored.sort(key=lambda x: x[0], reverse=True)
        best = scored[0]
        print(f"gen={gen:02d} best={best[0]:.3f} dH={best[2]['dH']:.2f} dS={best[2]['dS']:.2f} "
              f"S2={best[2]['topology']['s2_pass_fraction']:.2f} {best[2]['classification']}")
        elite_n = max(2, args.population // 4)
        elites = [x[1] for x in scored[:elite_n]]
        pop = elites[:]
        while len(pop) < args.population:
            pop.append(rng.choice(elites).mutate(rng))

    with open(os.path.join(args.out, "evolution_v03.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)

if __name__ == "__main__":
    main()
