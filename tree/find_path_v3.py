# -*- coding: utf-8 -*-

"""
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的从任何结点到另一个更深层级的结点形成的路径。
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
        tmp.append(root.val)
        tmp_path = []
        tmp_val = 0
        for i in range(len(tmp)-1, -1, -1):
            tmp_val += tmp[i]
            tmp_path.append(tmp[i])
            if tmp_val == target:
                result.append(copy.copy(tmp_path))
        self.find(root.left, val, target, tmp, result)
        self.find(root.right, val, target, tmp, result)
        #tmp.pop()

    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if root is None:
            return []
        tmp = []
        result = []
        self.find(root, 0, expectNumber, tmp, result)
        return result
