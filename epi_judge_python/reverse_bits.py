from test_framework import generic_test


# brute force
# time complexity: O(n)
"""
def reverse_bits(x: int) -> int:
    word_size = 64
    for i in range(word_size//2):
        if (x >> i) & 1 != (x >> (word_size - 1 - i)) & 1:
            x ^= (1 << i) | (1 << (word_size - 1 - i))
    return x
"""

# split word into chunks of size L and cache partial results
# time complexity: O(n/L) (filling the cache not included)
CACHE = []
def reverse_bits(x: int) -> int:
    word_size = 64
    chunk_size = 16

    if len(CACHE) == 0:
        for i in range(2 ** chunk_size):
            for j in range(chunk_size//2):
                if (i >> j) & 1 != (i >> (chunk_size - 1 - j)) & 1:
                    i ^= (1 << j) | (1 << (chunk_size - 1 - j))
            CACHE.append(i)

    res = 0
    nr_chunks = word_size // chunk_size

    for i in range(nr_chunks):
        res |= CACHE[x >> (i * 16) & 0xFFFF] << (nr_chunks - 1 - i) * 16
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
