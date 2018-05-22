# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Floyd动态规划求最短路径, 图最好用邻接矩阵表示

INF = 65535

class Graph(object):
    def __init__(self, vsize):
        self.vsize = vsize
        self.matrix = [[0 for _ in range(self.vsize)] for x in range(self.vsize)]

    def find_min_dist(self, distance, visit):
        u = -1
        mindist = INF
        for v in range(self.vsize):
            if distance[v] < mindist and not visit[v]:
                mindist = distance[v]
                u = v
        return u

    def echo(self, dp):
        print("Vertex tDistance from Source")
        for i in range(self.vsize):
            for j in range(self.vsize):
                if dp[i][j] == INF:
                    print('%7s'%('INF'))
                else:
                    print('%7d\t'%(dp[i][j]))
                if j == self.vsize - 1:
                    print()

    def floyd(self):
        dp = [[self.matrix[x][y] for y in range(self.vsize)] for x in range(self.vsize)]

        for k in range(self.vsize):
            for i in range(self.vsize):
                for j in range(self.vsize):
                    # 比较直达 和 不直达路径的大小
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

        self.echo(dp)

if __name__ == '__main__':
    g  = Graph(9)
    g.matrix = [[INF, 4, INF, INF, INF, INF, INF, 8, INF],
               [4, INF, 8, INF, INF, INF, INF, 11, INF],
               [INF, 8, INF, 7, INF, 4, INF, INF, 2],
               [INF, INF, 7, INF, 9, 14, INF, INF, INF],
               [INF, INF, INF, 9, INF, 10, INF, INF, INF],
               [INF, INF, 4, 14, 10, INF, 2, INF, INF],
               [INF, INF, INF, INF, INF, 2, INF, 1, 6],
               [8, 11, INF, INF, INF, INF, 1, INF, 7],
               [INF, INF, 2, INF, INF, INF, 6, 7, INF]
              ]
     
    g.floyd()
