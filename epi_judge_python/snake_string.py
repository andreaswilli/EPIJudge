from test_framework import generic_test
import math


# time: O(n)
# space: O(n)
# def snake_string(s: str) -> str:
#     snake = []
#     for i in range(1, len(s), 4):
#         snake.append(s[i])
#     for i in range(0, len(s), 2):
#         snake.append(s[i])
#     for i in range(3, len(s), 4):
#         snake.append(s[i])
#     return "".join(snake)


# time: O(n)
# space: O(n)
def snake_string(s: str) -> str:
    return s[1::4] + s[::2] + s[3::4]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "snake_string.py", "snake_string.tsv", snake_string
        )
    )
