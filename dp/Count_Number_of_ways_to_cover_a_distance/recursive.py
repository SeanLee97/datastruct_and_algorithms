# !/usr/bin/env python 
# -*- coding: utf-8 -*-

def f(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return f(n-1) + f(n-2) + f(n-3)

print(f(4))
