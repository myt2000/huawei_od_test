#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/3 10:50
# @Author  : Administrator
# @File    : 4.腐烂的橘子.py
# @Software: PyCharm
"""
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4
示例 2：

输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。
示例 3：

输入：grid = [[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
"""
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        bad = []
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    bad.append((i, j))
        ans = 0
        while bad and fresh > 0:
            ans += 1
            tmp = []
            for (i, j) in bad:
                for i0, j0 in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                    if 0 <= i0 <= m - 1 and 0 <= j0 <= n - 1 and grid[i0][j0] == 1:
                        grid[i0][j0] = 2
                        fresh -= 1
                        tmp.append((i0, j0))
            bad = tmp
        return ans if fresh == 0 else -1

        # minutes = -1
        # m = len(grid)
        # n = len(grid[0])
        # broken_orange = deque([])
        # for row in range(m):
        #     for col in range(len(grid[row])):
        #         if grid[row][col] == 2:
        #             broken_orange.append((row, col))
        # total = sum([grid[row][col] for row in range(m) for col in range(n)])
        # if total == 0:
        #     return 0
        # while broken_orange:
        #     for _ in range(len(broken_orange)):
        #         row, col = broken_orange.popleft()
        #         # 上面
        #         if row-1 >= 0 and grid[row-1][col] == 1:
        #             grid[row - 1][col] = 2
        #             broken_orange.append((row - 1, col))
        #         # 下面
        #         if row+1 < m and grid[row+1][col] == 1:
        #             grid[row + 1][col] = 2
        #             broken_orange.append((row + 1, col))
        #         # 左面
        #         if col-1 >= 0 and grid[row][col-1] == 1:
        #             grid[row][col - 1] = 2
        #             broken_orange.append((row, col - 1))
        #         # 右面
        #         if col+1 < len(grid[row]) and grid[row][col+1] == 1:
        #             grid[row][col + 1] = 2
        #             broken_orange.append((row, col + 1))
        #     minutes += 1
        # for row in range(m):
        #     for col in range(n):
        #         if grid[row][col] == 1:
        #             minutes = -1
        # return minutes

if __name__ == '__main__':
    # grid = [[2,1,1],[1,1,0],[0,1,1]]
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    print(Solution().orangesRotting(grid))
    # grid = [[2,1,1],[0,1,1],[1,0,1]]
    # print(Solution().orangesRotting(grid))
    # grid = [[0,2]]
    # print(Solution().orangesRotting(grid))
    # grid = [[0]]
    # grid = [[0,0,0,0]]