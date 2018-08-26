# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 洗牌算法(shuffle, 将有序表转为无序)生成随机数

import random

def shuffle(lst):
    n = len(lst)
    if n == 0:
        return
    for i in range(len(lst)-1, 0, -1):
        ridx = random.randint(0, i)
        lst[ridx], lst[i] = lst[i], lst[ridx]


if __name__ == '__main__':
    lst = [1, 2, 3, 4]
    shuffle(lst)
    print(lst)
    shuffle(lst)
    print(lst)
