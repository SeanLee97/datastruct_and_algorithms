# -*- coding: utf-8 -*-

"""题目描述
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
"""

class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if len(s) == 0 and len(pattern) == 0:
            return s == pattern
        plst = list(pattern)
        n = len(plst)
        slst = list(s)
        m = len(slst)
        dp = [[False for x in range(n+1)] for x in range(m+1)]
        dp[0][0] = True
        # init
        for i in range(1, n+1):
            if plst[i-1] == '*':
                dp[0][i] = dp[0][i-2]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if slst[i-1] == plst[j-1] or plst[j-1] == '.':
                    print(slst[i-1], plst[j-1])
                    dp[i][j] = dp[i-1][j-1]
                elif  plst[j-1] == '*':
                    print('abcd')
                    if plst[j-2] == slst[i-1] or plst[j-2] == '.':
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]
        return dp[i-1][j-1]
if __name__ == '__main__':
    s = Solution()
    s.match(',', '-')
