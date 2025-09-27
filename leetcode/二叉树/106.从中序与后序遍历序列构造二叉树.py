#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/19 22:29
# @Author  : Administrator
# @File    : 106.从中序与后序遍历序列构造二叉树.py
# @Software: PyCharm
"""
中序遍历
左 中 右
后序遍历
左 右 中

"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)

        root_index_in_inorder = inorder.index(root_val)
        # 分割中序遍历左右节点
        left_inorder = inorder[:root_index_in_inorder]
        right_inorder = inorder[root_index_in_inorder + 1:]

        # 分割后序遍历左右节点
        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder): -1]

        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)

        return root



        if not inorder or not postorder:
            return None

        root_val = postorder[-1]
        root = TreeNode(root_val)

        root_index_in_inorder = inorder.index(root_val)

        left_inorder = inorder[:root_index_in_inorder]
        right_inorder = inorder[root_index_in_inorder + 1:]

        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder): -1]

        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)

        return root