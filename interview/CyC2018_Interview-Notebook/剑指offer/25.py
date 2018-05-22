# -*- coding: utf-8 -*-

"""题目描述

输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""

class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

def merge(pHead1, pHead2):
    if pHead1 == None or pHead2 == None:
        return pHead1 if pHead1 else pHead2
    if pHead1.val < pHead2.val:
        prH = ListNode(pHead1.val)
        pHead1 = pHead1.next
    else:
        prH = ListNode(pHead2.val)
        pHead2 = pHead2.next

    rH = prH
    while pHead1 and pHead2:
        if pHead1.val < pHead2.val:
            rH.next = ListNode(pHead1.val)
            pHead1 = pHead1.next
        else:
            rH.next = ListNode(pHead2.val)
            pHead2 = pHead2.next
        rH = rH.next

    while pHead1:
        rH.next = ListNode(pHead1.val)
        pHead1 = pHead1.next
        rH = rH.next

    while pHead2:
        rH.next = ListNode(pHead2.val)
        pHead2 = pHead2.next
        rH = rH.next

    return prH

if __name__ == '__main__':
    lst1 = ListNode(1, ListNode(3, ListNode(5)))
    lst2 = ListNode(1, ListNode(3, ListNode(5)))

    lst = merge(lst1, lst2)
    while lst:
        print(lst.val)
        lst = lst.next

