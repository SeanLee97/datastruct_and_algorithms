# -*- coding: utf-8 -*-

"""
给定一个 double 类型的浮点数 base 和 int 类型的整数 exponent。求 base 的 exponent 次方。
"""

def _power(x, n):
    result = 1
    while n > 0:
        if n & 1 == 1:
            # 判断是否为奇数，如果是奇数则计算result
            result *= x
        n >>= 1
        x *= x
    return result

def power(x, n):
    pn = n if n > 0 else -n
    result = _power(x, pn)
    return 1.0 / result if n < 0 else result

print(power(2, -3))
