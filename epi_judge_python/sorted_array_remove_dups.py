import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# shift everything after a duplicte to the left by one
# time: O(n^2)
# space: O(1)
"""
def delete_duplicates(A: List[int]) -> int:
    num_del = 0
    i = 0
    while i + num_del < len(A) - 1:
        if A[i] == A[i + 1]:
            num_del += 1
            for j in range(i, len(A) - num_del):
                A[j] = A[j + 1]
        else:
            i += 1
    return len(A) - num_del
"""

# using a dict
# time: O(n)
# space: O(n)
"""
def delete_duplicates(A: List[int]) -> int:
    res = []
    occurred = {}
    for i in range(len(A)):
        if not A[i] in occurred:
            res.append(A[i])
            occurred[A[i]] = True
    A[:] = res
    return len(res)
"""

# reduce number of shifts
# time: O(n)
# space: O(1)
def delete_duplicates(A: List[int]) -> int:
    if (len(A) == 0):
        return 0
    write = 1
    for i in range(len(A)):
        if A[i] != A[write - 1]:
            A[write] = A[i]
            write += 1
    return write


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
