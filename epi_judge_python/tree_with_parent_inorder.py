from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


# time: O(n)
# space: O(1)
def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    result = []
    while tree and tree.left:
        tree = tree.left
    while tree:
        result.append(tree.data)
        if tree.right:
            tree = tree.right
            while tree.left:
                tree = tree.left
        else:
            while tree.parent and tree == tree.parent.right:
                tree = tree.parent
            tree = tree.parent
    return result


# time: O(n)
# space: O(1)
# def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
#     prev, result = None, []
#     while tree:
#         if prev is tree.parent:
#             if tree.left:
#                 next = tree.left
#             else:
#                 result.append(tree.data)
#                 next = tree.right or tree.parent
#         elif prev is tree.left:
#             result.append(tree.data)
#             next = tree.right or tree.parent
#         else:
#             next = tree.parent
#         prev, tree = tree, next
#     return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_with_parent_inorder.py",
            "tree_with_parent_inorder.tsv",
            inorder_traversal,
        )
    )
