#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/20 22:01
# @Author  : Administrator
# @File    : 162.寻找峰值.py
# @Software: PyCharm
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # [0, n-2]
        # (-1, n-1)
        left = -1
        right = len(nums) -1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid
        return right
