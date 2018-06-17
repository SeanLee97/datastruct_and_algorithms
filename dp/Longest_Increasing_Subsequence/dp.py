# !/usr/bin/env python
# -*- coding: utf-8 -*-

def LIS(arr, m):
    # init
    dp = [1]*(m+1)
    # bottom-up
    for i in range(1, m):
        for j in range(i):
            # 将当前值和之前的值依次比较看看递增大小为多少
            if arr[j] < arr[i] and dp[j]+1 > dp[i]:
                dp[i] = dp[j] + 1
    maximum = 0
    for i in range(m):
        maximum = max(maximum, dp[i])
    return maximum

arr = [5, 2, 11, 2, 20]
print(LIS(arr, len(arr))) 
                
