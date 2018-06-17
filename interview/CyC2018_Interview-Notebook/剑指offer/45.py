# -*- coding: utf-8 -*-

"""题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""

from functools import cmp_to_key

class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        key = cmp_to_key(lambda a, b: int(str(a+b))- int(str(b+a)))
        numbers = "".join(sorted(map(str, numbers), key=key)) 
        return numbers


if __name__ == '__main__':
    s = Solution()
    nums = s.PrintMinNumber([3, 2, 1, 4, 5])
    print(nums)
