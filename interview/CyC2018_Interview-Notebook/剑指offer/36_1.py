# -*- coding: utf-8 -*-

"""题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.root = None
        self.prev = None

    def inorder(self, node):
        if node is None:
            return None
        self.inorder(node.left)
        if self.root is None:
            self.root = node
        if self.prev != None:
            self.prev.right = node
            node.left = self.prev
        self.prev = node
        self.inorder(node.right)

    def Convert(self, pRootOfTree):
        # write code here
        self.inorder(pRootOfTree)
        return self.root
