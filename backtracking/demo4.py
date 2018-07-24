# -*- coding: utf-8 -*-

"""题目描述
电话键盘上有9个数字，其中2~9分别代表了几个字母，如2:ABC，3:DEF......等等。给定一个数字序列，输出它所对应的所有字母序列
"""
table = [[],['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'],
         ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'],
         ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

class Solution(object):
    def dfs(self, number, tmp, res):
        if len(number) == 0:
            res.append(tmp.copy())
            return
        global table
        k = int(number[0])
        for i in range(len(table[k])):
            self.dfs(number[1:], tmp+[table[k][i]], res)

    def numbers(self, number):
        tmp = []
        res = []
        n = len(number)
        self.dfs(number, tmp, res)
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.numbers('12')
    print(res)
