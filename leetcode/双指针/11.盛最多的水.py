#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/20 17:09
# @Author  : Administrator
# @File    : 11.盛最多的水.py
# @Software: PyCharm

"""
双指针
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n  = len(height)
        area = 0
        left, right = 0, n - 1
        while left < right:
            area = max(area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area

if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))