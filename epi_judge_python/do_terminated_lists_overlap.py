import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# time: O(n^2)
# space: O(n)
# def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
#     visited = []
#     cur = l0
#     while cur:
#         visited.append(cur)
#         cur = cur.next
#     cur = l1
#     while cur:
#         if cur in visited:
#             return cur
#         cur = cur.next
#     return None

# time: O(n^2)
# space: O(1)
# def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
#     cur = l0
#     while cur:
#         cur_inner = l1
#         while cur_inner:
#             if cur == cur_inner:
#                 return cur
#             cur_inner = cur_inner.next
#         cur = cur.next
#     return None

# time: O(n)
# space: O(1)
def overlapping_no_cycle_lists(
    l0: Optional[ListNode], l1: Optional[ListNode]
) -> Optional[ListNode]:
    def length(l: Optional[ListNode]) -> int:
        length = 0
        while l:
            length += 1
            l = l.next
        return length

    l0_len = length(l0)
    l1_len = length(l1)
    if l0_len > l1_len:
        l0, l1 = l1, l0
    for _ in range(abs(l1_len - l0_len)):
        if l1:  # unnecessary, but pyright will complain without this
            l1 = l1.next
    while l0 and l1 and l0 != l1:
        l0, l1 = l0.next, l1.next
    return l0


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure("Invalid result")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "do_terminated_lists_overlap.py",
            "do_terminated_lists_overlap.tsv",
            overlapping_no_cycle_lists_wrapper,
        )
    )
