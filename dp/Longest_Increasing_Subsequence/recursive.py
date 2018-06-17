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
        # 递归获取先前递增序列的最大值
        pre_max = _LIS(arr, i)
        # m-1为当前的标准数，依次比较先前的值，获得本次递增序列的大小
        if arr[i-1] < arr[m-1] and pre_max+1 > curr_max:
             curr_max = pre_max+1
    # 比较上一次和本次的结果
    maximum = max(maximum, curr_max)
    return curr_max

arr = [3, 10, 12, 15, 20]
print(LIS(arr, len(arr)))

