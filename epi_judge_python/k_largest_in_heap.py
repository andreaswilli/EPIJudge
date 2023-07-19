from typing import List
import heapq

from test_framework import generic_test, test_utils


# time: O(k log k)
# space: O(k)
def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    result = []
    candidates_max_heap = [(-A[0], 0)]

    for _ in range(k):
        v, i = heapq.heappop(candidates_max_heap)
        result.append(-v)

        for c in [2 * i + 1, 2 * i + 2]:
            if c < len(A):
                heapq.heappush(candidates_max_heap, (-A[c], c))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
