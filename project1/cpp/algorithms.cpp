#include "algorithms.h"
#include <vector>

long long insertion_sort(std::vector<int>& arr, int left, int right) {
    long long comparisons = 0;
    for (int i = left + 1; i <= right; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= left && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
            comparisons++;
        }
        if (j >= left)
            comparisons++;
        arr[j + 1] = key;
    }
    return comparisons;
}

long long merge(std::vector<int>& arr, int left, int mid, int right) {
    long long comparisons = 0;
    int n1 = mid - left + 1;
    int n2 = right - mid;

    std::vector<int> L(arr.begin() + left, arr.begin() + mid + 1);
    std::vector<int> R(arr.begin() + mid + 1, arr.begin() + right + 1);

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        comparisons++;
        k++;
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];

    return comparisons;
}

long long hybrid_sort(std::vector<int>& arr, int left, int right, int S) {
    if (right - left + 1 <= S)
        return insertion_sort(arr, left, right);
    int mid = (left + right) / 2;
    long long comparisons = 0;
    comparisons += hybrid_sort(arr, left, mid, S);
    comparisons += hybrid_sort(arr, mid + 1, right, S);
    comparisons += merge(arr, left, mid, right);
    return comparisons;
}

long long merge_sort(std::vector<int>& arr, int left, int right) {
    if (left >= right) return 0;
    int mid = (left + right) / 2;
    long long comparisons = 0;
    comparisons += merge_sort(arr, left, mid);
    comparisons += merge_sort(arr, mid + 1, right);
    comparisons += merge(arr, left, mid, right);
    return comparisons;
}
