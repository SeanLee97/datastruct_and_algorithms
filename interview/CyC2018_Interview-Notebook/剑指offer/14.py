# -*- coding: utf-8 -*-

"""题目描述
把一根绳子剪成多段，并且使得每段的长度乘积最大。

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).
"""

# 动态规划
def breakline(n):
    dp = [0]*(n+1)
    dp[1] = 1
    # 计算将每个数切割得到的可能
    for i in range(2, n+1):
        # 自问题，在该切割下的最大各部分最大乘积
        for j in range(1, i):
            dp[i] = max(dp[i], max(j*(i-j), dp[j]*(i-j)))
    return dp[n]

print(breakline(10))
