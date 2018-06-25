# -*- coding: utf-8 -*-

# 求二进制中1的位数
"""
本方案提供一个更具泛化性的方法
"""

def solution(num):
    i = 0
    if num < 0:
        num &= 0x7FFF   # 如果是负数则最高位为1，此时将其置0变为正数
        i += 1  # 由于最高位为1但是被0x7给置0了，所以i要先加1
    while num > 0:
        num &= (num-1)
        i += 1
    return i

if __name__ == '__main__':
    print(solution(1))
    print(solution(3))
    print(solution(5))
