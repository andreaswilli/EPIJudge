import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None  # Populates this field.


# time: O(n)
# space: O(h)
# def construct_right_sibling(tree: BinaryTreeNode | None) -> None:
#     if not tree:
#         return
#     cur_left = tree.left
#     cur_right = tree.right
#     while cur_left and cur_right:
#         cur_left.next = cur_right
#         cur_left = cur_left.right
#         cur_right = cur_right.left
#     construct_right_sibling(tree.left)
#     construct_right_sibling(tree.right)

# time: O(n)
# space: O(1)
def construct_right_sibling(tree: BinaryTreeNode | None) -> None:
    while tree and tree.left:
        cur = tree
        while cur:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            cur = cur.next
        tree = tree.left


def traverse_next(node):
    while node:
        yield node
        node = node.next
    return


def traverse_left(node):
    while node:
        yield node
        node = node.left
    return


def clone_tree(original):
    if not original:
        return None
    cloned = BinaryTreeNode(original.data)
    cloned.left, cloned.right = clone_tree(original.left), clone_tree(original.right)
    return cloned


@enable_executor_hook
def construct_right_sibling_wrapper(executor, tree):
    cloned = clone_tree(tree)

    executor.run(functools.partial(construct_right_sibling, cloned))

    return [[n.data for n in traverse_next(level)] for level in traverse_left(cloned)]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_right_sibling.py",
            "tree_right_sibling.tsv",
            construct_right_sibling_wrapper,
        )
    )
