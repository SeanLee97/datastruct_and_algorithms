# !/usr/bin/env python
# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def max_path_sum(root):
   if root == None:
       return 0
   l = max_path_sum(root.left)
   r = max_path_sum(root.right)
   lr_max = max(root.data, max(l, r) + root.data)
   m = max(lr_max, l+r+root.data)
   max_path_sum.maximum = max(max_path_sum.maximum, m)
   return lr_max 
    
Tree = Node(10, Node(2, Node(20), Node(1)), Node(10, None, Node(-25, Node(3), Node(4))))
#Tree = Node(1, Node(2), Node(3))
max_path_sum.maximum = float('-inf')
max_path_sum(Tree)
print(max_path_sum.maximum)
