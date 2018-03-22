# -*- coding: utf-8 -*-

# 最大公约数
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

print(gcd(12, 15))
