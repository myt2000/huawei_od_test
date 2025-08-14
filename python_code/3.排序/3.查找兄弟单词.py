"""
@file: 3.查找兄弟单词
@AUTHOR : brooks
@time: 2025/7/27 20:05
@desc:


描述：

定义一个字符串s的"兄弟单词"为：将s重新排序后得到的与原字符串不同的新字符串。
现在，对于给定的n个字符串s1, s2, ..., sn和另一个单独的字符串x, 你需要解决两个问题：
1. 统计这n个字符串中，有多少个是x 的"兄弟单词"(注意，这n个字符串可能有重复，重复字符串分别计算)
2. 将这n个字符串中x 的"兄弟单词" 按字典序从小到大排序，输出排序后的第k个兄弟单词（从1开始计数）。特别地，如果不纯在，则不输出任何内容。

输入
3 abc bca cab abc 1
输出
2
bca
说明：
在这个样例中，x 的兄弟单词为 "acb" 、"bac" 、"bca" 、"cab" 、"cba" 。其中，标橙色的两个字符串存在于所给定的 n 个字符串中。第 1 小的兄弟单词为 "bca"。


输入
3 a aa aaa a 1

输出：
0

说明：在这个样例中，按照定义，字符串 "a" 没有兄弟单词。

"""
if __name__ == '__main__':

    while True:
        try:
            # 读取输入数据，并且转换为列表
            data1 = input().split()
            # 获取单词的个数
            n1 = data1[0]
            # 按字典排序的第几个兄弟词
            n2 = data1[-1]
            # 获取输入的n个单词
            data2 = data1[1:-2]
            # 获取兄弟词
            data3 = data1[-2]

            # 用于存储兄弟词的数量
            n3 = 0
            # 用于存储兄弟词
            data4 = []

            for word in data2:
                if word == data3:
                    continue
                elif sorted(word) == sorted(data3):
                    n3 = n3 + 1
                    data4.append(word)
            print(n3)
            # 将兄弟词按照字典排序
            data5 = sorted(data4)
            print(data5[int(n2) - 1])
        except:
            break

# 3 abc bca cab abc 1

from collections import defaultdict


# def is_brother(s, x):
#     if len(s) != len(x) or s == x:
#         return False
#     # 统计字符频次
#     freq = defaultdict(int)
#     for c in x:
#         freq[c] += 1
#     for c in s:
#         if freq[c] == 0:
#             return False
#         freq[c] -= 1
#     return True
#
#
# def solve():
#     import sys
#     input = sys.stdin.read().split()
#     idx = 0
#     n = int(input[idx])
#     idx += 1
#     words = input[idx:idx + n]
#     idx += n
#     x = input[idx]
#     idx += 1
#     k = int(input[idx])
#
#     brothers = []
#     for word in words:
#         if is_brother(word, x):
#             brothers.append(word)
#
#     # 统计数量
#     count = len(brothers)
#     print(count)
#
#     # 输出第k个
#     if 1 <= k <= count:
#         brothers.sort()
#         print(brothers[k - 1])
#
#
# solve()