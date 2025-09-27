#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/20 14:22
# @Author  : Administrator
# @File    : 15.三数之和.py
# @Software: PyCharm

"""
三数之和
这个题也是二分查找


二分查找需要在有序数组查找，所以需要对数组重新排序，这样可以判断在哪一部分

问题分析：需要找到所有不重复的三元组，使得三个数的和为0。

关键观察：

先对数组排序，这样可以方便地跳过重复元素

固定一个数，然后使用双指针在剩余部分寻找另外两个数

注意去重处理，避免重复的三元组

算法步骤：

对数组进行排序

遍历数组，对于每个元素nums[i]：

如果nums[i] > 0，直接结束（因为数组已排序，后面的数都更大）

跳过重复的nums[i]

使用双指针在i+1到末尾的范围内寻找另外两个数


三个步骤：排序，去重，双指针
"""
from collections.abc import range_iterator
from typing import List


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         result = []
#         n = len(nums)
#         # 因为是三个数字，可以少循环两次，实际还是要遍历一遍
#         for i in range(n - 2):
#             # 跳过重复的起始元素
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             # # 如果当前数大于0，后面的数都更大，不可能和为0
#             if nums[i] > 0:
#                 break
#             left = i + 1
#             right = n - 1
#             while left < right:
#                 total = nums[i] + nums[left] + nums[right]
#                 if total == 0:
#                     result.append([nums[i], nums[left], nums[right]])
#                     # 跳过重复的left和right
#                     while left < right and nums[left] == nums[left + 1]:
#                         left += 1
#                     while left < right and nums[right] == nums[right - 1]:
#                         right -= 1
#                     left += 1
#                     right -= 1
#                 elif total < 0:
#                     left += 1
#                 else:
#                     right -= 1
#             return result

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):
            # 跳过重复的起始元素
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 如果当前数大于0，后面的数都更大，不可能和为0
            if nums[i] > 0:
                break

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # 跳过重复的left和right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result

class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result



if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))