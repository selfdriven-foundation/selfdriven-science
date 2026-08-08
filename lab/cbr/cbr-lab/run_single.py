import matplotlib.pyplot as plt
from cbr_lab.sim import run_one

row, graph, growth, spectral = run_one(seed=42)
print(row)

radii, counts = growth
plt.figure()
plt.loglog(radii, counts, marker="o")
plt.xlabel("Graph radius r")
plt.ylabel("N(r)")
plt.title(f"Ball growth; d≈{row['hausdorff_like_dimension']:.2f}")
plt.tight_layout()
plt.show()

steps, returns = spectral
plt.figure()
plt.loglog(steps, returns, marker="o")
plt.xlabel("Random walk step")
plt.ylabel("Return probability")
plt.title(f"Spectral dimension≈{row['spectral_dimension']:.2f}")
plt.tight_layout()
plt.show()
