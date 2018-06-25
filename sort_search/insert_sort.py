# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 时间复杂度 O(n^2)

def insert_sort(lst):
    n = len(lst)
    for i in range(1, n):
        k = lst[i]  # 新选择的数
        j = i-1
        while j>=0 and k < lst[j]:  # 和之前的数比较，放在合适的位置
            lst[j+1] = lst[j]
            j-=1
        lst[j+1] = k

lst = [2, 1, 5, 9, 4, 3]
print(lst)
insert_sort(lst)
print(lst)
