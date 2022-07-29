import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# time: O(n^2)
# space: O(1)
# def replace_and_remove(size: int, s: List[str]) -> int:
#     i = 0
#     while i < len(s):
#         if s[i] == "b":
#             del s[i]
#             size -= 1
#         elif s[i] == "a":
#             s[i] = "d"
#             s.insert(i, "d")
#             size += 1
#             i += 2
#         else:
#             i += 1
#     return size


# time: O(n)
# space: O(n)
# def replace_and_remove(size: int, s: List[str]) -> int:
#     result = []
#     for i in range(size):
#         if s[i] == "b":
#             continue
#         if s[i] == "a":
#             result.append("d")
#             result.append("d")
#         else:
#             result.append(s[i])
#     s[:] = result
#     return len(result)


# time: O(n)
# space: O(1)
def replace_and_remove(size: int, s: List[str]) -> int:
    write_idx = 0
    a_count = 0
    for i in range(size):
        if s[i] != "b":
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == "a":
            a_count += 1
    write_idx += a_count - 1
    size = write_idx + 1
    for i in reversed(range(size - a_count)):
        if s[i] == "a":
            s[write_idx - 1 : write_idx + 1] = "dd"
            write_idx -= 2
        else:
            s[write_idx] = s[i]
            write_idx -= 1
    return size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "replace_and_remove.py",
            "replace_and_remove.tsv",
            replace_and_remove_wrapper,
        )
    )
