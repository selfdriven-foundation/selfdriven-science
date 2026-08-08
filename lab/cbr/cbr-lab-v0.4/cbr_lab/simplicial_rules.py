from dataclasses import dataclass, asdict
import random


@dataclass
class SimplicialGenome:
    w14: float = 0.25
    w41: float = 0.25
    w23: float = 0.25
    w32: float = 0.25
    defect_probability: float = 0.01

    def clipped(self):
        vals = [max(0.001, x) for x in (self.w14, self.w41, self.w23, self.w32)]
        s = sum(vals)
        vals = [x / s for x in vals]
        return SimplicialGenome(*vals, max(0.0, min(0.20, self.defect_probability)))

    def mutate(self, rng: random.Random, scale=0.10):
        vals = [self.w14, self.w41, self.w23, self.w32]
        vals = [max(0.001, v + rng.gauss(0, scale)) for v in vals]
        return SimplicialGenome(*vals, self.defect_probability + rng.gauss(0, scale / 8)).clipped()

    def as_dict(self):
        return asdict(self)


def random_simplicial_genome(rng: random.Random):
    vals = [rng.random() + 0.05 for _ in range(4)]
    s = sum(vals)
    vals = [v / s for v in vals]
    return SimplicialGenome(*vals, rng.uniform(0.0, 0.08))


def apply_simplicial_rule(complex3d, genome: SimplicialGenome, rng: random.Random):
    if rng.random() < genome.defect_probability:
        return "defect", complex3d.defect_mutation(rng)

    moves = [
        ("1-4", genome.w14, complex3d.pachner_14),
        ("4-1", genome.w41, complex3d.pachner_41),
        ("2-3", genome.w23, complex3d.pachner_23),
        ("3-2", genome.w32, complex3d.pachner_32),
    ]
    x = rng.random() * sum(w for _, w, _ in moves)
    acc = 0.0
    chosen = moves[-1]
    for m in moves:
        acc += m[1]
        if x <= acc:
            chosen = m
            break

    name, _, fn = chosen
    if fn(rng):
        return name, True

    # If the selected move is unavailable, try other Pachner moves in random order.
    fallback = moves[:]
    rng.shuffle(fallback)
    for alt_name, _, alt_fn in fallback:
        if alt_name != name and alt_fn(rng):
            return alt_name, True
    return name, False
