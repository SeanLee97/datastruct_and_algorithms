# -*- coding: utf-8 -*-

"""题目描述
地上有一个 m 行和 n 列的方格。一个机器人从坐标 (0, 0) 的格子开始移动，每一次只能向左右上下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于 k 的格子。例如，当 k 为 18 时，机器人能够进入方格（35, 37），因为 3+5+3+7=18。但是，它不能进入方格（35, 38），因为 3+5+3+8=19。请问该机器人能够达到多少个格子？
"""

from functools import reduce

def sum(m, n):
    f = lambda x: reduce(lambda i, j: i+j, \
        list(map(lambda y: int(y), list(str(x)))))
    x1 = f(m)
    x2 = f(n)
    return x1 + x2

def find(m, n, i, j, k, flag):
    if i<0 or j<0 or i>=m or j>=n or sum(i, j)>k or flag[i][j]:
        return False
    flag[i][j] = True
    find.store += 1
    return (find(m, n, i+1, j, k, flag) or 
            find(m, n, i-1, j, k, flag) or
            find(m, n, i, j+1, k, flag) or
            find(m, n, i, j-1, k, flag))

def get_max(m, n, k):
    find.store = 0
    flag = [[False for x in range(n)] for x in range(m)]
    find(m, n, 0, 0, k, flag)
    return find.store
print(get_max(35, 38, 18))
