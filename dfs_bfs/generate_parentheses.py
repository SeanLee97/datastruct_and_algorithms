# -*- coding: utf-8 -*-

"""题目描述
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is: "((()))", "(()())", "(())()", "()(())", "()()()"
"""

def dfs(left, right, tmp, res):
    if left == 0 and right == 0:
        res.append(tmp)
        return
    # 如果左边还有则继续放
    if left > 0:
        tmp += "("
        dfs(left-1, right, tmp, res)
        tmp = tmp[:-1]
    # 如果左边<右边则放右边
    if left < right:
        tmp += ")"
        dfs(left, right-1, tmp, res)
        tmp = tmp[:-1]

def solution(n):
    tmp = ""
    res = []
    dfs(n, n, tmp, res)
    return res

if __name__ == '__main__':
    print(solution(3))
