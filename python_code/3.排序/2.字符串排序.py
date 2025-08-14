"""
@file: 2.字符串排序
@AUTHOR : brooks
@time: 2025/7/27 14:56
@desc:

描述：
对于给定的由大小写字母混合构成的n个单词，输出按字典从小到大排序后的结果。

【名词解释】
从字符串的第一个字符开始逐个比较，直至发现第一个不同的位置，比较这个位置字符的 Ascii 码，Ascii 码较小('A' < 'B' ... < 'Z' < 'a' < ... < 'z')


输入描述：
第一行输入一个整数n(1≤n≤10^3)代表给定的单词个数
此后n行，每行输入一个长度1≤length(s)≤100, 由大小写字母构成的字符串s, 代表一个单词。

输出描述：
一共n行，每行输出一个字符串，代表排序后的结果。第一行输出的字典序最小的单词。

11
cap
to
cat
card
two
too
up
boat
boot
AA
Aa

AA
Aa
boat
boot
cap
card
cat
to
too
two
up


num = input()#num记录输入的词的个数
num = int(num)
b = []
for i in range(num):
    b.append(input())#用列表b记录所有的输入的词汇
b.sort()#列表排序，默认为从小到大
for i in b:
    print(i)#按要求输出即可

"""

import sys
import re

def string_sort(string_list):
    string_list = sorted(string_list)
    return '\n'.join(string_list)

if __name__ == '__main__':
    strings= []
    for line in sys.stdin:
        if line.strip():
            line = re.sub('[^a-zA-Z]', '', line)
            if line:
                strings.append(line.strip())
        else:
            break
    print(string_sort(strings))
