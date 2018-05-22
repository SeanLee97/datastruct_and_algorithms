# !/usr/bin/env python
# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def check_full(root):
    if root == None:
        return True
    if root.left == None and root.right != None:
        return False
    return check_full(root.left) and check_full(root.right)
    

tree = Node(1, Node(2, None, Node(5)), Node(3))
print(check_full(tree))
