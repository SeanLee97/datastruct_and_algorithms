# -*- coding: utf-8 -*-

"""题目描述
根据二叉树的前序遍历和中序遍历的结果，重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
"""

class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def rebuild(prev, pL, pR, inn, iL, iR):
    if pL > pR:
        return None
    root = TreeNode(prev[pL])
    idx = inn.index(root.data)
    gap = idx - iL
    root.left = rebuild(prev, pL+1, pL+gap, inn, iL, iL+gap-1)
    root.right = rebuild(prev, pL+gap+1, pR, inn, iL+gap+1, iR)
    return root

def prevorder(root):
    if root != None:
        print(root.data)
        prevorder(root.left)
        prevorder(root.right)

if __name__ == '__main__':
    prev = [3, 9, 20, 15, 7]
    inn = [9, 3, 15, 20, 7]
    root = rebuild(prev, 0, len(prev)-1, inn, 0, len(inn)-1)
    prevorder(root)
