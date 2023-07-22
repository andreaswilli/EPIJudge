from typing import List

from test_framework import generic_test


# time: O(log n)
# space: O(1)
def search_smallest(A: List[int]) -> int:
    lower = 0
    upper = len(A) - 1

    while lower < upper:
        mid = lower + (upper - lower) // 2

        if A[mid] > A[upper]:
            lower = mid + 1
        else:
            upper = mid

    return lower


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
