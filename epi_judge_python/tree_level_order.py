from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# recursive
# time: O(n)
# def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
#     result = []

#     def traverse(tree: BinaryTreeNode | None, level: int):
#         if not tree:
#             return
#         if len(result) <= level:
#             result.append([])
#         result[level].append(tree.data)
#         traverse(tree.left, level + 1)
#         traverse(tree.right, level + 1)

#     traverse(tree, 0)
#     return result

# iterative with queue
# time: O(n)
def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    result = []
    current_lvl_nodes = [tree] if tree else []
    while current_lvl_nodes:
        result.append([node.data for node in current_lvl_nodes])
        nodes = current_lvl_nodes
        current_lvl_nodes = []
        for n in nodes:
            if n.left:
                current_lvl_nodes.append(n.left)
            if n.right:
                current_lvl_nodes.append(n.right)
    return result


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_level_order.py", "tree_level_order.tsv", binary_tree_depth_order
        )
    )
