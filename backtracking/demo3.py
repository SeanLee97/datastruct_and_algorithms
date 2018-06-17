# -*- coding: utf-8 -*-

"""题目描述
求一个n元集合的k元子集（n>=k>0）
"""

class Solution(object):
    def dfs(self, arr, n, k, tmp, res, visit):
        if len(tmp) == k:
            res.append(tmp.copy())
            return
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                tmp.append(arr[i])
                self.dfs(arr, n, k, tmp, res, visit)
                visit[i] = False
                tmp.pop()
        
    def subset_k(self, arr, k):
        tmp = []
        res = []
        n = len(arr)
        if n < k or n == 0:
            return
        visit = [False] * n
        arr.sort()
        self.dfs(arr, n, k, tmp, res, visit)
        return res

if __name__ == '__main__':
    s = Solution()
    arr = s.subset_k([1, 2, 5, 4], 3)
    print(arr)
