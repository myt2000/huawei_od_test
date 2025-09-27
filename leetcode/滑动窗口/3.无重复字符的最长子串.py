#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/20 21:06
# @Author  : Administrator
# @File    : 3.无重复字符的最长子串.py
# @Software: PyCharm
from collections import Counter
"""
Counter 是 Python 内置的 collections 模块中的一个类，它是一个字典子类，用于计数可哈希对象。它可以非常方便地统计元素出现的次数。
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        cnt = Counter()
        left = 0
        for right, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))