import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# time: O(n^2)
# space: O(n)
# def has_cycle(head: ListNode) -> Optional[ListNode]:
#     visited = list()
#     cur = head
#     while cur:
#         if cur in visited:
#             return cur
#         visited.append(cur)
#         cur = cur.next
#     return None

# time: O(n^2)
# space: O(1)
# def has_cycle(head: ListNode) -> Optional[ListNode]:
#     cur = head
#     i = 0
#     while cur:
#         cur_inner = head
#         j = 0
#         while j < i and cur_inner:
#             if cur.data == cur_inner.data:
#                 return cur
#             cur_inner = cur_inner.next
#             j += 1
#         cur = cur.next
#         i += 1
#     return None

# time: O(n)
# space: O(n)
# def has_cycle(head: ListNode) -> Optional[ListNode]:
#     visited = set()
#     cur = head
#     while cur:
#         if cur.data in visited:
#             return cur
#         visited.add(cur.data)
#         cur = cur.next
#     return None

# time: O(n)
# space: O(1)
# def has_cycle(head: ListNode) -> Optional[ListNode]:
#     slow = fast = head
#     while slow and fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow is fast:
#             cycle_len = 0
#             start = slow
#             while slow:
#                 cycle_len += 1
#                 slow = slow.next
#                 if slow is start:
#                     break
#             advanced_it = it = head
#             for _ in range(cycle_len):
#                 advanced_it = advanced_it.next if advanced_it else None
#             while it and advanced_it and it is not advanced_it:
#                 it = it.next
#                 advanced_it = advanced_it.next
#             return it
#     return None

# time: O(n)
# space: O(1)
def has_cycle(head: ListNode) -> Optional[ListNode]:
    fast = slow = head
    while slow and fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            slow = head
            while slow and slow is not fast:
                slow, fast = slow.next, fast.next
            return slow
    return None


@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError("Can't cycle empty list")
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError("Can't find a cycle start")
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure("Found a non-existing cycle")
    else:
        if result is None:
            raise TestFailure("Existing cycle was not found")
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    "Returned node does not belong to the cycle or is not the closest node to the head"
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            "Returned node does not belong to the cycle or is not the closest node to the head"
        )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_list_cyclic.py", "is_list_cyclic.tsv", has_cycle_wrapper
        )
    )
