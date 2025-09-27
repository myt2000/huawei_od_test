#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/14 23:07
# @Author  : Administrator
# @File    : 102.二叉树的层序遍历.py
# @Software: PyCharm
from typing import Optional, List

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque()
        queue.append(root)
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
