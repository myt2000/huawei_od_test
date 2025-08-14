"""
@file: 坐标移动
@AUTHOR : brooks
@time: 2025/7/26 20:10
@desc:
描述：
我们定义一个无限大的二维网格上有一个小人，小人的初始位置为(0,0)点，小人可以读取指令上下左右移动。一个合法的指令由三至四个符号组成：
第一个符号为"A/D/W/S"中的一个，代表小人移动的方向；分别代表向左、向右、向上、向下移动；记某个时刻小人的坐标为（x,y）,向左移动一格即抵达（x-1，y）、向右移动一格即抵达（x+1, y）、向上移动一格即抵达（x, y+1)、向下移动一格即抵达（x,y-1）。
最后一个符号为";",代表指令的结束，该符号固定存在；
中间为一个大于0且小于100的数字，代表小人移动的距离。特别地，如果这个数字小于10，那么它可能包含一个前导零，此时也视为合法。

如果你遇到一个不合法的指令，则直接忽略；例如，指令"A100;"是不合法的，因为100超出了规定的数字范围；"Y10;"也是不合法的，因为Y不是"A/D/W/S"中的一个。
输出小人的最终的坐标。

输入描述：
在一行输入一个长度1≤length(s)≤10^4, 由大写字母、数字和分号（‘；’）构成的字符串s, 代表输入的指令序列。 保证字符床中至少存在一个‘；’，且末尾一定‘；’。

输出描述：
在一行上输出一个两个整数，代表小人最终位置的横纵坐标，使用逗号间隔。


input_list = input().split(';')
initial = [0,0]

for item in input_list:
    if not 2 <= len(item) <= 3:
        continue

    try:
        direction = item[0]
        step = int(item[1:])
        if direction in ['A', 'D', 'W', 'S']:
            if 0 <= step <= 99:
                if direction == 'A':
                    initial[0] -= step
                elif direction == 'D':
                    initial[0] += step
                elif direction == 'S':
                    initial[1] -= step
                elif direction == 'W':
                    initial[1] += step
    except:
        continue

print(str(initial[0]) + ',' + str(initial[1]))
"""

if __name__ == '__main__':
    import sys
    s = sys.stdin.readline().strip()
    x, y = 0, 0
    operations = s.split(';')
    for operation in operations:
        if len(operation) <2:
            continue
        direction = operation[0]
        distance_str = operation[1:]
        if direction not in ['A', 'D', 'W', 'S']:
            continue
        if not distance_str.isdigit():
            continue
        distance = int(distance_str)
        if distance <1 or distance >99:
            continue
        if direction == 'A':
            x -= distance
        elif direction == 'D':
            x += distance
        elif direction == 'W':
            y += distance
        elif direction == 'S':
            y -= distance
    print(f"{x},{y}")

import sys
import re
x,y=0,0
cmd_list = sys.stdin.readline().strip().split(';')
fun={
    'A':lambda a,b,p:(a-p,b),
    'D':lambda a,b,p:(a+p,b),
    'W':lambda a,b,p:(a,b+p),
    'S':lambda a,b,p:(a,b-p)
}
for cmd in cmd_list:
    if re.search(r'^[A|S|W|D]\d\d?$', cmd) and len(cmd)<=3:
        x,y=fun[cmd[0]](x,y,int(cmd[1:]))
print(f'{x},{y}')