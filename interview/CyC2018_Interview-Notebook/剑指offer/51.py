# -*- coding: utf-8 -*-

"""题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
"""

class Solution:
    def __init__(self):
        self.P = 0
        self.tmp = []

    def merge(self, data, l, m, h):
        i, j, k = l, m + 1, l
        while i <= m or j <= h:
            if i>m:
                self.tmp[k] = data[j]
                j += 1
            elif j > h:
                self.tmp[k] = data[i]
                i += 1
            elif data[i] < data[j]:
                self.tmp[k] = data[i]
                i += 1
            else:
                self.tmp[k] = data[j]
                j += 1
                self.P += m-i+1    # data[i] > data[j]
            k +=1
        for x in range(l, h+1):
            data[x] = self.tmp[x]

    def merge_sort(self, data, low, high):
        if low < high:
            mid = low+ (high-low) // 2
            self.merge_sort(data, low, mid)
            self.merge_sort(data, mid+1, high)
            self.merge(data, low, mid, high)
    
    def InversePairs(self, data):
        # write code here
        self.tmp = [0]*len(data)
        self.merge_sort(data, 0, len(data)-1)
        return self.P%1000000007

if __name__ == '__main__':
    s = Solution()
    n = s.InversePairs([7, 5, 6, 4])
    print(n)
