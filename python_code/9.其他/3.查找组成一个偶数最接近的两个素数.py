#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/3 0:02
# @Author  : Administrator
# @File    : 3.查找组成一个偶数最接近的两个素数.py
# @Software: PyCharm

"""
题目：查找组成一个偶数最接近的两个素数

描述：
对于给定的偶数n, 找出两素素数a, b, 满足：
1. 它们的和等于n;
2. 它们的差值绝对值最小

我们可以保证， a,b 一定存在，从小到大输出满足条件的素数对。

输入：
20
输出
7
13

输入：
4
输出：
2
2

for j in range(i * i, max_num + 1, i):
为什么是i*i开始，is_prime[j] = False
i	当前质数	标记的合数 (j = i * i, i * (i+1), ...)	is_prime 更新
2	2	4, 6, 8, 10, 12, 14, 16, 18, 20	这些数设为 False
3	3	9, 12, 15, 18	这些数设为 False
4	4（已被标记为 False，跳过）	无	无
5	5	25（超过 20，不处理）	无

"""

def sieve(max_num):
    """
    这是一个经典的 埃拉托斯特尼筛法（Sieve of Eratosthenes），用于生成一个布尔数组 is_prime，其中 is_prime[i] 为 True 表示 i 是质数，否则 i 不是质数。
    """
    # is_prime 是一个长度为 max_num + 1 的数组，初始时所有元素设为 True（假设所有数都是质数）。
    is_prime = [True] * (max_num + 1)
    # is_prime[0] = is_prime[1] = False（因为 0 和 1 不是质数）。
    is_prime[0] = is_prime[1] = False
    # 从 2 开始遍历到 sqrt(max_num)（因为如果 n 是合数，它至少有一个因数小于等于 sqrt(n)）。
    for i in range(2, int(max_num ** 0.5) + 1):
        # 如果 i 是质数（is_prime[i] 为 True），则将所有 i 的倍数（从 i * i 开始）标记为非质数（is_prime[j] = False）。
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
    # 终 is_prime 数组会标记出所有小于等于 max_num 的质数。
    return is_prime

def find_prime_pair(n):
    """
    这个函数的目的是找到两个质数 a 和 b，使得 a + b = n，并且 a 是满足条件的最大可能较小质数。
    :param n:
    :return:
    """
    # 调用 sieve(n) 生成一个布尔数组 is_prime，用于快速判断某个数是否是质数。
    is_prime = sieve(n)
    # 初始化 a 为 n // 2（即从 n 的一半开始向下搜索）。
    a = n // 2
    while a >= 2:
        # 检查 a 和 n - a 是否都是质数：
        if is_prime[a] and is_prime[n - a]:
            return a, n - a
        # 如果不是，a 减 1，继续检查。
        a -= 1
    return None

n = int(input())
a, b = find_prime_pair(n)
print(a)
print(b)