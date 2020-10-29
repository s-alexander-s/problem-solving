# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/
# binary-search-tree binary-tree stack
from itertools import islice
from unittest import TestCase


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True

        stack = [(root, None, None)]
        while stack:
            current_node, lower_border, upper_border = stack.pop()

            if lower_border is not None and current_node.val <= lower_border:
                return False
            if upper_border is not None and current_node.val >= upper_border:
                return False

            if current_node.left:
                stack.append((current_node.left, lower_border, current_node.val))
            if current_node.right:
                stack.append((current_node.right, current_node.val, upper_border))

        return True


class Test(TestCase):
    def _build_tree(self, nodes):
        if not nodes:
            return None

        nodes_buff = [TreeNode(nodes[0])]
        for i, n in enumerate(islice(nodes, 1, None)):
            new_node = TreeNode(n) if n else None
            nodes_buff.append(new_node)
            if new_node is None:
                continue
            parent = nodes_buff[i // 2]
            if i % 2 == 0:
                parent.left = new_node
            else:
                parent.right = new_node

        return nodes_buff[0]

    def setUp(self) -> None:
        self.s = Solution()

    def test_empty_tree(self):
        self.assertEqual(
            True,
            self.s.isValidBST(None)
        )

    def test_normal_bst(self):
        self.assertEqual(
            True,
            self.s.isValidBST(self._build_tree([3, 1, 6, None, None, 4, 7]))
        )

    def test_single_node_tree(self):
        self.assertEqual(
            True,
            self.s.isValidBST(self._build_tree([1]))
        )

    def test_two_nodes_bst(self):
        self.assertEqual(
            True,
            self.s.isValidBST(self._build_tree([3, 1]))
        )

    def test_two_nodes_not_bst(self):
        self.assertEqual(
            False,
            self.s.isValidBST(self._build_tree([1, 3]))
        )

    def test_chain_bst(self):
        self.assertEqual(
            True,
            self.s.isValidBST(self._build_tree([1, None, 2, None, None, None, 3]))
        )

    def test_chain_not_bst(self):
        self.assertEqual(
            False,
            self.s.isValidBST(self._build_tree([1, None, 4, None, None, None, 3]))
        )

    def test_complete_bst(self):
        self.assertEqual(
            True,
            self.s.isValidBST(self._build_tree([10, 5, 15, 3, 7, 12, 17]))
        )

    def test_complete_not_bst(self):
        self.assertEqual(
            False,
            self.s.isValidBST(self._build_tree([10, 5, 15, 3, 7, 9, 17]))
        )

    def test_complete_bst_with_dangling_node(self):
        self.assertEqual(
            True,
            self.s.isValidBST(self._build_tree([10, 5, 15, 3, 7, 12, 17, 1]))
        )

    def test_complete_not_bst_with_dangling_node(self):
        self.assertEqual(
            False,
            self.s.isValidBST(self._build_tree([10, 5, 15, 3, 7, 12, 17, 11]))
        )

    def test_not_bst_with_repeating_values(self):
        self.assertEqual(
            False,
            self.s.isValidBST(self._build_tree([1, 1]))
        )
