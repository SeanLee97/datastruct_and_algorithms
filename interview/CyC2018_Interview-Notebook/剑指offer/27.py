# -*- coding: utf-8 -*-

"""题目描述
操作给定的二叉树，将其变换为源二叉树的镜像

二叉树的镜像定义：源二叉树 
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11

    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
"""

def mirror(root):
    if root is None:
        return None

    # swap left and right
    root.left, root.right = root.right, root.left
    self.Mirror(root.left)
    self.Mirror(root.right)
    return root
