#include <iostream>
#include <fstream>
#include <vector>
#include <random>
#include <chrono>
#include "algorithms.h"

// ── Data generation ───────────────────────────────────────────────────────────

std::vector<int> generate_array(int n, int x = 10'000'000) {
    std::mt19937 rng(std::random_device{}());
    std::uniform_int_distribution<int> dist(1, x);
    std::vector<int> arr(n);
    for (auto& v : arr) v = dist(rng);
    return arr;
}

// ── Experiment (c-i): fixed S, vary n ────────────────────────────────────────

void experiment_vary_n(int S) {
    std::vector<int> sizes = {1'000, 2'000, 5'000, 10'000, 20'000, 50'000,
                               100'000, 200'000, 500'000, 1'000'000,
                               2'000'000, 5'000'000, 10'000'000};

    std::ofstream csv("results_vary_n.csv");
    csv << "n,comparisons\n";

    std::cout << "\n=== (c-i) Fixed S=" << S << ", vary n ===\n";
    for (int n : sizes) {
        auto arr = generate_array(n);
        long long comps = hybrid_sort(arr, 0, n - 1, S);
        std::cout << "  n=" << n << "  comparisons=" << comps << "\n";
        csv << n << "," << comps << "\n";
    }
}

// ── Experiment (c-ii): fixed n, vary S ───────────────────────────────────────

void experiment_vary_S(int n) {
    auto arr_original = generate_array(n);

    std::ofstream csv("results_vary_S.csv");
    csv << "S,comparisons\n";

    std::cout << "\n=== (c-ii) Fixed n=" << n << ", vary S ===\n";
    for (int S = 1; S <= 100; S++) {
        auto arr = arr_original;
        long long comps = hybrid_sort(arr, 0, n - 1, S);
        std::cout << "  S=" << S << "  comparisons=" << comps << "\n";
        csv << S << "," << comps << "\n";
    }
}

// ── Experiment (c-iii): find optimal S ───────────────────────────────────────

void experiment_optimal_S() {
    std::vector<int> sizes = {1'000, 5'000, 10'000, 50'000, 100'000};

    std::ofstream csv("results_optimal_S.csv");
    csv << "n,optimal_S,comparisons\n";

    std::cout << "\n=== (c-iii) Optimal S per size ===\n";
    for (int n : sizes) {
        auto arr_original = generate_array(n);
        int best_S = 1;
        long long best_comps = LLONG_MAX;
        for (int S = 1; S <= 100; S++) {
            auto arr = arr_original;
            long long comps = hybrid_sort(arr, 0, n - 1, S);
            if (comps < best_comps) {
                best_comps = comps;
                best_S = S;
            }
        }
        std::cout << "  n=" << n << "  optimal S=" << best_S
                  << "  comparisons=" << best_comps << "\n";
        csv << n << "," << best_S << "," << best_comps << "\n";
    }
}

// ── Experiment (d): hybrid vs merge_sort on 10M ──────────────────────────────

void experiment_compare(int S, int n = 10'000'000) {
    auto arr = generate_array(n);

    auto arr1 = arr;
    auto t0 = std::chrono::high_resolution_clock::now();
    long long comps_hybrid = hybrid_sort(arr1, 0, n - 1, S);
    auto t1 = std::chrono::high_resolution_clock::now();

    auto arr2 = arr;
    auto t2 = std::chrono::high_resolution_clock::now();
    long long comps_merge = merge_sort(arr2, 0, n - 1);
    auto t3 = std::chrono::high_resolution_clock::now();

    double time_hybrid = std::chrono::duration<double>(t1 - t0).count();
    double time_merge  = std::chrono::duration<double>(t3 - t2).count();

    std::cout << "\n=== (d) Hybrid vs Mergesort on n=" << n << ", S=" << S << " ===\n";
    std::cout << "  hybrid_sort : " << comps_hybrid << " comparisons | " << time_hybrid << "s\n";
    std::cout << "  merge_sort  : " << comps_merge  << " comparisons | " << time_merge  << "s\n";
}

// ── Main ──────────────────────────────────────────────────────────────────────

int main() {
    const int S_FIXED = 32;
    const int N_FIXED = 100'000;

    experiment_vary_n(S_FIXED);
    experiment_vary_S(N_FIXED);
    experiment_optimal_S();
    experiment_compare(S_FIXED);

    return 0;
}
