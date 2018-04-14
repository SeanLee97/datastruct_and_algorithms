# -*- coding: utf-8 -*-

# Given three numbers x, y and p, compute (x^y) % p.

# recursive power
def power_rf(x, y):
    if y == 1:
        return x
    return x * power(x, y-1)

# for loop
def power(x, y):
    res = 1
    while y > 0:
       # 如果y是奇数，那么res = res * x
       if y & 1:
           res *= x
       y = y>>1 # 右移一位（除2）
       x = x*x
    return res

def compute(x, y, p):
    return power(x, y) % p

print(compute(2, 5, 13))

