# -*- coding:utf-8 -*-

"""根据先序遍历和中序遍历得到后序遍历，方法：重构树+后序遍历
"""

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build(pre_order, in_order):
    if len(pre_order) == 0:
        return None
    root = TreeNode(pre_order[0])
    mid = in_order.index(pre_order[0])
    root.left = build(pre_order[1: mid+1], in_order[:mid])
    root.right = build(pre_order[mid+1:], in_order[mid+1:])
    return root

def postorder(pRoot):
    if pRoot is None:
        return
    postorder(pRoot.left)
    postorder(pRoot.right)
    print(pRoot.val)

def rebuild(pre_order, in_order):
    assert len(pre_order) == len(in_order)
    root = build(pre_order, in_order)
    postorder(root)
    

if __name__ == '__main__':
    pre_order = [1, 2, 4, 5, 3]
    in_order = [4, 2, 5, 1, 3]
    rebuild(pre_order, in_order)
