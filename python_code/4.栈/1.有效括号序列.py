"""
@file: 1.有效括号序列
@AUTHOR : brooks
@time: 2025/7/27 21:10
@desc: 
"""
class Solution:
    def isValid(self , s: str) -> bool:
        d = {"]": "[", ")": "(", "}": "{"}
        stack = []
        for char in s:
            if char in d.values():
                stack.append(char)
            elif char in d.keys():
                if stack == [] or d[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
