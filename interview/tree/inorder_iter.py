# -*- coding: utf-8 -*-

"""题目描述
迭代中序遍历二叉树
"""

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(pRoot):
    if pRoot is None:
        return None
    stack = []
    while pRoot or len(stack) > 0:
        while pRoot:
            stack.append(pRoot)
            pRoot = pRoot.left
        p = stack.pop()
        print(p.val)
        pRoot = p.right


if __name__ == '__main__':
    t = TreeNode(6, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(8))
    inorder(t)
