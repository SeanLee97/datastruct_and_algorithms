# -*- coding: utf-8 -*-

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def is_subset(p1, p2):
    if p2 is None:
        return True
    if p1 is None:
        return False

    if p1.val == p2.val:
        return is_subset(p1.left, p2.left) and is_subset(p1.right, p2.right)
    else:
        return is_subset(p1.left, p2) or is_subset(p1.right, p2)

if __name__ == '__main__':
    
    p1 = TreeNode(4, TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(5))
    p2 = TreeNode(1, TreeNode(2), TreeNode(3))

    flag = is_subset(p1, p2)
    print(flag)
