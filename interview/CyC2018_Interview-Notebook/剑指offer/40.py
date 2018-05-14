# -*- coding: utf-8 -*-

"""题目描述
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""

class Solution:
    def partition(self, lst, low, high):
        lst[low], lst[high] = lst[high], lst[low]
        store_idx = low
        privot = lst[high]
        for i in range(low, high):
            if lst[i] < privot:
                lst[store_idx], lst[i] = lst[i], lst[store_idx]
                store_idx += 1
        lst[store_idx], lst[high] = lst[high], lst[store_idx] 
        return store_idx

    def quick_search(self, tinput, k, low, high):
        while low < high:
            j = self.partition(tinput, low, high)
            if j == k:
                break
            elif j > k:
                high = j - 1
            else:
                low = j + 1
        return tinput[:k]

    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k <=0 or k > len(tinput):
            return []
        ret = self.quick_search(tinput, k, 0, len(tinput)-1)
        return ret

if __name__ == '__main__':
    s = Solution()
    lst = s.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8], 1)
    print(lst)
