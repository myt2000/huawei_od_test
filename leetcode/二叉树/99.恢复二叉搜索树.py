#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/13 22:03
# @Author  : Administrator
# @File    : 99.恢复二叉搜索树.py
# @Software: PyCharm

"""
要恢复一棵二叉搜索树（BST）中被错误交换的两个节点，我们可以利用BST的中序遍历性质。BST的中序遍历结果应该是一个严格递增的序列。如果恰好有两个节点被错误交换，那么在中序遍历序列中会出现两个位置不满足递增关系。我们需要找到这两个节点并交换它们的值。


中序遍历：通过中序遍历BST，得到节点值，是必然按照顺序排列的

识别错误节点：

第一个错误节点（first）：第一个比其后节点大的节点（即前一个节点 prev 的值大于当前节点 node 的值）。

第二个错误节点（second）：最后一个比其前节点小的节点（即后续遍历中再次出现 prev.val > node.val 时的 node）。

交换节点值：找到这两个节点后，交换它们的值即可恢复BST。


这个题的边界，只需要处理两个错误节点，没有所有的错误节点

"""
from typing import Optional, List
from collections import deque





class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # self.first, self.second用于记录需要交换的两个错误节点
        self.first = None # 第一个错误节点
        self.second = None # 第二个错误节点
        self.prev = TreeNode(float('-inf'))  # 初始化最小值用于比较

        def inorder(node):
            if not node:
                return
            inorder(node.left) # 递归遍历左子树
            # 在中序遍历序列中，找到两个不满足递增关系的节点。第一个错误节点是第一个比其后节点大的节点，第二个错误节点是最后一个比其前节点小的节点。
            # 如果 first 未找到且 prev.val >= node.val，说明 prev 是第一个错误节点。
            if not self.first and self.prev.val >= node.val:
                # 第一个节点 变为上一个节点
                self.first = self.prev  # 记录第一个错误节点
            if self.first and self.prev.val >= node.val:
                # 第二个节点变为 当前节点
                self.second = node # 记录第二个错误节点

            self.prev = node  # 更新prev为当前节点
            inorder(node.right) # 递归遍历右子树

        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        return self.first


if __name__ == '__main__':
    root1 = [1,3,None,None,2]
    tree1 = buildTree(root1)
    s = Solution()
    print(s.recoverTree(tree1).val)