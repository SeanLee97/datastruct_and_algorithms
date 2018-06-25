# -*- coding: utf-8 -*-

"""
计数排序
非比较排序，桶排序原理
"""

# 解法1. 利用最大最小值来开辟具体的空间(易于理解)
def count_sort_v2(lst):
    minimum = min(lst)
    maximum = max(lst)
    n = len(lst)
    size = maximum - minimum + 1
    bucket = [0]*size
    ret = []
    for i in range(n):
        bucket[lst[i]-minimum] += 1

    # out
    for i in range(size):
        for j in range(bucket[i]):
            ret.append(minimum + i)

    for i in range(n):
        lst[i] = ret[i]

# 解法2. 正式解法，仅用最大值
def count_sort(lst):
    n = len(lst)
    maximum = max(lst)
    bucket = [0]*(maximum+1)
    tmp = [0]*n

    # 分桶
    for v in lst:
        bucket[v] += 1

    # 统计bucket中，小于等于i的元素个数
    for i in range(1, maximum + 1):
        bucket[i] += bucket[i-1]

    # 找出元素所在位置,将该值加入到辅助数组指定位置上
    for i in range(n-1, -1, -1):
        v = lst[i]
        pos = bucket[v] # 查看该值应该在哪个位置
        tmp[pos-1] = lst[i]
        bucket[v] -= 1

    for i in range(n):
        lst[i] = tmp[i]


if __name__ == '__main__':
    lst = [2, 11, 3, 4, 1]
    count_sort(lst)
    print(lst)
