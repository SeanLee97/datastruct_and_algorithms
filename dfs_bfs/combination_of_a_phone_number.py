# -*- coding: utf-8 -*-

"""题目描述
https://blog.csdn.net/u011095253/article/details/9158437
"""

def dfs(s, table, tmp, res):
    if len(s) == 0:
        res.append(tmp)
        return

    for v in table[int(s[0])-1]:
        dfs(s[1:], table, tmp+v, res)

def solution(s):
    tmp = ''
    res = []
    table = [[],['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'],
             ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'],
             ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
    dfs(s, table, tmp, res)
    return res

if __name__ == '__main__':
    print(solution('23'))
