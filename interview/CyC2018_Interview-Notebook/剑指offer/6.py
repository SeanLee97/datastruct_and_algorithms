# -*- coding: utf-8 -*-

"""题目描述
输入链表的第一个节点，从尾到头反过来打印出每个结点的值。
"""

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 1. 递归方式
def solution(root):
    if root == None or root.next == None:
        return root
    nroot = solution(root.next)
    root.next.next =  root
    root.next = None
    return nroot

# 2. 循环方式
def solution2(root):
    if root == None:
        return root
    prev = root
    curr = root.next
    prev.next = None
    while curr:
        n = curr.next
        curr.next = prev
        prev = curr
        curr = n
    return prev

# 输出链表
def echo(root):
    while root:
        print(root.data)
        root = root.next

if __name__ == '__main__':
    linklist = Node(1, Node(2, Node(3)))
    echo(linklist)
    r_linklist = solution(linklist)
    echo(r_linklist)

    linklist = solution2(r_linklist)
    echo(linklist)
