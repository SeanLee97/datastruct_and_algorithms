# -*- coding: utf-8 -*-

"""题目描述

求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数。

https://blog.csdn.net/yi_afly/article/details/52012593
"""

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        base = 1
        r = n
        while r > 0:
            weight = r % 10
            r //= 10
            count += r*base
            if weight == 1:
                count += (n%base) + 1
            elif weight > 1:
                count += base
            base *= 10

        return count

if __name__ == '__main__':
    s = Solution()
    c = s.NumberOf1Between1AndN_Solution(514)
    print(c)
        
