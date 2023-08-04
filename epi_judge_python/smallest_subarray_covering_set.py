import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


# time: O(n^2)
# space: O(k), where k is the number of keywords
# def find_smallest_subarray_covering_set(paragraph: List[str],
#                                         keywords: Set[str]) -> Subarray:
#     covered: Set[str] = set()
#     l_res = 0
#     r_res = len(paragraph) - 1
#
#     l = r = 0
#     while l <= r < len(paragraph):
#         covered = set(
#                 filter(lambda w: w in keywords, paragraph[l:r+1]))
#         if len(covered) < len(keywords):
#             r += 1
#         else:
#             if (r - l) < (r_res - l_res):
#                 l_res = l
#                 r_res = r
#             l += 1
#
#     return Subarray(l_res, r_res)


# time: O(n)
# space: O(k), where k is the number of keywords
def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    keywords_to_cover = collections.Counter(keywords)
    result = Subarray(start=-1, end=-1)
    remaining_to_cover = len(keywords)
    left = 0
    for right, p in enumerate(paragraph):
        if p in keywords:
            keywords_to_cover[p] -= 1
            if keywords_to_cover[p] == 0:
                remaining_to_cover -= 1

        while remaining_to_cover == 0:
            if result == Subarray(start=-1, end=-1) or (
                right - left < result.end - result.start):
                result = Subarray(start=left, end=right)

            pl = paragraph[left]
            if pl in keywords:
                keywords_to_cover[pl] += 1
                if keywords_to_cover[pl] > 0:
                    remaining_to_cover += 1
            left += 1
    return result


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
