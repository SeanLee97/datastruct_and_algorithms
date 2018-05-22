# !/usr/bin/env python
# -*- coding: utf-8 -*-

def f(mat, m, n):
    if m == 0 and n == 0:
        return mat[m][n]
    if m == 0 and n>0:
        return mat[m][n] + f(mat, m, n-1)
    if n == 0 and m>0:
        return mat[m][n] + f(mat, m-1, n) 
    return mat[m][n] + min(f(mat, m-1, n), f(mat, m, n-1), f(mat, m-1, n-1))

cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(f(cost, 2, 2))

