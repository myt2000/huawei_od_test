#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/14 21:49
# @Author  : Administrator
# @File    : 1780.判断一个数字是否可以表示成三的幂的和.py
# @Software: PyCharm



"""
要判断一个整数 n 是否可以表示为若干个不同的三的幂之和，我们可以将这个问题转化为三进制数的问题。具体来说，如果一个数的三进制表示中只包含 0 和 1，那么这个数就可以表示为不同的三的幂之和。如果三进制表示中包含 2，则不能这样表示。

示例说明
示例 1：n = 12

12 的三进制表示为 110（1*3² + 1*3¹ + 0*3⁰），没有 2，返回 true。

示例 2：n = 91

91 的三进制表示为 10101（1*3⁴ + 0*3³ + 1*3² + 0*3¹ + 1*3⁰），没有 2，返回 true。

示例 3：n = 21

21 的三进制表示为 210（2*3² + 1*3¹ + 0*3⁰），包含 2，返回 false。
"""


# class Solution:
#     def checkPowersOfThree(self, n: int) -> bool:
#         while n > 0:
#             remainder = n % 3
#             if remainder == 2:
#                 return False
#             n = n // 3
#         return True

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        for i in range(16,-1,-1):
            if ( n >= 3 ** i):
                n -= 3 ** i
                print(n)
        return (n == 0)