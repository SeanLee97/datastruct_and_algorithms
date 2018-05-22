# -*- coding:utf-8 -*-

class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def echo(root):
    if root == None:
        return
    echo(root.left)
    echo(root.right)
    print(root.data)

def build_tree(preorder, inorder, root):
    curr = preorder.pop(0)
    root.data = curr 
    try:
        idx = inorder.index(curr)
        l = inorder[:idx]
        r = inorder[idx:]
        #print(l, '##', r)
        if len(l) > 0 and len(set(preorder) & set(l)) > 0:
            root.left = Node()
            build_tree(preorder, l, root.left)
        if len(r) > 0 and len(set(preorder) & set(r)) > 0:
            root.right = Node()
            build_tree(preorder, r, root.right)
    except:
        pass
    return

def get_post(preorder, inorder):
    root = Node()
    tree = build_tree(preorder, inorder, root)
    # 输出 
    echo(root)
 
preorder = [4, 1, 2, 3, 5]
inorder = [2, 1, 3, 4, 5]
get_post(preorder, inorder)
