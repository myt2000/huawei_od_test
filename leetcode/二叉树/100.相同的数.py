#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/14 21:02
# @Author  : Administrator
# @File    : 100.相同的数.py
# @Software: PyCharm


"""

迭代的方法：
python
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        while stack:
            node_p, node_q = stack.pop()
            if not node_p and not node_q:
                continue
            if not node_p or not node_q:
                return False
            if node_p.val != node_q.val:
                return False
            stack.append((node_p.right, node_q.right))
            stack.append((node_p.left, node_q.left))
        return True


"""
from collections import deque
from typing import Optional, List




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 我自己的思路是中序遍历，没想到根本用不到啊，判断节点就可以，然后结尾反复递归，或者循环也可以实现
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 如果两节点都为空，返回 true；
        if not p and not q:
            return True
        # 如果一个为空另一个不为空，返回 false。
        if not p or not q:
            return False
        # 如果节点值不同，返回 false。
        if p.val != q.val:
            return False
        # 递归比较左子树和右子树，只有都相同才返回 true。
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def buildTree(nums: List[int]) -> Optional[TreeNode]:
    if not len(nums):
        return None
    node_list = deque(nums)
    # 创建根节点
    root = TreeNode(node_list.popleft())
    queue = deque([root])
    # 循环对垒，直到队列为空或者数组为空
    while len(queue) and len(node_list):
        node = queue.popleft()
        if len(node_list):
            value = node_list.popleft()
            if value is not None:
                node.left = TreeNode(value)
                # 左节点放入queue
                queue.append(node.left)
        if len(node_list):
            value = node_list.popleft()
            if value is not None:
                node.right = TreeNode(value)
                # 右节点放入queue
                queue.append(node.right)
    return root

if __name__ == '__main__':
    p = [1,2,1]
    q = [1,1,2]
    root1 = buildTree(p)
    root2 = buildTree(q)
    print(Solution().isSameTree(root1, root2))