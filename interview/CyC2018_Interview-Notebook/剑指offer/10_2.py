# -*- coding: utf-8 -*-

"""题目描述
一只青蛙一次可以跳上 1 级台阶，也可以跳上 2 级。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
"""

# 1. 递归
def f1(n):
    if n <= 2:
        return n
    return f1(n-1) + f1(n-2)

# 2. 动态规划
def f2(n):
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]

# 3. 动态规划
def f3(n):
    a, b = 1, 2
    while n>2:
        a, b, n = b, a+b, n-1

    return b

if __name__ == '__main__':
    print(f1(7))
    print(f2(7))
    print(f3(7))
