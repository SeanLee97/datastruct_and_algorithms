# -*- coding: utf-8 -*-

"""题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    def clone_all(self, pHead):
        while pHead:
            node = RandomListNode(pHead.label)
            node.next = pHead.next
            pHead.next = node
            pHead = node.next

    def link(self, pHead):
        while pHead:
            if pHead.random is not None:
                pHead.next.random = pHead.random.next
            pHead = pHead.next.next

    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return None

        self.clone_all(pHead)
        self.link(pHead)
   
        # 新结点的头指针
        npHead = pHead.next
        # 当前结点的头指针
        cpHead = pHead
        while cpHead.next:
            node = cpHead.next
            cpHead.next = node.next
            cpHead = node

        return npHead
