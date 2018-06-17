# -*- coding: utf-8 -*-

"""题目描述
一摞烙饼的排序
假设有一堆烙饼，大小不一，需要把它们摆成从下到上由大到小的顺序。每次翻转只能一次翻转最上面的几个烙饼，把它们上下颠倒。反复多次可以使烙饼有序。那么，最少应该翻转几次呢？

分析可知这是一个最优化问题
"""
class Solution(object):
    def __init__(self):
        self.maxstep = 0

    def up_bound(self, n):
        # 当前翻转的上界
        return 2*(n-1)

    def low_bound(self, lst, ncnt):
        # 判断位置相邻的两个烙饼是否为尺寸上相邻的
        # 根据当前的数组排序信息来判断最少需要交换多少次
        ret = 0
        for i in range(1, ncnt):
            if abs(lst[i-1] - lst[i]) == 1:
                continue
            else:
                ret += 1
        return ret

    def is_sorted(self, lst, n, step):
        for i in range(1, n):
            if lst[i-1] > lst[i]:
                return False
        if step < self.maxstep:
            return True
        return False

    def reverse(sef, lst, begin, end):
        # 翻转
        i = begin
        j = end
        while i<j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1

    def dfs(self, lst, n, step, tmp, res):
        if step + self.low_bound(lst, n) > self.maxstep:
            return
        if self.is_sorted(lst, n, step):
            self.maxstep = step
            
            for i in range(step):
                res[i] = tmp[i]
            return
        for i in range(1, n):
            self.reverse(lst, 0, i)
            tmp[step] = i
            self.dfs(lst, n, step+1, tmp, res)
            # 恢复现场
            self.reverse(lst, i, 0)            

    def cake_sort(self, cakes):
        n = len(cakes)
        self.maxstep = self.up_bound(n)
        step = 0
        tmp = [0]*(self.maxstep+1)
        res = [0]*(self.maxstep+1)
        self.dfs(cakes, n, step, tmp, res)
        return res

if __name__ == '__main__':
    s = Solution()
    cakes = [3, 2, 1, 6]
    res = s.cake_sort(cakes)
    print(res)
