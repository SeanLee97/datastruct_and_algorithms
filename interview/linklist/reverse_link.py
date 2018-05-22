# !/usr/bin/env python
# -*- coding: utf-8 -*-

class LinkList(object):
    def __init__(self, data, nexT=None):
        self.data = data
        self.nexT = nexT

# 栈实现
def stack_f(lst):
    stack = []
    while lst != None:
        stack.append(lst.data)
        lst = lst.nexT
    for _ in range(len(stack)):
        print(stack.pop())

# 单链表逆置(递归)
def recursive_f(head):
    if head == None or head.nexT == None:
        return head
    nhead = recursive_f(head.nexT)
    head.nexT.nexT = head
    head.nexT = None
    return nhead

# 循环实现
def loop_f(head):
    prev = head
    curr = head.nexT
    prev.nexT = None
    while curr:
        t = curr.nexT
        curr.nexT = prev
        prev = curr
        curr = t
    return prev

def echo(lst):
    while lst != None:
        print(lst.data)
        lst = lst.nexT
        
ll = LinkList(1, LinkList(2, LinkList(3)))

'''
ll = recursive_f(ll)
echo(ll)
'''
head = loop_f(ll)
echo(head)

