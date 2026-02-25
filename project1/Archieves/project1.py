"""
README
Edit size_of_arr when running and testing the code.
Remove or comment out 10M and 1M in the array as it will run for some time.
"""

import random
import time
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple


# ============================================================================
# SORTING ALGORITHMS
# ============================================================================

def insertion_sort(arr, left, right):
    """Insertion sort for subarray arr[left:right+1]."""
    comparisons = 0
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            comparisons += 1
        if j >= left:
            comparisons += 1
        arr[j + 1] = key
    return comparisons


def merge(arr, left, mid, right):
    """Merge function for merge sort and hybrid merge sort."""
    comparisons = 0
    n1 = mid - left + 1
    n2 = right - mid

    # create temp arrays
    L = arr[left:mid + 1].copy()
    R = arr[mid + 1:right + 1].copy()

    i, j, k = 0, 0, left

    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        comparisons += 1
        k += 1

    # copy remaining elements in L
    while i < n1:
        arr[k] = L[i]
        k += 1
        i += 1

    # copy remaining elements in R
    while j < n2:
        arr[k] = R[j]
        k += 1
        j += 1
    return comparisons


def hybrid_sort(arr, left, right, S):
    """
    Hybrid merge sort with insertion sort for small subarrays.
    S is the threshold - switch to insertion sort for subarrays <= S elements.
    Returns the number of comparisons made.
    """
    if right - left + 1 <= S:
        return insertion_sort(arr, left, right)
    mid = (left + right) // 2
    comparisons = 0
    comparisons += hybrid_sort(arr, left, mid, S)
    comparisons += hybrid_sort(arr, mid + 1, right, S)
    comparisons += merge(arr, left, mid, right)
    return comparisons


def merge_sort(arr, left, right):
    """Pure merge sort implementation. Returns the number of comparisons made."""
    if left >= right:
        return 0

    mid = (left + right) // 2
    comparisons = 0
    comparisons += merge_sort(arr, left, mid)
    comparisons += merge_sort(arr, mid + 1, right)
    comparisons += merge(arr, left, mid, right)
    return comparisons


# ── Buffered (no-slice) versions ──────────────────────────────────────────

def merge_buffered(arr, left, mid, right, buf):
    """Merge with preallocated buffer - avoids slicing."""
    comparisons = 0
    i, j, k = left, mid + 1, left

    # main merge
    while i <= mid and j <= right:
        comparisons += 1
        if arr[i] <= arr[j]:
            buf[k] = arr[i]
            i += 1
        else:
            buf[k] = arr[j]
            j += 1
        k += 1

    # copy remaining from left
    while i <= mid:
        buf[k] = arr[i]
        i += 1
        k += 1

    # copy remaining from right
    while j <= right:
        buf[k] = arr[j]
        j += 1
        k += 1

    # copy merged back to arr
    arr[left:right + 1] = buf[left:right + 1]
    return comparisons


def hybrid_sort_buffered(arr, left, right, S, buf=None):
    """Hybrid sort with buffered merge. Allocates buffer on first call."""
    if buf is None:
        buf = [0] * len(arr)
    
    if right - left + 1 <= S:
        return insertion_sort(arr, left, right)
    
    comparisons = 0
    mid = (left + right) // 2
    comparisons += hybrid_sort_buffered(arr, left, mid, S, buf)
    comparisons += hybrid_sort_buffered(arr, mid + 1, right, S, buf)
    comparisons += merge_buffered(arr, left, mid, right, buf)
    return comparisons


def merge_sort_buffered(arr, left, right, buf=None):
    """Pure merge sort with buffered merge. Allocates buffer on first call."""
    if buf is None:
        buf = [0] * len(arr)
    
    if left >= right:
        return 0

    mid = (left + right) // 2
    comparisons = 0
    comparisons += merge_sort_buffered(arr, left, mid, buf)
    comparisons += merge_sort_buffered(arr, mid + 1, right, buf)
    comparisons += merge_buffered(arr, left, mid, right, buf)
    return comparisons


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def generate_random_arr(size: int, max_value: int = None) -> List:
    """Generate random array of integers of given size."""
    if max_value is None:
        max_value = size
    return [random.randint(1, max_value) for _ in range(size)]

"""
(c) i. Analyze with fixed threshold, varying input sizes
"""
def analyze_fixed_threshold(sizes: List[int], threshold: int = 10, max_value: int = 1000000) -> Tuple[List[int], List[int]]:
    """
    Analyze performance with fixed threshold across different input sizes.
    Returns (sizes, comparisons_list)
    """
    comp_counts = []
    
    for size in sizes:
        print(f"Analyzing size {size} with threshold {threshold}")
        arr = generate_random_arr(size, max_value)
        arr_copy = arr.copy()
        comps = hybrid_sort(arr_copy, 0, len(arr_copy) - 1, threshold)
        comp_counts.append(comps)
    
    return sizes, comp_counts

"""
(c) ii. Analyze with fixed input size, varying thresholds
"""
def analyze_fixed_size(size: int, thresholds: List[int], max_value: int = 1000000) -> Tuple[List[int], List[int]]:
    """
    Analyze performance with fixed size across different thresholds.
    Returns (thresholds, comparisons_list)
    """
    comp_counts = []
    # Generate one array and use it for all threshold tests
    arr = generate_random_arr(size, max_value)
    
    for threshold in thresholds:
        print(f"Analyzing threshold {threshold} with size {size}")
        arr_copy = arr.copy()
        comps = hybrid_sort(arr_copy, 0, len(arr_copy) - 1, threshold)
        comp_counts.append(comps)
    
    return thresholds, comp_counts


"""
Run only (c)i and (c)ii analyses
takes around 1 min + to run with 10mil
"""


def run_analysis_c_i_ii():

    # Define test parameters
    size_of_arr = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 500000]
    thresholds = [1, 5, 10, 15, 20, 25, 30, 50]

    print("="*60)
    print("HYBRID MERGESORT-INSERTION SORT ANALYSIS")
    print("="*60)

    # (c)i: fixed threshold 10, varying sizes
    print("\n(c)i: Analysis with fixed threshold X=10")
    sizes_fixed_s, comparisons_fixed_s = analyze_fixed_threshold(size_of_arr, 10)

    # (c)ii: fixed size 20k, varying thresholds
    print("\n(c)ii: Analysis with fixed size n=20000")
    thresholds_fixed_n, comparisons_fixed_n = analyze_fixed_size(20000, thresholds)

    # ---- PLOTS (only two panels) ----
    plt.figure(figsize=(12, 5))

    # left plot: (c)i
    plt.subplot(1, 2, 1)
    plt.plot(sizes_fixed_s, comparisons_fixed_s, 'bo-', markersize=6, linewidth=2, label='Hybrid (X=10)')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Key Comparisons')
    plt.title('Key Comparisons vs Input Size (X=10)')
    plt.grid(True, alpha=0.3)

    theoretical = [n * np.log2(n) for n in sizes_fixed_s]  
    plt.plot(sizes_fixed_s, theoretical, 'r--', alpha=0.7, linewidth=2, label='O(n log n)')
    plt.legend()

    # right plot: (c)ii
    plt.subplot(1, 2, 2)
    plt.plot(thresholds_fixed_n, comparisons_fixed_n, 'go-', markersize=6, linewidth=2)
    plt.xlabel('Threshold (S)')
    plt.ylabel('Key Comparisons')
    plt.title('Key Comparisons vs Threshold (n=20,000)')
    plt.grid(True, alpha=0.3)


    plt.tight_layout()
    plt.savefig('hybrid_mergesort_c_i_ii.png', dpi=300, bbox_inches='tight')
    print("\nPlots saved to 'hybrid_mergesort_c_i_ii.png'")


    # print for (c)i and (c)ii)
    print("\n" + "="*60)
    print("DETAILED RESULTS")
    print("="*60)

    print(f"\n(c)i: Fixed Threshold Analysis (X=10)")
    print("Size\t\tComparisons")
    print("-" * 30)
    for size, comp in zip(sizes_fixed_s, comparisons_fixed_s):
        print(f"{size:,}\t\t{comp:,}")

    print(f"\n(c)ii: Fixed Size Analysis (n=20,000)")
    print("Threshold\tComparisons")
    print("-" * 30)
    for thresh, comp in zip(thresholds_fixed_n, comparisons_fixed_n):
        print(f"{thresh}\t\t{comp:,}")



"""
(c) iii. Find optimal threshold S* for each input size that minimizes comparisons
Takes around 2 min to run 1M, 9 min to run 10M. Optimal s=3
"""
def run_analysis_c_iii(
    max_value: int = 10_000_000,
    save_path: str = "hybrid_mergesort_c_iii.png",
):
    """Find optimal threshold for each input size (1 trial per (n,S))."""
    size_of_arr = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 500000, 1000000, 10000000]
    thresholds = [1, 2, 3, 4, 5, 10, 15, 20, 25, 30]
    results = {}

    print("\n" + "="*60)
    print("(c)iii: Finding optimal thresholds S* for each input size n (1 trial)")
    print("="*60)

    for n in size_of_arr:
        print(f"\nAnalyzing n = {n:,}")
        base_arr = generate_random_arr(n, max_value)

        min_comparisons = float("inf")
        best_S = thresholds[0]
        all_results = []

        for S in thresholds:
            arr = base_arr.copy()
            comps = hybrid_sort(arr, 0, len(arr) - 1, S)
            all_results.append((S, comps))
            if comps < min_comparisons:
                min_comparisons = comps
                best_S = S

        results[n] = {
            "optimal_threshold": best_S,
            "min_comparisons": min_comparisons,
            "all_results": all_results,
        }

    # ---- Plotting ----
    ns_sorted = sorted(results.keys())
    optimal_S = [results[k]["optimal_threshold"] for k in ns_sorted]
    min_comps = [results[k]["min_comparisons"] for k in ns_sorted]

    plt.figure(figsize=(12, 5))

    # Left: Optimal S vs n
    plt.subplot(1, 2, 1)
    x_pos = np.arange(len(ns_sorted))
    bars = plt.bar(x_pos, optimal_S, width=0.6, alpha=0.85)
    plt.xticks(x_pos, [f"{n:,}" for n in ns_sorted])
    plt.xlabel("Input Size n")
    plt.ylabel("Optimal Threshold S*")
    plt.title("Optimal Threshold S* vs Input Size n")
    plt.grid(True, axis="y", alpha=0.3)
    for b, s in zip(bars, optimal_S):
        plt.text(b.get_x() + b.get_width()/2, b.get_height() + 0.2, str(s),
                 ha="center", va="bottom", fontweight="bold", fontsize=9)

    # Right: Min comparisons vs n
    plt.subplot(1, 2, 2)
    plt.plot(ns_sorted, min_comps, "o-", linewidth=2, markersize=6)
    plt.xlabel("Input Size n")
    plt.ylabel("Minimum Key Comparisons (at S*)")
    plt.title("Minimum Comparisons vs Input Size n")
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    print(f"\nPlots saved to '{save_path}'")

    # Summary table
    print("\nSUMMARY (c)iii:  (1 trial)")
    print("n\t\tS*\t\tMin Comparisons")
    print("-" * 45)
    for n in ns_sorted:
        s_star = results[n]["optimal_threshold"]
        c_min = results[n]["min_comparisons"]
        print(f"{n:,}\t\t{s_star}\t\t{c_min:,}")

    return results

"""
(d) Compare hybrid mergesort (S=optimal_S) vs pure mergesort on n elements.
Not much difference in comparisons but shows CPU time reduction.
"""
def run_analysis_d(optimal_S: int = 3,
                   n: int = 10_000_000,
                   max_value: int = 10_000_000,
                   save_path: str = "part_d_comparison.png",
                   verify_sorted: bool = False):

    print("\n" + "="*60)
    print(f"(d) Comparing Hybrid(S={optimal_S}) vs Pure Mergesort on n={n:,}")
    print("="*60)

    base = generate_random_arr(n, max_value)

    # Hybrid
    arr_h = base.copy()
    t0 = time.perf_counter()
    comps_h = hybrid_sort(arr_h, 0, len(arr_h) - 1, optimal_S)
    t_h = time.perf_counter() - t0
    if verify_sorted:
        print("Hybrid sorted:", arr_h == sorted(arr_h))

    # Pure mergesort
    arr_p = base.copy()
    t0 = time.perf_counter()
    comps_p = merge_sort(arr_p, 0, len(arr_p) - 1)
    t_p = time.perf_counter() - t0
    if verify_sorted:
        print("Pure sorted:", arr_p == sorted(arr_p))

    # Print results
    print("\nRESULTS (n = {:,})".format(n))
    print("Algorithm\t\tComparisons\t\tCPU Time (s)")
    print("-"*60)
    print(f"Hybrid (S={optimal_S})\t{comps_h:,}\t\t{t_h:.4f}")
    print(f"Pure Mergesort\t\t{comps_p:,}\t\t{t_p:.4f}")

    comp_impr = (comps_p - comps_h) / comps_p * 100 if comps_p else 0.0
    time_impr = (t_p - t_h) / t_p * 100 if t_p else 0.0
    print("\nImprovement with Hybrid (S={}):".format(optimal_S))
    print(f"Comparisons: {comp_impr:.2f}% reduction")
    print(f"CPU Time:   {time_impr:.2f}% reduction")

    # Plot (bar charts)
    labels = [f"Hybrid\n(S={optimal_S})", "Pure"]
    comps = [comps_h, comps_p]
    times = [t_h, t_p]

    plt.figure(figsize=(12, 5))

    # Left: comparisons
    plt.subplot(1, 2, 1)
    x = np.arange(len(labels))
    bars1 = plt.bar(x, comps, width=0.6, alpha=0.85)
    plt.xticks(x, labels)
    plt.ylabel("Key Comparisons")
    plt.title(f"Comparisons (n={n:,})")
    plt.grid(True, axis="y", alpha=0.3)
    for b, v in zip(bars1, comps):
        plt.text(b.get_x()+b.get_width()/2, v*1.01, f"{v:,}", ha="center", va="bottom", fontsize=9)

    # Right: time
    plt.subplot(1, 2, 2)
    bars2 = plt.bar(x, times, width=0.6, alpha=0.85)
    plt.xticks(x, labels)
    plt.ylabel("CPU Time (s)")
    plt.title(f"CPU Time (n={n:,})")
    plt.grid(True, axis="y", alpha=0.3)
    for b, v in zip(bars2, times):
        plt.text(b.get_x()+b.get_width()/2, v*1.01, f"{v:.2f}s", ha="center", va="bottom", fontsize=9)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    print(f"\nPlot saved to '{save_path}'")

    return {
        "hybrid": {"comparisons": comps_h, "time": t_h, "S": optimal_S},
        "pure": {"comparisons": comps_p, "time": t_p},
        "improvement": {"comparisons_pct": comp_impr, "time_pct": time_impr}
    }


"""
(d) with buffering (no slicing) - Compare buffered versions of algorithms
Not much difference in comparisons but shows CPU time reduction.
"""
def run_analysis_d_buffered(optimal_S: int = 3,
                            n: int = 10_000_000,
                            max_value: int = 10_000_000,
                            save_path: str = "part_d_comparison_buffered.png",
                            verify_sorted: bool = False):
    """
    Compare buffered hybrid vs pure mergesort on n elements.
    Measures key comparisons and CPU time on the same dataset.
    """
    print("\n" + "="*60)
    print(f"(d) Buffered: Hybrid(S={optimal_S}) vs Pure on n={n:,}")
    print("="*60)

    base = generate_random_arr(n, max_value)

    # Hybrid buffered
    arr_h = base.copy()
    t0 = time.perf_counter()
    comps_h = hybrid_sort_buffered(arr_h, 0, len(arr_h) - 1, optimal_S)
    t_h = time.perf_counter() - t0
    if verify_sorted:
        print("Hybrid sorted:", arr_h == sorted(arr_h))

    # Pure buffered
    arr_p = base.copy()
    t0 = time.perf_counter()
    comps_p = merge_sort_buffered(arr_p, 0, len(arr_p) - 1)
    t_p = time.perf_counter() - t0
    if verify_sorted:
        print("Pure sorted:", arr_p == sorted(arr_p))

    # Print results
    print("\nRESULTS (n = {:,})".format(n))
    print("Algorithm\t\tComparisons\t\tCPU Time (s)")
    print("-"*60)
    print(f"Hybrid (S={optimal_S})\t{comps_h:,}\t\t{t_h:.4f}")
    print(f"Pure Mergesort\t\t{comps_p:,}\t\t{t_p:.4f}")

    comp_impr = (comps_p - comps_h) / comps_p * 100 if comps_p else 0.0
    time_impr = (t_p - t_h) / t_p * 100 if t_p else 0.0
    print("\nImprovement with Hybrid (S={}):".format(optimal_S))
    print(f"Comparisons: {comp_impr:.2f}% reduction")
    print(f"CPU Time:   {time_impr:.2f}% reduction")

    # Plot
    labels = [f"Hybrid\n(S={optimal_S})", "Pure"]
    comps = [comps_h, comps_p]
    times = [t_h, t_p]

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    x = np.arange(len(labels))
    bars1 = plt.bar(x, comps, width=0.6, alpha=0.85)
    plt.xticks(x, labels)
    plt.ylabel("Key Comparisons")
    plt.title(f"Comparisons (n={n:,})")
    plt.grid(True, axis="y", alpha=0.3)
    for b, v in zip(bars1, comps):
        plt.text(b.get_x()+b.get_width()/2, v*1.01, f"{v:,}", ha="center", va="bottom", fontsize=9)

    plt.subplot(1, 2, 2)
    bars2 = plt.bar(x, times, width=0.6, alpha=0.85)
    plt.xticks(x, labels)
    plt.ylabel("CPU Time (s)")
    plt.title(f"CPU Time (n={n:,})")
    plt.grid(True, axis="y", alpha=0.3)
    for b, v in zip(bars2, times):
        plt.text(b.get_x()+b.get_width()/2, v*1.01, f"{v:.2f}s", ha="center", va="bottom", fontsize=9)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    print(f"\nPlot saved to '{save_path}'")

    return {
        "hybrid": {"comparisons": comps_h, "time": t_h, "S": optimal_S},
        "pure": {"comparisons": comps_p, "time": t_p},
        "improvement": {"comparisons_pct": comp_impr, "time_pct": time_impr}
    }


if __name__ == "__main__":    
    # run the main analysis
    run_analysis_c_i_ii()

    run_analysis_c_iii()
    run_analysis_d(optimal_S=3, n=10_000_000, verify_sorted=False)
    run_analysis_d_buffered(optimal_S=3, n=10_000_000, verify_sorted=False)