# -*- coding: utf-8 -*-

"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder(self, pRoot):
        s = []
        p = pRoot
        root = None
        prev = None
        while p or len(s) > 0:
            while p:
                s.append(p)
                p = p.left
            p = s.pop()
            if root is None:
                root = p
            if prev is not None:
                prev.right = p
                p.left = prev
            prev = p
            p = p.right
        return root

    def Convert(self, pRoot):
        head = self.inorder(pRoot)
        return head
