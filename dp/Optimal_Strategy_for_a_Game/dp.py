# !/usr/bin/env python
# -*- coding: utf-8 -*-

def f(lst):
    n = len(lst)
    # init
    dp = [[0 for x in range(n+1)] for x in range(n+1)]
    # bottom-up
    for i in range(n+1):
        begin = 0
        end = i # 当前的结束位置
        while end < n:
            x, y, z = 0, 0, 0
            if begin+2 <= end:
                x = dp[begin+2][end]
            if begin+1 <= end-1:
                y = dp[begin+1][end-1]
            if begin <= end-2:
                z = dp[begin][end-2]
            # 当前状态
            dp[begin][end] = max(lst[begin]+min(x, y), lst[end]+min(y, z))
            begin += 1
            end += 1
    return dp[0][n-1]

lst = [3, 9, 1, 2]
print(f(lst))
