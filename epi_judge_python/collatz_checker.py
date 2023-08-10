from typing import Set
from test_framework import generic_test


def test_collatz_conjecture(n: int) -> bool:
    confirmed_nums: Set[int] = set([1])

    for x in range(2, n+1):
        path: Set[int] = set()
        cur = x
        while cur < 2 ** 32:
            if cur in path:
                return False
            path.add(cur)
            if cur < x:
                if cur in confirmed_nums:
                    confirmed_nums.add(x)
                break
            if cur % 2:
                cur *= 3
                cur += 1
            else:
                cur //= 2
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('collatz_checker.py',
                                       'collatz_checker.tsv',
                                       test_collatz_conjecture))
