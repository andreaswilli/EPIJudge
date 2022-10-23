from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# time: O(n)
# space: O(h)
def has_path_sum(tree: BinaryTreeNode | None, remaining_weight: int) -> bool:
    if not tree:
        return False

    if not tree.left and not tree.right:
        return remaining_weight == tree.data

    new_rem = remaining_weight - tree.data
    return has_path_sum(tree.left, new_rem) or has_path_sum(tree.right, new_rem)


if __name__ == "__main__":
    exit(generic_test.generic_test_main("path_sum.py", "path_sum.tsv", has_path_sum))
