"""
@file: 2.组合
@AUTHOR : brooks
@time: 2025/7/27 22:22
@desc:
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。



示例 1：

输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
示例 2：

输入：n = 1, k = 1
输出：[[1]]


提示：

1 <= n <= 20
1 <= k <= n

方法一：
from itertools import combinations
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1, n+1), k))


combinations(iterable, r)
iterable: 输入的可迭代对象（如列表、元组、range等）
r: 每个组合中元素的个数

功能：
从输入序列中选取 r 个元素的所有不重复组合
元素顺序不重要（即 [1,2] 和 [2,1] 被视为相同组合）
返回一个迭代器对象

这行代码会：
从 range(1, n+1)（即 [1, 2, ..., n]）中
选取 k 个数字的所有可能组合
例如当 n=4, k=2 时，生成：(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)

方法二：
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start, current):
            # 如果当前组合长度等于k，加入结果
            if len(current) == k:
                result.append(current[:])  # 复制当前组合
                return

            # 从start开始遍历，避免重复组合
            for i in range(start, n + 1):
                current.append(i)          # 选择
                backtrack(i + 1, current)  # 递归
                current.pop()              # 撤销选择（回溯）

        backtrack(1, [])
        return result


方法三：
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start, current):
            # 剪枝：如果剩余元素不够组成k个数的组合，直接返回
            if len(current) + (n - start + 1) < k:
                return

            # 如果当前组合长度等于k，加入结果
            if len(current) == k:
                result.append(current[:])
                return

            # 从start开始遍历
            for i in range(start, n + 1):
                current.append(i)
                backtrack(i + 1, current)
                current.pop()

        backtrack(1, [])
        return result

"""
from typing import List
from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [list(i) for i in combinations(range(1, n+1), k)]


if __name__ == '__main__':
    print(Solution().combine(4, 2))