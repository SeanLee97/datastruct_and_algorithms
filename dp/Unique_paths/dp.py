# -*- coding: utf-8 -*-

def f(m, n):
    dp = [[0 for i in range(n+1)] for i in range(m+1)]
    
    # init
    for i in range(m+1):
        dp[i][0] = 1
    for j in range(n+1):
        dp[0][j] = 1

    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

print(f(4, 5))
