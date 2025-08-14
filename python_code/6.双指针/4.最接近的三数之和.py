"""
@file: 4.最接近的三数之和
@AUTHOR : brooks
@time: 2025/8/1 15:54
@desc: 
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]  # 初始值

        for i in range(n - 2):
            # 跳过重复的 nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == target:
                    return target
                # 更新 closest_sum
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1
                    # 跳过重复的 nums[left]
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    # 跳过重复的 nums[right]
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return closest_sum

        # n = len(nums)
        # nums.sort()
        # ans = {}
        # minvalue = float("inf")
        #
        # for first in range(n):
        #     second: int = first + 1
        #     third: int = n - 1
        #     res = target - nums[first]
        #     while second < n and n > third > second:
        #
        #         s = nums[first] + nums[second] + nums[third]
        #         res = abs(s - target)
        #         old_value = minvalue
        #         minvalue = min(minvalue, res)
        #         if minvalue < old_value:
        #             ans[minvalue] = s
        #         second += 1
        #         third += 1
        #
        # return ans[minvalue]

if __name__ == '__main__':
    target = Solution().threeSumClosest([10,20,30,40,50,60,70,80,90], 1)
    print(target)
    # print(Solution().threeSumClosest([0, 0, 0], 1))