# !/usr/bin/env python
# -*- coding: utf-8 -*-

def LCS(str1, str2, m, n):
    # init
    dp = [[0]*(n+1)] * (m+1)

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

str1 = 'ABCDGH'
str2 = 'AEDFHRB'
print(LCS(str1, str2, len(str1), len(str2)))
