# !/usr/bin/env python
# -*- coding: utf-8 -*-

def shell_sort(lst):
    n = len(lst)
    d = n // 2
    while d > 0:
        for i in range(n):
            for j in range(i, 0, -d):
                if lst[j-d] > lst[j]:
                    lst[j-d], lst[j] = lst[j],lst[j-d]
        d = d // 2

lst = [3, 9, 1, 8, 11]
shell_sort(lst)
print(lst)
