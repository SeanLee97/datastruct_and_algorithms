# -*- coding: utf-8 -*-

"""题目描述

输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
"""

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def get_pre(pRoot, lst):
    if pRoot:
        lst.append(str(pRoot.val))
        get_pre(pRoot.left, lst)
        get_pre(pRoot.right, lst)
    else:
        lst.append(str('$'))

def get_in(pRoot, lst):
    if pRoot:
        get_in(pRoot.left, lst)
        lst.append(str(pRoot.val))
        get_in(pRoot.right, lst)
    else:
        lst.append(str('$'))

def in_array( src, tgt):        
    n = len(src)
    i, j = 0, 0
    flag = False
    while j < len(tgt):
        if i == n:
            if flag:
                return True
            return False
        if not flag and tgt[j] == src[i]:
            flag = True
            i += 1
            j += 1
            continue
        if flag and tgt[j] != src[i]:
            i = 0
            j -= 1
            flag = False
        if flag:
            i += 1
        j+=1

    return False

def hasSubtree(pRoot1, pRoot2):
    if not pRoot2 or not pRoot1:
        return False
    pre1, pre2 = [], []
    in1, in2 = [], []
    get_pre(pRoot1, pre1)
    get_pre(pRoot2, pre2)
    #print(pre1, pre2)
    # check 
    if in_array(pre2, pre1):
        get_in(pRoot1, in1)
        get_in(pRoot2, in2)
        return in_array(in2, in1)
    return False

if __name__ == '__main__':
    #print(in_array([4, 1, 2], [4, 4, 1, 2, 3, 5]))
    root1 = TreeNode(8, TreeNode(8, TreeNode(9), TreeNode(2)), TreeNode(7, TreeNode(1), TreeNode(1)))
    root2 = TreeNode(8, TreeNode(9), TreeNode(2))
    print(hasSubtree(root1, root2))
