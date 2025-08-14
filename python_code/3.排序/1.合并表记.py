"""
@file: 1.合并表记
@AUTHOR : brooks
@time: 2025/7/27 14:25
@desc:
描述
数据表中，一条记录包含表索引和数值两个值。请对表索引相同的记录进行合并（即将相同索引的数值进行求和运算），随后按照索引值的大小从小到大依次输出。

输入描述：
第一行输入一个整数n(1≤n≤500)代表数据表的记录数。
此后n行，第i行输入两个整数xi, yi(1≤xi≤11111111;1≤yi≤10^5)代表数据标的第i条记录的索引和数值。

输出描述：
一共若干行（视输入数据变化），第i行输入输出两个数，代表合并后数据表中第i条记录的索引和数值。


4
0 1
0 2
1 2
3 4


deepseek给的答案
def main():
    n = int(input().strip())  # 读取记录数
    data = {}  # 创建字典用于存储合并后的记录

    # 处理每条记录
    for _ in range(n):
        x, y = map(int, input().split())  # 读取索引和数值
        # 合并相同索引的记录（数值求和）
        data[x] = data.get(x, 0) + y

    # 按索引排序并输出结果
    for key in sorted(data.keys()):
        print(f"{key} {data[key]}")

if __name__ == "__main__":
    main()


题解


n = int(input())
dic = {}

# idea: 动态建构字典
for i in range(n):
    line = input().split()
    key = int(line[0])
    value = int(line[1])
    dic[key] = dic.get(key, 0) + value  # 累积key所对应的value

for each in sorted(dic):  # 最后的键值对按照升值排序
    print(each, dic[each])
"""
import sys

def merge_table(number_list):
    table = {}
    for i, n in number_list:
        if i in table:
            table[i] += n
        else:
            table[i] = n
    result = ""
    sort_list = sorted(table.keys())
    for i in sort_list:
        s = "{} {}\n".format(i, table[i])
        result += s
    return result


if __name__ == '__main__':
    n = sys.stdin.readline().strip()
    table_list = []
    for line in sys.stdin:
        if line.strip():
            index, num = map(int, line.strip().split(" "))
            table_list.append([index, num])
        else:
            break
    print(merge_table(table_list))
