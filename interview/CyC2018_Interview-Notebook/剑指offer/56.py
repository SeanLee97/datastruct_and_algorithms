# -*- coding:utf-8 -*-

"""题目描述
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""

from collections import OrderedDict
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        d = OrderedDict()
        for x in array:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        ret = []
        for k, v in d.items():
            if v == 1:
                ret.append(k)
        return ret
