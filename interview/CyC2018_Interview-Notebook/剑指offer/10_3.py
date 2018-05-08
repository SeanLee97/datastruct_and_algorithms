# -*- coding: utf-8 -*-

"""题目描述
一只青蛙一次可以跳上 1 级台阶，也可以跳上 2 级... 它也可以跳上 n 级。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
"""

# 动态规划
def f(n):
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            dp[i] = dp[i] + dp[j]

    return dp[n-1]

if __name__ == '__main__':
    print(f(5))
