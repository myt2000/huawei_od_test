#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/19 22:46
# @Author  : Administrator
# @File    : 107.二叉树的层序遍历II.py
# @Software: PyCharm
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        result = deque()
        while queue:
            levels = []
            for _ in range(len(queue)):
                node = queue.popleft()
                levels.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.appendleft(levels)
        return list(result)