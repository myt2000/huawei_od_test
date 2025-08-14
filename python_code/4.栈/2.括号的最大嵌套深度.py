"""
@file: 2.括号的最大嵌套深度
@AUTHOR : brooks
@time: 2025/7/27 21:46
@desc:
给定 有效括号字符串 s，返回 s 的 嵌套深度。嵌套深度是嵌套括号的 最大 数量。



示例 1：

输入：s = "(1+(2*3)+((8)/4))+1"

输出：3

解释：数字 8 在嵌套的 3 层括号中。

示例 2：

输入：s = "(1)+((2))+(((3)))"

输出：3

解释：数字 3 在嵌套的 3 层括号中。

示例 3：

输入：s = "()(())((()()))"

输出：3



提示：

1 <= s.length <= 100
s 由数字 0-9 和字符 '+'、'-'、'*'、'/'、'('、')' 组成
题目数据保证括号字符串 s 是 有效的括号字符串
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        stack =[]
        max_depth = 0
        for i in s:
            if i in "(":
                stack.append(i)
            if i in ")":
                max_depth = max(max_depth, len(stack))
                stack.pop()
        return max_depth

if __name__ == '__main__':
    print(Solution().maxDepth("(1+(2*3)+((8)/4))+1"))

