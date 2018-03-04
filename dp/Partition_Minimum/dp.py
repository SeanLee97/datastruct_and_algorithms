# !/usr/bin/env python
# -*- coding: utf-8 -*-

def f(arr, n, total):
    W = total//2
    
    # 将问题转化为类01背包问题，假设最大容量（为W），求子序列能达到的最大值
    dp = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, W+1):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], arr[i-1]+dp[i-1][j-arr[i-1]])

    return abs((total-dp[n][W]) - dp[n][W])

lst = [1, 6, 11, 5]
print(f(lst, len(lst), sum(lst)))

