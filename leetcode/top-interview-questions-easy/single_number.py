# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
from functools import reduce
from typing import List
from unittest import TestCase


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda a, b: a ^ b, nums)


class Test(TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_only_one_element(self):
        n = self.s.singleNumber([1])
        self.assertEqual(1, n)

    def test_sroted_array(self):
        n = self.s.singleNumber([1, 1, 2, 3, 3])
        self.assertEqual(2, n)

    def test_random_order(self):
        n = self.s.singleNumber([1, 3, 3, 2, 1])
        self.assertEqual(2, n)
