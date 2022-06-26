from test_framework import generic_test


# check every bit (brute force)
# time complexity: O(n)
"""
def parity(x: int) -> int:
    result = 0
    for i in range(0, 64):
        result ^= (x >> i) & 1
    return result
"""

# only iterate for each of the k set bits
# time complexity: O(k)
"""
def parity(x: int) -> int:
    result = 0
    while x != 0:
        result ^= 1
        x &= (x-1)
    return result
"""

# split up words into chunks of size L and cache partial solutions
# time complexity: O(n/L) (initialization of the cache not included)
"""
def partialParity(x: int) -> int:
    result = 0
    while x != 0:
        result ^= 1
        x &= (x-1)
    return result

CACHE = []
def parity(x: int) -> int:
    if len(CACHE) == 0:
        for i in range(2**16):
            CACHE.append(partialParity(i))

    result = 0
    while x != 0:
        result ^= CACHE[x & 0xffff]
        x >>= 16
    return result
"""

# use associativity of parity
# time complexity: O(log n)
def parity(x: int) -> int:
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1 # only last bit is relevant


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
