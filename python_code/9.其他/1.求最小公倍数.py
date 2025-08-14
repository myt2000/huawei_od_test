#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/2 21:40
# @Author  : Administrator
# @File    : 1.求最小公倍数.py
# @Software: PyCharm


"""
题目，求最小公倍数

描述：
对于给定的两个正整数a,b, 它们的最小公倍数lcm(a,b)是指能同时被a和b整除的最小正整数。
求解lcm


def lcm():
    two_nums = list(map(int, input().split()))
    a = two_nums[0]
    b = two_nums[1]
    max_num = max(two_nums)
    while True:
        if max_num % a == 0 and max_num % b == 0:
            return max_num
        max_num+=1

这个解法运行超时

math.gct(a,b) 是求a, b最小公约数

"""
import math


def lcm():
    two_nums = list(map(int, input().split()))
    a = two_nums[0]
    b = two_nums[1]
    return (a * b) // math.gcd(a, b)

if __name__ == '__main__':
    print(lcm())