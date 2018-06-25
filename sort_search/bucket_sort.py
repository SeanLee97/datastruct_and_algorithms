# -*- coding: utf-8 -*-

"""
桶排序
非比较排序算法
"""

def bucket_sort(lst):
    maximum = max(lst)
    bucket = [0]*(maximum+1)
    ret = []
    # 分桶
    for v in lst:
        bucket[v] += 1
    # 排序
    for v in range(maximum + 1):
        for i in range(bucket[v]):
            ret.append(v)
    for i in range(len(lst)):
        lst[i] = ret[i]

if __name__ == '__main__':
    lst = [3, 6, 9, 6, 2]
    bucket_sort(lst)
    print(lst)
