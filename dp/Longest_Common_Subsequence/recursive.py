# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 递归方案

def LCS(str1, str2, m, n):
    if m == 0 or n == 0:
        return 0
    if str1[m-1] == str2[n-1]:
        return 1 + LCS(str1, str2, m-1, n-1)
    else:
        return max(LCS(str1, str2, m-1, n), LCS(str1, str2, m, n-1))

str1 = 'ABCDGH'
str2 = 'AEDFHRB'
print(LCS(str1, str2, len(str1), len(str2)))
