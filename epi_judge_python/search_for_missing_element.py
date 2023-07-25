import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))

# time: O(n log n)
# space: O(1)
# def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
#     A = sorted(A)
#
#     duplicate = None
#     missing = None
#
#     for i in range(len(A)):
#         if i + 1 == len(A):
#             if missing is None:
#                 missing = A[i] + 1
#         else:
#             diff = A[i + 1] - A[i]
#             if diff == 0:
#                 duplicate = A[i]
#             elif diff == 2:
#                 missing = A[i] + 1
#
#     return DuplicateAndMissing(duplicate, missing)


# time: O(n)
# space: O(n)
# def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
#     counts = [0] * len(A)
#
#     for x in A:
#         counts[x] += 1
#
#     duplicate = 0
#     missing = 0
#
#     for i, c in enumerate(counts):
#         if c == 0:
#             missing = i
#         elif c == 2:
#             duplicate = i
#
#     return DuplicateAndMissing(duplicate, missing)

# time: O(n)
# space: O(1)
def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    dup_xor_miss = 0
    for i, x in enumerate(A):
        dup_xor_miss ^= x
        dup_xor_miss ^= i

    one_result = 0
    differing_bit = dup_xor_miss ^ (dup_xor_miss & (dup_xor_miss - 1))

    for i, x in enumerate(A):
        if i & differing_bit:
            one_result ^= i
        if x & differing_bit:
            one_result ^= x

    other_result = dup_xor_miss ^ one_result
    duplicate, missing = (one_result, other_result) if one_result in A else (other_result, one_result)

    return DuplicateAndMissing(duplicate, missing)


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED,
                                  PropertyName.RESULT) else value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_missing_element.py',
                                       'find_missing_and_duplicate.tsv',
                                       find_duplicate_missing,
                                       res_printer=res_printer))
