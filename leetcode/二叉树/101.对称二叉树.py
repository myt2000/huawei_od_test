#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/14 22:38
# @Author  : Administrator
# @File    : 101.对称二叉树.py
# @Software: PyCharm
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.check_symmetry(root.left, root.right)

    def check_symmetry(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.check_symmetry(p.left, q.right) and self.check_symmetry(p.right, q.left)