#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/4 22:00
# @Author  : Administrator
# @File    : hj15.求int型正整数在内存中存储是1的个数.py
# @Software: PyCharm


def bin_one(s):

    return bin(s).count('1')

print(bin_one(10))