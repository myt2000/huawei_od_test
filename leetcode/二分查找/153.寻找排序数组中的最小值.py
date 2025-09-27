#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/20 22:30
# @Author  : Administrator
# @File    : 153.寻找排序数组中的最小值.py
# @Software: PyCharm
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = -1
        right = len(nums) - 1
        while left+1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid
            else:
                left = mid
        return nums[right]