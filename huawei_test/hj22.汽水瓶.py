#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/6 15:42
# @Author  : Administrator
# @File    : hj22.汽水瓶.py
# @Software: PyCharm


"""

"""


# def max_bottles(n):
#     result = n // 3
#     bottles = n // 3 + n % 3
#     if bottles == 2:  # 空瓶数量为2，可以借一瓶，此后不能再兑换
#         result += 1
#     elif bottles < 2:  # 空瓶数小于2，无法兑换
#         result += 0
#     else:
#         result += max_bottles(bottles)
#     return result
# while True:
#     try:
#         n = int(input())
#         if n == 0:
#             break
#         else:
#             print(max_bottles(n))
#     except:
#         break

while True:
    n=int(input())
    if n==0:break
    print(n//2)