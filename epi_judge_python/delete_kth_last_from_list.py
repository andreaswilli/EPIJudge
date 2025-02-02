from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# time: O(n)
# space: O(1)
# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    dummy_head = ListNode(0, L)
    cur = L
    for _ in range(k):
        cur = cur.next
    node_to_delete = dummy_head
    while cur:
        cur = cur.next
        node_to_delete = node_to_delete.next
    node_to_delete.next = node_to_delete.next.next
    return dummy_head.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "delete_kth_last_from_list.py",
            "delete_kth_last_from_list.tsv",
            remove_kth_last,
        )
    )
