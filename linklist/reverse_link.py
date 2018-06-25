# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 递归版本
    def recursive(self, pHead):
        if pHead == None or pHead.next == None:
            return pHead
        nHead = self.recursive(pHead.next)
        pHead.next.next = pHead
        pHead.next = None
        return nHead

    # 递归版本
    def iter(self, pHead):
        curr = pHead.next
        prev = pHead
        prev.next = None
        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
        return prev

    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead == None:
            return None
        #head = self.recursive(pHead)
        head = self.iter(pHead)
        return head

