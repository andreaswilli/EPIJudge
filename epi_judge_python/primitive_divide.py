from test_framework import generic_test


# repeatedly subtract y from x and count
# time complexity: very high, takes x/y iterations
"""
def divide(x: int, y: int) -> int:
    result = 0
    while x >= y:
        x -= y
        result += 1
    return result
"""

# repeatedly subtract the largest 2^(k)y smaller than x
# time complexity: O(n)
def divide(x: int, y: int) -> int:
    result = 0
    power = 32

    while x >= y:
        while (y << power) > x:
            power -= 1
        x -= y << power
        result += 1 << power
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
