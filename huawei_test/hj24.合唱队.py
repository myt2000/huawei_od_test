#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/6 17:35
# @Author  : Administrator
# @File    : hj24.合唱队.py
# @Software: PyCharm
"""
描述：
音乐课上，老师将n为同学排成一排。 老师希望在不改变同学相对位置的前提下，从队伍中选出最少数量的同学，使得剩下的同学排成合唱队形。

记合唱队形中一共有k位同学，记编号1,2，..., k , 第i个人的身高为hi 。 要求：存在一位同学编号为i(1<i<k), 使得h1, h2, ..., hi-1严格递增，且hi+1, hi+2, ..., hk严格递减；
跟具体地，合唱队形呈 h1 < h2 < ... <hi-1 < hi 、 hi > hi+1 > ... >hk

你能帮助老师计算，最少需要出列多少位同学， 才能使得剩下的同学排成合唱队形？

输入
8
186 186 150 200 160 130 197 200

输出：
4

在这个样例中，有且仅有两种出列方式，剩下的同学分别为 {186,200,160,130} 和 {150,200,160,130} 。
"""

n = int(input())
heights = list(map(int, input().split()))

if n <= 2:
    print(0)
else:
    left = [1] * n
    for i in range(n):
        for j in range(i):
            if heights[j] < heights[i]:
                left[i] = max(left[i], left[j] + 1)

    right = [1] * n
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if heights[j] < heights[i]:
                right[i] = max(right[i], right[j] + 1)

    max_length = max(left[i] + right[i] - 1 for i in range(n))
    print(n - max_length)