"""
@file: 5.跳台阶
@AUTHOR : brooks
@time: 2025/7/26 19:50
@desc:
描述：
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）
数据范围：1≤n≤40
要求：时间复杂度O(n), 空间复杂度O（1）

跳到第 n 阶台阶有多少种不同的跳跃方式？

示例
n = 1 → 只有 [1]，返回 1。

n = 2 → 有 [1,1] 和 [2]，返回 2。

n = 3 → 有 [1,1,1]、[1,2]、[2,1]，返回 3。

n = 4 → 有 [1,1,1,1]、[1,1,2]、[1,2,1]、[2,1,1]、[2,2]，返回 5。

可以观察到，这个问题的解实际上是 斐波那契数列（Fibonacci Sequence）。

方法	递推式	代码实现	空间复杂度
动态规划（数组）	dp[i] = dp[i-1] + dp[i-2]	dp = [0,1,2]; for i in 3..n: dp.append(dp[i-1]+dp[i-2])	O(n)
动态规划（滚动变量）	dp[i] = dp[i-1] + dp[i-2]	a, b = 1, 2; for _ in 3..n: a, b = b, a+b	O(1)


def jumpFloor(self, number: int) -> int:
    if number <= 2:
        return number
    a, b = 1, 2  # a=dp[i-2], b=dp[i-1]
    for _ in range(3, number + 1):
        a, b = b, a + b  # dp[i] = dp[i-1] + dp[i-2]
    return b
"""
class Solution:
    def jumpFloor(self , number: int) -> int:
        if number<=2:
            return number
        dp = [0,1,2]
        for i in range(3,number+1):
             dp.append(dp[i-1]+dp[i-2])
        return dp[number]


if __name__ == '__main__':
    print(Solution().jumpFloor(5))