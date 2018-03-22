# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 时间复杂度Olog(n)
# 空间复杂度O(1)  -> store_idx
def quick_sort(lst, low, high):
    if low < high:
        pi = partition(lst, low, high)
        quick_sort(lst, low, pi-1)
        quick_sort(lst, pi+1, high)

def partition(lst, low, high):
    store_idx = low
    pivot = lst[high]
    for j in range(low, high):
        if lst[j] <= pivot:
            '''
            t = lst[j]
            lst[j] = lst[store_idx]
            lst[store_idx] = t 
            '''
            # 以下python语句可以一步完成两值的交换
            lst[store_idx], lst[j] = lst[j], lst[store_idx]
            store_idx += 1
    # 将pivot和探针所指位置互换
    lst[store_idx], lst[high] = lst[high], lst[store_idx]
    return store_idx


lst = [10, 80, 30, 90, 40, 50, 70]
quick_sort(lst, 0, len(lst)-1)
print(lst)
         
        
