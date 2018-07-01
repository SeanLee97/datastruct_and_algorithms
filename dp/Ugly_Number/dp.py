# -*- coding: utf-8 -*-

"""
把只包含因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""

class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 6:
            return index
        i2, i3, i5 = 0, 0, 0
        dp = [0]*index
        dp[0] = 1
        for i in range(1, index):
            n2 = dp[i2] * 2
            n3 = dp[i3] * 3
            n5 = dp[i5] * 5
            dp[i] = min((n2, n3, n5))
            if dp[i] == n2:
                i2 += 1
            if dp[i] == n3:
                i3 += 1
            if dp[i] == n5:
                i5 += 1
        return dp[index-1]

if __name__ == '__main__':
    s = Solution()
    n = s.GetUglyNumber_Solution(7)
    print(n)