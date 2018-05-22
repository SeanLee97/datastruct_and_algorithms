# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
# Check if a given array can represent Preorder Traversal of Binary Search Tree
Given an array of numbers, return true if given array can represent preorder traversal of a Binary Search Tree, else return false. Expected time complexity is O(n).
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
            # v做右子树
            root = stack.pop()  # 栈顶出栈作为根
        stack.append(v)
    return True

lst = [2, 4, 1]
print(f(lst))
