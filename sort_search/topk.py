# -*- coding: utf-8 -*-

""" 
取topK个小/大的数字（已经排列）
利用小/大顶堆实现
"""

def min_heap(lst, n, root):
    L = root * 2 + 1
    R = root * 2 + 2
    minimum = root
    if L < n and lst[L] < lst[minimum]:
        minimum = L
    if R < n and lst[R] < lst[minimum]:
        minimum = R
    if root != minimum:
        lst[minimum], lst[root] = lst[root], lst[minimum]
        min_heap(lst, n, minimum)

def max_heap(lst, n, root):
    L = root*2 + 1
    R = root*2 + 2
    maximum = root
    if L < n and lst[L] > lst[maximum]:
        maximum = L
    if R < n and lst[R] > lst[maximum]:
        maximum = R
    if root != maximum:
        lst[maximum], lst[root] = lst[root], lst[maximum]
        max_heap(lst, n, maximum)

def heap_sort_k(lst, k, fn):
    n = len(lst)
    ret = []
    for i in range((n-1)//2, -1, -1):
        fn(lst, n, i)
    for i in range(n-1, n-k-1, -1):
        lst[0], lst[i] = lst[i], lst[0]
        yield lst[i]
        fn(lst, i, 0)
    

lst = [4, 5, 3, 9, 1]
k = 3

# 前topK个小数
for i in heap_sort_k(lst, k, min_heap):
    print(i)
# 前topK个大数
lst = [4, 5, 3, 9, 1]
for i in heap_sort_k(lst, k, max_heap):
    print(i)
