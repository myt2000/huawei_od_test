#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/6 15:16
# @Author  : Administrator
# @File    : hj21.简单密码.py
# @Software: PyCharm

"""
规定这样一种密码的变换方法：
对于密码中的小写字母，参考九键手机键盘，将它们映射为对应的数字，具体地，
"""

s = input()

letter_to_number = {
    "a": "2",
    "b": "2",
    "c": "2",
    "d": "3",
    "e": "3",
    "f": "3",
    "g": "4",
    "h": "4",
    "i": "4",
    "j": "5",
    "k": "5",
    "l": "5",
    "m": "6",
    "n": "6",
    "o": "6",
    "p": "7",
    "q": "7",
    "r": "7",
    "s": "7",
    "t": "8",
    "u": "8",
    "v": "8",
    "w": "9",
    "x": "9",
    "y": "9",
    "z": "9",
}

s_letter = "abcdefghijklmnopqrstuvwxyz"
s_upper = "ZABCDEFGHIJKLMNOPQRSTUVWXY"

upper_to_letter = dict(zip(s_upper, s_letter))

result = []
for i in s:
    if i in letter_to_number:
        result.append(letter_to_number[i])
    elif i in upper_to_letter:
        result.append(upper_to_letter[i])
    else:
        result.append(i)

print("".join(result))

