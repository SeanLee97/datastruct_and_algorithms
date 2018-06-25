# -*- coding: utf-8 -*-

def solution(lst):
    m = 0
    maximum = 0
    for v in lst:
        m = max(v, m+v)
        if m > maximum:
            maximum = m
    return maximum

if __name__ == '__main__':
    print(solution([1, 2, -1, 3]))
