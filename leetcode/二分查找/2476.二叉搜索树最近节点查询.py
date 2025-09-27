#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/20 9:38
# @Author  : Administrator
# @File    : 2476.二叉搜索树最近节点查询.py
# @Software: PyCharm
"""
平衡二叉树是二叉搜索树的一种优化形式。
所有的平衡二叉树首先都是一棵二叉搜索树，
但并非所有的二叉搜索树都是平衡的。
平衡二叉树通过牺牲一定的插入/删除效率（用于维护平衡），
换取了稳定的、最坏情况下的高效查找性能。

"""
from bisect import bisect_left, bisect
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
#         nums = []
#         # 二叉搜索树中序遍历得到一个有序数组
#         def dfs(node):
#             if node is None:
#                 return
#             dfs(node.left)
#             nums.append(node.val)
#             dfs(node.right)
#         dfs(root)
#         # 对有序数组进行二分查找
#         n = len(nums)
#         # 结果
#         result = []
#         for q in queries:
#             mini = -1
#             maxi = -1
#             # 寻找小于等于q的数
#             left, right = 0, n-1
#             while left <= right:
#                 mid = (left + right) // 2
#                 if nums[mid] <= q:
#                     mini = nums[mid]
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#
#             low, high = 0, n-1
#             while low <= high:
#                 mid = (low + high) // 2
#                 if nums[mid] >= q:
#                     maxi = nums[mid]
#                     high = mid - 1
#                 else:
#                     low = mid + 1
#             result.append([mini, maxi])
#         return result


class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        if not root:
            return []

        a = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            dfs(node.left)
            a.append(node.val)
            dfs(node.right)

        dfs(root)

        n = len(a)
        ans = []

        for q in queries:
            j = bisect_left(a, q)

            # 处理maxi (大于等于q的最小值)
            maxi = a[j] if j < n else -1

            # 处理mini (小于等于q的最大值)
            if j < n and a[j] == q:
                mini = q
            else:
                mini = a[j - 1] if j > 0 else -1

            ans.append([mini, maxi])

        return ans

