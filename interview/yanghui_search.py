# -*- coding: utf-8 -*-

def search(mat, x):
    m = len(mat)
    n = len(mat[0])
    i, j = 0, n-1
    while i < m and j>=0:
        if mat[i][j] > x:
            j -= 1
        elif mat[i][j] < x:
            i += 1
        else:
            return True
    return False

mat = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]

print(search(mat, 10))
