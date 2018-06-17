# !/usr/bin/env python
# -*- coding: utf-8 -*-

def edit(str1, str2, m, n):
    # init
    dp = [[0 for _ in range(n)] for x  in range(m)]
    # bottom-up
    for i in range(1, m):
        for j in range(1, n):
            if i == 0 or j == 0:
                dp[i][j] = abs(i-j)
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],  # remove
                    dp[i][j-1],  # insert
                    dp[i-1][j-1] # replace
                )
    return dp[m-1][n-1]

src = 'peer'
tgt = 'pair'
print(edit(src, tgt, len(src), len(tgt)))
