# -*- coding: utf-8 -*-

"""题目描述
输入一个链表，输出该链表中倒数第k个结点。
"""

class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

def f(head, k):
    listsize = 0 
    thead = head
    while thead:
        listsize += 1
        thead = thead.next
    if k > listsize:
        return None
    diff = listsize - k
    thead = head
    for i in range(diff):
        thead = thead.next
    return thead

if __name__ == '__main__':
    link = ListNode(1, ListNode(2, ListNode(3)))
    head = f(link, 2)
    print(head.val)
