# !/usr/bin/env python
# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def min_depth(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    # 如果左子树为空则遍历右子树
    if root.left == None:
        return min_depth(root.right) + 1
    # 如果右子树为空则遍历左子树
    if root.right == None:
        return min_depth(root.left) + 1

    return 1 + min(min_depth(root.left), min_depth(root.right))
        
Tree = Node(1, Node(2, Node(4), Node(5)), Node(3))
Tree = Node(10, Node(5))
print(min_depth(Tree))
