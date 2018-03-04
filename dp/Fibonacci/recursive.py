# !/usr/bin python
# -*- coding: utf-8 -*-

fib = lambda x: 1 if x<2 else fib(x-1) + fib(x-2)

print(fib(30))
