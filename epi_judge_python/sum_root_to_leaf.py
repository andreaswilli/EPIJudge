from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# time: O(n)
# space: O(h)
def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    def traverse(tree: BinaryTreeNode, number: int) -> int:
        if not tree:
            return 0

        new_number = number * 2 + tree.data
        if tree.left or tree.right:
            return traverse(tree.left, new_number) + traverse(tree.right, new_number)
        return new_number

    return traverse(tree, 0)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sum_root_to_leaf.py", "sum_root_to_leaf.tsv", sum_root_to_leaf
        )
    )
