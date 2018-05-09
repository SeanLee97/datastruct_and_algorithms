# -*- coding: utf-8 -*-

"""题目描述
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
    tips:
可用回溯法实现: 回溯法也是设计递归过程的一种重要方法，它的求解过程实质上是一个先序遍历一棵"状态树"的过程,只是这棵树不是遍历前预先建立的,而是隐含在遍历过程中
"""

def find(mat, m, n, i, j, str, idx, flag):
    if (i<0 or j<0 or i>=m or j>=n or  
        flag[i][j] or mat[i][j] != str[idx]):
        return False
    if idx == len(str)-1:    
        return True
    flag[i][j] = True
    if (find(mat, m, n, i+1, j, str, idx+1, flag) or 
        find(mat, m, n, i-1, j, str, idx+1, flag) or  
        find(mat, m, n, i, j+1, str, idx+1, flag) or  
        find(mat, m, n, i, j-1, str, idx+1, flag)):
        return True
    # 回溯
    flag[i][j] = False
    return False

def has_path(mat, str):
    m = len(mat)
    n = len(mat[0])
    flag = [[False for x in range(n)] for x in range(m)]
    for i in range(m):
        for j in range(n):
            if find(mat, m, n, i, j, str, 0, flag):
                return True
    return False

if __name__ == '__main__':
    mat = [['a', 'd', 'c'],
           ['e', 'f', 'g']]
    if has_path(mat, 'adf'):
        print('yes.')
    else:
        print('no.')

