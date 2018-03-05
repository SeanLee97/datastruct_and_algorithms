# !/usr/bin/env python
# -*- coding: utf-8 -*-

def f(arr, n, t):
    if n == 0 and t != 0:
        return False
    # 为真的条件为t减少到0
    if t == 0:
        return True
    # 当当前值大与t时则不取当前值，回到之前的状态
    if arr[n-1] > t:
       return f(arr, n-1, t)
    # 有两种状态：1. 选择当前数 2.不选当前数
    # 使得两种状态做与运算，条件会一直为真到结束
    return f(arr, n-1, t) or f(arr, n-1, t-arr[n-1])
    

lst = [3, 34, 4, 12, 5, 2]
t = 18
print(f(lst, len(lst), t)) 
