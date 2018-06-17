# -*- coding: utf-8 -*-

"""题目描述
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. The same repeated number may be chosen from C unlimited number of times.
"""

def dfs(lst, n, t, tmp, res, pos):
    # 加了pos保证集合不重复，由于{2,2,3}和{3, 2, 2}是同一个集合，加了pos可以避免这种情况
    if t < 0:
        return
    elif t == 0:
        res.append(tmp.copy())
        return 
    for i in range(pos, n):
        # 如果选择了当前数则目标值t-=当前值
        tmp.append(lst[i])
        # pos = i 使得值可以重复选择
        dfs(lst, n, t-lst[i], tmp, res, i)  
        tmp.pop()

# lst有重复值的情况, 且集合中的数不能重复使用
def dfs1(lst, n, t, tmp, res, pos):
    if t == 0:
        res.append(tmp.copy())
        return
    elif t < 0:
        return 

    for i in range(pos, n):
        tmp.append(lst[i])
        # pos = i+1 保证值不能重复
        dfs1(lst, n, t-lst[i], tmp, res, i+1)
        tmp.pop()
        while i<n-1 and lst[i] == lst[i+1]:
            i += 1


def solution(lst, t):
    tmp = []
    res = []
    dfs1(lst, len(lst), t, tmp, res, 0)
    print(res)

solution([1, 2, 3, 6, 7, 1], 7)
