from typing import Counter
from test_framework import generic_test


# time: O(n)
# space: O(c), where c is the number of distinct characters in the string
def can_form_palindrome(s: str) -> bool:
    counter = Counter(s)

    num_odd = 0

    for c in counter.values():
        if c % 2:
            num_odd += 1

    return num_odd <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
