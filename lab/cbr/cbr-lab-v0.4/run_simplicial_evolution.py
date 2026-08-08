#!/usr/bin/env python3
import argparse, csv, os, random
from cbr_lab.simplicial_rules import random_simplicial_genome
from cbr_lab.simplicial_sim import run_simplicial_simulation


def main():
    p = argparse.ArgumentParser(description="Dimension-blind evolution over Pachner/defect rule mixtures")
    p.add_argument("--generations", type=int, default=10)
    p.add_argument("--population", type=int, default=20)
    p.add_argument("--steps", type=int, default=2000)
    p.add_argument("--replicates", type=int, default=1)
    p.add_argument("--seed", type=int, default=7)
    p.add_argument("--seed-mode", choices=["s3", "random"], default="s3")
    p.add_argument("--max-tetrahedra", type=int, default=600)
    p.add_argument("--out", default="results-v04")
    args = p.parse_args()
    os.makedirs(args.out, exist_ok=True)
    rng = random.Random(args.seed)
    pop = [random_simplicial_genome(rng) for _ in range(args.population)]
    rows = []

    for gen in range(args.generations):
        scored = []
        for idx, genome in enumerate(pop):
            reps = [run_simplicial_simulation(genome, args.steps,
                    args.seed + gen*100000 + idx*1000 + rep, args.seed_mode, args.max_tetrahedra)
                    for rep in range(args.replicates)]
            fit = sum(x["fitness"] for x in reps) / len(reps)
            r0 = reps[0]
            scored.append((fit, genome, r0))
            topo = r0["topology"]
            rows.append({"generation":gen,"index":idx,**genome.as_dict(),"fitness":fit,
                         "persistence":r0["persistence"],"complexity":r0["complexity"],"stability":r0["stability"],
                         "dH":r0["dH"],"dS":r0["dS"],"dH_vertex":r0["dH_vertex"],"dS_vertex":r0["dS_vertex"],"tetrahedra":r0["snapshot"]["tetrahedra"],
                         "vertices":r0["snapshot"]["vertices"],"face_closed_fraction":topo["face_closed_fraction"],
                         "face_valid_fraction":topo["face_valid_fraction"],"s2_pass_fraction":topo["s2_pass_fraction"],
                         "global_betti":str(topo["global_betti"]),"accepted_fraction":r0["accepted_fraction"]})
        scored.sort(key=lambda x:x[0], reverse=True)
        best = scored[0]
        t = best[2]["topology"]
        print(f"gen={gen:02d} fit={best[0]:.3f} defect={best[1].defect_probability:.3f} "
              f"dH={best[2]['dH']:.2f} dS={best[2]['dS']:.2f} S2={t['s2_pass_fraction']:.2f} "
              f"closed={t['face_closed_fraction']:.2f} T={best[2]['snapshot']['tetrahedra']}")
        elites = [x[1] for x in scored[:max(2,args.population//4)]]
        pop = elites[:]
        while len(pop) < args.population:
            pop.append(rng.choice(elites).mutate(rng))

    path = os.path.join(args.out, "simplicial_evolution_v04.csv")
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print("wrote", path)

if __name__ == "__main__":
    main()
