"""
@file: 3.明明的随机数
@AUTHOR : brooks
@time: 2025/7/26 16:59
@desc:


输入描述：
	第一行输入一个整数n(1≤n≤1000),代表明明生成的数字个数
	此后n行，第i行输入一个整数ai(1≤ai≤500），代表明明生成的随机整数。

输出描述：
	输入若干行，每行输入一个整数，代表输入数据排序后的结果。第一行输出最小的数字。

import sys

for line in sys.stdin:
    a = line.strip().split()
    print(int(a[0]) + int(a[1]))

"""

if __name__ == '__main__':
    import sys

    n = int(sys.stdin.readline().strip())
    numbers = [int(sys.stdin.readline().strip()) for _ in range(n)]
    unique_sorted_numbers = sorted(set(numbers))

    for num in unique_sorted_numbers:
        print(num)
