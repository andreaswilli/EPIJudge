from typing import List, Tuple
from itertools import chain
import heapq

from test_framework import generic_test


# time: O(n log n)
# space: O(n)
def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    return sorted(chain(*sorted_arrays))


# time: O(n log k), where k is the number of lists
# space: O(k), (+ O(n) for result)
# class Node:
#     def __init__(self, list_i, i, value):
#         self.list_i = list_i
#         self.i = i
#         self.value = value
#
#     def __lt__(self, other):
#         return self.value < other.value
#
# def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
#     min_heap: List[Node] = []
#     result = []
#
#     for i in range(len(sorted_arrays)):
#         heapq.heappush(min_heap, Node(i, 0, sorted_arrays[i][0]))
#
#     while len(min_heap) > 0:
#         next = heapq.heappop(min_heap)
#         result.append(next.value)
#         if len(sorted_arrays[next.list_i]) > next.i + 1:
#             heapq.heappush(min_heap, Node(next.list_i, next.i + 1,
#                                           sorted_arrays[next.list_i][next.i + 1]))
#
#     return result


# time: O(n log k), where k is the number of lists
# space: O(k), (+ O(n) for result)
# def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
#     min_heap: List[Tuple[int, int]] = []
#     sorted_array_iters = [iter(x) for x in sorted_arrays]
#
#     for i, it in enumerate(sorted_array_iters):
#         first_element = next(it, None)
#         if first_element is not None:
#             heapq.heappush(min_heap, (first_element, i))
#
#     result = []
#
#     while min_heap:
#         smallest_entry, smallest_array_i = heapq.heappop(min_heap)
#         smallest_array_iter = sorted_array_iters[smallest_array_i]
#         result.append(smallest_entry)
#         next_element = next(smallest_array_iter, None)
#         if next_element is not None:
#             heapq.heappush(min_heap, (next_element, smallest_array_i))
#
#     return result


# pythonic solution
# def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
#     return list(heapq.merge(*sorted_arrays))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
