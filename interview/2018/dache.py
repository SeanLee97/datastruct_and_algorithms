# -*- coding: utf-8 -*-

def f(Wt, W, n):
    Vt = [1]*n
    dp = [[0 for x in range(W+1)] for x  in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, W+1):
            if Wt[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                x1 = Vt[i-1] + dp[i-1][j-Wt[i-1]]
                x2 = dp[i-1][j]
                dp[i][j] = max(x1, x2)
    return dp[n][W]


def solution():
    line = input()
    arr = line.strip().split()
    n = int(arr[0])
    W = int(arr[1])
    line = input()
    Wt = list(map(lambda x: int(x), line.strip().split()))
    Wt.sort()
    print(f(Wt, W, n))

solution()