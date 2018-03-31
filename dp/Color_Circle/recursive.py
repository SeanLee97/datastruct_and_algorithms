# !/usr/bin/env python
# -*- coding: utf-8 -*-

# m, 颜色数
# n, 分块数
import math
def f(m, n):
    if n < 1:
        return m
    return m*math.pow(m-1, n-1) - f(m, n-1)

print(f(4, 6))
