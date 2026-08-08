#!/usr/bin/env python3
import argparse, json, random
from cbr_lab.simplicial_rules import random_simplicial_genome, SimplicialGenome
from cbr_lab.simplicial_sim import run_simplicial_simulation


def main():
    p = argparse.ArgumentParser(description="CBR-Lab v0.4 explicit simplicial-complex experiment")
    p.add_argument("--steps", type=int, default=3000)
    p.add_argument("--seed", type=int, default=7)
    p.add_argument("--seed-mode", choices=["s3", "random"], default="s3")
    p.add_argument("--max-tetrahedra", type=int, default=800)
    p.add_argument("--defect", type=float, default=None, help="Override defect probability")
    args = p.parse_args()
    rng = random.Random(args.seed)
    genome = random_simplicial_genome(rng)
    if args.defect is not None:
        genome = SimplicialGenome(genome.w14, genome.w41, genome.w23, genome.w32, args.defect).clipped()
    r = run_simplicial_simulation(genome, args.steps, args.seed, args.seed_mode, args.max_tetrahedra)
    summary = {
        "genome": genome.as_dict(), "fitness": r["fitness"], "persistence": r["persistence"],
        "complexity": r["complexity"], "stability": r["stability"], "dH": r["dH"], "dS": r["dS"],
        "dH_vertex": r["dH_vertex"], "dS_vertex": r["dS_vertex"],
        "accepted_fraction": r["accepted_fraction"], "move_counts": r["move_counts"],
        "snapshot": r["snapshot"],
        "topology": {k:v for k,v in r["topology"].items() if k != "details"},
    }
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
