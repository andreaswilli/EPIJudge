from test_framework import generic_test


# time: O(log k)
# space: O(1)
def square_root(k: int) -> int:
    lower = 0
    upper = k

    while lower <= upper:
        mid = lower + (upper - lower) // 2

        if mid * mid <= k:
            lower = mid + 1
        else:
            upper = mid - 1

    return lower - 1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
