from test_framework import generic_test


# time: O(n(1 + log_b2(b1)))
def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    if num_as_string == "0":
        return "0"
    numerals = "0123456789ABCDEF"
    isNegative = num_as_string[0] == "-"
    num = 0
    for n in num_as_string[isNegative:]:
        num = num * b1 + numerals.index(n)
    result = []
    while num > 0:
        result.append(numerals[num % b2])
        num //= b2
    if isNegative:
        result.append("-")
    return "".join(reversed(result))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "convert_base.py", "convert_base.tsv", convert_base
        )
    )
