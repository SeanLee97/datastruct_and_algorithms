# !/usr/bin/env python
# -*- coding: utf-8 -*-

maximum = 0

def LIS(arr, m):
    _LIS(arr, m)
    return maximum

def _LIS(arr, m):
    global maximum 
    if m == 1:
        return 1
    curr_max = 1
    for i in range(m):
        pre_max = _LIS(arr, i)
        if arr[i-1] < arr[m-1] and pre_max+1 > curr_max:
             curr_max = pre_max+1
    maximum = max(maximum, curr_max)
    return curr_max

arr = [3, 10, 2, 5, 20]
print(LIS(arr, len(arr)))

