# !/usr/bin/env python
# -*- coding: utf-8 -*-

def f(Vt, Wt, W, n):
    # init
    dp = [[0 for x in range(W+1)] for x in range(n+1)]
    # bottom-up
    for i in range(n+1):
        for j in range(W+1):  # 一定要记住j为容量
            if Wt[i-1] > j:
                dp[i][j] = dp[i-1][j] # 之前的价值
            else:
                dp[i][j] = max(dp[i-1][j], Vt[i-1]+dp[i-1][j-Wt[i-1]])
    return dp[n][W]

Vt = [60, 100, 120]
Wt = [10, 20, 30]
W = 50
print(f(Vt, Wt, W, len(Vt))) 
