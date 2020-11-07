# https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/587/
# array sorted-array merge merge-sort
from typing import List
from unittest import TestCase


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        while i >= 0 or j >= 0:
            if i < 0 or j >= 0 and nums1[i] < nums2[j]:
                nums1[i + j + 1] = nums2[j]
                j -= 1
            else:
                nums1[i + j + 1] = nums1[i]
                i -= 1


class Test(TestCase):
    def setUp(self):
        self.s = Solution()

    def test_both_arrays_are_regular(self):
        nums1 = [1, 3, 5]
        nums2 = [2, 4, 6]
        m = len(nums1)
        n = len(nums2)
        nums1 += [0] * n
        self.s.merge(nums1, m, nums2, n)
        self.assertListEqual(
            nums1,
            [1, 2, 3, 4, 5, 6]
        )

    def test_both_arrays_are_empty(self):
        nums1 = []
        nums2 = []
        m = len(nums1)
        n = len(nums2)
        nums1 += [0] * n
        self.s.merge(nums1, m, nums2, n)
        self.assertListEqual(
            nums1,
            []
        )

    def test_first_array_is_empty(self):
        nums1 = []
        nums2 = [2, 4, 6]
        m = len(nums1)
        n = len(nums2)
        nums1 += [0] * n
        self.s.merge(nums1, m, nums2, n)
        self.assertListEqual(
            nums1,
            [2, 4, 6]
        )

    def test_second_array_is_empty(self):
        nums1 = [1, 3, 5]
        nums2 = []
        m = len(nums1)
        n = len(nums2)
        nums1 += [0] * n
        self.s.merge(nums1, m, nums2, n)
        self.assertListEqual(
            nums1,
            [1, 3, 5]
        )

    def test_first_array_has_one_element(self):
        nums1 = [1]
        nums2 = [2, 4, 6]
        m = len(nums1)
        n = len(nums2)
        nums1 += [0] * n
        self.s.merge(nums1, m, nums2, n)
        self.assertListEqual(
            nums1,
            [1, 2, 4, 6]
        )

    def test_second_array_has_one_element(self):
        nums1 = [1, 3, 5]
        nums2 = [2]
        m = len(nums1)
        n = len(nums2)
        nums1 += [0] * n
        self.s.merge(nums1, m, nums2, n)
        self.assertListEqual(
            nums1,
            [1, 2, 3, 5]
        )

    def test_both_array_non_trivial(self):
        nums1 = [2, 7, 8]
        nums2 = [1, 4, 5, 9, 10]
        m = len(nums1)
        n = len(nums2)
        nums1 += [0] * n
        self.s.merge(nums1, m, nums2, n)
        self.assertListEqual(
            nums1,
            [1, 2, 4, 5, 7, 8, 9, 10]
        )

    def test_with_repeating_elements(self):
        nums1 = [1, 2, 5, 7, 8]
        nums2 = [1, 4, 5, 9, 10]
        m = len(nums1)
        n = len(nums2)
        nums1 += [0] * n
        self.s.merge(nums1, m, nums2, n)
        self.assertListEqual(
            nums1,
            [1, 1, 2, 4, 5, 5, 7, 8, 9, 10]
        )
