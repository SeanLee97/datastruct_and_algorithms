# -*- coding: utf-8 -*-

"""
基数排序
非比较排序方法，结合了桶排序和计数排序的思想，对数按位来排序
https://www.cnblogs.com/skywang12345/p/3603669.html
"""

# 计数排序,在这里最大值是9
def count_sort(lst, base):
    # base 位数
    n = len(lst)
    bucket = [0]*10  # 每个位出现数的范围 0-9
    tmp = [0]*n

    # 分桶
    for i in range(n):
        bucket[(lst[i] // base)%10] += 1

    # 统计bucket中，小于等于i的元素个数
    for i in range(1, 10):
        bucket[i] += bucket[i-1]

    # 将数据存储到tmp中
    for i in range(n-1, -1, -1):
        v = lst[i]
        pos = bucket[(lst[i]//base)%10]
        tmp[pos-1] = lst[i]
        bucket[(lst[i]//base)%10] -= 1

    # 将排好序的数据复制给lst
    for i in range(n):
        lst[i] = tmp[i]


def radix_sort(lst):
    n = len(lst)
    maximum = max(lst)
    base = 1
    while maximum // base > 0:
        count_sort(lst, base)
        base *= 10

if __name__ == '__main__':
    lst = [3, 2, 28, 66]
    radix_sort(lst)
    print(lst)
