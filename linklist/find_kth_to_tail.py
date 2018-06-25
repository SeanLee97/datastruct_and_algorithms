# -*- coding: utf-8 -*-
"""
题目描述：
输入一个链表，输出该链表中倒数第k个结点。
"""

class Solution:
    def FindKthToTail(self, head, k):
        # 典型的runner chaser题型
        runner = head
        chaser = head

        # runner先走k步
        while k and runner:
            runner = runner.next
            k -= 1
        if k > 0:
            return None

        # chaser 追赶
        while runner:
            runner = runner.next
            chaser = chaser.next
        return chaser
