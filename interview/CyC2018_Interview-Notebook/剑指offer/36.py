# -*- coding: utf-8 -*-

"""题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return None
        stack = []
        p = pRootOfTree
        prev = None
        root = None
        # 迭代方式
        while p != None or len(stack) > 0:
            # 获取最左边的子树
            while p != None:
                stack.append(p)
                p = p.left
            p = stack.pop()
            if root is None:
                root  = p
                prev = root
            else:
                prev.right = p
                p.left = prev
                prev = p
            p = p.right
        return root

if __name__ == '__main__':
    t = TreeNode(6, TreeNode(4), TreeNode(8))
    s = Solution()
    root = s.Convert(t)
    print(root)
