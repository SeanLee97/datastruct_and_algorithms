# -*- coding: utf-8 -*-

def solution(lst, k, d):
    ms = lst[0]
    i = 0
    n = len(lst)
    d = min(n, d)
    for i in range(n):
        for j in range(i+1, d):
            ms = max(ms, lst[i]*lst[j])
    return ms

if __name__ == '__main__':
    n = int(raw_input())
    line = raw_input().strip()
    lst = map(lambda x: int(x), line.split())
    line = raw_input().strip()
    arr = line.split()
    k = int(arr[0])
    d = int(arr[1])
    ms = solution(lst, k, d)
    print(ms)