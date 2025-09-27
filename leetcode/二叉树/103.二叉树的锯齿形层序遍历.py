#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/16 18:25
# @Author  : Administrator
# @File    : 103.二叉树的锯齿形层序遍历.py
# @Software: PyCharm

"""

"""
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])
        level = 0
        while queue:
            levels = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if level % 2 == 0:
                    levels.append(node.val)
                else:
                    levels.appendleft(node.val)
                if node.left:
                     queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(list(levels))
            level += 1
        return result