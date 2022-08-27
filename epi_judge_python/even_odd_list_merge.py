from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# repeatedly point prev node to next node
# time: O(n)
# space: O(1)
def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    odd_dummy_head = ListNode(0)
    prev = odd_dummy_head
    cur = L
    even = True
    even_dummy_tail = None
    while cur:
        prev.next = cur.next
        prev = cur
        if even:
            even_dummy_tail = cur
        cur = cur.next
        even = not even
    if even_dummy_tail:
        even_dummy_tail.next = odd_dummy_head.next
    return L


# assign to even and odd lists and concatenate them together
# time: O(n)
# space: O(1)
# def even_odd_merge(L: ListNode) -> Optional[ListNode]:
#     even_dummy_head, odd_dummy_head = ListNode(0), ListNode(0)
#     tails = [even_dummy_head, odd_dummy_head]
#     turn = False
#     while L:
#         tails[turn].next = L
#         tails[turn] = L
#         L = L.next
#         turn = not turn
#     tails[0].next = odd_dummy_head.next
#     tails[1].next = None
#     return even_dummy_head.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "even_odd_list_merge.py", "even_odd_list_merge.tsv", even_odd_merge
        )
    )
