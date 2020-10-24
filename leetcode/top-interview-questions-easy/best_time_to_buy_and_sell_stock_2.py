# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/564/
from typing import List
from unittest import TestCase


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i - 1])

        return profit


class Test(TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_constant_stock_price(self):
        self.assertEqual(
            0,
            self.s.maxProfit([1, 1, 1, 1, 1])
        )

    def test_stock_price_constantly_drops(self):
        self.assertEqual(
            0,
            self.s.maxProfit([5, 4, 3, 2, 1])
        )

    def test_stock_price_constantly_rises(self):
        self.assertEqual(
            4,
            self.s.maxProfit([1, 2, 3, 4, 5])
        )

    def test_stock_price_fluctuates(self):
        self.assertEqual(
            3 + 5,
            self.s.maxProfit([1, 4, 2, 7, 3])
        )

    def test_1_day_data(self):
        self.assertEqual(
            0,
            self.s.maxProfit([1])
        )
