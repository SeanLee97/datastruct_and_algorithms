# !/usr/bin/env python
# -*- coding: utf-8 -*-

def select_sort(lst):
    n = len(lst)
    for i in range(n):
        minimum = lst[i]
        minidx = i
        for j in range(i, n):
            if lst[j] < minimum:
                minimum = lst[j]
                minidx = j
        t = lst[i]
        lst[i] = minimum
        lst[minidx] = t

lst = [3, 5, 1, 7, 2]
select_sort(lst)
print(lst)
