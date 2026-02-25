import random
import time
import matplotlib.pyplot as plt
from algorithms import hybrid_sort, merge_sort


# ── Data generation ───────────────────────────────────────────────────────────

def generate_array(n, x=10_000_000):
    """Return a list of n random integers in [1, x]."""
    return [random.randint(1, x) for _ in range(n)]


# Sizes from 1,000 to 10,000,000 — exponentially spaced for good coverage
SIZES = [1_000, 2_000, 5_000, 10_000, 20_000, 50_000,
         100_000, 200_000, 500_000, 1_000_000, 2_000_000,
         5_000_000, 10_000_000]


# ── Experiment (c-i): fixed S, vary n ────────────────────────────────────────

def experiment_vary_n(S, sizes=SIZES):
    """Run hybrid_sort with a fixed S over increasing array sizes.
    Returns (sizes, comparisons_list)."""
    results = []
    for n in sizes:
        arr = generate_array(n)
        comps = hybrid_sort(arr, 0, n - 1, S)
        results.append(comps)
        print(f"  n={n:>10,}  comparisons={comps:,}")
    return sizes, results


# ── Experiment (c-ii): fixed n, vary S ───────────────────────────────────────

def experiment_vary_S(n, S_values):
    """Run hybrid_sort with a fixed n over different S values.
    Returns (S_values, comparisons_list)."""
    arr_original = generate_array(n)
    results = []
    for S in S_values:
        arr = arr_original.copy()
        comps = hybrid_sort(arr, 0, n - 1, S)
        results.append(comps)
        print(f"  S={S:>6}  comparisons={comps:,}")
    return S_values, results


# ── Experiment (c-iii): find optimal S ───────────────────────────────────────

def experiment_optimal_S(sizes, S_values):
    """For each array size, find the S that minimises comparisons.
    Returns dict {n: optimal_S}."""
    optimal = {}
    for n in sizes:
        arr_original = generate_array(n)
        best_S, best_comps = None, float('inf')
        for S in S_values:
            arr = arr_original.copy()
            comps = hybrid_sort(arr, 0, n - 1, S)
            if comps < best_comps:
                best_comps = comps
                best_S = S
        optimal[n] = best_S
        print(f"  n={n:>10,}  optimal S={best_S}  comparisons={best_comps:,}")
    return optimal


# ── Experiment (d): hybrid vs merge_sort on 10M ──────────────────────────────

def experiment_compare(S, n=10_000_000):
    """Compare hybrid_sort vs merge_sort on n elements."""
    arr = generate_array(n)

    arr1 = arr.copy()
    t0 = time.time()
    comps_hybrid = hybrid_sort(arr1, 0, n - 1, S)
    t1 = time.time()

    arr2 = arr.copy()
    t2 = time.time()
    comps_merge = merge_sort(arr2, 0, n - 1)
    t3 = time.time()

    print(f"\n{'':=<50}")
    print(f"  n = {n:,},  S = {S}")
    print(f"  hybrid_sort : {comps_hybrid:,} comparisons  |  {t1-t0:.3f}s")
    print(f"  merge_sort  : {comps_merge:,} comparisons  |  {t3-t2:.3f}s")
    print(f"{'':=<50}")


# ── Plotting helpers ──────────────────────────────────────────────────────────

def plot_vary_n(sizes, comparisons, S):
    plt.figure()
    plt.plot(sizes, comparisons, marker='o')
    plt.xlabel("Input size (n)")
    plt.ylabel("Key comparisons")
    plt.title(f"Hybrid sort comparisons vs n  (S={S})")
    plt.tight_layout()
    plt.savefig(f"plot_vary_n_S{S}.png")
    plt.show()


def plot_vary_S(S_values, comparisons, n):
    plt.figure()
    plt.plot(S_values, comparisons, marker='o')
    plt.xlabel("Threshold S")
    plt.ylabel("Key comparisons")
    plt.title(f"Hybrid sort comparisons vs S  (n={n:,})")
    plt.tight_layout()
    plt.savefig(f"plot_vary_S_n{n}.png")
    plt.show()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    S_FIXED = 32          # fixed S for experiment (c-i)
    N_FIXED = 100_000     # fixed n for experiment (c-ii)
    S_VALUES = list(range(1, 101))   # S from 1 to 100 for experiments

    print("=== (c-i) Fixed S, vary n ===")
    sizes, comps = experiment_vary_n(S=S_FIXED)
    plot_vary_n(sizes, comps, S=S_FIXED)

    print("\n=== (c-ii) Fixed n, vary S ===")
    s_vals, comps2 = experiment_vary_S(n=N_FIXED, S_values=S_VALUES)
    plot_vary_S(s_vals, comps2, n=N_FIXED)

    print("\n=== (c-iii) Optimal S per size ===")
    small_sizes = [1_000, 5_000, 10_000, 50_000, 100_000]
    optimal = experiment_optimal_S(sizes=small_sizes, S_values=S_VALUES)

    print("\n=== (d) Hybrid vs Mergesort on 10M ===")
    experiment_compare(S=S_FIXED)
