# -*- coding: utf-8 -*-

"""题目描述

输入一棵二叉树，判断该二叉树是否是平衡二叉树。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def IsBalanced_Solution(self, pRoot):
        self.isbalance = True
        self.height(pRoot)
        return self.isbalance
        
    def height(self, pRoot):
        # write code here
        if pRoot == None:
            return 0
        left = self.height(pRoot.left)
        right = self.height(pRoot.right)
        if abs(left - right) > 1:
            self.isbalance =  False
        return left+1 if left > right else right + 1 
