#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/2 22:25
# @Author  : Administrator
# @File    : 2.素数伴侣.py
# @Software: PyCharm


"""
题目：素数伴侣
定义两个正整数a和b是“素数伴侣”，当且仅当a+b是一个素数

现在，密码学会邀请你设计一个程序，从给定的n个正整数{a1, a2, ..., an}种，挑选出最多的“素数伴侣”， 你只需要挑选出最多的“素数伴侣”对数。保证n为偶数，一个数字只能用一次

输入：
4
2 5 6 13
输出
2

输入：
4
1 2 2 2
输出
1

"""

import sys
import math

def is_prime(num):
    """
    判断一个数是否为素数。
    :param num:
    :return:
    """
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def hungarian(adj, n, m):
    # 实现匈牙利算法，求解二分图的最大匹配。
    match_to = [-1] * m  # 记录偶数匹配的奇数。
    result = 0

    def bpm(u, seen):
        """
        尝试为当前奇数找到一个未匹配的偶数。
        :param u:
        :param seen:
        :return:
        """
        for v in range(m):
            if adj[u][v] and not seen[v]:
                seen[v] = True
                if match_to[v] == -1 or bpm(match_to[v], seen):
                    match_to[v] = u
                    return True
        return False

    for u in range(n):
        seen = [False] * m
        if bpm(u, seen):
            result += 1
    return result

def solve():
    # 读取数字个数
    n = int(sys.stdin.readline())
    # 读取数字列表
    nums = list(map(int, sys.stdin.readline().split()))
    # 划分奇数和偶数
    odds = []   # 奇数列表
    evens = []  # 偶数列表
    for num in nums:
        if num % 2 == 1:
            odds.append(num)
        else:
            evens.append(num)
    len_odds = len(odds)
    len_evens = len(evens)
    # 构建邻接矩阵 adj，表示奇数和偶数是否可以配对。
    adj = [[False] * len_evens for _ in range(len_odds)]
    for i in range(len_odds):
        for j in range(len_evens):
            if is_prime(odds[i] + evens[j]):
                adj[i][j] = True
    # 调用 hungarian 计算最大匹配数并输出。
    print(hungarian(adj, len_odds, len_evens))

solve()
