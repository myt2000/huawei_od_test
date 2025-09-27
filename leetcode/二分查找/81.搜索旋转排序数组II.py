#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/20 13:57
# @Author  : Administrator
# @File    : 81.搜索旋转排序数组II.py
# @Software: PyCharm
from typing import List

"""
问题分析：旋转数组中可能包含重复元素，需要判断目标值是否存在。

关键挑战：当nums[left] == nums[mid] == nums[right]时，无法确定哪一半是有序的。

解决方案：

在标准二分查找的基础上，处理重复元素的情况

当无法判断有序部分时，通过缩小搜索范围来继续查找

算法步骤：

使用二分查找

当nums[left] == nums[mid] == nums[right]时，无法判断有序部分，只能缩小范围

否则，按照标准旋转数组搜索的方法进行


判断有序部分：

左半部分有序 (nums[left] <= nums[mid])：

检查目标值是否在有序范围内 [nums[left], nums[mid])

如果是，搜索左半部分；否则搜索右半部分

右半部分有序 (nums[left] > nums[mid])：

检查目标值是否在有序范围内 (nums[mid], nums[right]]

如果是，搜索右半部分；否则搜索左半部分
"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # 左半部分有序
            elif nums[left] < target:
                if nums[left] <= target <= nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
                # 右半部分有序
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


if __name__ == '__main__':
    nums = [1,0,1,1,1]
    target = 0
    s = Solution()
    r = s.search(nums, target)
    print(r)

