#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/20 12:41
# @Author  : Administrator
# @File    : 74.搜索二维矩阵.py
# @Software: PyCharm
from typing import List


# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m,n = len(matrix), len(matrix[0])
#         for row in matrix:
#             left = 0
#             right = n-1
#             if row[left] <= target <= row[right]:
#                 while left <= right:
#                     mid = (left + right) // 2
#                     if row[mid] == target:
#                         return True
#                     elif target <= row[mid]:
#                         left = mid + 1
#                     else:
#                         right = mid - 1
#         return False

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         if not matrix or not matrix[0]:
#             return False
#
#         m, n = len(matrix), len(matrix[0])
#         left, right = 0, m * n - 1
#
#         while left <= right:
#             # 二维数组转为一维数组的中心位置
#             mid = (left + right) // 2
#             # 将一维索引转换为二维坐标
#             row = mid // n
#             col = mid % n
#             mid_value = matrix[row][col]
#
#             if mid_value == target:
#                 return True
#             elif mid_value < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return False


# 另一种实现方式（先确定行，再在行内查找）
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])

        # 先确定目标可能在哪一行
        top, bottom = 0, m - 1
        target_row = -1

        while top <= bottom:
            mid_row = (top + bottom) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                target_row = mid_row
                break
            elif matrix[mid_row][0] > target:
                bottom = mid_row - 1
            else:
                top = mid_row + 1

        if target_row == -1:
            return False

        # 在目标行内进行二分查找
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False