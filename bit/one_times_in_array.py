# -*- coding: utf-8 -*-

# 题目描述:
# 在一个数组中除了一个数字只出现1次外，其他均出现2次，求这个数字
# 思路：异或，x ^ x = 0 ，重复的数字经过异或都变为了0剩下的就是要找的数字

def solution(lst):
    v  = 0  # x ^ 0x0000...0000 = x
    for x in lst:
        v ^= x
    return v

if __name__ == '__main__':
    print(solution([1, 2, 3, 1, 2]))
