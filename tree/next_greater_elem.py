# -*- coding: utf-8 -*-

# for loop
def f1(lst):
    d = {}
    n = len(lst)
    for i in range(n):
        flag = True
        j = i+1
        while flag and j<n:
            if lst[j] > lst[i]:
                d[lst[i]] = lst[j]
                flag = False
            j+=1
        if flag is True:
            d[lst[i]] = -1
    print(d)

# use stack
def f2(lst):
    # init
    d = dict(list(zip(lst, [-1]*len(lst))))
    # use stack
    stack = []
    for v in lst:
        while len(stack) > 0  and stack[-1] < v:
            p = stack.pop()
            d[p] = v
        stack.append(v)
    print(d)  

f1([11, 13, 21, 3])
f2([11, 13, 21, 3])
                
