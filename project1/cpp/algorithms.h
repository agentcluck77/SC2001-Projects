#pragma once
#include <vector>

long long insertion_sort(std::vector<int>& arr, int left, int right);
long long merge(std::vector<int>& arr, int left, int mid, int right);
long long hybrid_sort(std::vector<int>& arr, int left, int right, int S);
long long merge_sort(std::vector<int>& arr, int left, int right);
