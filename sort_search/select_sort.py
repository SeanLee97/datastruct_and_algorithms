# !/usr/bin/env python
# -*- coding: utf-8 -*-

def select_sort(lst):
    n = len(lst)
    for i in range(n):
        minidx = i
        for j in range(i+1, n):
            if lst[j] < lst[minidx]:
                minidx = j
        if minidx != i:
            lst[i], lst[minidx] = lst[minidx], lst[i]

lst = [3, 5, 1, 7, 2]
select_sort(lst)
print(lst)
