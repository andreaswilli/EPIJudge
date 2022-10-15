from typing import Deque
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# iterative
# time: O(n)
# space: O(n)
# def is_symmetric(tree: BinaryTreeNode) -> bool:
#     q_left = Deque()
#     q_right = Deque()
#     q_left.append(tree.left if tree and tree.left else BinaryTreeNode(None))
#     q_right.append(tree.right if tree and tree.right else BinaryTreeNode(None))

#     while q_left and q_right:
#         l = q_left.popleft()
#         r = q_right.popleft()
#         if l.data != r.data:
#             return False
#         if l.left or l.right or r.left or r.right:
#             q_left.append(l.left if l.left else BinaryTreeNode(None))
#             q_left.append(l.right if l.right else BinaryTreeNode(None))
#             q_right.append(r.right if r.right else BinaryTreeNode(None))
#             q_right.append(r.left if r.left else BinaryTreeNode(None))

#     return 0 == len(q_left) == len(q_right)

# recursive
# time: O(n)
# space: O(h), where h is the height of the tree
def is_symmetric(tree: BinaryTreeNode) -> bool:
    def recursive_check(t1, t2) -> bool:
        if not t1 and not t2:
            return True
        elif t1 and t2:
            return (
                t1.data == t2.data
                and recursive_check(t1.left, t2.right)
                and recursive_check(t1.right, t2.left)
            )
        else:
            return False

    if not tree:
        return True
    return recursive_check(tree.left, tree.right)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_symmetric.py", "is_tree_symmetric.tsv", is_symmetric
        )
    )
