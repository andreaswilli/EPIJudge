from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# time: O(n^2) ?
# space: O(nh)
# def binary_tree_from_preorder_inorder(
#     preorder: List[int], inorder: List[int]
# ) -> BinaryTreeNode | None:
#     if not preorder:
#         return None

#     root_idx = inorder.index(preorder[0])
#     return BinaryTreeNode(
#         preorder[0],
#         binary_tree_from_preorder_inorder(
#             preorder[1 : root_idx + 1], inorder[0:root_idx]
#         ),
#         binary_tree_from_preorder_inorder(
#             preorder[root_idx + 1 :], inorder[root_idx + 1 :]
#         ),
#     )


# time: O(n)
# space: O(n)
def binary_tree_from_preorder_inorder(
    preorder: List[int], inorder: List[int]
) -> BinaryTreeNode | None:
    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    def get_tree(pre_start, pre_end, in_start, in_end):
        if pre_start >= pre_end or in_start >= in_end:
            return None

        root_idx = node_to_inorder_idx[preorder[pre_start]]
        left_subtree_size = root_idx - in_start
        return BinaryTreeNode(
            preorder[pre_start],
            get_tree(
                pre_start + 1, pre_start + left_subtree_size + 1, in_start, root_idx
            ),
            get_tree(pre_start + left_subtree_size + 1, pre_end, root_idx + 1, in_end),
        )

    return get_tree(0, len(preorder), 0, len(inorder))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_from_preorder_inorder.py",
            "tree_from_preorder_inorder.tsv",
            binary_tree_from_preorder_inorder,
        )
    )
