#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/19 22:58
# @Author  : Administrator
# @File    : 108.将有序数组转换为二叉搜索树.py
# @Software: PyCharm
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        n = len(nums) // 2
        root = TreeNode(nums[0])
        left = self.sortedArrayToBST(nums[:n])
        right = self.sortedArrayToBST(nums[n+1:])
        return root