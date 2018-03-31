# !/usr/bin/env python
# -*- coding: utf-8 -*-

# O(n^2)
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i, n):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
   

lst = [3, 1, 5, 2, 8, 7, 6]
bubble_sort(lst)
print(lst)
