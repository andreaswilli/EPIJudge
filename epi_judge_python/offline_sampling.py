import functools
import random
from typing import List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


# repeatedly pick a random number from A (pick again if number is picked twice)
# time: O(k)
# space: O(k)
"""
def random_sampling(k: int, A: List[int]) -> None:
    result = []
    for _ in range(k):
        pick = None
        while pick == None or pick in result:
            pick = random.choice(A)
        result.append(pick)
    A[:] = result
    return
"""

# repeatedly pick a random number from A and swap it to the start of A
# time: O(k)
# space: O(1)
"""
def random_sampling(k: int, A: List[int]) -> None:
    for i in range(k):
        pick = random.randint(i, len(A) - 1)
        A[i], A[pick] = A[pick], A[i]
    return
"""

# optimize for k > n/2
# time: O(min(k, n-k))
# space: O(1)
def random_sampling(k: int, A: List[int]) -> None:
    if k <= len(A) / 2:
        for i in range(k):
            pick = random.randint(i, len(A) - 1)
            A[i], A[pick] = A[pick], A[i]
    else:
        for i in range(len(A) - k):
            pick = random.randint(0, len(A) - 1 - i)
            A[len(A) - 1 -i], A[pick] = A[pick], A[len(A) - 1 -i]
    return


@enable_executor_hook
def random_sampling_wrapper(executor, k, A):
    def random_sampling_runner(executor, k, A):
        result = []

        def populate_random_sampling_result():
            for _ in range(100000):
                random_sampling(k, A)
                result.append(A[:k])

        executor.run(populate_random_sampling_result)

        total_possible_outcomes = binomial_coefficient(len(A), k)
        A = sorted(A)
        comb_to_idx = {
            tuple(compute_combination_idx(A, len(A), k, i)): i
            for i in range(binomial_coefficient(len(A), k))
        }

        return check_sequence_is_uniformly_random(
            [comb_to_idx[tuple(sorted(a))] for a in result],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_sampling_runner, executor, k, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('offline_sampling.py',
                                       'offline_sampling.tsv',
                                       random_sampling_wrapper))
