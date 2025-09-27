#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/19 20:16
# @Author  : Administrator
# @File    : 2348.全0子数组的数目.py
# @Software: PyCharm
from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        zero_count = []
        zero_num = 0
        for i in range(n):
            if nums[i] == 0:
                zero_num += 1
                zero_count.append(zero_num)
            else:
                zero_num = 0
        return sum(zero_count)

if __name__ == '__main__':
    s = Solution()
    print(s.zeroFilledSubarray([1,3,0,0,2,0,0,4]))
    print(s.zeroFilledSubarray([0,0,0,2,0,0]))
    print(s.zeroFilledSubarray([2,10,2019]))

