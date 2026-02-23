

def insertion_sort(arr, left, right):

    comparisons = 0
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1 # we assume that the first element (i-1) is considered sorted
        # so j is the last item in the prefix
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j] # move item forward by one
            j -= 1
            comparisons += 1
        if j >= left:
            comparisons += 1
        # at the last j + 1 where the loop breaks, there is now a gap for the key to be placed
        arr[j + 1] = key
    return comparisons

def merge(arr, left, mid, right):
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
    if right - left + 1 <= S:
        return insertion_sort(arr, left, right)
    mid = (left + right) // 2
    comparisons = 0
    comparisons += hybrid_sort(arr, left, mid, S)
    comparisons += hybrid_sort(arr, mid + 1, right, S)
    comparisons += merge(arr, left, mid, right)
    return comparisons

def merge_sort(arr, left, right):
    if left >= right:
        return 0

    mid = (left + right) // 2
    comparisons = 0
    comparisons += merge_sort(arr, left, mid)
    comparisons += merge_sort(arr, mid + 1, right)
    comparisons += merge(arr, left, mid, right)
    return comparisons
