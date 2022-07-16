import functools
import random
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName, TestFailure
from test_framework.test_utils import enable_executor_hook


# for each position find min/max remaining number
# time: O(n^2)
# space: O(1)
"""
def rearrange(A: List[int]) -> None:
    for i in range(len(A)):
        next = i
        if i % 2 == 1:
            for j in range(i, len(A)):
                next = j if A[j] > A[next] else next
        else:
            for j in range(i, len(A)):
                next = j if A[j] < A[next] else next
        A[i], A[next] = A[next], A[i]
    return
"""

# sort and swap elements
# time: O(n log n)
# space: O(1)
"""
def rearrange(A: List[int]) -> None:
    A.sort()
    for i in range(1, len(A) - 1, 2):
        A[i], A[i+1] = A[i+1], A[i]
    return
"""

# find median
# time: O(n) on average, O(n^2) worst case (like quick sort)
# space: O(1)
"""
def rearrange(A: List[int]) -> None:
    left = 0
    right = len(A) - 1
    median_pos = (len(A) - 1) // 2
    median = None
    count = 0
    while median == None and left < right:
        count += 1
        pivot_idx = random.randint(left, right)
        pivot = A[pivot_idx]
        new_pivot_idx = left
        A[right], A[pivot_idx] = A[pivot_idx], A[right]
        for i in range(left, right):
            if A[i] <= pivot:
                A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                new_pivot_idx += 1
        A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
        if new_pivot_idx == median_pos:
            median = A[median_pos]
        elif new_pivot_idx > median_pos:
            right = new_pivot_idx - 1
        else:
            left = new_pivot_idx + 1
    if median_pos % 2 == 0:
        for i in range(1, median_pos, 2):
            A[median_pos - i], A[median_pos + i + 1] = A[median_pos + i + 1], A[median_pos - i]
    else:
        for i in range(0, median_pos, 2):
            A[median_pos - i], A[median_pos + i + 1] = A[median_pos + i + 1], A[median_pos - i]
    return
"""

# compare two local elements and swap if necessary
# time: O(n)
# space: O(1)
def rearrange(A: List[int]) -> None:
    for i in range(0, len(A) - 1):
        if (i % 2 == 0 and A[i] > A[i + 1]) or (i % 2 == 1 and A[i] < A[i + 1]):
            A[i], A[i + 1] = A[i + 1], A[i]

@enable_executor_hook
def rearrange_wrapper(executor, A):
    def check_answer(A):
        for i in range(len(A)):
            if i % 2:
                if A[i] < A[i - 1]:
                    raise TestFailure().with_property(
                        PropertyName.RESULT, A).with_mismatch_info(
                            i, 'A[{}] <= A[{}]'.format(i - 1, i),
                            '{} > {}'.format(A[i - 1], A[i]))
                if i + 1 < len(A):
                    if A[i] < A[i + 1]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                                i, 'A[{}] >= A[{}]'.format(i, i + 1),
                                '{} < {}'.format(A[i], A[i + 1]))
            else:
                if i > 0:
                    if A[i - 1] < A[i]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                                i, 'A[{}] >= A[{}]'.format(i - 1, i),
                                '{} < {}'.format(A[i - 1], A[i]))
                if i + 1 < len(A):
                    if A[i + 1] < A[i]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                                i, 'A[{}] <= A[{}]'.format(i, i + 1),
                                '{} > {}'.format(A[i], A[i + 1]))

    executor.run(functools.partial(rearrange, A))
    check_answer(A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('alternating_array.py',
                                       'alternating_array.tsv',
                                       rearrange_wrapper))
