# -*- coding: utf-8 -*-

"""
题目描述：
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""
class Solution:
    def echo(self, x, y, m, n, matrix):
        lst = []
        # 打印顶部第一行
        for i in range(y, n-y):
            lst.append(matrix[x][i])
        # 打印右部
        if m-x-1 > x:
            for i in range(x+1, m-x):
                lst.append(matrix[i][n-y-1])
        # 打印底部
        if m-x-1 > x and n-y-1 > y:
            for i in range(n-y-2, y, -1):
                lst.append(matrix[m-x-1][i])
        # 打印左部
        if m-x-1 > x and n-y-1 > y:
            for i in range(m-x-1, x, -1):
                lst.append(matrix[i][y])

        return lst

    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        x = 0
        y = 0
        lst = []
        while 2*x<m and 2*y < n:
            lst += self.echo(x, y, m, n ,matrix)
            x += 1
            y += 1

        return lst
