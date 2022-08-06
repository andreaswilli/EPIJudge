from test_framework import generic_test
from test_framework.test_failure import TestFailure


# time: O(n)
# space: O(n)
def decoding(s: str) -> str:
    result = []
    start = i = 0
    while i < len(s):
        while s[i].isdigit():
            i += 1
        result.append(s[i] * int(s[start:i]))
        i += 1
        start = i
    return "".join(result)


# time: O(n)
# space: O(n)
def encoding(s: str) -> str:
    result = []
    start = cur = 0
    while cur < len(s):
        while cur < len(s) and s[start] == s[cur]:
            cur += 1
        result.append(str(cur - start) + s[cur - 1])
        start = cur
    return "".join(result)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure("Decoding failed")
    if encoding(decoded) != encoded:
        raise TestFailure("Encoding failed")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "run_length_compression.py", "run_length_compression.tsv", rle_tester
        )
    )
