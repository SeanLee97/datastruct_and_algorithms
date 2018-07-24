# -*- coding: utf-8 -*-

"""题目描述
输出不重复数字的全排列
"""

class Solution(object):
    def dfs(self, arr, n, tmp, res, visit):
        if len(tmp) == n:
            res.append(tmp.copy())
            return
        for i in range(n):
            if not visit[i]:
                # 保存现场
                visit[i] = True
                tmp.append(arr[i])
                self.dfs(arr, n, tmp, res, visit)
                # 恢复现场
                tmp.pop()
                visit[i] = False
                # 跳过重复
                while i<n-1 and arr[i] == arr[i+1]:
                    i += 1

    def permutation(self, arr):
        n = len(arr)
        tmp = []
        res = []
        visit = [False]*n
        self.dfs(arr, n, tmp, res, visit)
        return res

if __name__ == '__main__':
    s = Solution()
    arr = s.permutation([1, 2, 3])
    print(arr)
