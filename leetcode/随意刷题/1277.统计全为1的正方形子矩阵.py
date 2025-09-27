#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/20 9:42
# @Author  : Administrator
# @File    : 1277.统计全为1的正方形子矩阵.py
# @Software: PyCharm
from typing import List


# class Solution:
#     def countSquares(self, matrix: List[List[int]]) -> int:
#         m = len(matrix)
#         n = len(matrix[0])
#         f = [[0] * (n+1) for _ in range(m+1)]
#         for i, row in enumerate(matrix):
#             for j, val in enumerate(row):
#                 if val:
#                     f[i+1][j+1] = min(f[i][j], f[i][j+1], f[i+1][j]) +1
#         return sum(map(sum, f))

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        total = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    total += dp[i][j]
        return total


if __name__ == '__main__':
    s = Solution()

    print(s.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))