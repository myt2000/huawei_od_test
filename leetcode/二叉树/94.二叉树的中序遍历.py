#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/13 15:16
# @Author  : Administrator
# @File    : 94.二叉树的中序遍历.py
# @Software: PyCharm
from idlelib.tree import TreeNode
from typing import Optional, List


"""
前序遍历  中 左 右
中序遍历  左 中 右
后序遍历  右 中 左

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []

        def dfs(node: Optional[TreeNode]):
            if node.left:
                dfs(node.left)
            result.append(node.val)
            if node.right:
                dfs(node.right)

        dfs(root)
        return result
