"""
@file: 4.合并区间
@AUTHOR : brooks
@time: 2025/7/27 21:03
@desc:


# class Interval:
#     def __init__(self, a=0, b=0):
#         self.start = a
#         self.end = b
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param intervals Interval类一维数组
# @return Interval类一维数组


"""
from typing import List


class Solution:
    def merge(self , intervals: List[Interval]) -> List[Interval]:
        if len(intervals) <1:
            return intervals
        temp = sorted(intervals, key=lambda x: x.start)
        res = []
        res.append(temp[0])
        for i in range(1, len(temp)):
            if temp[i].start <= res[-1].end:
                res[-1].end = max(res[-1].end, temp[i].end)
            else:
                res.append(temp[i])
        return res