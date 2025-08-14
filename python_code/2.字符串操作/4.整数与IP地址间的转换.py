"""
@file: 4.整数与IP地址间的转换
@AUTHOR : brooks
@time: 2025/7/26 23:42
@desc:

原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001
组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。

数据范围：保证输入的是合法的 IP 序列

输入描述：
输入
1 输入IP地址
2 输入10进制型的IP地址

输出描述：
输出
1 输出转换成10进制的IP地址
2 输出转换后的IP地址


"""
import sys

def ip_to_int(ip):
    # 将IP地址按'.'分割成四段
    parts = ip.split('.')
    full_bin = ''
    for p in parts:
        # 每段转为整数，再转为8位二进制字符串（前面补0）  bin(10)得到的是'0b1010'所以需要去掉'0b'
        bin_str = bin(int(p))[2:].zfill(8)
        full_bin += bin_str
    # 将32位二进制字符串转为整数
    return int(full_bin, 2)

def int_to_ip(num):
    # 将整数转为二进制字符串并去掉'0b'
    bin_str = bin(int(num))[2:]
    # 补0到32位长度
    bin_str = bin_str.zfill(32)
    parts = []
    # 每8位分割一次
    for i in range(0, 32, 8):
        # 取8位二进制转为整数
        part = bin_str[i:i+8]
        # int(part, 2) 是二进制转换为十进制
        parts.append(str(int(part, 2)))
    # 用点连接四段数字
    return '.'.join(parts)


if __name__ == '__main__':
    ip = sys.stdin.readline().strip()
    number = sys.stdin.readline().strip()
    print(ip_to_int(ip))
    print(int_to_ip(number))
    # 10.0.3.193
    # 167969729