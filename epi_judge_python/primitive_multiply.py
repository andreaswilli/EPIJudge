from test_framework import generic_test

def add(a: int, b: int) -> int:
    return a if b == 0 else add(a^b, (a&b) << 1)

# repeatedly add
# time complexity: O(2^n)
"""
def multiply(x: int, y: int) -> int:
    result = 0
    for _ in range(x):
        result = add(y, result)
    return result
"""

# add 2^(k)y for every set bit in x
# time complexity: O(n^2)
def multiply(x: int, y: int) -> int:
    result = 0
    while x:
        if x & 1:
            result = add(result, y)
        x >>= 1
        y <<= 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))

