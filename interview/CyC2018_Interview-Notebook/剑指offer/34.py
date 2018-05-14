# -*- coding: utf-8 -*-

"""题目描述
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
"""

import copy

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:

    def find(self, root, tgt, v, lst, alst):
        if root is None:
            return

        v += root.val
        lst.append(root.val)
        
        if v < tgt:
            self.find(root.left, tgt, v, lst, alst)
            self.find(root.right, tgt, v, lst, alst)
        elif v == tgt:
            #print(v, tgt, lst)
            if root.left is None and root.right is None: 
                alst.append(copy.copy(lst))  # 这里要用到浅复制，由于下面用到pop()如果不复制的话那么会跟着改变
        # 移除当前结点
        lst.pop()

    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        lst, alst = [], []
        self.find(root, expectNumber, 0, lst, alst)
        return alst


if __name__ == '__main__':
    t = TreeNode(10, TreeNode(5, TreeNode(4), TreeNode(7)), TreeNode(12))
    s = Solution()
    lst = s.FindPath(t, 22)
    print(lst)
