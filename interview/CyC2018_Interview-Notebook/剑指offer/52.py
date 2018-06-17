# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        comm_node = None
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                pHead1 = pHead1.next
            elif pHead1.val == pHead2.val:
                comm_node = pHead1
                break
            else:
                pHead2 = pHead2.next
        while pHead1 and pHead2:
            if pHead1.val != pHead2.val:
                return None
            else:
                pHead1 = pHead1.next
                pHead2 = pHead2.next
        return comm_node
