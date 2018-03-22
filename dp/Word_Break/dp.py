# !/usr/bin/env python
# -*- coding: utf-8 -*-

vocab = ["mobile","samsung","sam","sung",
         "man","mango","icecream","and",
         "go","i","like","ice","cream"]

def f(inp):
    n = len(inp)
    dp = [False]*(n+1)
    dp[0] = True
    for i in range(n+1):
        if dp[i]:
            j = 1
            while i+j-1 < n: 
                if inp[i:i+j] in vocab:
                    dp[i+j] = True
                j += 1
    return dp[n]

inp = 'ilikesamsungandicecream'
print(f(inp))
