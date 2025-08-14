"""
@file: 两数之和
@AUTHOR : brooks
@time: 2025/7/26 16:26
@desc:

给出一个整型数组 numbers 和一个目标值 target，请在数组中找出两个加起来等于目标值的数的下标，返回的下标按升序排列。
（注：返回的数组下标从1开始算起，保证target一定可以由数组里面2个数字相加得到）
数据范围：2≤len(numbers)≤10^5, -10≤numbers≤10^9;0≤target≤10^9
要求：空间复杂度O（n）,时间复杂度O(nlogn)

"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            print("i:{%s}, num:{%s}" % (i, num))
            if target - num in dic:
                return [dic[target - num] + 1, i + 1]
            dic[num] = i

if __name__ == '__main__':
    twoSum = Solution().twoSum
    print(twoSum([2, 7, 11, 15], 9))