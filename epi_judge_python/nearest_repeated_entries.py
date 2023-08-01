from typing import Dict, List
import typing

from test_framework import generic_test


# time: O(n)
# space: O(n)
def find_nearest_repetition(paragraph: List[str]) -> int:
    nearest_rep = float('inf')
    word_occurance: Dict[str, int] = dict()

    for i, word in enumerate(paragraph):
        if word in word_occurance:
            dist = i - word_occurance.get(word, 0)
            if dist == 1:
                return dist
            if dist < nearest_rep:
                nearest_rep = dist
        word_occurance[word] = i

    if nearest_rep == float('inf'):
        nearest_rep = -1

    return typing.cast(int, nearest_rep)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
