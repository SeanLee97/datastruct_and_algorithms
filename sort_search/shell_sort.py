# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 其实就是分组插入排序

def shell_sort(lst):
    n = len(lst)
    d = n // 2
    while d > 0:
        for i in range(n):
            # 插入排序
            k = lst[i]
            j = i-d
            while j>=0 and k < lst[j]:
                lst[j+d] = lst[j]
                j -= d
            lst[j+d] = k

        d //= 2

lst = [3, 9, 1, 8, 11]
shell_sort(lst)
print(lst)
