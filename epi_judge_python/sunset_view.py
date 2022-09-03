from collections import namedtuple
from typing import Iterator, List

from test_framework import generic_test


# time: O(n)
def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    House = namedtuple("House", ["id", "height"])
    houses_with_view = []
    for id, height in enumerate(sequence):
        while houses_with_view and houses_with_view[-1].height <= height:
            houses_with_view.pop()
        houses_with_view.append(House(id, height))
    return [house.id for house in reversed(houses_with_view)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sunset_view.py", "sunset_view.tsv", examine_buildings_with_sunset
        )
    )
