#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/20 12:05
# @Author  : Administrator
# @File    : 34.在排序数组中查找元素的第一个和最后一个.py
# @Software: PyCharm
from typing import List





from bisect import bisect_left, bisect_right


# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         if not nums:
#             return [-1, -1]
#
#         # 查找第一个大于等于target的位置
#         left_index = bisect_left(nums, target)
#
#         # 查找第一个大于target的位置
#         right_index = bisect_right(nums, target) - 1
#
#         # 检查找到的位置是否有效
#         if left_index < len(nums) and nums[left_index] == target:
#             return [left_index, right_index]
#         else:
#             return [-1, -1]

# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         def find_first(nums, target):
#             left, right = 0, len(nums) - 1
#             first = -1
#             while left <= right:
#                 mid = (left +right) // 2
#                 if nums[mid] == target:
#                     first = mid
#                     right = mid - 1   # 继续在左半部分查找
#                 elif nums[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             return first
#
#         def find_last(nums, target):
#             left, right = 0, len(nums) - 1
#             last = -1
#             while left <= right:
#                 mid = (left + right) // 2
#                 if nums[mid] == target:
#                     last = mid
#                     left = mid + 1
#                 elif nums[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             return last
#
#         if not nums:
#             return [-1, -1]
#         first = find_first(nums, target)
#         last = find_last(nums, target)
#         return [first, last]


def lower_bound(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1    # 闭区间 (left, right)
    while left <= right:  # 区间不为空
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1   # [mid+1, right]
        else:
            right = mid - 1   # [left, mid-1]
    return left

def lower_bound2(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)   # 左闭右开区间[left, right)
    while left < right: # 区间不为空
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # [mid+1, right]
        else:
            right = mid     # [left, mid)
    return left     # 也可以返回right

def lower_bound3(nums: List[int], target: int) -> int:
    left = -1
    right = len(nums) # 开区间(left, right)
    while left + 1 < right:  # 区间不为空
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid     # (mid, right)
        else:
            right = mid     # (left, mid)
    return right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = lower_bound(nums, target+1) - 1
        return [start, end]


if __name__ == '__main__':
    nums = [5,7,7,8,8,10]
    target = 8
    s = Solution()
    r = s.searchRange(nums, target)
    print(r)