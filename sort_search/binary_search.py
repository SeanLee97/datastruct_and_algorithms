# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 二分搜索对象是有序表
# 时间复杂度 O(logn)
def binary_search(lst, t):
    high = len(lst)-1
    low = 0
    while low <= high:
        mid = (low+high)//2
        if lst[mid] > t:
            high = mid - 1
        elif lst[mid] < t:
            low = mid + 1
        else:
            return mid
    return -1

lst = [3, 5, 8, 11, 13]
t = 11
print(t, binary_search(lst, t))
        
