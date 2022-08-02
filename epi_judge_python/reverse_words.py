import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
# time: O(n)
# space: O(n)
# def reverse_words(s):
#     s[:] = list(" ".join(reversed("".join(s).split(" "))))

# time: O(n)
# space: O(1)
def reverse_words(s):
    def reverse(arr, low, high):
        for i in range(low, (low + high + 1) // 2):
            arr[i], arr[high + low - i] = arr[high + low - i], arr[i]

    reverse(s, 0, len(s) - 1)
    start = end = 0
    while end < len(s):
        while end < len(s) and s[end] != " ":
            end += 1
        reverse(s, start, end - 1)
        start = end = end + 1


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return "".join(s_copy)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_words.py", "reverse_words.tsv", reverse_words_wrapper
        )
    )
