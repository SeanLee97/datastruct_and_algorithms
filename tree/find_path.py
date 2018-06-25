# -*- coding: utf-8 -*-

"""
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
"""
import copy

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def find(self, root, val, target, tmp, result):
        if root is None:
            return
        val += root.val
        tmp.append(root.val)
        if val == target and root.left is None and root.right is None:
            result.append(copy.copy(tmp))
        self.find(root.left, val, target, tmp, result)
        self.find(root.right, val, target, tmp, result)
        tmp.pop()

    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if root is None:
            return []
        tmp = []
        result = []
        self.find(root, 0, expectNumber, tmp, result)
        return result
