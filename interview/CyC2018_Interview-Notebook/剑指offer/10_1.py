# -*- coding: utf-8 -*-

"""题目描述
求菲波那契数列的第 n 项
"""

# 1 递归
def fib1(n):
    if n < 2:
        return n
    return fib1(n-1) + fib1(n-2)

# 2 缓存
from functools import lru_cache
@lru_cache(None)
def fib2(n):
    if n < 2:
        return n
    return fib1(n-1) + fib1(n-2)


# 3 动态规划
def fib3(n):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# 4 最优动态规划
def fib4(n):
    a, b = 0, 1
    while n>=2:
        a, b ,n = b, a+b, n-1
    return b

if __name__ == '__main__':
    print(fib1(7))
    print(fib2(7))
    print(fib3(7))
    print(fib4(7))
