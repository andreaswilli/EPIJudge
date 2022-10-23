from typing import List, Tuple

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# time: O(n)
# space: O(h)
# def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
#     stack = [tree] if tree else []
#     result = []

#     while stack:
#         cur = stack.pop()
#         if cur.right:
#             stack.append(cur.right)
#         if cur.left or cur.right:
#             stack.append(BinaryTreeNode(cur.data, None, None))
#         else:
#             result.append(cur.data)
#         if cur.left:
#             stack.append(cur.left)
#     return result


# time: O(n)
# space: O(h)
def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    stack: List[Tuple[BinaryTreeNode | None, bool]] = [(tree, False)]
    result = []

    while stack:
        cur, left_subtree_traversed = stack.pop()
        if cur:
            if left_subtree_traversed:
                result.append(cur.data)
            else:
                stack.append((cur.right, False))
                stack.append((cur, True))
                stack.append((cur.left, False))
    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_inorder.py", "tree_inorder.tsv", inorder_traversal
        )
    )
