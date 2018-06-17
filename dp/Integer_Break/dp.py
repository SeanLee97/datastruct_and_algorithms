# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 题目描述：For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).
'''
正整数从1开始，但是1不能拆分成两个正整数之和，所以不能当输出。
那么2只能拆成1+1，所以乘积也为1。
数字3可以拆分成2+1或1+1+1，显然第一种拆分方法乘积大为2。
数字4拆成2+2，乘积最大，为4。
数字5拆成3+2，乘积最大，为6。
数字6拆成3+3，乘积最大，为9。
数字7拆为3+4，乘积最大，为12。
数字8拆为3+3+2，乘积最大，为18。
数字9拆为3+3+3，乘积最大，为27。
数字10拆为3+3+4，乘积最大，为36。
'''

def f(n):
    dp = [1] * (n+1)
    for i in range(2, n+1):
        if i % 3 == 0:
            dp[i] = 3 * dp[i-3]
        elif n-i+1 == 4 or n-i+1 == 2:
            dp[i] = (n-i+1) * dp[i-1]
    
    maximum = 1
    for v in dp:
        maximum = max(v, maximum)
    return maximum

print(f(100))
