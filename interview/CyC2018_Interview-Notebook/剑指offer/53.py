# -*- coding:utf-8 -*-

"""题目描述
统计一个数字在排序数组中出现的次数。
"""

class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if len(data) == 0:
            return 0
        elif len(data) == 1:
            return 1 if data[0] == k else 0

        l, h = 0, len(data)-1
        num = 0
        while l < h:
            m = (l + h) // 2
            if data[m] == k:
                for i in range(m, l-1, -1):
                    if data[i] == k:
                        num += 1
                    else:
                        break
                for j in range(m+1, h+1):
                    if data[j] == k:
                        num += 1
                    else:
                        break
                break
            elif data[m] < k:
                l = m+1
            else:
                h = m-1
        return num
    
