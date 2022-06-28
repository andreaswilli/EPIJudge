from test_framework import generic_test


# iterate through bits until they differ and swap them
# time complexity: O(n)
"""
def closest_int_same_bit_count(x: int) -> int:
    i = 0
    while (x >> i) & 1 == (x >> i+1) & 1:
        i += 1
    x ^= 0b11 << i
    return x
"""

# find least significant differing bits and swap them
# time complexity: O(1)
def closest_int_same_bit_count(x: int) -> int:
    i = (x&-x).bit_length() - 1 # least significant on bit index
    if i == 0:
        i = (~x&-~x).bit_length() - 1 # least significant off bit index
    x ^= 0b11 << i-1
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
