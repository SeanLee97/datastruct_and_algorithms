# -*- coding: utf-8 -*-

"""题目描述
下图的矩阵顺时针打印结果为：1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10
# 题目分析：http://wiki.jikexueyuan.com/project/for-offer/question-twenty.html
"""

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if matrix is None:
            return
        m = len(matrix)
        n = len(matrix[0])
        startX = 0
        startY = 0
        lst = []
        # 对每一个环进行处理
        # 行号最大是 (m-1) / 2
        # 列号最大是 (n-1) / 2
        while 2*startX < m and 2*startY < n:
            lst += self.printMatrixInCircle(matrix, startX, startY)
            # 指向下一个要处理的环
            startX += 1
            startY += 1
        return lst

    def printMatrixInCircle(self, mat, x, y):
        m = len(mat)
        n = len(mat[0])
        lst = []
        # 打印最上面一行
        for i in range(y, n-y):
            lst.append(mat[x][i])

        # 打印右边的一列
        # 环高度至少为2才输出右边的一列
        # m-x-1是环最下一行的行号
        if m-x-1 > x:
            # 右边的最上面一个已经被输出，所以从x+1开始
            for i in range(x+1, m-x):
                lst.append(mat[i][n-y-1])
        
        # 打印最下面一行
        # 环高度至少是2并且环的宽度至少是2才会打印最后一行
        if n-y-1 > y and m-x-1 > x:
            for i in range(n-y-2, y, -1):
                lst.append(mat[m-x-1][i])

        # 打印最左边的一列
        # 环的宽度至少是2并且环的高度至少是3才会输出左边的一列
        if m-x-1 > x and n-y-1 > y:
            for i in range(m-x-1, x, -1):
                lst.append(mat[i][y])

        return lst
         
if __name__ == '__main__':
    mat = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]

    s = Solution()
    lst = s.printMatrix(mat)
    print(lst)
