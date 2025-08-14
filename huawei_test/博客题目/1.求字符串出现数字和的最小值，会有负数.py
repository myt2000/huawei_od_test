#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/3 23:11
# @Author  : Administrator
# @File    : 1.求字符串出现数字和的最小值，会有负数.py
# @Software: PyCharm
"""
题目描述

输入字符串s，输出s中包含所有整数的最小和。

说明:

字符串s，只包含a-zA-Z+-;合法的整数包括

1正整数一个或者多个0-9组成，如0230021022)负整数负号-开头，数字部分由一个

或者多个0-9组成，如-0 -012 -23 -00023

输入描述

包含数字的字符串

输出描述

所有整数的最小和


字符串格式：a-zA-Z±
示例:abc12ss-123b
最小值：1+2+（-123）= -120

ab0c12ss-123b–1ss+dd–g1g
-120

"""


def min_sum_of_integers(s):
    i = 0
    n = len(s)
    numbers = []

    while i < n:
        if s[i] == '-':
            # 检查 '-' 后面是否紧跟数字，如果是，则提取整个负数
            if i + 1 < n and s[i + 1].isdigit():
                j = i + 1
                while j < n and s[j].isdigit():
                    j += 1
                num_str = s[i:j]
                numbers.append(int(num_str))
                i = j
            else:
                i += 1
        elif s[i].isdigit():
            # 提取整个正整数
            j = i
            while j < n and s[j].isdigit():
                j += 1
            num_str = s[i:j]
            numbers.append(int(num_str))
            i = j
        else:
            # 其他字符（字母、单独的 '+' 等）跳过
            i += 1

    return sum(numbers)


# 测试
s = input().strip()
print(min_sum_of_integers(s))