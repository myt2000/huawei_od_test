#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/3 22:33
# @Author  : Administrator
# @File    : hj4.字符串隔离.py
# @Software: PyCharm


def handle_char(s):
    n = len(s)
    end = 0
    for start in range(0, n, 8):
        end += 8
        if n - start >= 8:
            print(s[start:end])
        else:
            res = 8 - (n - start)
            print(s[start:end] + "".join(["0"] * res))


if __name__ == '__main__':
    handle_char("hellonowcoder")
