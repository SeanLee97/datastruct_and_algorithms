# !/usr/bin/env python
# -*- coding: utf-8 -*-

def _merge_sort(lst, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid
    L = [0]*n1
    R = [0]*n2
    for i in range(0, n1):
        L[i] = lst[low+i]
    for j in range(0, n2):
        R[j] = lst[mid+j+1]

    i = 0
    j = 0
    k = low
   
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        lst[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        lst[k] = R[j]
        j += 1
        k += 1

def merge_sort(lst, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(lst, low, mid)
        merge_sort(lst, mid+1, high)
        _merge_sort(lst, low, mid, high)

lst = [5, 1, 7, 2, 6, 3]
merge_sort(lst, 0, len(lst)-1)
print(lst)
