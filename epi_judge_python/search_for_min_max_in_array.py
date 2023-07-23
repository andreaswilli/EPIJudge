import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


# time: O(n)
# space: O(1)
def find_min_max(A: List[int]) -> MinMax:
    lowest = float('inf')
    highest = -float('inf')

    for i in range(0, len(A) - 1, 2):
        min_candidate, max_candidate = sorted([A[i], A[i + 1]])
        lowest = min(lowest, min_candidate)
        highest = max(highest, max_candidate)

    if len(A) % 2:
        lowest = min(lowest, A[-1])
        highest = max(highest, A[-1])


    return MinMax(lowest, highest)


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_min_max_in_array.py',
                                       'search_for_min_max_in_array.tsv',
                                       find_min_max,
                                       res_printer=res_printer))
