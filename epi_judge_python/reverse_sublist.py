from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# time: O(n)
# space: O(1)
def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    dummy_head = before_sub = ListNode(0, L)
    for _ in range(1, start):
        before_sub = before_sub.next

    new_sub_tail = before_sub.next
    for _ in range(start, finish):
        tmp = new_sub_tail.next
        new_sub_tail.next, tmp.next, before_sub.next = tmp.next, before_sub.next, tmp
    return dummy_head.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_sublist.py", "reverse_sublist.tsv", reverse_sublist
        )
    )
