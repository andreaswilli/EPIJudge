from typing import List

from test_framework import generic_test


# brute force
# time: O(n^2)
# space: O(n)
"""
def can_reach_end(A: List[int]) -> bool:
    reachable = [True] + [False] * (len(A) - 1)
    for i in range(len(A)):
        if not reachable[i]:
            continue
        if A[i] >= len(A) - i - 1:
            return True
        for j in range(A[i]):
            reachable[i + j + 1] = True
    return False
"""

# iterate once and keep track of furthest
# time: O(n)
# space: O(1)
def can_reach_end(A: List[int]) -> bool:
    furthest = 0
    i = 0
    while furthest < len(A) - 1:
        furthest = max(furthest, i + A[i])
        if furthest == i:
            return False
        i += 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
