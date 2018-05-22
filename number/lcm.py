# -*- coding: utf-8 -*-

# 最小公倍数
def gcd(a, b):
    if a > b:
        a, b = b, a
    if b%a == 0:
        return a
    return gcd(b, b%a)

def lcm(a, b):
    return a*b / gcd(a, b)

print(lcm(5, 6))
