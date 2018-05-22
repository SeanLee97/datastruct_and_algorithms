# !/usr/bin/env python
# -*- coding: utf-8 -*-

def _f(i, j, mat, dp):
    n = len(mat)
    if i < 0 or i>=n or j < 0 or j>=n:
        return 0
    steps = [1]
    # 向下移动
    if i>0 and mat[i][j] <= mat[i-1][j]:
        steps.append(1 + _f(i-1, j, mat, dp))
    # 向上移动
    if i<n-1 and mat[i][j] <= mat[i+1][j]:
        steps.append(1 + _f(i+1, j, mat, dp))
    # 向左移动
    if j>0 and mat[i][j] <= mat[i][j-1]:
        steps.append(1 + _f(i, j-1, mat, dp))
    # 向右移动
    if j<n-1 and mat[i][j] <= mat[i][j+1]:
        steps.append(1 + _f(i, j+1, mat, dp))
    # 选择移动步数最多的作为当前状态的值
    dp[i][j] = max(steps)
    return dp[i][j]

def f(mat):
    n = len(mat)
    result = 1
    dp = [[-1 for x in range(n)] for x in range(n)]
    for i in range(n):
        for j in range(n):
            if dp[i][j] == -1:
                # 从当前位置出发
                _f(i, j, mat, dp)
            result = max(result, dp[i][j])
    return result

mat = [
    [1, 2, 9],
    [5, 3, 8],
    [4, 2, 7]
] 
print(f(mat))
