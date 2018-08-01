# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
检测一个数组是否是一棵二叉搜索树的前序遍历，若是则返回True，否则返回false
'''
# 二叉搜索树：左子树小于根，右子树大于根
# 先序遍历：先根->左子->右子
def f(lst):
    root = float('-inf')
    stack = []
    for v in lst:
        # if right son < root -> False
        if v < root:
            return False
        while len(stack) > 0 and stack[-1] < v:
            # v 做右子树
            root = stack.pop()  # 栈顶出栈作为根
        stack.append(v)
    return True

lst = [5, 3, 2, 4, 6]
print(f(lst))
