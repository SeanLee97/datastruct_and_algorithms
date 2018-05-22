# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# 递归方式
def check_recurse(S, T):
    if S == None:
        return True
    if T == None:
        return False
    if S.data == T.data:
        return check_recurse(S.left, T.left) and check_recurse(S.right, T.right)
    else:
        return check_recurse(S, T.left) or check_recurse(S, T.right)

# 先序中序唯一确定二叉数

def get_preorder(root, lst):
    if root != None:
        lst.append(root.data)
        get_preorder(root.left, lst)
        get_preorder(root.right, lst)

def get_inorder(root, lst):
    if root != None:
        get_inorder(root.left, lst)
        lst.append(root.data)
        get_inorder(root.right, lst)

def checkin(s, t):
    flag = True
    while flag:
        x = t.pop(0)
        if x == s[0]:
            s.pop(0)
            flag = False

    while True:
        if len(s) == 0:
            return True
        x = t.pop(0)
        y = s.pop(0)
        if x != y:
            return False

def check_order(S, T):
    spre, sin = [], []
    tpre, tin = [], []
    get_preorder(S, spre)
    get_preorder(T, tpre)
    
    if not checkin(spre, tpre):
        return False

    get_inorder(S, sin)
    get_inorder(T, tin)

    if not checkin(sin, tin):
        return False

    return True

S = Node(1, Node(2), Node(3))
T = Node(4, Node(1, Node(2), Node(3)), Node(5))

#flag = check_recurse(S, T)
flag = check_order(S, T)
print(flag)


