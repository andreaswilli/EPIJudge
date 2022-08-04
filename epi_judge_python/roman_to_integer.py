from test_framework import generic_test


# time: O(n)
# space: O(1)
def roman_to_integer(s: str) -> int:
    numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    i = 0
    while i < len(s):
        if i + 1 == len(s) or numerals[s[i]] >= numerals[s[i + 1]]:
            sum += numerals[s[i]]
            i += 1
        else:
            sum += numerals[s[i + 1]] - numerals[s[i]]
            i += 2
    return sum


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", "roman_to_integer.tsv", roman_to_integer
        )
    )
