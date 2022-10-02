from typing import Tuple
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# time: O(n)
# space: O(h), where h is the height of the tree
def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def is_balanced(root: BinaryTreeNode | None) -> Tuple[bool, int]:
        if not root:
            return True, -1
        l_balanced, l_height = is_balanced(root.left)
        r_balanced, r_height = is_balanced(root.right)
        return (
            l_balanced and r_balanced and abs(l_height - r_height) <= 1,
            max(l_height, r_height) + 1,
        )

    balanced, _ = is_balanced(tree)
    return balanced


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_balanced.py", "is_tree_balanced.tsv", is_balanced_binary_tree
        )
    )
