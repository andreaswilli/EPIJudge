from test_framework import generic_test
import functools


# for loop
# time: O(n)
# space: O(1)
# def ss_decode_col_id(col: str) -> int:
#     result = 0
#     for c in col:
#         result = result * 26 + ord(c) - ord("A") + 1
#     return result


# reduce function
# time: O(n)
# space: O(1)
def ss_decode_col_id(col: str) -> int:
    return functools.reduce(lambda acc, cur: acc * 26 + ord(cur) - ord("A") + 1, col, 0)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "spreadsheet_encoding.py", "spreadsheet_encoding.tsv", ss_decode_col_id
        )
    )
