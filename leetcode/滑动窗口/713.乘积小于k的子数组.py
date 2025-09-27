#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/20 20:36
# @Author  : Administrator
# @File    : 713.乘积小于k的子数组.py
# @Software: PyCharm
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        ans = 0
        left = 0
        s = 1
        for right, x in enumerate(nums):
            s *= x
            while s >= k:
                s /= nums[left]
                left += 1
            ans += right - left + 1
        return ans

if __name__ == '__main__':
    s = Solution()
    nums = [10,5,2,6]
    k = 100
    print(s.numSubarrayProductLessThanK(nums, k))