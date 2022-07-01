from test_framework import generic_test


# string manipulation
# time complexity: O(n)
"""
def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    return sign * int(str(abs(x))[::-1])
"""

# using mod 10
# time complexity: O(n)
def reverse(x: int) -> int:
    result = 0
    sign = -1 if x < 0 else 1
    x = abs(x)
    while x > 0:
        result *= 10
        result += x % 10
        x //= 10
    return sign * result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
