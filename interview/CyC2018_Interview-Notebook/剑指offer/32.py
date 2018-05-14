# -*- coding:utf-8 -*-

"""题目描述
(层序遍历二叉树)
从上往下打印出二叉树的每个节点，同层节点从左至右打印
"""

from collections import defaultdict

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def hdview(self, root, hd, level):
        if root is None:
            return None
        hd[level].append(root.val)
        self.hdview(root.left, hd, level+1)
        self.hdview(root.right, hd, level+1)

    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        hd = defaultdict(list)
        self.hdview(root, hd, 0)
        lst = []
        for k, v in hd.items():
            lst.extend(v)
        return lst

if __name__ == '__main__':
    t = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4))
    s = Solution()
    lst = s.PrintFromTopToBottom(t)
    print(lst)
