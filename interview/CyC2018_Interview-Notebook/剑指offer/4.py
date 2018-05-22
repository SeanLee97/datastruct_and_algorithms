# -*- coding:utf-8 -*-

"""题目描述
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

def solution(mat, num):
    m = len(mat)
    n = len(mat[0])
    i = 0
    j = n - 1
    while i < m and j >= 0:
        if mat[i][j] > num:
            j -= 1
        elif mat[i][j] < num:
            i += 1
        else:
            return True
    return False

if __name__ == '__main__':
    mat = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print(solution(mat, 69)) 
    
