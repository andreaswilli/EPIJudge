from test_framework import generic_test
import functools


# time: O(n^2)
# space: O(1)
# def rabin_karp(t: str, s: str) -> int:
#     for i in range(len(t) - len(s) + 1):
#         matchStart = i
#         matchLen = 0
#         while (
#             i + matchLen < len(t)
#             and matchLen < len(s)
#             and t[i + matchLen] == s[matchLen]
#         ):
#             matchLen += 1
#         if matchLen == len(s):
#             return matchStart
#     return -1

# time: O(n+m), n is length of t, m is length of s
# space: O(1)
def rabin_karp(t: str, s: str) -> int:
    if len(s) > len(t):
        return -1
    BASE = 26

    def rolling_hash(hash: int, char: str) -> int:
        return hash * BASE + ord(char)

    t_hash = functools.reduce(rolling_hash, t[: len(s)], 0)
    s_hash = functools.reduce(rolling_hash, s, 0)

    for i in range(len(s), len(t) + 1):
        if t_hash == s_hash and t[i - len(s) : i] == s:
            return i - len(s)
        if i == len(t):
            return -1
        t_hash -= ord(t[i - len(s)]) * BASE ** (len(s) - 1)
        t_hash = t_hash * BASE + ord(t[i])
    return -1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "substring_match.py", "substring_match.tsv", rabin_karp
        )
    )
