from test_framework import generic_test


# time: O(n)
def is_well_formed(s: str) -> bool:
    parens = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack = []
    for p in s:
        if p in parens:
            if not stack or stack.pop() != parens[p]:
                return False
        else:
            stack.append(p)
    return not stack


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_valid_parenthesization.py",
            "is_valid_parenthesization.tsv",
            is_well_formed,
        )
    )
