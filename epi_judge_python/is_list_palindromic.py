from list_node import ListNode
from test_framework import generic_test


# time: O(n)
# space: O(1)
def is_linked_list_a_palindrome(L: ListNode) -> bool:
    fast = slow = L
    while slow and fast and fast.next:
        slow, fast = slow.next, fast.next.next
    dummy_head_rev = ListNode(0)
    while slow:
        dummy_head_rev.next, slow.next, slow = slow, dummy_head_rev.next, slow.next
    first = L
    second = dummy_head_rev.next
    while first and second:
        if first.data != second.data:
            return False
        first, second = first.next, second.next
    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_list_palindromic.py",
            "is_list_palindromic.tsv",
            is_linked_list_a_palindrome,
        )
    )
