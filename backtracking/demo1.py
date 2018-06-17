# -*- coding: utf-8 -*-

"""题目描述
求一个集合的所有子集
"""

class Solution(object):
    def dfs(self, arr, n, tmp, res, visit):
        res.append(tmp.copy())
        for i in range(n):
            if not visit[i]:
                # 设置断点
                visit[i] = True
                tmp.append(arr[i])
                self.dfs(arr, n, tmp, res, visit)
                # 恢复断点
                tmp.pop()
                visit[i] = False
            # 防止arr中的重复项，重复的直接跳过
            while i<n-1 and arr[i] == arr[i+1]:
                i += 1
                
    def subset(self, arr):
        n = len(arr)
        tmp = []
        res = []
        visit = [False] * n
        arr.sort()  # 排序
        self.dfs(arr, n, tmp, res, visit)
        return res

if __name__ == '__main__':
    s = Solution()
    arr = s.subset(['a', 'b'])
    print(arr)
