# !/usr/bin/env python
# -*- coding: utf-8 -*-

# O(n^2)
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n):
            if lst[i] < lst[j]:
                t = lst[i]
                lst[i] = lst[j]
                lst[j] = t
   

lst = [3, 1, 5, 2, 8, 7, 6]
bubble_sort(lst)
print(lst)
