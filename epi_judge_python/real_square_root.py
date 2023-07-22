from test_framework import generic_test
import math


# time: O(log (x / s)), where s is the tolerance (precision)
# space: O(1)
def square_root(x: float) -> float:
    lower = 1 if x >= 1 else x
    upper = x if x >= 1 else 1

    while True:
        mid = lower + (upper - lower) / 2
        square = mid * mid

        if math.isclose(square, x):
            return mid
        elif square < x:
            lower = mid
        else:
            upper = mid


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
