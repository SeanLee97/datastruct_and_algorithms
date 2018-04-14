# -*- coding: utf-8 -*-

# 最大公约数


def gcd(a, b):
    if a > b:
        a, b = b, a
    if b%a == 0:
        return a
    return gcd(b, b%a)

print(gcd(3, 6))
