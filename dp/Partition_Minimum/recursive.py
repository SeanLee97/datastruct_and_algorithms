# !/usr/bin/env python
# -*- coding: utf-8 -*-

def f(arr, m, set_total, total):
    if m == 0:
        return abs((total - set_total) - set_total)
    # 1. 不选择当前数，则当前差值 = 先前最小差值
    c1 = f(arr, m-1, set_total, total)
    # 2. 选择当前数，则当前差值 = 包含当前数的先前差值
    c2 = f(arr, m-1, set_total+arr[m-1], total)
    return min(c1, c2)

lst = [1, 6, 11, 5]
print(f(lst, len(lst), 0, sum(lst)))
