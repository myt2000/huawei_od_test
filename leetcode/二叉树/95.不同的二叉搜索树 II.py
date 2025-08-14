#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/13 16:27
# @Author  : Administrator
# @File    : 95.不同的二叉搜索树 II.py
# @Software: PyCharm

"""
二叉搜索树的性质是：左子树的所有节点值都小于根节点的值，右子树的所有节点值都大于根节点的值。
二叉搜索树：
左小于根节点
右大于根节点

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(l, r):
            if l > r:
                return [None]
            ans = []
            for i in range(l, r + 1):
                for x in dfs(l, i - 1):
                    for y in dfs(i + 1, r):
                        root = TreeNode(i)
                        root.left, root.right = x, y
                        ans.append(root)
            return ans
        return dfs(1, n)


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        f=[[[None]for _ in range(n+2)]for _ in range(n+2)]
        for l in range(1,n+1):
            for i in range(1,n+2-l):
                j=i+l-1
                f[i][j]=[]
                for k in range(i,j+1):
                    for left in f[i][k-1]:
                        for right in f[k+1][j]:
                            f[i][j].append(TreeNode(k,left,right))
        return f[1][n]
"""


from idlelib.tree import TreeNode
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        return self.generate_trees(1, n)

    def generate_trees(self, start, end):
        if start > end:
            return [None]

        all_trees = []
        print("all_trees = []")
        for i in range(start, end + 1):
            # 左子树 start 到 i - 1 [start, i-1]
            left_trees = self.generate_trees(start, i-1)
            # 右子树 i 到 end - 1  [i+1, end]
            right_trees = self.generate_trees(i+1, end)
            # 这样划分区间天然保证了左子树的所有节点值都小于 i，右子树的所有节点值都大于 i，无需显式比较。

            for l in left_trees:
                for r in right_trees:
                    current_tree = TreeNode(i)
                    current_tree.left = l
                    current_tree.right = r
                    all_trees.append(current_tree)
                    print(current_tree.val)
        return all_trees




if __name__ == '__main__':
    s = Solution()
    result = s.generateTrees(3)
    print([i.val for i in result])
    print(result)
# [1, 1, 2, 3, 3]
# [<__main__.TreeNode object at 0x000001C9ED0236F0>, <__main__.TreeNode object at 0x000001C9EDF34290>, <__main__.TreeNode object at 0x000001C9ECF69350>, <__main__.TreeNode object at 0x000001C9ED0074D0>, <__main__.TreeNode object at 0x000001C9EDF220D0>]
# 这道题只需要给