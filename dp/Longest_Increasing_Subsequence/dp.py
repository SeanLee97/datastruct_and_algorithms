# !/usr/bin/env python
# -*- coding: utf-8 -*-

def LIS(arr, m):
    # init
    dp = [1]*(m+1)
    # bottom-up
    for i in range(1, m):
        curr_max = 1
        for j in range(i):
            if arr[j] < arr[i] and dp[j]+1 > dp[i]:
                dp[i] = dp[j] + 1
    maximum = 0
    for i in range(m):
        maximum = max(maximum, dp[i])
    return maximum

arr = [3, 10, 2, 5, 20]
print(LIS(arr, len(arr))) 
                
