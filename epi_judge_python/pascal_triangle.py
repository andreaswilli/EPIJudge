from typing import List

from test_framework import generic_test


# time: O(n^2)
# space: O(1)
def generate_pascal_triangle(n: int) -> List[List[int]]:
    triangle = [[1] * x for x in range(1, n + 1)]
    for i in range(n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "pascal_triangle.py", "pascal_triangle.tsv", generate_pascal_triangle
        )
    )
