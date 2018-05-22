# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Print Binary Tree in Vertical Order OR
Print the Binary Tree in Vertical Order Path OR
Vertical order traversal of a Binary Tree. 
Find Vertical Sum of given Binary Tree
'''
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

def echo(record):
    for level, lst in record.items():
        print(level)        
        for obj in lst:
            print(' ', obj.val)

tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
record = defaultdict(list)
vertical_order(tree, 0, record)
echo(record)
