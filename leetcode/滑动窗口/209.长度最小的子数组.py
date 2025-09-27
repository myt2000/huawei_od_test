#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/20 20:15
# @Author  : Administrator
# @File    : 209.长度最小的子数组.py
# @Software: PyCharm
from typing import List

"""
固定两个端点，比如左端点和右端点
先移动右端点，求数组元素的累加和s，如果大于target
就移动左端点，累加和s减去当前左端点对应的nums[left]
求最小值， right - left + 1  这里+1表示left, right指向同一个数组元素，这时候就是1
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        s = 0
        left = 0
        for right, x in enumerate(nums):
            s += x
            while s >= target:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1
        return ans if ans<=n else 0

if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2, 3, 1, 4, 5]))