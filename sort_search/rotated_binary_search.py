# -*- coding: utf-8 -*-

"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might
 become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.

"""
def binary_search(lst, target):
    n = len(lst)
    if n < 1:
        return -1
    low, high = 0, n-1 
    while low <= high:
        mid = high - (high-low)//2
        if lst[mid] == target:
            return mid 
        if lst[low] < lst[mid]: # 左边升序
            if lst[low] <= target and target <= lst[mid]:
                # 左边升序，目标在左边
                high = mid-1
            else:
                low = mid+1
        elif lst[low] > lst[mid]: # 右边升序
            if lst[mid] <= target and target<=lst[high]:
                low = mid+1
            else:
                high = mid-1
        else:
            low += 1
    return -1

if __name__ == '__main__':
    lst = [4, 5, 6, 0, 1, 2]
    print(binary_search(lst, 0))
