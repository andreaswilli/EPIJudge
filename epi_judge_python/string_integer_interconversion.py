from test_framework import generic_test
from test_framework.test_failure import TestFailure


# time: O(n)
# space: O(n)
def int_to_string(x: int) -> str:
    if x == 0:
        return "0"
    isNegative = x < 0
    x = abs(x)
    string = []
    while x != 0:
        string.append(chr(ord("0") + x % 10))
        x //= 10
    if isNegative:
        string.append("-")
    return "".join(reversed(string))


# time: O(n)
# space: O(n)
def string_to_int(s: str) -> int:
    integer = 0
    sign = -1 if s[0] == "-" else 1
    for i in range(s[0] in "+-", len(s)):
        integer = 10 * integer + ord(s[i]) - ord("0")
    return sign * integer


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "string_integer_interconversion.py",
            "string_integer_interconversion.tsv",
            wrapper,
        )
    )
