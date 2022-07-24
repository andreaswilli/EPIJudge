from typing import List

from test_framework import generic_test


# time: O(n^2), matrix is of size n * n
# space: O(n^2)
# def rotate_matrix(square_matrix: List[List[int]]) -> None:
#     length = length
#     rot_matrix = [[0] * length for _ in range(length)]
#     for row in range(length):
#         for col in range(length):
#             rot_matrix[col][length - row] = square_matrix[row][col]
#     square_matrix[:] = rot_matrix
#     return

# time: O(n^2), matrix is of size n * n
# space: O(1)
def rotate_matrix(square_matrix: List[List[int]]) -> None:
    l = len(square_matrix) - 1
    for i in range(len(square_matrix) // 2):
        for j in range(i, l - i):
            topLeft = square_matrix[i][j]
            square_matrix[i][j] = square_matrix[-j - 1][i]
            square_matrix[-j - 1][i] = square_matrix[-i - 1][-j - 1]
            square_matrix[-i - 1][-j - 1] = square_matrix[j][-i - 1]
            square_matrix[j][-i - 1] = topLeft
    return


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "matrix_rotation.py", "matrix_rotation.tsv", rotate_matrix_wrapper
        )
    )
