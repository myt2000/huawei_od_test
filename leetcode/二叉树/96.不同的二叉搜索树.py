#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/13 20:30
# @Author  : Administrator
# @File    : 96.不同的二叉搜索树.py
# @Software: PyCharm

"""
要计算由 n 个节点组成的不同的二叉搜索树（BST）的数量，我们可以利用动态规划来解决这个问题。这个问题实际上是计算卡塔兰数（Catalan numbers）的一个经典应用。
态规划：我们可以使用动态规划来计算卡塔兰数。初始化一个数组 dp，其中 dp[i] 表示 i 个节点可以组成的BST的数量。然后，通过递推关系逐步计算 dp[n]。


这个跟卡特兰数有关，没有学过卡特兰数
"""

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.numTrees(10))