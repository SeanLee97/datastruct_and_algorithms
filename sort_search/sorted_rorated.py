# !/usr/bin/env python
# -*- coding: utf-8 -*-

def find(lst, t):
    low = 0
    high = len(lst)-1
    while low <= high:
        mid = (low+high)//2
        if lst[mid] == t:
            return True
        if lst[mid] == lst[low]:
            low += 1
        elif lst[mid] > lst[low]: 
            if lst[mid] > t and lst[low] <= t: 
                high = mid - 1
            else:
                low = mid + 1
        else:
            if lst[mid] < t and lst[high] >= t:
                low = mid + 1
            else:
                high = mid -1
    return False

lst = [3, 4, 5, 1, 2]
print(find(lst, 1))
             
