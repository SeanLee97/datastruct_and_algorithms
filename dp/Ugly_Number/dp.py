# -*- coding: utf-8 -*-

"""
把只包含因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
分析：
和求解素数一样，利用ugly(k) 来求解 ugly(n) k < n, 在这里由于是三个因子，故可维护三个下标来访问
"""

class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 6:
            return index
        dp = [1] + [0] * (index-1)
        i2, i3, i5 = 0, 0, 0

        for i in range(1, index):
            n2 = dp[i2] * 2
            n3 = dp[i3] * 3
            n5 = dp[i5] * 5
            n = min((n2, n3, n5))
            print(n)
            dp[i] = n
            if n == n2:
                i2 += 1
            if n == n3:
                i3 += 1
            if n == n5:
                i5 += 1
        return dp[index-1]

if __name__ == '__main__':
    s = Solution()
    n = s.GetUglyNumber_Solution(7)
    print(n)
