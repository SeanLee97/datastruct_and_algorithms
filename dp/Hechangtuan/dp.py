# -*- coding: utf-8 -*-

"""
题目描述：
链接：https://www.nowcoder.com/questionTerminal/661c49118ca241909add3a11c96408c8
有 n 个学生站成一排，每个学生有一个能力值，牛牛想从这 n 个学生中按照
顺序选取 k 名学生，要求相邻两个学生的位置编号的差不超过 d，
使得这 k 个学生的能力值的乘积最大，你能返回最大的乘积吗？

分析:
考虑要从n个人中找出k人且k人的编号不超过d，考虑一个二维状态数组
考虑一个二维状态数组dp[i][j]表示从i人中选择j人时能力值最大，那么状态
转移矩阵应是 dp[i][j] = max(dp[i][j], dp[i-1 -> i-d-1][j-1])
由于编号限制不超过d也即是状态只能回溯到前d位
再考虑由于是乘，不是加，故存在“负负得正”的问题，如果仅考虑正数显然是不行的，
故还需要维护一个记录最小值的状态二维矩阵综上可得状态转移方程
tmax = dpmax[i-1 -> i-d-1][j-1]*arr[i-1]
tmin = dpmin[i-1 -> i-d-1][j-1]*arr[i-1]
dpmax[i][j] = max(dpmax[i][j], max(tmax, tmin))
dpmin[i][j] = min(dpmin[i][j], min(tmax, tmin))
"""

def solution(n, arr, k, d):
    dpmax = [[0 for x in range(k+1)] for x in range(n+1)]
    dpmin = [[0 for x in range(k+1)] for x in range(n+1)]
    # 初始化最大最小
    for i in range(n):
        dpmax[i][1] = arr[i]
        dpmin[i][1] = arr[i]

    for i in range(1, n+1):
        for j in range(1, k+1):
            t = 0 if i-d-1 < 0 else i-d-1
            for x in range(i-1, t, -1):
                #print(i, x, j-1)
                #print(dpmax[x][j-1], arr[i-1])

                tmpmax = dpmax[x][j-1]*arr[i-1]
                tmpmin = dpmin[x][j-1]*arr[i-1]
                dpmax[i][j] = max(dpmax[i][j], max(tmpmax, tmpmin))
                dpmin[i][j] = min(dpmin[i][j], min(tmpmax, tmpmin))

    return dpmax[n][k]
if __name__ == '__main__':
    n = 3
    arr = [7, -4, 7]
    k = 2
    d = 50
    print(solution(n, arr, k, d))
