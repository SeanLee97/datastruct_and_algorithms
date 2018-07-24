# -*- coding: utf-8 -*-
"""
把只包含因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含因子7。 习惯上我们把1当做是第一个丑数。
求按从小到大的顺序的第N个丑数。

解法：
本解法采用循环方法，效率低下时间复杂度过大，AC不了
"""

class Solution:
    def GetUglyNumber_Solution(self, index):
        if index < 6:
            return index
        n = 0
        i = 1
        #global INT_MAX
        while n < index:
            if self.isUglyNumber(i):
                n += 1
            i += 1
        return i

    def isUglyNumber(self, num):
        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5
        return num == 1
if __name__ == '__main__':
    s = Solution()
    n = s.GetUglyNumber_Solution(150)
    print(n)

