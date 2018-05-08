# -*- coding: utf-8 -*-

"""题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""

class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def next_node(pNode):
    if pNode == None:
        return None
    if pNode.right != None:
        tNode = pNode.right
        while tNode != None:
            tNode = tNode.left
        return tNode
    else:
        while pNode != None:
            parent = pNode.next
            if parent.left == pNode:
                return parent
            pNode = pNode.next
