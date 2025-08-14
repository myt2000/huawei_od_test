"""
@file: 1.有重复字符串的排列组合
@AUTHOR : brooks
@time: 2025/7/27 22:07
@desc:
有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。

示例 1：

 输入：S = "qqe"
 输出：["eqq","qeq","qqe"]
示例 2：

 输入：S = "ab"
 输出：["ab", "ba"]
提示:

字符都是英文字母。
字符串长度在[1, 9]之间。






提交的方法：
class Solution:
    def permutation(self, S: str) -> List[str]:
      return list(set(map(lambda x: ''.join(x), permutations(S))))


permutations特点
处理重复元素：permutations 会考虑重复元素，对相同字符的不同位置也会生成不同排列
返回元组：每个排列以元组形式返回
有序性：按照字典序生成排列（基于输入序列中元素的位置）
对于示例 S = "qqe"：
会生成 ('q','q','e'), ('q','e','q'), ('q','q','e'), ('q','e','q'), ('e','q','q'), ('e','q','q')
转为字符串并去重后得到 ["eqq","qeq","qqe"]


算法思路
这是一个典型的回溯算法：
选择：每次选择一个未被使用过的字符作为当前排列的第一个字符
递归：对剩余字符进行全排列
组合：将选中的字符与递归结果组合
去重：通过if S[i] in S[:i]: continue避免重复字符产生重复排列
执行过程示例（S="qqe"）
第一层：选择q(位置0)、跳过q(位置1，因为之前出现过)、选择e(位置2)
选择q时：递归处理"qe"
选择q：递归处理"e" → 返回"e" → 组合得"qe"
选择e：递归处理"q" → 返回"q" → 组合得"eq"
得到["qe", "eq"]
选择e时：递归处理"qq"
选择q(位置0)：递归处理"q" → 返回"q" → 组合得"q"
跳过q(位置1)：因为之前出现过
得到["qq"]
最终组合：q+["qe","eq"] 和 e+["qq"] → ["qqe","qeq","eqq"]
关键技巧
去重机制：if S[i] in S[:i]: continue 确保相同字符只在第一次出现时被选择
递归分治：将问题分解为"选一个字符+剩余字符的排列"的子问题
这种解法避免了使用itertools.permutations后还需要set去重的步骤，直接在生成过程中避免重复

class Solution:
    def permutation(self, S: str) -> List[str]:
        # 这个方法完全看不懂
        n = len(S)
        if n == 0:
            return [""]
        res = []
        for i in range(n):
            # print(S[i], S[:i])
            if S[i] in S[:i]:
                continue
            for s1 in self.permutation(S[:i] + S[i + 1:]):
                res.append(S[i] + s1)
        return res
"""
from itertools import permutations,combinations
from typing import List


class Solution:
    def permutation(self, S: str) -> List[str]:
        # 这个方法完全看不懂
        strings = [i for i in S]
        return list(set(map(lambda x: ''.join(x), permutations(S))))


if __name__ == '__main__':
    print(Solution().permutation("qqe"))


