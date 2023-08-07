from typing import Counter, Dict, List

from test_framework import generic_test


# time: O(n^2)
# space: O(n)
# def longest_subarray_with_distinct_entries(A: List[int]) -> int:
#     def distinct(counter: Counter[int]) -> bool:
#         for _, c in counter.items():
#             if c > 1:
#                 return False
#         return True
#
#     max_length = 0
#     left = 0
#     right = 0
#     counter: Counter[int] = Counter(A[0:1])
#
#     while left <= right < len(A):
#         if distinct(counter):
#             length = right - left + 1
#             if length > max_length:
#                 max_length = length
#             right += 1
#             counter.update(A[right:right+1])
#         else:
#             counter[A[left]] -= 1
#             left += 1
#
#     return max_length


# time: O(n)
# space: O(n)
def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    most_recent_occurence: Dict[int, int] = dict()
    longest_subarray_start = 0
    result = 0

    for i, a in enumerate(A):
        if a in most_recent_occurence:
            prev_a_idx = most_recent_occurence[a]
            if prev_a_idx >= longest_subarray_start:
                length = i - longest_subarray_start
                if length > result:
                    result = length
                longest_subarray_start = prev_a_idx + 1
        most_recent_occurence[a] = i

    return max(result, len(A) - longest_subarray_start)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
