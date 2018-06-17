# -*- coding: utf-8 -*-

class BTNode(object):
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

def create_tree():
    return BTNode(1, BTNode(2, BTNode(4), BTNode(5)), BTNode(3))

# 树的深度
def tree_depth(p):
    if p is None:
        return 0
    left = tree_depth(p.left)
    right = tree_depth(p.right)
    return left + 1 if left > right else right + 1

# 递归层序遍历
def layer_dfs(p, level):
    if level == 1:
        print(p.data)
    if p.left:
        layer_dfs(p.left, level-1)
    if p.right:
        layer_dfs(p.right, level-1)

def layer_order(p):
    depth = tree_depth(p)
    for i in range(1, depth+1):
        layer_dfs(p, i)

# 非递归层序遍历
def layer_order_iter(p):
    q = []
    q.append(p)
    while len(q) > 0:
       p = q[0]
       q = q[1:]
       print(p.data)
       if p.left:
           q.append(p.left)
       if p.right:
           q.append(p.right)

# 递归后序遍历
def post_order(p):
    if p is None:
        return None
    post_order(p.left)
    post_order(p.right)
    print(p.data)

# 非递归后序遍历
def post_order_iter(p):
    s = []
    while p or len(s) > 0:
        while p:
            s.append((p, 0))
            p = p.left
        p, tag = s.pop()
        if tag == 0:
            s.append((p, 1))
            p = p.right
        else:
            print(p.data)
            p = None

# 前序遍历递归
def preorder(p):
    if p is None:
        return None
    print(p.data)
    preorder(p.left)
    preorder(p.right)

# 非递归
def preorder_iter(p):
    s = []
    s.append(p)
    while len(s) > 0:
        p = s.pop()
        while p:
            print(p.data)
            if p.right:
                s.append(p.right)
            p = p.left
# 中序遍历
def inorder(p):
    if p is None:
        return None
    inorder(p.left)
    print(p.data)
    inorder(p.right)
   
def inorder_iter(p):
    s = []
    while p or len(s) > 0:
        while p:
            s.append(p)
            p = p.left
        p = s.pop()
        print(p.data)
        p = p.right

if __name__ == '__main__':
    print(" -- layer order -- ")
    tree = create_tree()
    layer_order(tree)
    print(" --- ")
    layer_order_iter(tree)

    print(" -- post order --")
    tree = create_tree()
    post_order(tree)
    print(" --- ")
    post_order_iter(tree)

    print(" -- preorder --")
    tree = create_tree()
    preorder(tree)
    print(" --- ")
    preorder_iter(tree)
   
    print(" -- inorder --")
    tree = create_tree()
    inorder(tree)
    print(" --- ")
    inorder_iter(tree)
