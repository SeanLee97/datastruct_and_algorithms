# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 时间复杂度 Olog(n)

def insert_sort(lst):
    n = len(lst)
    for i in range(n):
        k = lst[i]
        j = i-1
        while j>=0 and k < lst[j]:
            lst[j+1] = lst[j]
            j-=1
        lst[j+1] = k

lst = [2, 1, 5, 9, 4, 3]
print(lst)
insert_sort(lst)
print(lst)
