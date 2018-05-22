# !/usr/bin/env python
# -*- coding: utf-8 -*-

def f(n):
    dp = [0]*(n+1)
    for i in range(n+1):
        if i == 0:
            dp[i] = 1
        elif i < 0:
            dp[i] = 0
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]

print(f(4))
