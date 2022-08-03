from test_framework import generic_test
import itertools


# nested loops
# time: O(n * 2^n)
# space: O(n * 2^n)
# def look_and_say(n: int) -> str:
#     result = [1]
#     for _ in range(1, n):
#         i = 0
#         current = []
#         while i < len(result):
#             num = result[i]
#             count = 0
#             while i < len(result) and result[i] == num:
#                 count += 1
#                 i += 1
#             current.append(count)
#             current.append(num)
#         result = current
#     return "".join(map(str, result))

# groupby
# time: O(n * 2^n)
# space: O(n * 2^n)
def look_and_say(n: int) -> str:
    result = "1"
    for _ in range(1, n):
        result = "".join(
            [str(len(list(gr))) + k for k, gr in itertools.groupby(result)]
        )
    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "look_and_say.py", "look_and_say.tsv", look_and_say
        )
    )
