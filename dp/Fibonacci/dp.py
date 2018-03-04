# !/usr/bin/env python
# -*- coding: utf-8 -*-

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, b+a
    return b

print(fib(30))
