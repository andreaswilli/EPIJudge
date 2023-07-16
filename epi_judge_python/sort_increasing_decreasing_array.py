from typing import List
import heapq

from test_framework import generic_test


# time: O(n log k), where k is the number of lists
# space: O(n)
def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    was_increasing = True
    sorted_lists = [[A[0]]]

    for i in range(1, len(A)):
        is_increasing = A[i-1] <= A[i]
        if was_increasing == is_increasing:
            sorted_lists[-1].append(A[i])
        else:
            if not was_increasing:
                sorted_lists[-1] = list(reversed(sorted_lists[-1]))
            sorted_lists.append([A[i]])
        was_increasing = is_increasing

    if not was_increasing:
        sorted_lists[-1] = list(reversed(sorted_lists[-1]))

    return list(heapq.merge(*sorted_lists))


# time: O(n log n), but it's faster :')
#       is n too small or k/n too large?
# def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
#     return sorted(A)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
