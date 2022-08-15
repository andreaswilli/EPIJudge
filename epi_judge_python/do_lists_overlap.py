import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# time: O(n^2)
# space: O(n)
# def overlapping_lists(
#     l0: Optional[ListNode], l1: Optional[ListNode]
# ) -> Optional[ListNode]:
#     visited_l0 = []
#     while l0 and l0 not in visited_l0:
#         visited_l0.append(l0)
#         l0 = l0.next
#     visited_l1 = []
#     while l1 and l1 not in visited_l0 and l1 not in visited_l1:
#         visited_l1.append(l1)
#         l1 = l1.next
#     return l1 if l1 in visited_l0 else None


# time: O(n)
# space: O(1)
def overlapping_lists(
    l0: Optional[ListNode], l1: Optional[ListNode]
) -> Optional[ListNode]:
    def length(L):
        slow = fast = L
        length = 0
        while slow and fast and fast.next:
            slow, fast = slow.next, fast.next.next
            length += 1
            if slow is fast:
                return -1, slow
        while slow:
            length += 1
            slow = slow.next
        return length, None

    l0_length, l0_loop = length(l0)
    l1_length, l1_loop = length(l1)
    if (l0_loop == None) != (l1_loop == None):
        return None
    if l0_loop != None:
        cur = l0_loop
        while True:
            cur = cur.next
            if cur is l1_loop:
                return cur
            if cur is l0_loop:
                break
    else:
        if l0_length > l1_length:
            l0, l1 = l1, l0
        for _ in range(abs(int(l0_length - l1_length))):
            if l1:
                l1 = l1.next
        while l0 and l1 and l0 != l1:
            l0, l1 = l0.next, l1.next
        return l0
    return None


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError("Invalid input data")
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError("Invalid input data")
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure("Invalid result")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "do_lists_overlap.py", "do_lists_overlap.tsv", overlapping_lists_wrapper
        )
    )
