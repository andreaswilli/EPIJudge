from typing import List
import random

from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.

# time: O(n), technically, the worst case is O(n^2), if the lowest or highest
#             value is randomly picked every time. However, the possibility of
#             this happening decreases exponentially with the size of the array.
# space: O(1)
def find_kth_largest(k: int, A: List[int]) -> int:
    def partition(lower, upper, pivot_idx):
        pivot_value = A[pivot_idx]
        A[pivot_idx], A[upper] = A[upper], A[pivot_idx]
        new_pivot_idx = lower

        for i in range(lower, upper):
            if A[i] > pivot_value:
                A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                new_pivot_idx += 1

        A[new_pivot_idx], A[upper] = A[upper], A[new_pivot_idx]
        return new_pivot_idx

    lower = 0
    upper = len(A) - 1

    while lower <= upper:
        pivot_idx = random.randint(lower, upper)
        new_pivot_idx = partition(lower, upper, pivot_idx)

        if new_pivot_idx == k - 1:
            return A[new_pivot_idx]
        elif new_pivot_idx < k - 1:
            lower = new_pivot_idx + 1
        else:
            upper = new_pivot_idx - 1

    # not possible - just for satisfying the linter
    return -1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
