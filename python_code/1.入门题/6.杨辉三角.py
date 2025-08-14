#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/2 10:29
# @Author  : Administrator
# @File    : 6.杨辉三角.py
# @Software: PyCharm
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        # if numRows == 0:
        #     return []
        # triangle = [[1]]
        # for row in range(1, numRows):
        #     current_row = [1]
        #     for col in range(1, row):
        #         current_row.append(triangle[row - 1][col - 1] + triangle[row - 1][col])
        #     current_row.append(1)
        #     triangle.append(current_row)
        # return triangle
        C = [[1] * (i + 1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
        return C

if __name__ == '__main__':
    solution = Solution()
    print(solution.generate(5))