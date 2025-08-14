#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/3 16:56
# @Author  : Administrator
# @File    : 6.数据分类处理.py
# @Software: PyCharm

"""
题目：数据分类处理

描述：
对于给定的分类规则集R={R1, R2, ..., Rm}, 规范化它， 具体地：
1. 将R中的整数按从小到大的顺序重新排序
2. 去除R中的重复元素
记规范化后的分类规则集为 r= {r1, r2, ..., rm}

对于收集到的、由若干个整数组成的数据集I, 按照下方的要求，使用规范后的分类规则集r 输出分类后的结果。

1. 对于第i条分类规则ri, 如果I种存在以ri为连续子串的整数，则改规则集有效；进一步地， 你需要输出由多少条数据符合改规则，以及这些数据在I中的位置、数据本身。


"""

def handle_data():
    data = input().split()[1:]
    rule = list(map(int, input().split()[1:]))
    rule.sort()
    rule_set = set(rule)
    rule = list(map(str, sorted(list(rule_set))))
    result = []
    for i in rule:
        # 统计符合规则元素的数量

        count = 0
        # 统计符合规则的index和数据
        rule_list = []
        for j in range(len(data)):
            if i in data[j]:
                count += 1
                rule_list.append(j)
                rule_list.append(data[j])
        if len(rule_list):
            result.append(i)
            result.append(count)
            result += rule_list
    sum = len(result)
    res = [sum]
    res = res + result
    print(" ".join(map(str, res)))


handle_data()