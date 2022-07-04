from typing import List

from test_framework import generic_test

# brute force: convert to int, increment, convert back to list
# time: O(n)
# space: O(n)
"""
def plus_one(A: List[int]) -> List[int]:
    numberInt = int("".join(map(str, A)))
    numberInt += 1
    return list(map(int, str(numberInt)))
"""

# directly work with list
# time: O(n)
# space: O(1)
def plus_one(A: List[int]) -> List[int]:
    for i in reversed(range(len(A))):
        A[i] += 1
        A[i] %= 10
        if A[i] != 0:
            break
        if i == 0:
            A.insert(0, 1)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
