from typing import List

from test_framework import generic_test


# convert to int, multiply, convert back to lists
# time: O(n*m), where n and m are the number of digits
# space: O(n+m)
"""
def multiply(num1: List[int], num2: List[int]) -> List[int]:
    int1 = int("".join(map(str, num1)))
    int2 = int("".join(map(str, num2)))
    sign = -1 if int1 < 0 else 1
    sign *= -1 if int2 < 0 else 1
    result = list(map(int, str(abs(int1) * abs(int2))))
    result[0] *= sign
    return result
"""

# work with lists directly
# time: O(n*m), where n and m are the number of digits
# space: O(n+m)
def multiply(num1: List[int], num2: List[int]) -> List[int]:
    sign = -1 if num1[0] * num2[0] < 0 else 1
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])

    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    i = 0
    while result[i] == 0 and i < len(result) - 1:
        i += 1
    result = result[i:]

    result[0] *= sign
    return result



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
