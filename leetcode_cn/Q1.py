import unittest
from typing import List


class Solution:
    """
    给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
    你可以按任意顺序返回答案。

    ISSUE: https://github.com/mixhowie/algorithm/issues/1
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for index in range(len(nums)):
            num = nums[index]
            if num in cache:
                return [index, cache[num]]
            cache[target - num] = index


class Test(unittest.TestCase):
    def test(self):
        cases = [
            (9, [2, 7, 11, 15], [0, 1]),
            (6, [3, 2, 4], [1, 2]),
            (6, [3, 3], [0, 1]),
        ]
        solution = Solution()
        for (target, nums, answer) in cases:
            result = solution.twoSum(nums, target)
            self.assertListEqual(sorted(result), sorted(answer))
