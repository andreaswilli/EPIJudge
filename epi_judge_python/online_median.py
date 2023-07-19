from typing import Iterator, List
import heapq

from test_framework import generic_test


# time: O(n log n); O(log n) per entry
# space: O(n)
def online_median(sequence: Iterator[int]) -> List[float]:
    result = []
    upper_min_heap = []
    lower_max_heap = []

    for num in sequence:
        heapq.heappush(lower_max_heap, -heapq.heappushpop(upper_min_heap, num))

        if len(lower_max_heap) > len(upper_min_heap):
            heapq.heappush(upper_min_heap, -heapq.heappop(lower_max_heap))

        if len(lower_max_heap) == len(upper_min_heap):
            result.append((-lower_max_heap[0] + upper_min_heap[0]) / 2)
        else:
            result.append(upper_min_heap[0])

    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
