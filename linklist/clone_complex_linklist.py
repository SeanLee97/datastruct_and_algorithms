# -*- coding: utf-8 -*-

"""
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead is None:
            return None
            
        self.clone_all(pHead)
        self.link(pHead)

        npHead = pHead.next
        cpHead = pHead
        while cpHead.next:
            node = cpHead.next
            cpHead.next = node.next
            cpHead = node
        return npHead

    def clone_all(self, pHead):
        while pHead:
            node = RandomListNode(pHead.label)
            node.next = pHead.next
            pHead.next = node 
            pHead = node.next

    def link(self, pHead):
        while pHead:
            if pHead.random:
                pHead.next.random = pHead.random.next
            pHead = pHead.next.next