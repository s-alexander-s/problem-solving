# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
# binary-tree stack
from itertools import islice
from unittest import TestCase


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        stack = [(root, 1)]
        max_depth = 1
        while stack:
            current_node, current_depth = stack.pop()
            max_depth = max(max_depth, current_depth)
            for node in [current_node.left, current_node.right]:
                if node is None:
                    continue
                stack.append((node, current_depth + 1))

        return max_depth


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
            0,
            self.s.maxDepth(None)
        )

    def test_normal_tree(self):
        self.assertEqual(
            3,
            self.s.maxDepth(self._build_tree([3, 9, 20, None, None, 15, 7]))
        )

    def test_single_node_tree(self):
        self.assertEqual(
            1,
            self.s.maxDepth(self._build_tree([1]))
        )

    def test_two_nodes_tree(self):
        self.assertEqual(
            2,
            self.s.maxDepth(self._build_tree([1, 2]))
        )

    def test_chain_tree(self):
        self.assertEqual(
            3,
            self.s.maxDepth(self._build_tree([1, None, 2, None, None, None, 3]))
        )

    def test_complete_tree(self):
        self.assertEqual(
            3,
            self.s.maxDepth(self._build_tree([1, 2, 3, 4, 5, 6, 7]))
        )

    def test_complete_tree_with_dangling_node(self):
        self.assertEqual(
            4,
            self.s.maxDepth(self._build_tree([1, 2, 3, 4, 5, 6, 7, 8]))
        )
