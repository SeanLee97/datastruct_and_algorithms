# -*- coding: utf-8 -*-

def dpf(mat, m, n):
    # init
    dp = [[0 for x in range(m+1)] for x in range(n+1)]
    dp[0][0] = mat[0][0]
    for i in range(1, m+1):
        dp[i][0] = mat[i][0] + dp[i-1][0]
    for j in range(1, n+1):
        dp[0][j] = mat[0][j] + dp[0][j-1]
    # bottom-up
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = mat[i][j] + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
    return dp[m][n]

cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(dpf(cost, 2, 2))
