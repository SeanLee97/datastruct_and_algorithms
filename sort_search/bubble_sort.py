# !/usr/bin/env python
# -*- coding: utf-8 -*-

# O(n^2)
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


lst = [3, 1, 5, 2, 8, 7, 6]
bubble_sort(lst)
print(lst)
