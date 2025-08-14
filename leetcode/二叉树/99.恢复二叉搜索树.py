#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/13 22:03
# @Author  : Administrator
# @File    : 99.恢复二叉搜索树.py
# @Software: PyCharm

"""
要恢复一棵二叉搜索树（BST）中被错误交换的两个节点，我们可以利用BST的中序遍历性质。BST的中序遍历结果应该是一个严格递增的序列。如果恰好有两个节点被错误交换，那么在中序遍历序列中会出现两个位置不满足递增关系。我们需要找到这两个节点并交换它们的值。


中序遍历
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # self.first, self.second用于记录需要交换的两个错误节点
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            # 在中序遍历序列中，找到两个不满足递增关系的节点。第一个错误节点是第一个比其后节点大的节点，第二个错误节点是最后一个比其前节点小的节点。
            if not self.first and self.prev.val >= node.val:
                self.first = self.prev
            if self.first and self.prev.val >= node.val:
                self.second = node
            self.prev = node
            inorder(node.right)

        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val


if __name__ == '__main__':
    pass