# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
# array hash-map
from collections import Counter
from typing import List
from unittest import TestCase


class Solution:
    def _get_counts(self, nums):
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 0
            counts[n] += 1
        return counts

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts1 = self._get_counts(nums1)
        counts2 = self._get_counts(nums2)
        intersection = []
        for k in counts1:
            intersection += [k] * min(counts1[k], counts2.get(k, 0))
        return intersection


class Test(TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_two_empty_arrays(self):
        self.assertEqual(
            Counter(self.s.intersect([], [])),
            Counter()
        )

    def test_first_array_empty(self):
        self.assertEqual(
            Counter(self.s.intersect([1, 2, 3, 4], [])),
            Counter()
        )

    def test_second_array_empty(self):
        self.assertEqual(
            Counter(self.s.intersect([], [1, 2, 3, 4])),
            Counter()
        )

    def test_no_intersection(self):
        self.assertEqual(
            Counter(self.s.intersect([1, 2, 3], [7, 6, 5])),
            Counter()
        )

    def test_intersection_of_unique_elements(self):
        self.assertEqual(
            Counter(self.s.intersect([1, 2, 3, 4, 5], [5, 1, 3, 6])),
            Counter([1, 3, 5])
        )

    def test_intersection_with_repeating_elements(self):
        self.assertEqual(
            Counter(self.s.intersect([1, 1, 2, 2, 3, 4, 5, 5], [5, 1, 1, 3, 6])),
            Counter([1, 1, 3, 5])
        )
