"""
@file: 5.输入整型数组和排序标识
@AUTHOR : brooks
@time: 2025/7/27 11:10
@desc:
题目：输入整型数组和排序标识，对其元素按照升序或降序进行排序



描述：
对于给出的n个整数组成的数组{a1, a2, ..., an}, 根据输入需要，按升序或降序排列后输出。

输入描述
第一行输入一个整数n(1≤n≤10^3)代表数组中的元素个数。
第二行输入n个整数a1, a2, ..., an(0≤n≤10^5)代表数组中的元素。
第三行输入一个整数op(1≤op≤1)代表排序方式，其中，op=0表示按升序，op=1表示按降序。

输出描述：
在一行上输出n个整数，代表排序后的数组。

输入
5
1 2 2 5 4
0

输出
1 2 2 4 5
"""
import sys

def sort_array(n, number, op):
    if op == 0:
        number.sort()
    else:
        number.sort(reverse=True)
    return " ".join(map(str, number))

if __name__ == '__main__':
    n = sys.stdin.readline().strip()
    number = sys.stdin.readline().strip().split(" ")
    number_list = [int(i) for i in number]

    op = int(sys.stdin.readline().strip())
    print(sort_array(n, number_list, op))


