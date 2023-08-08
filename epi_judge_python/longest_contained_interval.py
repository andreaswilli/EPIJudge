from typing import FrozenSet, List, Set

from test_framework import generic_test


# time: O(n^2)
# space: O(n)
# def longest_contained_range(A: List[int]) -> int:
#     result = 0
#     groups: Set[FrozenSet[int]] = set()
#
#     for a in A:
#         new_group: Set[int] = set([a])
#         adj_groups: Set[FrozenSet[int]] = set()
#         for g in groups:
#             if a+1 in g or a-1 in g:
#                 adj_groups.add(g)
#                 new_group |= g
#         for g in adj_groups:
#             groups.remove(g)
#         groups.add(frozenset(new_group))
#         if len(new_group) > result:
#             result = len(new_group)
#
#     return result


# time: O(n log n)
# space: O(n)
# def longest_contained_range(A: List[int]) -> int:
#     longest = 0
#
#     prev_a = None
#     current = 0
#     for a in sorted(set(A)):
#         if prev_a is None or a == prev_a + 1:
#             current += 1
#         else:
#             if current > longest:
#                 longest = current
#             current = 1
#         prev_a = a
#
#     return max(longest, current)


# time: O(n)
# space: O(n)
def longest_contained_range(A: List[int]) -> int:
    result = 0
    remaining_values = set(A)

    while remaining_values:
        a = remaining_values.pop()
        upper = a + 1
        while upper in remaining_values:
            remaining_values.remove(upper)
            upper += 1
        lower = a - 1
        while lower in remaining_values:
            remaining_values.remove(lower)
            lower -= 1
        if upper - lower - 1 > result:
            result = upper - lower - 1

    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
