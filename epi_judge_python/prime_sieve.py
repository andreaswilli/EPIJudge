from typing import List
import math

from test_framework import generic_test


# brute force
# time: O(n * sqrt(n))
# space: O(1)
"""
def generate_primes(n: int) -> List[int]:
    primes = []
    for i in range(2, n + 1):
        isPrime = True
        for j in range(2, math.floor(math.sqrt(i)) + 1):
            if i % j == 0:
                isPrime = False
                break;
        if isPrime:
            primes.append(i)
    return primes
"""

# remove multiples of primes
# time: O(n log log n)
# space: O(n)
def generate_primes(n: int) -> List[int]:
    is_prime = [False] * 2 + [True] * n
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                is_prime[j] = False
    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
