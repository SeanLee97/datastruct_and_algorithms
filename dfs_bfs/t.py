# -*- coding: utf-8 -*-

"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:

输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
"""

import copy
class Solution:
    def dfs(self, lst, n, tmp, res, visit):
        if len(tmp) == n:
            ntmp = copy.copy(tmp)
            res.append(''.join(ntmp))
            return
        for i in range(n):
            if not visit[i]:
                tmp.append(lst[i])
                visit[i] = True
                self.dfs(lst, n, tmp, res, visit)
                tmp.pop()
                visit[i] = False
                while i+1 < n and lst[i] == lst[i+1]:
                    i += 1

    def Permutation(self, ss):
        if len(ss) == 0:
            return []
        lst = list(ss)
        lst.sort()
        n = len(lst)
        res = []
        visit = [False]*n
        self.dfs(lst, n, [], res, visit)
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.Permutation('abc')
    print(res)
