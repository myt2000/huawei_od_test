#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/2 18:31
# @Author  : Administrator
# @File    : 2.二叉树的锯齿形层序遍历.py
# @Software: PyCharm

"""
给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。



示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：[[3],[20,9],[15,7]]
示例 2：

输入：root = [1]
输出：[[1]]
示例 3：

输入：root = []
输出：[]

def zigzagLevelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True  # 第一层从左到右

    while queue:
        level_size = len(queue)
        current_level = deque()  # 使用双端队列方便左右添加

        for _ in range(level_size):
            node = queue.popleft()

            # 根据方向决定添加到当前层的头部还是尾部
            if left_to_right:
                current_level.append(node.val)
            else:
                current_level.appendleft(node.val)

            # 将子节点加入队列（先左后右）
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(current_level))
        left_to_right = not left_to_right  # 切换方向

    return result
"""
from idlelib.tree import TreeNode
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
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
        odd_stack = [root]  # 奇数层，从左到右
        even_stack = [] # 偶数层，从右到左
        level = 1
        while odd_stack or even_stack:
            current_level = []
            if level % 2 == 1:
                while odd_stack:
                    node = odd_stack.pop()
                    current_level.append(node.val)
                    if node.left:
                        even_stack.append(node.left)
                    if node.right:
                        even_stack.append(node.right)
            else:
                while even_stack:
                    node = even_stack.pop()
                    current_level.append(node.val)
                    if node.right:
                        odd_stack.append(node.right)
                    if node.left:
                        odd_stack.append(node.left)
            result.append(current_level)
            level += 1
        return result


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().zigzagLevelOrder(root))




