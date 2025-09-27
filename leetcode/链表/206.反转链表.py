#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/20 22:56
# @Author  : Administrator
# @File    : 206.反转链表.py
# @Software: PyCharm
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre