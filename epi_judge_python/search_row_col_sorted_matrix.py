from typing import List

from test_framework import generic_test


# time: O(m + n), m = no. of rows, n = no. of cols
# space: O(1)
def matrix_search(A: List[List[int]], x: int) -> bool:
    col = len(A[0]) - 1
    row = 0

    while col >= 0 and row < len(A):
        if A[row][col] == x:
            return True
        elif A[row][col] < x:
            row += 1
        else:
            col -= 1

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
