import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# time: O(n)
# space: O(1)
def list_pivoting(l: ListNode, x: int) -> Optional[ListNode]:
    dummy_head_lower = lower = ListNode()
    dummy_head_pivot = pivot = ListNode()
    dummy_head_greater = greater = ListNode()
    while l:
        if l.data < x:
            lower.next = l
            lower = lower.next
        elif l.data == x:
            pivot.next = l
            pivot = pivot.next
        else:
            greater.next = l
            greater = greater.next
        l = l.next
    greater.next = None
    pivot.next = dummy_head_greater.next
    lower.next = dummy_head_pivot.next
    return dummy_head_lower.next


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure("List is not pivoted")
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure("List is not pivoted")

    if sorted(original) != sorted(pivoted):
        raise TestFailure("Result list contains different values")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "pivot_list.py", "pivot_list.tsv", list_pivoting_wrapper
        )
    )
