from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# time: O(n)
# space: O(1)
def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    cur = L
    while cur:
        while cur.next and cur.data == cur.next.data:
            cur.next = cur.next.next
        cur = cur.next
    return L


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            "remove_duplicates_from_sorted_list.tsv",
            remove_duplicates,
        )
    )
