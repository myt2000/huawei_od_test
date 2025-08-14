"""
@file: 3.最小覆盖子串
@AUTHOR : brooks
@time: 2025/7/30 22:33
@desc:

描述
给出两个字符串 s 和 t, 要求在 s 中找出最短的包含 t 中所有字符的连续子串。

示例1
输入：XDOYEZODEYXNZ，XYZ

输出：YXNZ

示例2
输入：abcAbA，AA

输出：AbA

defaultdict 的作用
自动初始化缺失的键：
当访问一个不存在的键时，defaultdict 会自动创建该键并赋予一个默认值
避免了 KeyError 异常
简化代码：
不需要在访问前检查键是否存在
减少了冗余的初始化代码

# from collections import defaultdict
#
# # 创建 defaultdict，指定默认值类型
# dict_with_default = defaultdict(int)  # 默认值为 0
# dict_with_default = defaultdict(list) # 默认值为 []
# dict_with_default = defaultdict(set)  # 默认值为 set()
#
# # 访问不存在的键时自动创建并赋予默认值
# print(dict_with_default['new_key'])  # 输出: 0 (对于int类型)
"""
class Solution:
    def minWindow(self , S: str, T: str) -> str:
        from collections import defaultdict

        # 需要的字符及其数量
        need = defaultdict(int)
        # 窗口中的字符及其数量
        window = defaultdict(int)

        # 统计T中每个字符的需求量
        for c in T:
            need[c] += 1

        # 已满足条件的字符种类数
        valid = 0

        # 记录最小覆盖子串的起始索引和长度
        start = 0
        min_len = float('inf')

        # 滑动窗口的左右指针
        left, right = 0, 0

        while right < len(S):
            # c 是即将进入窗口的字符
            c = S[right]
            # 扩大窗口
            right += 1

            # 更新窗口内的数据
            if c in need:
                window[c] += 1
                # 如果该字符的数量刚好满足需求，则valid加1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩
            while valid == len(need):
                # 更新最小覆盖子串
                if right - left < min_len:
                    start = left
                    min_len = right - left

                # d 是即将移出窗口的字符
                d = S[left]
                # 缩小窗口
                left += 1

                # 更新窗口内的数据
                if d in need:
                    # 如果该字符之前刚好满足需求，移除后就不满足了
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        # 返回最小覆盖子串
        return "" if min_len == float('inf') else S[start:start + min_len]


if __name__ == '__main__':
    print(Solution().minWindow("ADOBECODEBANC", "ABC"))