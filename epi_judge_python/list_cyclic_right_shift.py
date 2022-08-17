from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# time: O(n)
# space: O(1)
def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if not L:
        return L
    length = 1
    tail = L
    while tail.next:
        length += 1
        tail = tail.next
    tail.next = L
    k %= length
    cur = L
    for _ in range(length - k - 1):
        cur = cur.next
    L = cur.next
    cur.next = None
    return L


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "list_cyclic_right_shift.py",
            "list_cyclic_right_shift.tsv",
            cyclically_right_shift_list,
        )
    )
