"""
@file: 5.成绩排序
@AUTHOR : brooks
@time: 2025/7/27 20:31
@desc:


3
0
fang 90
yang 50
ning 70
"""
import sys

while True:
    try:
        number = int(input())
        if input() == "0":
             flag = True
        else:
            flag = False

        ls = []
        for i in range(number):
            name, score = input().split()
            ls.append((name, int(score)))
            ls.sort(key=lambda x: x[1], reverse=True)
        for x in ls:
            print(*x)
    except:
        break