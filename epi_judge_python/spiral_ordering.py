from typing import List

from test_framework import generic_test


# time: O(n), where n is the total number of elements in the matrix
# space: O(n)
def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    result = []
    size = len(square_matrix)
    offset = 0
    while size > 1:
        result += square_matrix[offset][offset : offset + size - 1]
        for i in range(offset, offset + size - 1):
            result.append(square_matrix[i][offset + size - 1])
        result += square_matrix[offset + size - 1][offset + 1 : offset + size][::-1]
        for i in range(offset + size - 1, offset, -1):
            result.append(square_matrix[i][offset])
        size -= 2
        offset += 1
    if size == 1:
        result.append(square_matrix[offset][offset])
    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "spiral_ordering.py", "spiral_ordering.tsv", matrix_in_spiral_order
        )
    )
