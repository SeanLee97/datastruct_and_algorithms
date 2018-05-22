# !/usr/bin/env python
# -*- coding: utf-8 -*-

def f(m, n):
    if m < 0 or n < 0:
        return 0
    if m == 1 or n == 1:
        return 1
    return f(m-1, n) + f(m, n-1)

print(f(8, 6))
