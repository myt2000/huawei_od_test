#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/20 11:40
# @Author  : Administrator
# @File    : 33.搜索旋转排序数组.py
# @Software: PyCharm
from typing import List


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if target not in nums:
#             return -1
#         target_index = nums.index(target)
#         return target_index

# 二分查找的方式解决问题
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            #  # 左半部分有序
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 右半部分有序
            else:
                # 目标值在右半部分的有序范围内
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def is_blue(i:int) -> bool:
            end = nums[-1]
            if nums[i] > end:
                return target > end and nums[i] >= target
            else:
                return target > end or nums[i] >= target

        left = -1
        right = len(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if is_blue(mid):
                right = mid
            else:
                left = mid
        if right == len(nums) or nums[right] != target:
            return -1
        return right



