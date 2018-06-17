# -*- coding: utf-8 -*-

"""题目描述
Given a set of distinct integers, S, return all possible subsets.

Note: Elements in a subset must be in non-descending order. The solution set must not contain duplicate subsets.

For example, If S = [1,2,3], a solution is: [ [3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], [] ]

子集问题
"""

def dfs(lst, n, sub, subs, k):
    subs.append(sub.copy())
    for i in range(k, n):
        sub.append(lst[i])
        dfs(lst, n, sub, subs, i+1)
        sub.pop()   # backtrack

# 解决输入lst中有重复值问题    
def dfs1(lst, n, sub, subs, k):
    subs.append(sub)
    for i in range(k, n):
        sub.append(lst[i])
        dfs(lst, n, sub, subs, i+1)
        sub.pop()
        # 检查后面的值是否和当前值重复，重复则跳过
        while i<n-1 and lst[i] == lst[i+1]:
            i+=1

def solution(lst):
    sub = []
    subs = []
    lst.sort()
    n = len(lst)
    #dfs(lst, n, sub, subs, 0)
    dfs1(lst, n, sub, subs, 0)
    print(subs)

solution([1, 1, 2])
