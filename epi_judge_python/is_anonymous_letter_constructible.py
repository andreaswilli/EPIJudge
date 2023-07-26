from typing import Counter
from test_framework import generic_test


# pythonic solution
# time: O(m + n)
# space: O(L + M), where L and M are the numbers of distinct characters in the
#                  letter and magazine, respectively
# def is_letter_constructible_from_magazine(letter_text: str,
#                                           magazine_text: str) -> bool:
#     return len(Counter(letter_text) - Counter(magazine_text)) == 0


# time: O(m + n)
# space: O(L), where L is the number of distinct characters in the letter
def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    letter_count = Counter(letter_text)

    for c in magazine_text:
        if c in letter_count:
            letter_count[c] -= 1
        if letter_count[c] == 0:
            del letter_count[c]
        if not letter_count:
            break

    return not letter_count


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
