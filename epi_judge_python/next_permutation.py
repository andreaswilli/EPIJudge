from typing import List

from test_framework import generic_test


# time: O(n)
# space: O(1)
def next_permutation(perm: List[int]) -> List[int]:
    desc_idx = len(perm) - 2
    while desc_idx >= 0 and perm[desc_idx + 1] <= perm[desc_idx]:
        desc_idx -= 1
    if desc_idx == -1:
        return []
    for i in reversed(range(desc_idx + 1, len(perm))):
        if perm[i] > perm[desc_idx]:
            perm[desc_idx], perm[i] = perm[i], perm[desc_idx]
            break
    perm[desc_idx + 1:] = list(reversed(perm[desc_idx + 1:]))
    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
