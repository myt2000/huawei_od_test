#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/4 21:24
# @Author  : Administrator
# @File    : hj9.提取不重复的整数.py
# @Software: PyCharm


def handle_number(s):
    numbers = [int(i) for i in s]
    n = len(numbers) - 1
    result = []
    while n >= 0:
        if numbers[n] not in result:
            result.append(numbers[n])
        n -= 1
    print("".join(list(map(str, result))))


handle_number("9876673")