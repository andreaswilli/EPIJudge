from test_framework import generic_test
import math


# traverse half of the string and compare with second half
# time complexity: O(n)
# space complexity: O(n)
"""
def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    strRep = str(x)
    length = len(strRep)
    for i in range(length):
        if strRep[i] != strRep[length-1-i]:
            return False
    return True
"""

# using numbers only
# time complexity: O(n)
# space complexity: O(1)
def is_palindrome_number(x: int) -> bool:
    if x <= 0:
        return x == 0
    num_digits = math.floor(math.log10(x)) + 1
    while num_digits > 1:
        if x % 10 != x // 10 ** (num_digits-1):
            return False
        x %= 10 ** (num_digits-1) # remove most significant digit
        x //= 10 # remove least significant digit
        num_digits -= 2
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
