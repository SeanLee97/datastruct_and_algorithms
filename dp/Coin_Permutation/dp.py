# -*- coding: utf-8 -*-
'''
题目描述：
给定一个值N，表示需要兑换的金额为N，现在拥有可以无限供应的、面值为S={s1, s2, s3, ...}的硬币，请找出所有选择方案
分析：
对于每个硬币只有两种情况，1. 选择该硬币 2. 不选
'''

def solution(S, N):
    n = len(S)
    dp  = [0]*(N+1)
    dp[0] = 1
    for i in range(n): # 先从每一种面值出发
        for j in range(N+1):
            if j >= S[i]:  #大于当前面值就选
                dp[j] += dp[j-S[i]]
    return dp[N]

if __name__ == '__main__':
    S = [1, 2, 5, 10, 20, 50]
    N = 5
    print("totoal solutions", solution(S, N))
