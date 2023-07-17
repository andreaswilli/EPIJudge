import functools
import math
from typing import Iterator, List, Tuple
import heapq

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class Star:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs: 'Star') -> bool:
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)

# time: O(n log n)
# space: O(n), would not work with this size of dataset
# def find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:
#     min_heap = []
#     result = []
#
#     for star in stars:
#         heapq.heappush(min_heap, star)
#
#     for _ in range(k):
#         result.append(heapq.heappop(min_heap))
#
#     return result


# time: O(n log k)
# space: O(k)
def find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:
    max_heap: List[Tuple[float, Star]] = []
    result = []

    for star in stars:
        heapq.heappush(max_heap, (-star.distance, star))
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    while max_heap:
        result.append(heapq.heappop(max_heap)[1])

    return result


def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d)
        for s, d in zip(sorted(output), expected_output))


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(functools.partial(find_closest_k_stars, iter(stars),
                                          k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_closest_stars.py',
                                       'k_closest_stars.tsv',
                                       find_closest_k_stars_wrapper, comp))
