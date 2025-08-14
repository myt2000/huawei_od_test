#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/3 23:28
# @Author  : Administrator
# @File    : hj6.质数因子.py
# @Software: PyCharm

"""
描述
对于给定的整数 n，从小到大依次输出它的全部质因子。即找到这样的质数 p1, p2, ... , pk, 使得 n = p1 * p2 * ... * pk.

输入：
180
输出：
2 2 3 3 5

输入
47
输出
47

思路：
1. 设定最小质数2
2. 确定质数的平方 <= 传入数值
3. n % p == 0, 判断n是否被p整除， 如果可以，加入分解质因子列表
4. n = n // p 将n设定为被分解质因子
5. p+=1 可以不一定是质数，这个是我无法想到的
6. 最后加入本身这个质数。
"""

def prime_factors(n):
    factors = []
    p = 2  # 从最小的质数开始
    while p * p <= n:  # 只需检查到 √n  只需检查 p ≤ √n，因为如果 n 有大于 √n 的质因子，它本身必然是质数。
        while n % p == 0:  # 如果 p 能整除 n
            # 如果 p 能整除 n，则 p 是 n 的质因子，加入 factors，并让 n = n // p。
            factors.append(p)
            n = n // p
        # 如果不能整除，尝试下一个数（注意：p 不一定是质数，但非质数 p 一定不会被整除，因为它的质因子已经被处理过了）。
        p += 1
    if n > 1:  # 如果最后剩下的 n > 1，说明它本身是质数
        factors.append(n)
    return factors

n = int(input())
factors = prime_factors(n)
print(' '.join(map(str, factors)))


