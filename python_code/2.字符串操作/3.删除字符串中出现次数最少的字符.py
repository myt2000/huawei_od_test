"""
@file: 3.删除字符串中出现次数最少的字符
@AUTHOR : brooks
@time: 2025/7/26 22:30
@desc:

描述
对于给定的仅由小写字母构成的字符串， 删除字符串中出现次数最少的字符。输出删除后的字符串，字符串中其他字符串保持原来的顺序。
特别地，若有多个字符出现的字数都最少，泽吧这些字符都删掉。
输入描述：
在一行上输入一个长度为11≤length(s)≤20， 仅由小写字母构成的字符串s, 代表待处理的字符串。
输出描述：
在一行上输出一个字符串，代表删除后的答案。保证这个字符串至少包含一个字符。

"""
import sys

def delete_min_char(s):
    """
    删除字符串中出现次数最少的字符
    :param s:
    :return:
    """
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    min_count = min(char_count.values())
    result = ""
    for char in s:
        if char_count[char] != min_count:
            result += char
    return result


if __name__ == '__main__':
    for line in sys.stdin:
        a = line.strip()
        print(delete_min_char(a))
