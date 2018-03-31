# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 计算最短路径(类似于Prim算法)，图最好用邻接矩阵表示

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

    def echo(self, distance):
        print("Vertex tDistance from Source")
        for u in range(self.vsize):
            print(u, "t", distance[u])

    def dijkstra(self, src):
        distance = [INF]*self.vsize
        distance[src] = 0
        visit = [False]*self.vsize


        for _ in range(self.vsize):
            u = self.find_min_dist(distance, visit)
            visit[u] = True

            for v in range(self.vsize):
                if self.matrix[u][v] > 0 and distance[v] > (distance[u] + self.matrix[u][v]) and not visit[v]:
                    distance[v] = distance[u] + self.matrix[u][v]
        self.echo(distance)

if __name__ == '__main__':
    g  = Graph(9)
    g.matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
              ];
     
    g.dijkstra(0)
