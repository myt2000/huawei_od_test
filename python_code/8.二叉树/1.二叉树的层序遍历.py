#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/2 17:23
# @Author  : Administrator
# @File    : 1.二叉树的层序遍历.py
# @Software: PyCharm

"""
原来的题目叫做：
*leetcode 剑指offer 32 — II.从上到下打印二叉树 II


给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。



示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
示例 2：

输入：root = [1]
输出：[[1]]
示例 3：

输入：root = []
输出：[]

解题思路
层序遍历通常使用队列（Queue）来实现。具体步骤如下：

1. 初始化队列：将根节点放入队列。

2. 循环处理队列：每次处理一层的所有节点。

3. 遍历当前层的节点，将它们的值存入当前层的列表。

4. 将每个节点的左右子节点加入队列，作为下一层的节点。

返回结果：将每一层的列表存入最终结果中。

具体步骤
1. 检查根节点是否为空：如果为空，直接返回空列表。

初始化队列和结果列表：

队列 queue：用于存储待处理的节点，初始时包含根节点。

结果 result：用于存储每一层的节点值列表。

层序遍历：

1. 当队列不为空时，循环处理：

获取当前层的节点数量 level_size（即队列的长度）。

初始化当前层的列表 current_level。

遍历 level_size 次，每次从队列中取出一个节点：

将节点的值加入 current_level。

如果节点有左子节点，将左子节点加入队列。

如果节点有右子节点，将右子节点加入队列。

将 current_level 加入 result。

返回结果。


def levelOrder(root):
    result = []

    def dfs(node, level):
        if not node:
            return
        if len(result) == level:
            result.append([])
        result[level].append(node.val)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)
        return result

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().levelOrder(root))

