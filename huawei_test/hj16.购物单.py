#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/4 22:20
# @Author  : Administrator
# @File    : hj16.购物单.py
# @Software: PyCharm


"""
描述
王强决定把年终奖用于购物，他把想买的物品分为两类：主件与附件。
1. 主件可以没有附件，至多有2个附件。附件不再有属于自己的附件。
2. 若要购买某附件，必须先购买该附件所属的主件，且每件物品只能购买一次。

王强查到了 m 件物品的价格，而他只有n元的预算。为了先购买中药的物品，他给每件物品规定了一个重要度，用整数1~5表示。他希望在不超过预算的前提下，使满意度最大。

满意度定义为所够每件物品价格与重要度乘积之和。具体地说，记第i件物品的价格vi, 重要度为wi; 若共选中k件物品，编号为j1, j2, ..., jk, 则满意度计算为
    ∑vjt * wjt = vj1 * wj1 + vj2 * wjt + ... + vjk * wjk

请帮助王强计算可获得的最大满意度

输入
50 5
20 3 5
20 3 5
10 3 0
10 2 0
10 1 0
输出
130

输入
1000 5
800 2 0
400 5 1
300 5 1
400 3 0
500 2 0
输出
2200


# 1. 要满足预算
# 2. 要满足满意度最大
# 3. 要买附件需要看主件

# 感觉像线性规划


分组：将每个主件及其可能的附件组合作为一个组。对于每个主件，有以下几种选择：

1. 不选该主件。

2. 只选主件。

3. 选主件 + 附件1。

4. 选主件 + 附件2。

4. 选主件 + 附件1 + 附件2。

因此，每个主件组有最多4种选择（如果主件有0、1或2个附件）。

动态规划：

1. 定义 dp[j] 表示预算为 j 时的最大满意度。

2. 对于每个主件组，枚举所有可能的选择组合，然后更新 dp。
"""


n, m = map(int, input().split())
primary = {}
accessory = {}

for i in range(1, m + 1):
    v, w, q = map(int, input().split())
    if q == 0:
        primary[i] = (v, w)
    else:
        if q not in accessory:
            accessory[q] = []
        accessory[q].append((v, w))

dp = [0] * (n + 1)

for p in primary:
    v_p, w_p = primary[p]
    attachments = accessory.get(p, [])
    # 生成所有可能的组合
    combinations = []
    # 1. 不选（不处理）
    # 2. 只选主件
    combinations.append((v_p, w_p * v_p))
    # 3. 主件 + 第一个附件
    if len(attachments) >= 1:
        v_a1, w_a1 = attachments[0]
        combinations.append((v_p + v_a1, w_p * v_p + w_a1 * v_a1))
    # 4. 主件 + 第二个附件
    if len(attachments) >= 2:
        v_a2, w_a2 = attachments[1]
        combinations.append((v_p + v_a2, w_p * v_p + w_a2 * v_a2))
    # 5. 主件 + 两个附件
    if len(attachments) >= 2:
        v_a1, w_a1 = attachments[0]
        v_a2, w_a2 = attachments[1]
        combinations.append((v_p + v_a1 + v_a2, w_p * v_p + w_a1 * v_a1 + w_a2 * v_a2))

    # 更新dp，类似01背包，从后往前
    for j in range(n, -1, -1):
        for v, s in combinations:
            if j >= v:
                dp[j] = max(dp[j], dp[j - v] + s)
# v：当前物品（或组合）的价格。
# s：当前物品（或组合）的满意度（v * w）。
# j - v：如果当前预算为 j，且购买了价格为 v 的物品，那么剩余的预算是 j - v。
# dp[j - v]：在剩余预算 j - v 时，之前能获得的最大满意度。
# dp[j - v] + s：如果购买当前物品（花费 v），则总满意度是之前 j - v 的满意度加上当前物品的满意度 s。
print(max(dp))