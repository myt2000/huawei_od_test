#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/13 21:12
# @Author  : Administrator
# @File    : 98.验证二叉搜索树.py
# @Software: PyCharm

"""
中序遍历
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, prev = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归验证
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            val = node.val
            # 中间节点大于左子树，小于右子树
            if val <= lower or val >= upper:
                return False
            return helper(node.left, lower, val) and helper(node.right, val, upper)
        return helper(root)

if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(5)


    print(Solution().isValidBST(root))
