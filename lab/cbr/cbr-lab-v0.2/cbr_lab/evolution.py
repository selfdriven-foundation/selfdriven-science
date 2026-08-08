from dataclasses import asdict
import random

from .rules import RuleParams


def random_rule(rng: random.Random) -> RuleParams:
    return RuleParams(
        target_degree=rng.randint(3, 10),
        triangle_bias=rng.random(),
        rewire_probability=rng.uniform(0.0, 0.15),
        random_link_probability=rng.uniform(0.0, 0.12),
    )


def mutate(rule: RuleParams, rng: random.Random, rate=0.25) -> RuleParams:
    d = asdict(rule)
    if rng.random() < rate:
        d["target_degree"] = max(2, min(14, d["target_degree"] + rng.choice([-2, -1, 1, 2])))
    for key, scale, upper in [
        ("triangle_bias", 0.15, 1.0),
        ("rewire_probability", 0.03, 0.25),
        ("random_link_probability", 0.03, 0.20),
    ]:
        if rng.random() < rate:
            d[key] = max(0.0, min(upper, d[key] + rng.gauss(0.0, scale)))
    return RuleParams(**d)


def crossover(a: RuleParams, b: RuleParams, rng: random.Random) -> RuleParams:
    ad, bd = asdict(a), asdict(b)
    child = {k: (ad[k] if rng.random() < 0.5 else bd[k]) for k in ad}
    return RuleParams(**child)


def tournament(scored, rng: random.Random, k=3):
    sample = rng.sample(scored, min(k, len(scored)))
    return max(sample, key=lambda x: x[0])[1]
