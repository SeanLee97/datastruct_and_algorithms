# -*- coding: utf-8 -*-

"""题目描述
https://blog.csdn.net/u011095253/article/details/9158437
"""

def dfs(s, table, tmp, res):
    if len(s) == 0:
        res.append(tmp)
        return
    k = int(s[0]) - 1
    for i in range(len(table[k])):
        # 以s[0]为当前根结点遍历下去，获得所有可能
        dfs(s[1:], table, tmp+table[k][i], res)

def solution(s):
    tmp = ''
    res = []
    table = [[],['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'],
             ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'],
             ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
    dfs(s, table, tmp, res)
    print(res)

solution('23')
