# -*- coding: utf-8 -*-

"""
统计矩阵中团的个数以及团中最大个数是多少，
"""
def dfs(matrix, i, j, m, n):
    if i<0 or j<0 or i>=m or j>=n or matrix[i][j] <= 0:
        return 0
    matrix[i][j] = -1 # visited
    count = 1 + (dfs(matrix, i+1, j, m, n) + dfs(matrix, i-1, j, m, n) +
    	dfs(matrix, i, j-1, m, n) + dfs(matrix, i, j+1, m, n))
    return count

def solution(matrix):
    m = len(matrix)
    n = len(matrix[0])
    max_num = 0
    groups = 0
    for i in range(m):
        for j in range(n):
            curr_num = dfs(matrix, i, j, m, n)
            if curr_num > 0:
                groups += 1
            if curr_num > max_num:
                max_num = curr_num
    return groups, max_num

if __name__ == '__main__':
    matrix = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,1,0,1,0,0,0],
        [0,1,0,0,0,0,0,1,0,1],
        [1,0,0,0,0,0,0,0,1,1],
        [0,0,0,1,1,1,0,0,0,1],
        [0,0,0,0,0,0,1,0,1,1],
        [0,1,1,0,0,0,0,0,0,0],
        [0,0,0,1,0,1,0,0,0,0],
        [0,0,1,0,0,1,0,0,0,0],
        [0,1,0,0,0,0,0,0,0,0]
    ]
    print(solution(matrix))
