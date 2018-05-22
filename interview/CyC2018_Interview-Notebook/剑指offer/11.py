# -*- coding: utf-8 -*-

def get_min(lst):
    l = 0
    h = len(lst) - 1
    while l < h:
        m = (l+h) // 2
        if lst[m] > lst[h]:
            l = m + 1
        else:
            h = m
    return lst[l]

if __name__ == '__main__':
    n = get_min([3, 4, 5, 1, 2])
    print(n)
