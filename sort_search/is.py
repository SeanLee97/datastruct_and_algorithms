# !/usr/bin/env python
# -*- coding: utf-8 -*-

def insert_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i):
            if lst[j] > lst[i]:
                lst[j+1] = lst[j]
            
