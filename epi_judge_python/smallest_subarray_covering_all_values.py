import collections
import functools
from typing import Dict, List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


# time: O(n)
# space: O(k), where k is the number of keywords
def find_smallest_sequentially_covering_subset(paragraph: List[str],
                                               keywords: List[str]
                                               ) -> Subarray:
    result = Subarray(0, len(paragraph) - 1)
    last_occurence: Dict[str, int] = dict()
    start: Dict[int, int] = dict()

    for i, word in enumerate(paragraph):
        if word == keywords[0]:
            start[i] = i
            last_occurence[word] = i
        elif word in keywords:
            prev_keyword = keywords[keywords.index(word) - 1]
            if prev_keyword in last_occurence:
                start[i] = start[last_occurence[prev_keyword]]
                last_occurence[word] = i
                if word == keywords[-1] and i - start[i] < result.end - result.start:
                    result = Subarray(start[i], i)

    return result


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    result = executor.run(
        functools.partial(find_smallest_sequentially_covering_subset,
                          paragraph, keywords))

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError('Subarray start index is negative')

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure('Not all keywords are in the generated subarray')
        if para_idx >= len(paragraph):
            raise TestFailure('Subarray end index exceeds array size')
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_all_values.py',
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))
