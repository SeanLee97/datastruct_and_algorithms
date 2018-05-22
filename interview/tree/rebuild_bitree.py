# -*- coding: utf-8 -*-

# 根据二叉树的前序遍历和中序遍历的结果，重建出该二叉树。
# http://blog.csdn.net/yeoman92/article/details/77868367

class BiNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build(preorder, midorder):
    if len(preorder) == 0:
        return None
    if len(preorder) == 1:
        return BiNode(preorder[0])
    else:
        parent = BiNode(preorder[0])
        pidx = preorder.index(preorder[0])
        parent.left = build(preorder[1:pidx], midorder[:pidx])
        parent.left = build(preorder[pidx+1:], midorder[pidx+1:])
        return parent

def pre_echo(root):
    if root == None:
        return None
    print(root.val)
    pre_echo(root.left)
    pre_echo(root.right)

#tree = BiNode('A', BiNode('C', BiNode('B'), BiNode('E')), BiNode('D'))
pre = ['A', 'C', 'B', 'E', 'D']
mid = ['B', 'C', 'E', 'A', 'D']

tree = build(pre, mid)
pre_echo(tree)

