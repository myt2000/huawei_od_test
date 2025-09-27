#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/20 14:48
# @Author  : Administrator
# @File    : 1.两数之和.py
# @Software: PyCharm
from typing import List
"""
两数之和

这个不是有序数组，不能用双指针
"""
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         left, right = 0, len(nums) - 1
#         while left < right:
#             if nums[left] + nums[right] == target:
#                 return [left, right]
#             elif nums[left] + nums[right] < target:
#                 left += 1
#             else:
#                 right -= 1
#         return []

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num] , i ]
            dic[num] = i

if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    s = Solution()
    print(s.twoSum(nums, target))