# -*- coding:utf-8 -*-

"""题目描述
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
"""

class Solution:
    def StrToInt(self, s):
        # write code here
        if len(s) == 0:
            return 0
        lst = list(s)
        res = []
        isNegative = False
        for i in range(len(lst)):
            if lst[i] == '+':
                continue
            if lst[i] == '-':
                isNegative = True

            if ord(lst[i]) < ord('0') or ord(lst[i]) > ord('9'):
                return 0
            res.append(ord(lst[i])-ord('0'))

        if len(res) == 0:
            return 0
        base = 1
        total = 0
        while len(res) > 0:
            total += base * res.pop()
            base *= 10
        return total if isNegative == False else -total

if __name__ == '__main__':
    s = Solution()
    n = s.StrToInt('-2147483647')
    print(n)
