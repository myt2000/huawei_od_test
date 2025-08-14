#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/6 21:25
# @Author  : Administrator
# @File    : hj26.字符串排序.py
# @Software: PyCharm

"""
字符串排序

对于给定的由可见字符和空格组成的字符串，按照下方的规则进行排序：
1. 按照字母表中的顺序排序（不区分大小写）
2. 同一字母的大小写同时存在时，按照输入顺序排列
3. 非字母字符保持原来的位置不参与排序

直接输出排序后的字符串。

字符串由ASCII码在32到126范围内的字符组成。您可以参阅下表获得其详细信息。

输出：
BabA
输出：
aABb

输入：
Hello NowCoder!
输出：
CdeeH llNooorw!

"""


def sort_string(s):
    # 提取字母字符及其原始索引和原始字符
    letters = [(i, c) for i, c in enumerate(s) if c.isalpha()]
    # 分离非字母字符的索引和字符（如果需要可以记录，但实际不需要）

    # 对字母进行排序：不区分大小写，稳定排序保留原始顺序
    # 使用小写字母作为排序键，但保留原始字符
    sorted_letters = sorted(letters, key=lambda x: (x[1].lower(), x[0]))

    # 重新构建字符串
    result = list(s)
    # 将排序后的字母按顺序放回原字母位置
    for idx, (original_pos, _) in enumerate(letters):
        result[original_pos] = sorted_letters[idx][1]

    return ''.join(result)


# 测试示例
# print(sort_string("BabA"))  # 输出: "aABb"
print(sort_string("Hello NowCoder!"))  # 输出: "CdeeH llNooorw!"



# while True:
#     try:
#         s = input()
#         a = ''
#         for i in s:
#             if i.isalpha():
#                 a += i
#         b = sorted(a, key=str.upper)
#         index = 0
#         d = ''
#         for i in range(len(s)):
#             if s[i].isalpha():
#                 d += b[index]
#                 index += 1
#             else:
#                 d += s[i]
#         print(d)
#     except:
#         break