#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/3 22:11
# @Author  : Administrator
# @File    : hj2.计算某字符串出现次数.py
# @Software: PyCharm


def count_char(s: str, c: str):
    s = s.lower()
    c = c.lower()
    count = 0
    for i in s:
        if i == c:
           count +=1
    return count


if __name__ == '__main__':
    print(count_char("111111aAbbbbbbrbrbr", "A"))