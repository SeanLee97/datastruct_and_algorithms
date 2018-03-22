# -*- coding: utf-8 -*-

# 最大公倍数 = a*b / gcd(a, b)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return a*b / gcd(a, b)

print(lcm(12, 15))

