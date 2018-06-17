# -*- coding: utf-8 -*-

"""题目描述
求 1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case 等关键字及条件判断语句（A?B:C）。
"""

class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n and n + self.Sum_Solution(n-1)

if __name__ == '__main__':
    s = Solution()
    n = s.Sum_Solution(2)
    print(n)
