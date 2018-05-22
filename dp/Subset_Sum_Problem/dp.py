# !/usr/bin/env python
# -*- coding: utf-8 -*-

def f(arr, n, t):
    # init
    dp = [[0 for x in range(t+1)] for x in range(n+1)]
    # bottom-up
    for i in range(n+1):
        for j in range(t+1):  # 一定要记住，j为当前匹配值的大小
           if arr[i-1] > j:
               # j-0：当前值不合适，当前状态等于上一状态
               dp[i][j] = dp[i-1][j-0]
           else:
               # j-arr[i-1]: 采用了当前值,则相应的过去状态发生了改变
               dp[i][j] = dp[i-1][j-arr[i-1]] + arr[i-1] 
           if dp[i][j] == t:
               return True
    return False

lst = [3, 34, 4, 12, 5, 2]
s = 38
print(f(lst, len(lst), s))
