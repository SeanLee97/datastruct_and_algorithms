# -*- coding: utf-8 -*-

"""题目描述
输入一个递增排序的数组和一个数字 S，在数组中查找两个数，使得他们的和正好是 S，如果有多对数字的和等于 S，输出两个数的乘积最小的。
"""

class Solution:
    def FindSequence(self, data, S):
        l, r = 0, len(data)-1
        a, b = 0, 0
        minimum = float('inf')
        while l < r:
            curr = data[l] + data[r]
            if curr == S:
                p = data[l] * data[r]
                if p < minimum:
                    minimum = p
                    a, b = data[l], data[r]
                l += 1
                r -= 1
            elif curr > S:
                r -= 1
            else:
                l += 1
        return [a, b]
                
