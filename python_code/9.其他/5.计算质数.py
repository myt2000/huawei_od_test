#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/3 16:01
# @Author  : Administrator
# @File    : 5.计算质数.py
# @Software: PyCharm


"""
题目：计算质数

给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。



示例 1：

输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
示例 2：

输入：n = 0
输出：0
示例 3：

输入：n = 1
输出：0

"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        count_list = [True] * n
        count_list[0] = count_list[1] = False
        for i in range(2, int(n ** 0.5)+1):
            if count_list[i]:
                for j in range(i*i, n, i):
                    count_list[j] = False
        return sum(count_list)


if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(10))

