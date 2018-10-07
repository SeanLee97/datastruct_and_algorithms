# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random
# 时间复杂度Olog(n)
# 空间复杂度O(1)  -> store_idx
def quick_sort(lst, low, high):
    s = [(low, high)]
    while len(s) > 0:
        low, high = s.pop()
        while low < high:
            pidx = partition(lst, low, high)
            if low < high:
                low = pidx + 1
                s.append((low, high))
            high = pidx - 1

def partition(lst, low, high):
    store_idx = low
    # 选取最后一个元素作为基准，可能会出现最坏情况
    # pivot = lst[high]
    rand_pivot_idx = random.randint(low, high)
    lst[rand_pivot_idx], lst[high] = lst[high], lst[rand_pivot_idx]
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


lst = [2, 1, 4, 3, 1, 1]
quick_sort(lst, 0, len(lst)-1)
print(lst)
