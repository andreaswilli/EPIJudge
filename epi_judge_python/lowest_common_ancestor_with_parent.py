from collections import deque
import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# time: O(h^2)
# space: O(1)
# def lca(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
#     it0 = node0
#     it1: BinaryTreeNode
#     while it0.parent:
#         it1 = node1
#         while it1.parent:
#             if it0.data == it1.data:
#                 return it0
#             it1 = it1.parent
#         it0 = it0.parent
#     return it0

# time: O(h)
# space: O(h)
# def lca(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
#     path0 = deque()
#     path1 = deque()
#     while node0:
#         path0.appendleft(node0)
#         node0 = node0.parent
#     while node1:
#         path1.appendleft(node1)
#         node1 = node1.parent
#     commonAncestor = None
#     i = 0
#     minPath = min(len(path0), len(path1))
#     while i < minPath and path0[i] == path1[i]:
#         commonAncestor = path0[i]
#         i += 1
#     return commonAncestor

# time: O(h)
# space: O(1)
def lca(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    def get_depth(node) -> int:
        depth = 0
        while node.parent:
            depth += 1
            node = node.parent
        return depth

    d0, d1 = get_depth(node0), get_depth(node1)

    for _ in range(d0 - d1):
        node0 = node0.parent
    for _ in range(d1 - d0):
        node1 = node1.parent

    while node0 != node1:
        node0, node1 = node0.parent, node1.parent

    return node0


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0), must_find_node(tree, node1))
    )

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor_with_parent.py",
            "lowest_common_ancestor.tsv",
            lca_wrapper,
        )
    )
