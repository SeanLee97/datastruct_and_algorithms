# -*- coding: utf-8 -*-

"""题目描述
我们可以用 2*1 的小矩形横着或者竖着去覆盖更大的矩形。请问用 n 个 2*1 的小矩形无重叠地覆盖一个 2*n 的大矩形，总共有多少种方法？
"""

def f(n):
    if n <= 2:
        return n
    dp = [0]*n
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]

if __name__ == '__main__':
    print(f(5))
