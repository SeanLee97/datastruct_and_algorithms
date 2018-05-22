# -*- coding: utf-8 -*-

# 1
f1 = lambda n: 1 if n < 2 else f1(n-2) + f1(n-1)

# recursive
def f2(n):
    if n < 2:
        return 1
    return f2(n-2) + f2(n-1)

# cache
def cache(cls, *args):
    instance = {}
    def getinstance(*args):
        if cls not in instance:
            instance[args] = cls(*args)
        return instance[args]
    return getinstance

@cache
def f3(n):
    if n < 2:
        return 1
    return f3(n-2) + f3(n-1)

# dp
def f4(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, b+a
    return b

print('lambda:', f1(30))
print('recursive:', f2(30))
print('cache:', f3(30))
print('dp:', f4(30))
