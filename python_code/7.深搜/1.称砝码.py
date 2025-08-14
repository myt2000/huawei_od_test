#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/2 11:04
# @Author  : Administrator
# @File    : 1.称砝码.py
# @Software: PyCharm

"""
称砝码

描述：对于给定的n种砝码，重量互不相等，依次为m1, m2, ..., mn, 数量依次为x1, x2, ..., xn,
现在要用这些砝码去称物体的重量（放在同一侧）， 问能称出多少种不同的重量。特别地，称重重量包括0.

输入描述：
第一行输入一个整数n(1≤n≤10)代表砝码的个数。
第二行输入n个整数m1, m2, ..., mn(1≤mi≤2000)代表没中砝码的重量。
第三行输入n个整数x1, x2, ..., xn(1≤xi≤10)代表没中砝码的数量。

输出描述：
输出一个整数，代表利用给定的砝码可以称出的不同的重量数。


核心代码是这个
def count_unique_sums(nums):
    sums = {0}
    for num in nums:
        new_sums = set()
        for s in sums:
            new_sums.add(s + num)
        sums.update(new_sums)
    return len(sums)

"""

def weight_count():
    kind = input()
    weight = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    dp = {0}
    for i in range(int(kind)):
        # 砝码重量
        mi = weight[i]
        # 砝码数量
        xi = nums[i]
        temp = set()
        for w in dp:
            for k in range(1, xi + 1):
                temp.add(w + k * mi)  # 生成新重量
        dp.update(temp)  # 将新重量合并到 dp
    return len(dp)

if __name__ == '__main__':
    print(weight_count())


