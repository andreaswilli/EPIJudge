from typing import List

from test_framework import generic_test


# time: O(n)
# space: O(n)
"""
def apply_permutation(perm: List[int], A: List[int]) -> None:
    result = [0] * len(A)
    for i in range(len(perm)):
        result[perm[i]] = A[i]
    A[:] = result
    return
"""

# swap items in both lists one by one
# time: O(n)
# space: O(1), or O(n) if perm cannot be mutated
"""
def apply_permutation(perm: List[int], A: List[int]) -> None:
    i = 0
    while i < len(A):
        if perm[i] == i:
            i += 1
        else:
            A[perm[i]], A[i] = A[i], A[perm[i]]
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]
    return
"""

# swap items in A one by one (and restore perm list)
# time: O(n)
# space: O(1)
def apply_permutation(perm, A) -> None:
    for i in range(len(A)):
        cur = i
        while perm[cur] >= 0:
            A[i], A[perm[cur]] = A[perm[cur]], A[i]
            prev = cur
            cur = perm[cur]
            perm[prev] = -1 * perm[prev] - 1
    for i in range(len(A)):
        perm[i] = -1 * (perm[i] + 1)
    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
