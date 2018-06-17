# -*- coding: utf-8 -*-

"""排列问题
"""

def dfs(lst, n, tmp, res, visit):
    if len(tmp) == n:
        res.append(tmp.copy())
        return
    for i in range(n):
        if visit[i] == False:
            # 如果i先前没有访问过，则以该结点开始进行DFS
            visit[i] = True
            tmp.append(lst[i])
            dfs(lst, n, tmp, res, visit)
            # 先前的结点已经DFS完，则回到该结点继续i+1的情况
            tmp.pop()
            visit[i] = False

# lst 中有重复值时
def dfs1(lst, n, tmp, res, visit):
    if len(tmp) == n:
        res.append(tmp.copy())
        return 
    i = 0
    while i < n:
        if not visit[i]:
            visit[i] = True
            tmp.append(lst[i])
            dfs1(lst, n, tmp, res, visit)
            tmp.pop()
            visit[i] = False
            # 跳过重复值
            while i<n-1 and lst[i] == lst[i+1]:
               i+=1
        i += 1

def solution(lst):
    n = len(lst)
    res = []
    tmp = []
    lst.sort()
    visit = [False]*n
    dfs1(lst, n, tmp, res, visit)
    print(res)

solution([1, 1, 2])
