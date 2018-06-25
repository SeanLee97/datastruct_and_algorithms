# -*- coding: utf-8 -*-

# 操作给定的二叉树，将其变换为源二叉树的镜像。

class Solution(object):
    # 递归版本(先序遍历)
    def recursive(self, pRoot):
        if pRoot is None:
            return None
        pRoot.left, pRoot.right = pRoot.right, pRoot.left
        self.recursive(pRoot.left)
        self.recursive(pRoot.right)

    # 迭代版本
    def iter(self, pRoot):
        if pRoot is None:
            return None
        s = []
        s.append(pRoot)
        while len(s) > 0:
            pRoot = s.pop()
            while pRoot:
                pRoot.left, pRoot.right = pRoot.right, pRoot.left
                if pRoot.right:
                    s.append(pRoot.right)
                pRoot = pRoot.left

    def Mirror(self, root):
        self.iter(root)

