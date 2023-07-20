from typing import List
import bisect

from test_framework import generic_test


# time: O(log n)
# space: O(1)
# def search_first_of_k(A: List[int], k: int) -> int:
#     i = bisect.bisect_left(A, k)
#     return i if (i < len(A) and A[i] == k) else -1


# time: O(log n)
# space: O(1)
def search_first_of_k(A: List[int], k: int) -> int:
    lower = 0
    upper = len(A) - 1

    while lower < upper:
        mid = lower + (upper - lower) // 2
        if A[mid] < k:
            lower = mid + 1
        elif A[mid] > k:
            upper = mid - 1
        else:
            upper = mid

    return lower if (lower < len(A) and A[lower] == k) else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
