import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# time: O(n)
# space: O(1)
def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    def reconstruct_preorder_helper(preorder_iter):
        data = next(preorder_iter)
        if data == None:
            return None
        return BinaryTreeNode(
            data,
            reconstruct_preorder_helper(preorder_iter),
            reconstruct_preorder_helper(preorder_iter),
        )

    return reconstruct_preorder_helper(iter(preorder))


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == "null" else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_from_preorder_with_null.py",
            "tree_from_preorder_with_null.tsv",
            reconstruct_preorder_wrapper,
        )
    )
