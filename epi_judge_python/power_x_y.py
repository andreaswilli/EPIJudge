from test_framework import generic_test


# repeatedly multiply by x
# time complexity: O(2^n)
"""
def power(x: float, y: int) -> float:
    result = 1
    for _ in range(abs(y)):
        result *= x
    if y < 0:
        result = 1/result;
    return result
"""

# reduce multiplications by grouping terms
# time complexity: O(n)
def power(x: float, y: int) -> float:
    result = 1.0
    if y < 0:
        x = 1/x
        y = abs(y)
    while y:
        if y & 1:
            result *= x
        x *= x
        y >>= 1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))

