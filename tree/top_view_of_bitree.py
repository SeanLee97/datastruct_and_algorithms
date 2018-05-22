# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Given a Binary Tree, we need to print the top view from left to right. A node x is there in output if x is the bottommost node at its horizontal distance. Horizontal distance of left child of a node x is equal to horizontal distance of x minus 1, and that of right child is horizontal distance of x plus 1.
这其实是个vertical-order问题
'''
# http://javabypatel.blogspot.jp/2015/10/print-binary-tree-in-vertical-order.html
# http://javabypatel.blogspot.jp/2015/10/print-binary-tree-in-vertical-order.html

from collections import defaultdict

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def vertical_order(root, level, record):
    record[level].append(root)
    if root.left != None:
        vertical_order(root.left, level-1, record)
    if root.right != None:
        vertical_order(root.right, level+1, record)

def bottom_view(root):
    record = defaultdict(list)
    vertical_order(root, 0, record)
    
    for level, lst in record.items():       
        print(lst[0].val)

tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))

bottom_view(tree)
