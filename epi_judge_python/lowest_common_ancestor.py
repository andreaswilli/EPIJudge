import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import (
    collections,
    must_find_node,
    strip_parent_link,
)
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# time: O(n)
# space: O(h), where h is the height of the tree
def lca(
    tree: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode
) -> Optional[BinaryTreeNode]:
    Result = collections.namedtuple("Result", ("count", "ancestor"))

    def lca_helper(
        tree: BinaryTreeNode | None, node0: BinaryTreeNode, node1: BinaryTreeNode
    ) -> Result:
        if not tree:
            return Result(count=0, ancestor=None)

        left_result = lca_helper(tree.left, node0, node1)
        if left_result.count == 2:
            return left_result

        right_result = lca_helper(tree.right, node0, node1)
        if right_result.count == 2:
            return right_result

        cnt = left_result.count + right_result.count + (node0, node1).count(tree)
        return Result(cnt, tree if cnt == 2 else None)

    return lca_helper(tree, node0, node1).ancestor


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(
            lca, tree, must_find_node(tree, key1), must_find_node(tree, key2)
        )
    )

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor.py", "lowest_common_ancestor.tsv", lca_wrapper
        )
    )
