# !/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def f(m, n):
    dp = [0] * (n+1)
    dp[0] = m
    for i in range(1, n+1):
        dp[i] = m*math.pow(m-1, i-1) - dp[i-1]
    return int(dp[n])

print(f(4 ,6))
