"""
@file: 1.进制转换
@AUTHOR : brooks
@time: 2025/7/26 15:57
@desc:

对于给定的十六进制数，输出其对应的十进制表示。
在本题中，十六进制数的格式为：
0x 开头，后跟若干个十六进制数字（保证为 0-9 和 A-F 中的一个）。其中，A-F 依次代表十进制中的 10∼15。

输入描述
在一行上输入一个十六进制数 s，代表待转换的十六进制数，格式见题干。保证 s 转化得到的十进制数 ,x 的范围为 1≦x<2^31。

输出描述
在一行上输出一个整数，代表 s 对应的十进制数。

最簡單的方案
if __name__ == '__main__':
    import sys
    for line in sys.stdin:
        hex_string = line.strip()
        # 直接使用int函数转换16进制字符串为10进制
        decimal_value = int(hex_string, 16)
        print(decimal_value)
"""


# def oct_to_dec(s):
#     s = s[2:]
#     res = 0
#     for i in range(len(s)):
#         res += int(s[i], 16) * (16 ** (len(s) - i - 1))
#     return res


def hex_to_decimal():
    oct_value = input()
    decimal_value = int(oct_value, 16)
    return decimal_value

hex_to_decimal()


if __name__ == '__main__':
    # print(oct_to_dec("0xFA93"))
    import sys
    res = 0
    for line in sys.stdin:
        s = line.strip().split("0x")[1]
        for i in range(len(s)):
            res += int(s[i], 16) * (16 ** (len(s) - i - 1))
        print(res)



