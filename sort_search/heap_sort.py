# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 堆排序
def max_heap(lst, n, root):
    # root为当前根节点
    largest = root # 初始化最大值
    L = 2*root + 1 # 左子树
    R = 2*root + 2 # 右子树
    # 判断左子树是否存在，且是否大于根
    if L < n and  lst[L] > lst[largest]:
        largest = L
    # 判断右子树是否存在，且是否大于根
    if R < n and lst[R] > lst[largest]:
        largest = R
    # 如果最大值的下标不等于当前根的下标那么交换两者的值
    if largest != root:
        # 将较大值作为当前根的值
        lst[root], lst[largest] = lst[largest], lst[root]
        # 由于一次调整后，堆仍然违反堆性质，所以需要递归的测试，使得整个堆都满足堆性质
        max_heap(lst, n, largest)

def heap_sort(lst):
    n = len(lst) -1
    # 建立大顶堆
    # 作用是将一个数组改造成一个最大堆，为了保证下标i的结点之后的结点都能满足最大堆的性质，采用自下而上（数组中从后往前）的调用max_heap()函数来往上构建大顶堆
    for i in range(n, -1, -1):
        max_heap(lst, n, i)
    
    # 从底往上（对应数组的从后往前）抽取元素,其中lst[0]必然是堆中最大元素，每次都将lst[i]和lst[0]位置互换，接着再重建大顶堆
    for i in range(n, 0, -1):
        # lst[0]
        lst[i], lst[0] = lst[0], lst[i]
        # 重建大顶堆
        max_heap(lst, i, 0)

lst = [ 12, 11, 13, 5, 6, 7]
heap_sort(lst)
print(lst)
