"""
@file: 6.字符串逆序
@AUTHOR : brooks
@time: 2025/7/27 11:47
@desc:
描述
对于给定的由小写字母和空格混合构成的字符串 s，将其翻转后输出。
保证给定的字符串 s的首尾不为空格。

输入描述
在一行上输入一个长度为1≤len(s)≤10^4、由小写字母和空格混合构成的字符串s。

输出描述
输出一个字符串，表示将输入字符串s翻转后的结果。
"""
import sys

def reverse_string(s):
    return s[::-1]


if __name__ == '__main__':
    for line in sys.stdin:
        s = line.strip()
        print(reverse_string(s))


