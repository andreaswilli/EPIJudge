from typing import List

from test_framework import generic_test


# time: O(n^2)
# space: O(n)
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    def is_valid_part(part: List[int]) -> bool:
        filled_entries = [0] * (len(part) + 1)
        for entry in part:
            if entry != 0:
                if filled_entries[entry] > 0:
                    return False
                filled_entries[entry] += 1
        return True

    for row in partial_assignment:
        if not is_valid_part(row):
            return False

    for i in range(len(partial_assignment[0])):
        col = []
        for row in partial_assignment:
            col.append(row[i])
        if not is_valid_part(col):
            return False

    for row in range(0, len(partial_assignment), 3):
        for col in range(0, len(partial_assignment[0]), 3):
            square = []
            for i in range(3):
                for j in range(3):
                    square.append(partial_assignment[row + i][col + j])
            if not is_valid_part(square):
                return False
    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_valid_sudoku.py", "is_valid_sudoku.tsv", is_valid_sudoku
        )
    )
