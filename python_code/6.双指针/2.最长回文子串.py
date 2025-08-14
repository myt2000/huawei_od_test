"""
@file: 2.最长回文子串
@AUTHOR : brooks
@time: 2025/7/27 23:00
@desc:
描述：
对于长度为n的一个字符串A(仅包含数字，大小写英文字母)， 请设计一个高效算法，计算其中最长回文子串的长度。

数据范围：1≤n≤1000
要求：空间复杂度O(1), 时间复杂度O(n2)
进阶：空间复杂度O(n), 时间复杂度O(n)


多年前我自己的思路
class Solution:
    def getLongestPalindrome(self , A: str) -> int:
        if len(A) < 2:
            return A
        max_length = 0
        center = 0
        for i in range(len(A)):
            begin = self.center_expand(A, i, i)  # 子串是偶数长度
            end = self.center_expand(A, i, i + 1)  # 子串是奇数长度
            if max_length < max(begin, end):
                center = i
                max_length = max(begin, end)
        return len(A[center - (max_length - 1) // 2:center + max_length // 2 + 1])

    def center_expand(self, s: str, begin: int, end: int) -> int:
        '''
        :param s: 字符串
        :param begin: 字符串左边偏移起始位置
        :param end: 字符串右边偏移起始位置
        :return:  计算子串离中间点偏移量
        '''
        left = begin
        right = end
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return right - left - 1


方法：
解题思路
中心扩展法（满足时间复杂度O(n²)，空间复杂度O(1)）
这个问题可以使用中心扩展法来解决：
核心思想：遍历字符串中的每个字符，以每个字符或每两个相邻字符为中心向两边扩展，寻找回文子串
两种情况：
奇数长度回文：以单个字符为中心向两边扩展
偶数长度回文：以两个相邻字符为中心向两边扩展

def getLongestPalindrome(self, A: str) -> int:
    if len(A) < 2:
        return len(A)  # 修正：应该返回长度而不是字符串本身
    max_length = 0
    for i in range(len(A)):
        # 检查奇数长度回文（以i为中心）
        len1 = self.center_expand(A, i, i)
        # 检查偶数长度回文（以i和i+1为中心）
        len2 = self.center_expand(A, i, i + 1)
        # 更新最大长度
        max_length = max(max_length, len1, len2)
    return max_length

算法步骤
对于字符串中的每个位置 i：
以 A[i] 为中心，向两边扩展寻找奇数长度回文
以 A[i] 和 A[i+1] 为中心，向两边扩展寻找偶数长度回文
使用 center_expand 函数计算以指定位置为中心能扩展出的最长回文长度
记录并返回所有可能回文中长度的最大值
时间与空间复杂度
时间复杂度：O(n²) - 外层循环O(n)，内层扩展最坏情况O(n)
空间复杂度：O(1) - 只使用了常数个额外变量
这种方法满足题目要求的基本复杂度限制，是一种高效的解决方案。


最优方法
1. Manacher算法（满足进阶要求：时间O(n)，空间O(n)）
class Solution:
    def getLongestPalindrome(self, A: str) -> int:
        if not A:
            return 0

        # 预处理字符串，在每个字符间插入#
        processed = '#'.join('^{}$'.format(A))
        n = len(processed)

        # P[i]：表示以位置 i 为中心的回文半径（不包括中心点）
        P = [0] * n
        center = right = 0  # center是当前回文中心，right是右边界

        max_len = 0

        for i in range(1, n - 1):
            # 利用回文的对称性
            if i < right:
                P[i] = min(right - i, P[2 * center - i])

            # 尝试扩展回文
            try:
                while processed[i + P[i] + 1] == processed[i - P[i] - 1]:
                    P[i] += 1
            except IndexError:
                pass

            # 更新中心和右边界
            if i + P[i] > right:
                center, right = i, i + P[i]

            # 更新最大长度
            max_len = max(max_len, P[i])

        return max_len

# 测试
if __name__ == '__main__':
    solution = Solution()
    print(solution.getLongestPalindrome("ababc"))  # 输出: 3 (bab或aba)
    print(solution.getLongestPalindrome("abcdef")) # 输出: 1


"""
class Solution:
    def getLongestPalindrome(self , A: str) -> int:
        if not A:
            return 0

            # 预处理字符串，在每个字符间插入#
        processed = '#'.join('^{}$'.format(A))
        n = len(processed)

        # P[i]表示以i为中心的回文半径
        P = [0] * n
        center = right = 0  # center是当前回文中心，right是右边界

        max_len = 0

        for i in range(1, n - 1):
            # 利用回文的对称性
            if i < right:
                P[i] = min(right - i, P[2 * center - i])

            # 尝试扩展回文
            try:
                while processed[i + P[i] + 1] == processed[i - P[i] - 1]:
                    P[i] += 1
            except IndexError:
                pass

            # 更新中心和右边界
            if i + P[i] > right:
                center, right = i, i + P[i]

            # 更新最大长度
            max_len = max(max_len, P[i])

        return max_len


if __name__ == '__main__':
    print(Solution().getLongestPalindrome("ababc"))