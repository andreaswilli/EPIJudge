from test_framework import generic_test


# time complexity: O(1)
def swap_bits(x, i, j):
    if ((x >> i) & 1 != (x >> j) & 1):
        # invert both bits if they differ
        x ^= (1 << i) | (1 << j)
    return x

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
