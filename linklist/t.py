# -*- coding: utf-8 -*-

import random

def partition(lst, low, high):
    rand_idx = random.randint(low, high)
    lst[rand_idx], lst[high] = lst[high], lst[rand_idx]
    store_idx = low
    privot = lst[high]
    for i in range(low, high):
        if lst[i] < privot:
            lst[store_idx], lst[i] = lst[i], lst[store_idx]
            store_idx += 1
    lst[store_idx], lst[high] = lst[high], lst[store_idx]
    return store_idx

def quick_sort(lst):
    if len(lst) == 0:
        return []
    low = 0
    high = len(lst)-1
    stack = []
    stack.append((low, high))
    while len(stack) > 0:
        low, high = stack.pop()
        while low < high:
            mid = partition(lst, low, high)
            if mid < high:
                stack.append((mid+1, high))
            high = mid - 1

def build_max_heap(lst, n, root):
    L = 2 * root + 1
    R = 2 * root + 2
    largest = root
    if L < n and lst[L] > lst[largest]:
        largest = L
    if R < n and lst[R] > lst[largest]:
        largest = R
    if root != largest:
        lst[largest], lst[root] = lst[root], lst[largest]
        build_max_heap(lst, n, largest)

def heap_sort(lst):
    n = len(lst) - 1
    for i in range(n//2, -1, -1):
        build_max_heap(lst, n, i)

    for i in range(n, -1, -1):
        lst[0], lst[i] = lst[i], lst[0]
        build_max_heap(lst, i, 0)
        #lst[0], lst[i] = lst[i], lst[0]

if __name__ == '__main__':
    lst = [3, 1, 2, 4, 1, 2]
    heap_sort(lst)
    #quick_sort(lst)
    print(lst)

