#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/19 21:25
# @Author  : Administrator
# @File    : 105.从前序与中序遍历序列构造二叉树.py
# @Software: PyCharm

"""
前序遍历
中 左 右
中序遍历
左 中 右

如何构建二叉树呢？
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # 前序遍历第一个节点是根节点
        root_val = preorder[0]
        root = TreeNode(root_val)
        # 确定中序遍历中根节点的位置
        root_index_in_inorder = inorder.index(root_val)
        # 中序遍历拆分
        left_inorder = inorder[:root_index_in_inorder]
        right_inorder = inorder[root_index_in_inorder + 1:]
        # 前序遍历拆分
        left_preorder = preorder[1:1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder):]

        # 赋值左右节点
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root
