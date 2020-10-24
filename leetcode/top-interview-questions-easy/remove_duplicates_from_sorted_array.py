# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/
from typing import List
from unittest import TestCase


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0
        j = 1
        while j < len(nums):
            if nums[j] == nums[i]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1

        del nums[i + 1:]
        return i + 1


class Test(TestCase):
    def setUp(self):
        self.s = Solution()

    def test_removes_duplicate(self):
        nums = [1, 2, 3, 4, 4]
        n = self.s.removeDuplicates(nums)
        self.assertEqual(4, n)
        self.assertListEqual([1, 2, 3, 4], nums)

    def test_remove_results_to_one_element(self):
        nums = [1, 1, 1]
        n = self.s.removeDuplicates(nums)
        self.assertEqual(1, n)
        self.assertListEqual([1], nums)

    def test_removes_multiple_duplicates(self):
        nums = [1, 2, 2, 3, 4, 4]
        n = self.s.removeDuplicates(nums)
        self.assertEqual(4, n)
        self.assertListEqual([1, 2, 3, 4], nums)

    def test_doesnt_remove_duplicate_if_there_are_no_any(self):
        nums = [1, 2, 3, 4, 5]
        n = self.s.removeDuplicates(nums)
        self.assertEqual(5, n)
        self.assertListEqual([1, 2, 3, 4, 5], nums)

    def test_works_with_empty_list(self):
        nums = []
        n = self.s.removeDuplicates(nums)
        self.assertEqual(0, n)
        self.assertListEqual([], nums)

    def test_works_with_large_list_without_duplicates(self):
        nums = list(range(10**6))
        n = self.s.removeDuplicates(nums)
        self.assertEqual(10**6, n)
        self.assertListEqual(list(range(10**6)), nums)

    def test_works_with_large_list_with_duplicates(self):
        nums = [x // 2 for x in range(10**6)]
        n = self.s.removeDuplicates(nums)
        self.assertEqual(10**6 // 2, n)
        self.assertListEqual(list(range(10**6 // 2)), nums)